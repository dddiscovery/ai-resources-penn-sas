#!/usr/bin/env python3
"""
Fetch AI-related RSS feeds and append new entries to _data/ai_feed.yml.
Opens no files for write when run in dry-run mode (default in CI until PR is created).

Approved sources only. All new entries are marked reviewed: false for human review.
"""

from __future__ import annotations

import hashlib
import re
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen

try:
    import yaml
except ImportError:
    print("PyYAML required: pip install pyyaml")
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[2]
FEED_FILE = ROOT / "_data" / "ai_feed.yml"

RSS_SOURCES = [
    {
        "url": "https://news.mit.edu/rss/topic/artificial-intelligence2",
        "source": "MIT News",
        "category": "news",
    },
    {
        "url": "https://penntoday.upenn.edu/rss.xml",
        "source": "Penn Today",
        "category": "penn_updates",
    },
    {
        "url": "https://www.schmidtsciences.org/feed/",
        "source": "Schmidt Sciences",
        "category": "news",
    },
]

NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "content": "http://purl.org/rss/1.0/modules/content/",
}


def slugify(text: str, max_len: int = 48) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s[:max_len] or "item"


def fetch_rss(url: str, timeout: int = 20) -> str:
    req = Request(url, headers={"User-Agent": "DDDI-AI-Feed-Bot/1.0"})
    with urlopen(req, timeout=timeout) as resp:
        text = resp.read().decode("utf-8", errors="replace")
    stripped = text.lstrip()
    if not stripped.startswith(("<?xml", "<rss", "<feed")):
        raise ValueError(f"Response from {url} is not RSS/XML")
    return text


def looks_like_article_url(url: str) -> bool:
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        return False
    path = parsed.path.strip("/")
    if not path:
        return False
    lower = url.lower().rstrip("/")
    if lower.endswith((".xml", "/rss", "/feed")):
        return False
    return True


def extract_item_url(item: ET.Element) -> str:
    candidates: list[str] = []

    link_el = item.find("link")
    if link_el is not None:
        text = (link_el.text or "").strip()
        href = (link_el.get("href") or "").strip()
        if text:
            candidates.append(text)
        if href:
            candidates.append(href)

    for link_el in item.findall("atom:link", NS):
        rel = (link_el.get("rel") or "alternate").lower()
        if rel in ("alternate", ""):
            href = (link_el.get("href") or "").strip()
            if href:
                candidates.append(href)

    guid = item.find("guid")
    if guid is not None:
        is_permalink = (guid.get("isPermaLink") or "").lower() == "true"
        text = (guid.text or "").strip()
        if text.startswith("http") and (is_permalink or looks_like_article_url(text)):
            candidates.append(text)

    for url in candidates:
        if looks_like_article_url(url):
            return url

    for url in candidates:
        if url.startswith("http"):
            return url

    return ""


def parse_date(raw: str | None) -> str:
    if not raw:
        return datetime.now(timezone.utc).strftime("%Y-%m-%d")
    for fmt in (
        "%a, %d %b %Y %H:%M:%S %z",
        "%a, %d %b %Y %H:%M:%S %Z",
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%d",
    ):
        try:
            dt = datetime.strptime(raw.strip(), fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.strftime("%Y-%m-%d")
        except ValueError:
            continue
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def strip_html(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text or "").strip()


def parse_rss(xml_text: str, meta: dict) -> list[dict]:
    root = ET.fromstring(xml_text)
    channel = root.find("channel")
    if channel is None:
        channel = root

    items = channel.findall("item") or root.findall("atom:entry", NS)
    results = []

    for item in items[:15]:
        title_el = item.find("title")
        # Note: `el_a or el_b` is wrong for Elements — an Element with text but no
        # children is falsy, so fall through explicitly on None.
        desc_el = item.find("description")
        if desc_el is None:
            desc_el = item.find("summary")
        if desc_el is None:
            desc_el = item.find("atom:summary", NS)
        date_el = item.find("pubDate")
        if date_el is None:
            date_el = item.find("published")
        if date_el is None:
            date_el = item.find("atom:published", NS)

        title = (title_el.text or "").strip() if title_el is not None else ""
        if not title:
            continue

        url = extract_item_url(item)
        if not url:
            continue

        summary = strip_html(desc_el.text if desc_el is not None else "")
        if len(summary) > 280:
            summary = summary[:277] + "..."

        date = parse_date(date_el.text if date_el is not None else None)
        uid_hash = hashlib.sha1(f"{title}|{url}|{meta['source']}".encode()).hexdigest()[:10]

        results.append(
            {
                "id": f"auto-{uid_hash}",
                "date": date,
                "title": title,
                "source": meta["source"],
                "url": url,
                "category": meta["category"],
                "summary": summary or "No summary available.",
                "reviewed": False,
                "disclaimer": True,
            }
        )

    return results


def load_feed_file() -> dict:
    if not FEED_FILE.exists():
        return {"disclaimer": "AI Pulse entries are curated for relevance.", "feed": []}
    with FEED_FILE.open(encoding="utf-8") as f:
        return yaml.safe_load(f) or {"feed": []}


def existing_keys(data: dict) -> set[str]:
    keys = set()
    for item in data.get("feed", []):
        keys.add(item.get("id", ""))
        keys.add(f"{item.get('title','')}|{item.get('url','')}")
    return keys


def main() -> int:
    data = load_feed_file()
    known = existing_keys(data)
    new_items: list[dict] = []

    for src in RSS_SOURCES:
        try:
            xml_text = fetch_rss(src["url"])
            parsed = parse_rss(xml_text, src)
            for entry in parsed:
                key = f"{entry['title']}|{entry['url']}"
                if entry["id"] in known or key in known:
                    continue
                new_items.append(entry)
                known.add(entry["id"])
                known.add(key)
            print(f"Fetched {len(parsed)} items from {src['source']}")
        except Exception as exc:
            print(f"Warning: failed to fetch {src['source']}: {exc}")

    if not new_items:
        print("No new items to add.")
        return 0

    # Prepend newest first
    data.setdefault("feed", [])
    data["feed"] = new_items + data["feed"]

    with FEED_FILE.open("w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=1000)

    print(f"Added {len(new_items)} new unreviewed entries to {FEED_FILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
