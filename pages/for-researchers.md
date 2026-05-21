---
layout: researchers
title: AI for Researchers
description: Practical AI guidance across research tasks — literature review, coding, analysis, writing, and grants — with honest notes on risks.
permalink: /for-researchers/
css: /assets/css/researchers.css

header:
  heading: "AI for Your Research."
  subtext: "Practical guidance across research tasks — with honest notes on where AI falls short."

phases:
  - id: litreview
    num: "01"
    sidebar_label: "Literature Review"
    title: "Literature Review & Discovery"
    subtitle: "Orienting yourself in a field"
    callout: "<strong>Research doesn't follow a straight line</strong> — and neither does AI use. The phases below often overlap, repeat, and happen in any order. Use this as a menu, not a sequence."
    helps:
      - "Summarizing papers and identifying key claims"
      - "Finding gaps and contradictions across a body of literature"
      - "Explaining jargon from adjacent fields"
      - "Generating search queries and keyword variations"
      - "Drafting annotated bibliographies"
    risks:
      - "Models hallucinate citations — always verify DOIs before use"
      - "Training cutoffs mean recent work may be missing entirely"
      - "Summaries can flatten nuance or misrepresent methodology"
      - "AI-generated search queries may reinforce existing biases"
    prompt: |
      I'm reviewing literature on [topic]. Here are 3 abstracts: [paste].
      What are the key claims? Are there contradictions or gaps?
      Suggest 3 search queries I haven't tried yet.
    tools:
      - fn: "chat"
        label: "Chat & Assistant"

  - id: design
    num: "02"
    sidebar_label: "Research Design"
    title: "Research Design & Hypotheses"
    subtitle: "Structuring your inquiry"
    helps:
      - "Stress-testing hypotheses and assumptions"
      - "Brainstorming confounds and alternative explanations"
      - "Comparing study design approaches across fields"
      - "Reviewing methods protocols from adjacent disciplines"
    risks:
      - "AI anchors on common designs — niche field-specific norms often missed"
      - "Brainstormed confounds may be plausible but domain-wrong"
      - "No IRB or ethics awareness — AI cannot substitute for institutional review"
    prompt: |
      I'm designing a study to test [hypothesis]. My approach: [describe].
      Act as a skeptical reviewer: what are the 3 most likely confounds?
      What alternative designs would address them?
    tools:
      - fn: "chat"
        label: "Chat & Assistant"

  - id: coding
    num: "03"
    sidebar_label: "Coding"
    title: "Coding & Scripting"
    subtitle: "Automating and building research tools"
    helps:
      - "Writing Python / R / STATA scripts from scratch or from a description"
      - "Debugging errors and tracing unexpected outputs"
      - "Translating code between languages (e.g., STATA → Python)"
      - "Automating repetitive data collection or file-processing tasks"
      - "Setting up reproducible analysis environments and pipelines"
    risks:
      - "Generated code can look correct but produce silently wrong results — always test on known data"
      - "AI cannot reason about your specific dataset structure without seeing a sample"
      - "Version mismatches and deprecated APIs are common in generated code — check the docs"
      - "Do not paste private, IRB-restricted, or personally identifiable data into any commercial tool"
    prompt: |
      Here is a Python error I'm getting: [paste error + relevant code].
      What is causing it? Fix the issue and explain what was wrong
      so I understand and can avoid it next time.
    tools:
      - fn: "coding"
        label: "Coding"
      - fn: "ide"
        label: "IDE Integration"

  - id: analysis
    num: "04"
    sidebar_label: "Data & Analysis"
    title: "Data Collection & Analysis"
    subtitle: "Working with evidence"
    helps:
      - "Data cleaning and wrangling pipelines"
      - "Generating and iterating on visualizations"
      - "Writing and debugging Python / R analysis scripts"
      - "Explaining statistical output in plain language"
      - "Coding qualitative interview transcripts"

    risks:
      - "Generated code may be syntactically correct but logically wrong — validate all outputs"
      - "Do not input sensitive or IRB-restricted data into commercial tools"
      - "Statistical interpretations can be confidently wrong — verify with a domain expert"
      - "Qualitative coding may miss cultural context and researcher positionality"
    prompt: |
      Here is the output of my regression in R: [paste].
      Explain each coefficient in plain language.
      Flag anything that looks unusual or worth investigating.
    tools:
      - fn: "coding"
        label: "Coding"
      - fn: "ide"
        label: "IDE Integration"

  - id: writing
    num: "05"
    sidebar_label: "Writing"
    title: "Writing & Communication"
    subtitle: "Shaping and sharing your findings"
    helps:
      - "Drafting and restructuring sections"
      - "Adapting writing for different audiences"
      - "Editing for clarity and concision"
      - "Drafting abstracts, cover letters, and lay summaries"
    risks:
      - "AI prose tends toward over-polished generic voice — revise to preserve your own style"
      - "Factual claims can be smoothly stated but wrong — never trust without verification"
      - "Check your institution's and target journal's AI-disclosure policies"
      - "AI editing can inadvertently soften claims in ways that change your argument"
    prompt: |
      Here is my methods section: [paste].
      You are a reviewer from [adjacent field] with no deep background in my specialty.
      Give me detailed feedback on clarity, structure, and accessibility — where did you
      lose the thread, what terms need defining, what could be reordered?
      Do not rewrite; give specific, actionable suggestions I can act on myself.
    tools:
      - fn: "chat"
        label: "Chat & Assistant"

  - id: grants
    num: "06"
    sidebar_label: "Grants & Proposals"
    title: "Grants & Proposals"
    subtitle: "Making the case for your work"
    helps:
      - "Tailoring proposals to funder priorities"
      - "Checking whether your framing and proposal sections meet call-specific requirements (management plan, timeline, broader impacts, etc.)"
      - "Strengthening Significance and Innovation sections"
      - "Simulating reviewer feedback before submission"
    risks:
      - "<strong class=\"pink-text\">Check funder AI policy first</strong> — NIH, NSF, and many foundations restrict AI use in proposals"
      - "AI-generated grant text can trigger AI-detection flags"
      - "Preliminary data sections should never rely on AI-generated figures"
      - "Simulated reviewer feedback is generic — it cannot replicate actual study section dynamics"
    prompt: |
      Here is my Specific Aims draft: [paste].
      Act as an NIH study section reviewer.
      What are the 2–3 weakest points? Rewrite the opening paragraph
      to hook reviewers immediately.
    tools:
      - fn: "chat"
        label: "Chat & Assistant"
---
