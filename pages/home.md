---
layout: home
title: "AI Resources for Penn Arts & Sciences"
description: A curated guide to AI and LLM tools for Penn Arts & Sciences researchers.
permalink: /
css: [/assets/css/home.css, /assets/css/quadmap.css]

hero:
  eyebrow: "Penn Arts & Sciences · Data Driven Discovery Initiative"
  heading: "AI Resources for <em>Penn Arts & Sciences</em>"
  subtext: "A curated guide to AI and LLM tools for researchers: what's available, what it genuinely does well, and where the risks lie."
  buttons:
    - label: "AI Tools Matrix"
      url: "/tools/"
      style: "btn-dark"
    - label: "AI for Learning"
      url: "/for-students/"
      style: "btn-ghost"
    # Archived with pages/for-teaching.md (published: false). Uncomment when it returns.
    # - label: "AI for Teaching"
    #   url: "/for-teaching/"
    #   style: "btn-ghost"
    - label: "AI for Research"
      url: "/for-researchers/"
      style: "btn-ghost"

# ── How to judge an AI answer ──────────────────────────────────────────────────
# The map itself is shared with §4 of the ten-minute guide (pages/evaluating-ai.md)
# through _includes/quadmap.html, so both pages read from the same `map:` shape and
# the include has to keep working against both. Every string here is content: the
# layout draws the grid and the axes, and knows none of the words.
evaluating:
  eyebrow: "Before you trust it"
  heading: "How the four fit together"
  intro: "Most online arguments about whether a model is good turn on four words: hallucination, confabulation, unfaithfulness, sycophancy. They answer two independent questions \u2014 does it stick to the source you gave it, and does it hold its answer when you push back \u2014 which is why you can be caught by one failure while carefully checking for the other."
  map:
    x_low: "Sticks to the source"
    x_high: "Invents freely"
    y_high: "Holds its answer"
    y_low: "Tells you what you want"
    quadrants:
      - id: "good"
        pos: "top-left"
        label: "Worth trusting"
        term: ""
        body: "Grounded in what you gave it, and it does not fold when you push. Still check it, but this is the behaviour you are looking for."
      - id: "invents"
        pos: "top-right"
        label: "Confidently wrong"
        term: "Hallucination \u00b7 Confabulation"
        body: "It will defend an invented citation as readily as a real one. Pushing back does not help here, because the problem was never a lack of conviction."
      - id: "caves"
        pos: "bottom-left"
        label: "Right until questioned"
        term: "Sycophancy"
        body: "The answer was fine. Your doubt was enough to move it. This is the failure that punishes you for checking."
      - id: "worst"
        pos: "bottom-right"
        label: "Tells you whatever you want"
        term: "Both at once"
        body: "It invents, and it re-invents in whichever direction you lean. Leading questions produce this, which is a reason to ask neutral ones."
  callout: "The distinction most evaluation posts turn on: a claim can be <strong>unfaithful and still perfectly true</strong>. If you ask for a summary of a paper and the model adds a correct fact that the paper never mentioned, it has been accurate about the world and unfaithful to your source. Faithful and correct are measured separately, and a model can pass one while failing the other."
  link:
    label: "Read the 10-minute guide"
    url: "/evaluating-ai/"

about:
  heading: "About this resource"
  text: "Maintained and edited by <a href=\"https://yuxinlg.github.io/\" target=\"_blank\" rel=\"noopener\">Yuxin (Elena) Liang</a>, data scientist at the <a href=\"https://datascience.sas.upenn.edu/\" target=\"_blank\" rel=\"noopener\">Data Driven Discovery Initiative (DDDI)</a>, Penn Arts & Sciences. Access status is updated as Penn license agreements change. Inspired by <a href=\"https://polkwagner.github.io/penn-law-ai-resources/\" target=\"_blank\" rel=\"noopener\">Penn Carey Law AI Resources</a>, maintained by R. Polk Wagner. If you have any concerns, contact us at <a href=\"mailto:yuxinlg@upenn.edu\">yuxinlg@upenn.edu</a>."

# ── Offline ────────────────────────────────────────────────────────────────────
# The news strip renders only when `news:` exists (see _layouts/home.html). Uncomment
# and rewrite when there is something current; the PennChat pilot below ended in
# mid-August 2026.
# news:
#   label: "News"
#   text: "Penn is piloting <strong>PennChat</strong>, a secure University AI portal offering access to Claude and ChatGPT models within Penn's protected network. The pilot runs through mid-August, when Penn expects to launch its official AI service."
#   link_label: "Read the details"
#   link_url: "https://www.thedp.com/article/2026/07/penn-artificial-intelligence-claude-chatgpt-anthropic-data-security"
---
