---
layout: students
title: AI for Students
description: Practical AI guidance for SAS students — coursework tasks, prompts, student scenarios, and curated AI news.
permalink: /for-students/
css: /assets/css/students.css

header:
  heading: "AI for Students."
  subtext: "Explore what AI can do for your coursework, research, and career — and how to stay in the driver's seat."

course_rules_banner:
  title: "Course rules come first."
  body: "These examples are not permission to use AI on an assignment. Some instructors permit AI for brainstorming, feedback, or debugging; others prohibit it — under Penn's Code of Academic Integrity, using AI without your instructor's permission can constitute unauthorized assistance or plagiarism. Before using AI on graded work, check the syllabus or ask your instructor. When AI use is permitted, follow the instructor's disclosure or citation requirements."
  data_note: "Do not upload personal information, unpublished research, or other sensitive data. Course materials — readings, slides, lecture notes — are often copyrighted and may be covered by your course's AI policy, so check before sharing them with an AI tool. For anything involving coursework or personal data, prefer Penn-licensed AI tools."
  link_label: "See which tools are Penn-licensed →"
  link_url: "/tools/"

labels:
  tasks_title: "Find your task"
  tasks_desc: "Pick a coursework area — expand to see where AI may help, what to watch for, and prompts to try."
  helps_heading: "When permitted, AI may help with"
  tools_heading: "Useful AI functions"
  risks_heading: "Watch out for"
  do_heading: "Do"
  dont_heading: "Don't"
  prompts_heading: "Prompts to try"
  external_tools_heading: "Penn resources first — third-party examples are not endorsements"
  library_title: "Prompt library"
  library_desc: "Copyable prompts for coursework — filter by discipline or intent. Check the label on each prompt: many require your instructor's permission before use on coursework."
  scenarios_title: "Student stories"
  scenarios_desc: "Fictional composite scenarios — swipe or use arrows to browse."
  scenario_tried: "What they tried"
  scenario_worked: "What worked"
  scenario_didnt: "What didn't"
  sidebar_label: "On this page"
  status_labels:
    independent: "Independent study"
    permission: "Coursework: permission required"

disclosure_template:
  heading: "AI-use disclosure template"
  desc: "When your instructor permits AI and asks you to disclose it, a note like this covers what most policies want to see."
  text: |
    AI-use note: I used [tool] to [brainstorm/check/debug/explain].
    I provided [type of material]. I verified the output by [method].
    The final prose, code, analysis, and conclusions are my own
    except where specifically noted.
  note: "Use this only if it matches your instructor's disclosure requirements. If your course requires formal citation instead, APA, Chicago, and MLA each publish citation formats for AI tools."

tasks_disclaimer: "Tools and links in this section are listed for reference and exploration only. DDDI does not advertise, recommend, or endorse any specific product. Check access, cost, privacy, and your course or employer policies before use."

tasks:
  - id: writing
    title: "Writing"
    subtitle: "Essays, reflection papers, personal statements"
    helps:
      - "Challenging a thesis you developed — spotting gaps, leaps, and counterarguments"
      - "Getting feedback on clarity and argument flow in your drafts"
      - "Checking your own reading of a difficult passage"
    risks:
      - "AI prose can sound polished but generic — your voice matters"
      - "Always check your syllabus and course AI policy before using AI on graded work"
    dos:
      - "Start from your own thesis and notes — use AI to question them, not to write"
      - "Ask for critiques and questions, not finished paragraphs"
      - "Write from your own notes and argument — never paraphrase AI-generated text into a submission"
    donts:
      - "Submit AI-generated text as your own writing"
      - "Skip reading the source material AI summarizes"
      - "Assume AI knows your professor's expectations"
    prompts:
      - label: "Test your thesis"
        status: permission
        text: |
          Here is my tentative thesis and the evidence I plan to use: [paste].
          Identify one unsupported leap, one plausible counterargument,
          and one question I need to answer.
          Do not rewrite the thesis or propose a replacement.
      - label: "Peer feedback"
        status: permission
        text: |
          Here is a draft paragraph from my essay: [paste].
          Act as a thoughtful peer reader. Tell me where the argument is unclear
          and what evidence is missing. Do not rewrite my paragraph.
      - label: "Check your reading"
        status: independent
        text: |
          Here is a passage from [text/author] and my own explanation of it: [paste both].
          Tell me what I may be misunderstanding and point to words or sentences
          in the passage that I should examine more closely.
          Do not replace my interpretation with yours.
    tools:
      - fn: chat
        label: "Chat & Assistant"

  - id: quantitative
    title: "Quantitative Work"
    subtitle: "Problem sets, stats homework, data interpretation"
    helps:
      - "Explaining the relevant concept after you have attempted a problem"
      - "Checking reasoning you have already written out, step by step"
      - "Checking your interpretation of statistical output against the numbers"
    risks:
      - "AI can solve problems correctly but skip the reasoning you need to learn"
      - "Double-check all calculations — models make arithmetic errors"
    dos:
      - "Attempt the problem first and show AI your approach"
      - "Ask for hints and explanations, not full solutions"
      - "Verify every step yourself before moving on"
    donts:
      - "Submit AI-generated work on graded problem sets"
      - "Paste a graded assignment into an AI tool unless course rules permit it"
      - "Trust AI arithmetic without checking"
    prompts:
      - label: "Stuck on a problem"
        status: permission
        text: |
          I attempted this problem and got as far as follows: [describe your approach].
          Do not solve it. Identify the relevant concept, tell me whether
          my approach is promising, and ask me one question that will help me
          determine the next step.
      - label: "Check my work"
        status: permission
        text: |
          Here is my work on this problem: [paste your steps].
          Check my reasoning step by step. If something is wrong,
          tell me which step and why — but don't fix it for me.
    tools:
      - fn: chat
        label: "Chat & Assistant"

  - id: coding
    title: "Coding"
    subtitle: "Debugging strategies, explaining code, practice projects"
    helps:
      - "Explaining error messages and suggesting diagnostic strategies"
      - "Explaining unfamiliar code line by line"
      - "Building practice projects outside graded coursework"
    risks:
      - "Many courses prohibit AI on assignments — working through bugs independently is often the skill being taught"
      - "Generated code can look correct but produce wrong results — always test on small examples"
    dos:
      - "Use AI for personal projects and practice exercises — for coursework only when the instructor explicitly permits it"
      - "Ask for explanations and diagnostic strategies before asking for replacement code"
      - "Test every script on known inputs first"
    donts:
      - "Paste assignment code into an AI system unless the course explicitly permits it"
      - "Use AI-generated code in a submission unless the course permits both the use and the manner of disclosure"
      - "Skip reading the documentation AI references"
    prompts:
      - label: "Debug an error"
        status: permission
        text: |
          If my course policy permits this use: here is the smallest relevant
          code excerpt and the error message: [paste].
          Explain what category of error this is and suggest two diagnostic
          tests I can perform. Do not provide replacement code.
      - label: "Explain code"
        status: permission
        text: |
          Explain this code line by line as if I'm a beginner: [paste code].
          Then suggest one small modification I could try to test my understanding.
    tools:
      - fn: coding
        label: "Coding"
      - fn: ide
        label: "IDE Integration"

  - id: lab
    title: "Lab & Data Reports"
    subtitle: "Checking your methods, results, and figure descriptions"
    helps:
      - "Reviewing your draft methods for missing reproducibility details"
      - "Checking your figure descriptions against the data actually shown"
      - "Structuring notes you already collected"
    risks:
      - "Never use AI to generate or fabricate experimental data"
      - "Never upload human-subject data, identifiable information, unpublished research data, a research group's data, or proprietary material without explicit permission and an approved tool"
    dos:
      - "Write your methods and figure descriptions first, then ask AI to check them"
      - "Use AI to structure notes you already collected"
      - "Write discussion points from your own analysis"
    donts:
      - "Generate fake data or results"
      - "Let AI write conclusions you haven't drawn yourself"
      - "Alter or selectively omit results — retain your raw data and follow the assignment's instructions about including data or appendices"
    prompts:
      - label: "Check your methods"
        status: permission
        text: |
          If my course permits this use: here is my draft methods section
          and my protocol checklist: [paste].
          Identify information required for reproducibility that I have omitted.
          Do not rewrite the section.
      - label: "Check a figure description"
        status: permission
        text: |
          If my course permits this use: here is my figure and my description
          of it: [paste or describe].
          Check whether each claim is directly supported by the axes, data,
          and uncertainty shown. Ask me questions wherever I move from
          observation to interpretation. Do not rewrite my description.
    tools:
      - fn: chat
        label: "Chat & Assistant"

  - id: research
    title: "Research Projects"
    subtitle: "Source discovery, reading papers, thesis prep"
    helps:
      - "Generating search queries to run in Penn Libraries and disciplinary databases"
      - "Previewing abstracts to decide what to read fully"
      - "Pressure-testing thesis ideas you developed from your reading"
    risks:
      - "AI hallucinates citations — always verify DOIs and sources"
      - "Summaries can miss nuance; read the full paper for anything you cite"
    dos:
      - "Use AI for search strategies — do the actual searching in Penn Libraries and disciplinary databases"
      - "Verify every citation before including it"
      - "Read full papers for anything you cite in your work"
    donts:
      - "Trust AI-generated bibliographies without checking"
      - "Cite a paper based only on an AI summary"
      - "Skip the actual reading because AI summarized it"
    prompts:
      - label: "Search strategies"
        status: independent
        text: |
          I'm researching [topic] for a paper in [discipline].
          Suggest 5 search queries I might not have tried,
          including synonyms and adjacent concepts.
          Do not invent specific citations.
      - label: "Abstract preview"
        status: permission
        text: |
          Based only on this abstract: [paste].
          State what the authors claim, what method they report,
          and three questions I should investigate in the full paper.
          Do not infer limitations or results that are not stated in the abstract.
    tools:
      - fn: chat
        label: "Chat & Assistant"

  - id: career
    title: "Career & Beyond"
    subtitle: "Cover letters, interview prep, skill exploration"
    helps:
      - "Outlining cover letters and application materials"
      - "Preparing for interviews with likely questions"
      - "Exploring career paths and skill gaps"
    risks:
      - "Generic AI cover letters stand out — personalize everything"
      - "Interview answers must come from your real experience"
    dos:
      - "Use AI to plan and outline, then write in your voice"
      - "Practice answering AI-generated interview questions aloud"
      - "Remove phone numbers, addresses, ID numbers, and other unnecessary personal information before pasting a résumé or application materials"
    donts:
      - "Submit AI-written cover letters without heavy editing"
      - "Fabricate experiences for interview prep"
      - "Rely on AI to choose your career path for you"
    prompts:
      - label: "Cover letter outline"
        status: independent
        text: |
          I'm applying for [role] at [organization].
          Job description: [paste]. My experiences: [paste].
          Outline a cover letter structure — bullet points per section.
          Don't write the letter.
      - label: "Interview prep"
        status: independent
        text: |
          I have an interview for [role]. Based on this job description: [paste],
          what are 5 questions they might ask? For each, suggest
          what kind of example from my background would be strong.
    tools:
      - fn: chat
        label: "Chat & Assistant"
    external_tools:
      - name: Penn Career Services (Handshake)
        href: "https://careerservices.upenn.edu/"
        desc: "Penn's official career hub — advising, events, and Handshake job and internship listings. Start here."
      - name: Simplify
        href: "https://simplify.jobs/"
        desc: "Third-party example, not an endorsement — AI job search with personalized matches, resume tailoring, application autofill, and a job tracker."
      - name: Jobright
        href: "https://jobright.ai/"
        desc: "Third-party example, not an endorsement — AI job search copilot with matched roles, tailored resumes, and networking suggestions."

scenarios:
  - persona: "Maya · Junior · English"
    discipline: humanities
    context: "Writing a thesis chapter on Victorian poetry"
    tried: "After checking that her course policy allowed AI as a study aid, she asked Claude to build a comparison table of claims she had already identified in three critical essays she'd read."
    worked: "The table helped her see connections between critics. She returned to the original essays, checked every entry, and wrote the literature review directly from her own notes and the sources."
    didnt_work: "The AI table misattributed a quote to the wrong critic. She caught it because she verified every entry against the essays themselves."

  - persona: "James · Sophomore · Biology"
    discipline: stem
    context: "Stuck on a genetics problem set"
    tried: "Pasted the problem into ChatGPT and asked for the solution — without checking whether his course allowed it."
    worked: "Only what came after: he reworked the problem himself, and from then on asked AI to check reasoning he had already written out instead of asking for answers."
    didnt_work: "Copying the solution. The AI skipped a step in the Punnett square reasoning his professor specifically tested, and he got a similar exam question wrong because he hadn't learned the concept."

  - persona: "Priya · Senior · Economics"
    discipline: social_sciences
    context: "Running regressions for her senior thesis"
    tried: "With her advisor's approval, used Copilot in VS Code to debug R scripts — keeping her unpublished thesis data out of the tool. She wrote her own interpretation of each regression before asking AI to critique it."
    worked: "Debugging saved hours. The AI critique flagged wording that overstated her results, and she disclosed the AI assistance in her thesis as her department required."
    didnt_work: "AI once suggested removing a control variable that was actually important. She caught it by cross-checking with her advisor."

  - persona: "Alex · First-year · Undeclared"
    discipline: any
    context: "Exploring whether to take a CS course"
    tried: "Asked ChatGPT to explain what you'd learn in an intro programming course and generate 3 tiny practice exercises."
    worked: "The exercises gave a realistic taste of coding. He tried them, got stuck, tried again — and decided he enjoyed the puzzle-solving."
    didnt_work: "The AI oversimplified how hard the course would be. He still struggled in week 3, but was prepared for that."

  - persona: "Jordan · Junior · Political Science"
    discipline: social_sciences
    context: "Preparing a 10-minute presentation on voting rights"
    tried: "After confirming the course allowed AI for preparation, used it to outline slides and generate practice questions an audience might ask."
    worked: "The outline gave a clear narrative arc. Practicing answers to AI-generated questions made the Q&A less stressful."
    didnt_work: "The AI-suggested hook felt too generic. Jordan replaced it with a personal anecdote from their internship."

  - persona: "Sam · Sophomore · Mathematics"
    discipline: stem
    context: "Working through a difficult proof-based homework set"
    tried: "His course allowed AI for studying but not on submitted work — so he asked AI to explain concepts and analogous examples from lecture notes, never the assigned problems, then reconstructed each proof independently."
    worked: "Step-by-step explanations helped when the textbook was too dense. Reconstructing afterward cemented the logic."
    didnt_work: "When he asked AI to prove a theorem from a practice set, the proof had a subtle error in step 4 that he wouldn't have caught without class."

  - persona: "Nina · First-year · Chemistry"
    discipline: stem
    context: "Weekly problem sets in general chemistry"
    tried: "Considered using AI when stuck, but the syllabus said the problem sets were designed to build the exact skills tested on exams — so she decided not to use AI on them at all."
    worked: "Working through the problems herself was slow at first, but by midterm she could handle new problem types without help — which was the point. She saved AI for quizzing herself on definitions, where the policy allowed it."
    didnt_work: "Early on she peeked at an AI walkthrough for one problem and realized she had absorbed the answer without the reasoning — that's what convinced her to stop."

sections:
  - id: course-tasks
    label: "Find your task"
  - id: prompt-library
    label: "Prompt library"
  - id: scenarios
    label: "Student stories"

scenario_disciplines:
  - id: all
    label: "All"
  - id: humanities
    label: "Humanities"
  - id: stem
    label: "STEM"
  - id: social_sciences
    label: "Social Sciences"
  - id: any
    label: "Any"

---
