---
layout: evaluating
title: "Evaluating AI Output | AI Resources for Penn Arts & Sciences"
description: A ten-minute guide to the vocabulary people use when they argue about whether an AI model is any good.
permalink: /evaluating-ai/
css: [/assets/css/evaluating.css, /assets/css/quadmap.css]

header:
  eyebrow: "A ten-minute guide"
  heading: "Evaluating what an AI gives you"
  subtext: "Read one thread about whether a model is good and you will hit hallucination, faithfulness, confabulation, and sycophancy inside a paragraph. None of them require knowing how a model works. All of them are things you can check yourself."

# ── §1 The worked example ──────────────────────────────────────────────────────
# NOT YET WRITTEN. This section renders only when `example:` exists, so the page ships
# without it. To add it, uncomment and fill in from a real transcript. Do not invent one:
# the section is presented to readers as a genuine exchange, so it has to be genuine.
#
# example:
#   title: "What it actually looks like"
#   desc: "One real exchange, marked up."
#   setup: "Say what was asked for, and what source the model was given."
#   model: "Which model and version, and when."
#   turns:
#     - speaker: "The request"
#       text: "..."
#     - speaker: "The answer"
#       text: "..."
#       annotations:
#         - quote: "the exact phrase from the answer above"
#           term: "Hallucination"
#           note: "why this phrase is an instance of it"
#     - speaker: "Pushing back"
#       text: "..."
#     - speaker: "The answer, second time"
#       text: "..."
#       annotations:
#         - quote: "..."
#           term: "Sycophancy"
#           note: "..."

# ── §2 The four failure words ──────────────────────────────────────────────────
failures:
  title: "Four things that go wrong"
  desc: "Each of these is a different kind of wrong. Telling them apart is most of the skill, because the fix for one is not the fix for another."
  items:
    - id: "hallucination"
      term: "Hallucination"
      aka: "fabrication · making things up"
      plain: "The model states something that is not true, in the same even tone it uses for things that are true."
      why: "The word stuck because the output feels perceptual, as though the model saw something that was not there. That framing is misleading, which is why the next word exists."
      test: "Ask for the source of any specific claim, then open it yourself. Invented citations are the easiest instance to catch, because a DOI either resolves or it does not."
    - id: "confabulation"
      term: "Confabulation"
      aka: "the same phenomenon, a better word for it"
      plain: "The model fills a gap with the most plausible-sounding thing available, smoothly and without signalling that it is doing so."
      why: "Borrowed from clinical psychology, where it describes filling a memory gap with invented detail told in complete sincerity. Many researchers prefer it because it explains why the invented parts look so ordinary: the model is not malfunctioning, it is doing the thing it always does, in a place where it has nothing to go on. Treat hallucination and confabulation as the same event described by people with different priorities."
      test: "Ask the same question three times in separate sessions. Facts stay put. Confabulations tend to move."
    - id: "faithfulness"
      term: "Faithfulness"
      aka: "groundedness · attribution · the opposite is unfaithful"
      plain: "Whether the output stays true to a source you supplied, as opposed to whether it is true about the world."
      why: "This is the one that changes how you read everything else. Faithfulness is measured against your document, not against reality, so the two can come apart in both directions. A summary can add a claim that is perfectly true and still be unfaithful, because your paper never said it. A summary can also reproduce an error from your source and be entirely faithful. When an evaluation reports faithfulness and accuracy as separate numbers, this is why."
      test: "Take the output a sentence at a time and find the line in your source that supports it. Anything you cannot point at is unfaithful, whether or not it happens to be correct."
    - id: "sycophancy"
      term: "Sycophancy"
      aka: "caving · agreement bias"
      plain: "The model changes its answer because you pushed, not because you gave it a reason."
      why: "Models are tuned on human approval, and humans approve of being agreed with. The result is a system whose confidence tracks your mood rather than the evidence. It matters most in exactly the situation where you would want a second opinion: you already suspect something, and you are asking to check."
      test: "Get an answer, then say you think it is wrong without saying why. An answer that reverses under content-free pressure was never telling you anything about the question."

# ── §3 The measurement vocabulary ──────────────────────────────────────────────
measuring:
  title: "Words you hit as soon as people start measuring"
  desc: "The four above are what goes wrong. These five are how people argue about how often it goes wrong, and they are most of the remaining fog in an evaluation thread."
  callout: "Worth knowing before you read any leaderboard: a benchmark score is an average over a fixed list of questions that everyone can see. Models are trained on the public internet, which now includes those questions. A high score can mean the model is good, or that the test leaked into its training data. This is called <strong>contamination</strong>, and it is the single most common reason a model that tops a chart disappoints on your actual work."
  items:
    - term: "Benchmark"
      body: "A fixed set of questions with known answers, run against every model so the numbers can be compared. Useful for ranking, weak evidence about your particular task, since your task is not on the list."
    - term: "Eval"
      body: "Short for evaluation, and used for anything from a formal benchmark to a spreadsheet of twenty prompts someone tried by hand. When somebody says they ran an eval, ask which kind. The gap between those two is enormous."
    - term: "RAG, and grounding"
      body: "Retrieval-augmented generation: the system looks things up and puts what it found into the prompt before answering. This is what most tools mean by connecting to your documents. It is the main defence against hallucination and the main reason faithfulness becomes the number that matters, because now there is a source to be faithful to."
    - term: "LLM-as-a-judge"
      body: "Using one model to grade another model's output, because grading by hand does not scale. Cheap and surprisingly serviceable, with a known flaw: judges favour longer, more confident answers, and favour output from the model family they belong to."
    - term: "Context window"
      body: "How much text the model can hold at once, prompt and answer together. Exceeding it does not produce an error; the earliest material simply stops being available, which is a quiet way to make a long session go wrong."

# ── §4 The map ─────────────────────────────────────────────────────────────────
map:
  title: "How the four fit together"
  desc: "Two independent questions, which is why you can be caught by one failure while carefully checking for the other."
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
      term: "Hallucination · Confabulation"
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

# ── §5 ─────────────────────────────────────────────────────────────────────────
closing:
  title: "What to actually do with this"
  paras:
    - "You do not need to run an evaluation every time you hand a model a task. This page is here for reading the ones other people run: when a colleague says a model is unfaithful, or a vendor says theirs hallucinates less, you know which claim is being made and what would count as evidence."
    - "Hold any single result loosely. Models differ from one another and from their own earlier versions, sometimes sharply, and how well one does depends as much on the task you gave it as on the model itself. A number from someone else's evaluation, run on someone else's task, is not on its own a reason to adopt a model or to rule one out."
    - "So keep trying things, and keep half an eye on what is being released. The model that suits you is the one that holds up on your own work, which you find by putting your own work through it."
  note: "Terminology here follows ordinary usage in current evaluation writing. It is not settled: hallucination and confabulation are actively argued over, and faithfulness is measured differently by different groups. If something on this page conflicts with a definition you rely on, the definition you rely on is probably the one to keep."
---
