---
# Archived — set published: true to bring the page back, then restore the three
# links to it: the nav in _layouts/default.html, the hero button in pages/home.md, and
# the "Teaching a course?" paragraph in pages/for-students.md.
published: false
layout: teaching
title: AI for Teaching
description: "Practical guidance on teaching in a course where every student has an AI assistant: what to change, what to keep, and how to decide."
permalink: /for-teaching/
css: [/assets/css/guide.css, /assets/css/teaching.css]

header:
  heading: "AI for Teaching"
  subtext: "What to change in your course, what to keep, and how to decide."

labels:
  sidebar_label: "On this page"
  mode_label: "Where you are"
  sequence_label: "A suggested order"
  helps_heading: "Where AI genuinely helps"
  keep_heading: "Keep this yours"
  tools_heading: "Useful AI functions"
  risks_heading: "Watch out for"
  rail_heading: "Keep in mind"
  do_heading: "Do"
  dont_heading: "Don't"
  prompts_heading: "Prompts to try"
  tasks_title: "Find your task"
  tasks_desc: "Pick a teaching task to see where AI helps, what it costs, and prompts to try."
  assessment_title: "AI-resilient assessment"
  assessment_desc: "How to keep an assignment meaningful when the model can do it in nine seconds."
  shifts_label: "Four shifts"
  makeovers_label: "Assignment makeovers"
  makeover_before: "Before"
  makeover_after: "After"
  makeover_breaks: "Why it breaks"
  makeover_measures: "What it now measures"
  makeover_cost: "What it costs you"
  policy_title: "Your course AI policy"
  policy_desc: "How to decide what your policy should say — and why this page does not hand you one to paste."
  stances_label: "Four stances"
  stance_fits: "Fits when"
  stance_tradeoff: "The trade-off"
  stance_watch: "Most likely to go wrong"
  must_answer_label: "Your policy has to answer"
  failure_modes_label: "Where policies fail"
  mode_labels:
    adapt: "Revising an existing course"
    build: "Building a new course"

tasks_disclaimer: "Tools and links on this page are listed for reference and exploration only. DDDI does not advertise, recommend, or endorse any specific product. Check access, cost, privacy, and Penn and departmental policy before use."

sections:
  - id: start-here
    label: "Start here"
    sub: blocks
  - id: teaching-tasks
    label: "Find your task"
    sub: tasks
  - id: assessment
    label: "AI-resilient assessment"
  - id: ai-policy
    label: "Your course AI policy"

default_section: start-here

divisions:
  - id: all
    label: "All"
  - id: humanities
    label: "Humanities"
  - id: social-sciences
    label: "Social Sciences"
  - id: natural-sciences
    label: "Natural Sciences"

# ─────────────────────────────────────────────────────────────
# Tab 1 — Start here
# ─────────────────────────────────────────────────────────────
start_here:
  title: "Start here"
  desc: "What changed, what it means for your course, and the constraints you are teaching inside. Worth reading once before you change anything."
  blocks:
    - heading: "Run your own assignment through the model"
      paras:
        - >-
          Before reading further, do this: take the assignment you care most about — the
          term paper prompt, the problem set, the lab report spec — paste it into Claude or
          ChatGPT exactly as your students receive it, and read what comes back.
        - >-
          If it produces something you would grade in the B range or above, that assignment
          no longer measures what you designed it to measure. It measures access to a tool
          every student already has. This is not a prediction about the future; it is a fact
          about your course as it currently runs.
        - >-
          Most faculty find the result uncomfortable and clarifying in roughly equal measure.
          It also tells you where to spend your effort: usually two or three assignments are
          badly exposed and the rest are fine. You are looking for those two or three, not
          for a reason to rebuild the whole course.
    - heading: "AI is a teaching assistant, not a replacement"
      paras:
        - >-
          The gains here are real but bounded. A model can draft a rubric, generate twenty
          practice problems, restructure a lecture, or cluster three hundred course
          evaluations into themes — work that is genuinely tedious and genuinely yours to
          check. It cannot decide what your course is for, what a student in your field needs
          to be able to do, or which of two defensible approaches is right for this room.
        - >-
          Treat it the way you would a capable first-year graduate assistant: give it context
          and constraints, let it produce a first pass, and read the output as a draft rather
          than an answer. You remain the instructor of record for everything that reaches
          your students.
    - heading: "Trust, but verify"
      paras:
        - >-
          Models are fluent and confident well past the edge of what they actually know. In
          a teaching context the specific failure modes are worth naming: fabricated
          citations in a reading list, worked solutions with a plausible error in the middle
          step, historical or empirical claims that are almost right, and confident
          statements about disciplinary conventions that are simply wrong for your field.
        - >-
          The material you put in front of students carries your name. Verify anything
          factual, and work every generated problem yourself before assigning it.
    - heading: "Student work is an education record"
      paras:
        - >-
          <!-- TODO(verify): confirm exact Penn guidance with the Provost's office, SAS
               Computing, and/or the Office of General Counsel before this page goes live.
               Wording below is deliberately conservative. -->
          Student submissions are education records, and putting them into a commercial AI
          tool means disclosing them to a third party. Do not upload identifiable student
          work — papers, exams, code, or anything carrying a name or PennID — to a
          general-purpose consumer AI tool.
        - >-
          Where you want AI assistance with grading, prefer
          <a href="https://pennchat.upenn.edu/" target="_blank" rel="noopener">PennChat</a>
          or another Penn-licensed and reviewed tool, remove identifying information first,
          and confirm the current rules with your department and with
          <a href="%BASEURL%/tools/">Penn's tool guidance</a> before you build it into your
          workflow. This is the one item on this page where getting it wrong has consequences
          beyond a disappointing output.
    - heading: "You may not have the right to upload your course materials"
      paras:
        - >-
          Assigned readings, textbook chapters, publisher test banks, and slides a colleague
          shared with you are typically licensed, not owned. Uploading them to a commercial
          tool can breach that licence regardless of how convenient it is.
        - >-
          Material you wrote yourself is a different matter, and is usually the highest-value
          thing to give a model anyway: your own lecture notes, your own assignment prompts,
          your own past exams. Prefer
          <a href="%BASEURL%/tools/">Penn-licensed tools</a>, particularly PennChat, which
          stays inside the Penn community and does not train models on what you put into it.
    - heading: "Detection does not work; disclosure does"
      paras:
        - >-
          AI detectors are unreliable in both directions. They miss AI-written text routinely,
          and they flag human writing as machine-generated often enough that using them as
          evidence puts you in the position of making a serious accusation on the basis of a
          number you cannot explain or defend. Non-native English speakers are
          disproportionately misflagged.
        - >-
          The workable alternative is structural rather than forensic: require a short
          disclosure statement with each submission, design assignments where undisclosed AI
          use would be visible in the work itself, and make the expectation specific enough
          that students can actually comply. A student who knows exactly what is permitted
          rarely needs to be caught.
    - heading: "Norms vary sharply by department"
      paras:
        - >-
          Nothing on this page overrides what your department expects. Attitudes across the
          School differ more than any general guidance can capture — practices that are
          uncontroversial in a computational methods course can be unacceptable in a
          language seminar or a writing-intensive first-year course, and colleagues in your
          own department may hold sharply different views.
        - >-
          Before you change how a course is assessed, find out what your chair, your
          undergraduate curriculum committee, and the colleagues who teach the courses on
          either side of yours actually expect. This page is a starting point for that
          conversation, not a substitute for it.

# ─────────────────────────────────────────────────────────────
# Tab 2 — Find your task
# ─────────────────────────────────────────────────────────────
modes:
  - id: adapt
    label: "Revising an existing course"
    blurb: >-
      You have a syllabus that worked. The question is which parts still do, and what to
      change without rebuilding the course from nothing.
    sequence:
      - num: "01"
        title: "Stress-test what you assign"
        desc: "Run two or three assignments through a model as your students receive them. Read the output before deciding anything."
        task: assessment
      - num: "02"
        title: "Triage, don't rebuild"
        desc: "Sort assessments into still works, needs reworking, and now measures nothing. Most courses have only two or three in the last group."
        task: assessment
      - num: "03"
        title: "Rework the exposed ones"
        desc: "Change those assignments, not the whole course. The four shifts under AI-resilient assessment are where to start."
        task: assessment
      - num: "04"
        title: "Set your policy"
        desc: "Decide what is permitted, assignment by assignment, and write it down in terms students can act on."
        task: materials
      - num: "05"
        title: "Tell students why"
        desc: "Put the reasoning in the syllabus and say it out loud in week one. A rule without a reason gets reinterpreted."
        task: materials
  - id: build
    label: "Building a new course"
    blurb: >-
      Nothing exists yet. You can design assessments that hold up from the start, rather
      than retrofitting them later.
    sequence:
      - num: "01"
        title: "Decide what students should be able to do"
        desc: "Write objectives concrete enough that you could tell, from a piece of work, whether a student met them."
        task: design
      - num: "02"
        title: "Sequence the material"
        desc: "Compare two or three orderings and their trade-offs before committing to a week-by-week plan."
        task: design
      - num: "03"
        title: "Anticipate where students get stuck"
        desc: "List the misconceptions you expect, then build the explanations and activities around them."
        task: classroom
      - num: "04"
        title: "Design assessments up front"
        desc: "Decide how each objective is evidenced — and check each assessment against a model before it exists on a syllabus."
        task: assessment
      - num: "05"
        title: "Draft the materials"
        desc: "Syllabus, problem sets, readings, slides. This is the fastest part, and the part most worth generating drafts for."
        task: materials

tasks:
  - id: design
    title: "Course design & objectives"
    subtitle: "Deciding what the course is for"
    intro:
      adapt: >-
        Your objectives already exist, though they may live in your head rather than the
        syllabus. The useful work here is surfacing them, then checking honestly whether what
        you assess still lines up with what you say the course is for. Drift accumulates
        quietly over a decade of teaching the same course.
      build: >-
        Nothing constrains you yet, which is the opportunity and the trap. The common failure
        is writing objectives that read well and cannot be assessed — "students will
        appreciate the complexity of…" gives you nothing to grade against. Push every
        objective until you could look at a piece of student work and say whether it was met.
    keep_yourself:
      - "What the course is for, and which of the many defensible versions of this course you are teaching"
      - "Which objectives matter enough to spend limited weeks on, and which are nice to have"
      - "What counts as good work in your field, at this level"
    helps:
      - "Turning a vague aim into objectives specific enough to assess against"
      - "Checking whether your objectives, your weekly topics, and your assessments actually align — and naming where they don't"
      - "Proposing two or three alternative sequences for the same material, with the pedagogical trade-off of each"
      - "Surfacing prerequisites you have stopped noticing you assume"
      - "Comparing your coverage against publicly posted syllabi in the same subfield"
    risks:
      - "Models anchor hard on the most common version of a course; a distinctive or heterodox syllabus reads to them as a mistake to be corrected"
      - "Generated objectives drift toward generic Bloom's-taxonomy phrasing that sounds rigorous and constrains nothing"
      - "Suggested coverage reflects what is widely published in English, not what your field currently argues about"
      - "It cannot know your students' actual preparation, your enrollment, or what the department needs this course to do"
    dos:
      - "Give it your existing syllabus and ask what it thinks the course is for, then compare that to your intent"
      - "Ask it to argue for a sequence you rejected, so you can see the case against your choice"
      - "Ask which of your objectives your assessments do not actually test"
    donts:
      - "Accept an objective you could not grade against"
      - "Let benchmarking against other syllabi flatten what is distinctive about yours"
      - "Treat its account of disciplinary consensus as reliable without checking"
    prompts:
      - label: "Find the drift"
        mode: adapt
        text: |
          Here is my syllabus, including the assignments and their weights: [paste].
          Infer what this course appears to be for, based only on what is assessed.
          Then list every stated objective that no assessment actually tests,
          and every assessment that tests something not stated as an objective.
          Do not propose fixes yet.
      - label: "Make objectives assessable"
        mode: build
        text: |
          I'm designing a [level] course in [field] on [topic]. My rough aims: [paste].
          Rewrite each as an objective specific enough that I could look at a piece of
          student work and judge whether it was met. For each one, name the kind of
          evidence that would demonstrate it.
          Flag any aim that resists this — those are the ones I need to think harder about.
      - label: "Argue the other sequence"
        mode: build
        text: |
          Here is my planned week-by-week sequence for [course]: [paste].
          Propose one genuinely different ordering of the same material.
          For each, give the pedagogical argument in favour and what it costs.
          Be concrete about which topics become harder to teach under each.
      - label: "Surface hidden prerequisites"
        text: |
          Here is week [n] of my [field] course: [topic, readings, planned activity].
          List what a student must already understand to follow this,
          including things an experienced instructor stops noticing they assume.
          Mark which of these my earlier weeks actually cover.
    tools:
      - fn: chat
        label: "Chat & Assistant"

  - id: materials
    title: "Syllabus & materials"
    subtitle: "Drafting what students read and receive"
    intro:
      adapt: >-
        Most of your materials are fine and do not need touching. The work concentrates in
        two places: syllabus language about AI, which probably does not exist yet or is a
        single vague sentence, and any handout whose instructions assume students cannot get
        outside help. This is also where you explain your reasoning to students.
      build: >-
        This is the fastest part of building a course and the part where a model saves the
        most real time — drafting a syllabus, generating problem sets, converting a dense
        source into a teachable form. It is also where generated material is most likely to
        be subtly wrong in ways students will find before you do.
    keep_yourself:
      - "Every worked solution and answer key — do the problem yourself before it goes out"
      - "The reasoning you give students for your AI policy; borrowed reasoning does not survive a challenge"
      - "Selection of readings, which is a scholarly judgment and the thing your students are paying for"
    helps:
      - "Drafting syllabus sections you write from scratch every time: schedules, policies, expectations"
      - "Converting a dense source into a teaching format — a reading guide, a one-page summary, a set of discussion questions at graduated difficulty"
      - "Generating problem sets and practice items at a specified difficulty, with the wrinkle each one tests"
      - "Producing worked examples and alternative explanations of a concept students reliably find hard"
      - "Building the tedious scaffolding: timelines, comparison tables, decision trees, glossaries"
    risks:
      - "Generated problems can be subtly unsolvable, ambiguous, or have a different answer than the key claims — work every one yourself"
      - "Uploading licensed readings, publisher materials, or a colleague's slides may breach the licence"
      - "Reading lists come back with fabricated citations that look entirely plausible; verify every one"
      - "Generated prose drifts toward a flat institutional register that does not sound like you, and students notice"
      - "Difficulty calibration is unreliable — what a model calls 'advanced' rarely matches your course"
    dos:
      - "Give it your own past materials as the model for tone, format, and level"
      - "Ask for more items than you need and select, rather than accepting a set"
      - "Solve every generated problem before it reaches students"
    donts:
      - "Upload a textbook, publisher test bank, or a colleague's materials"
      - "Assign a reading you have not confirmed exists and read yourself"
      - "Ship generated prose in your syllabus without rewriting it in your own voice"
    prompts:
      - label: "Draft your syllabus AI section"
        mode: adapt
        text: |
          Here is my syllabus and my assignment list: [paste].
          I want to permit AI for [X] and prohibit it for [Y], because [reasoning].
          Draft syllabus language that states this in terms a student could actually act on
          — naming specific actions, not general attitudes — and that explains my reasoning.
          Then list the edge cases my wording leaves ambiguous.
      - label: "Turn a source into teaching material"
        text: |
          Attached is [reading/source] that I assign in week [n] of a [level] [field] course.
          Produce: a one-page reading guide, five discussion questions ordered from
          comprehension to synthesis, and the two passages students most often misread,
          with what they get wrong.
          Do not summarise the source in place of the students reading it.
      - label: "Generate graduated practice"
        mode: build
        text: |
          Write [n] practice problems on [topic] for a [level] [field] course,
          ordered from routine application to genuinely difficult.
          For each: the problem, a full worked solution, and one line naming
          the specific thing it tests.
          Flag any problem where a competent student could reasonably read the prompt
          two different ways.
    tools:
      - fn: chat
        label: "Chat & Assistant"

  - id: classroom
    title: "Lectures & activities"
    subtitle: "What happens in the room"
    intro:
      adapt: >-
        The classroom is the part of your course AI has changed least, and the part that has
        become most valuable. Time with students in the room is now the most reliable evidence
        you have of what they can actually do — which is an argument for spending more of it
        on work rather than delivery.
      build: >-
        Design the room around the things that only work in the room: live problem-solving,
        discussion that builds on itself, and the moments where you can see who is lost.
        A model is useful here for generating raw material — examples, questions, activities —
        not for deciding how the ninety minutes should feel.
    keep_yourself:
      - "Reading the room, and changing the plan when it is not landing"
      - "The examples drawn from your own research and your own field experience — those are why students are in your class rather than watching a video"
      - "Deciding which confusions are worth stopping for"
    helps:
      - "Generating fresh examples when your standard one has gone stale or dated"
      - "Building branching question sequences keyed to the answers students actually give"
      - "Listing the ten misconceptions students most commonly hold about a topic, as a design input"
      - "Producing the same concept explained three ways for students who did not get it the first way"
      - "Designing in-class activities to a constraint — fifteen minutes, groups of four, no laptops"
    risks:
      - "Generated examples skew toward the canonical and the American; they will not reflect your students or your field's current debates"
      - "Its list of 'common misconceptions' is a plausible reconstruction, not evidence from your classroom — treat it as hypotheses to check"
      - "Activities come back optimistically timed; assume they take longer than stated"
      - "Over-scripted question sequences make discussion worse, not better"
    dos:
      - "Give it the specific confusion you saw last time you taught this"
      - "Ask for more examples than you need and pick the ones that fit your students"
      - "Use its misconception list as a hypothesis to test against your own past exams"
    donts:
      - "Replace examples from your own work with generated ones"
      - "Follow a generated question sequence at the cost of where the discussion actually wants to go"
      - "Assume its timing estimates survive contact with a real room"
    prompts:
      - label: "Fresh examples for a stale topic"
        text: |
          I teach [concept] in a [level] [field] course. My standard example is [describe],
          and it has stopped landing.
          Give me six alternative examples at the same conceptual level, varying in domain
          and in how much background they assume.
          For each, name what it illustrates well and what it obscures.
      - label: "Build a question sequence"
        text: |
          I want a fifteen-minute discussion on [topic] in a [level] seminar.
          Build a branching sequence: an opening question, then for each of the three
          most likely student responses, the follow-up that pushes the reasoning further.
          Include the answer that would tell me they have missed the point, and how to
          recover from it.
      - label: "Map the misconceptions"
        text: |
          List the ten errors students most commonly make when learning [topic]
          in [field], ordered by how often you would expect them.
          For each: what the student is probably thinking, why it is intuitive,
          and the question that would surface it quickly in class.
    tools:
      - fn: chat
        label: "Chat & Assistant"

  - id: assessment
    title: "Assignments & assessment"
    subtitle: "How you find out what students learned"
    intro:
      adapt: >-
        This is where the work is. Start by running your existing assignments through a model
        exactly as students receive them, then sort the results: still works, needs reworking,
        now measures nothing. Most courses have two or three assignments in the last category
        and the rest are fine — resist the urge to redesign everything at once.
      build: >-
        Designing assessments before the course exists means you can build in AI resilience
        rather than retrofitting it. The discipline to hold: draft the assignment, then run it
        through a model yourself before it ever reaches a syllabus. If the model does it well,
        redesign it now, while changing it costs nothing.
    keep_yourself:
      - "The judgment of what constitutes evidence that a student learned this"
      - "Where the line falls between assistance and substitution in your field"
      - "Final grading decisions, and every borderline case"
    helps:
      - "Stress-testing an assignment by attempting it, so you can see what a student with the same tool would produce"
      - "Proposing redesigns that keep the learning goal but resist unassisted generation"
      - "Drafting issue-by-issue rubrics, then testing them against sample answers to check they discriminate"
      - "Generating exam questions at a stated difficulty, with the reasoning each one tests"
      - "Designing process-based scaffolding: proposal, annotated draft, revision memo, reflection"
    risks:
      - "A model attempting your assignment shows you one output, not the distribution — try it two or three times"
      - "Generated rubrics tend to reward completeness over insight unless you push back explicitly"
      - "Redesign suggestions default to more work for you; ask what it costs before adopting"
      - "AI-resilient assignments are usually more labour-intensive to grade, and that cost is real"
      - "Difficulty calibration is unreliable; check generated exam items against your own past papers"
    dos:
      - "Attempt your own assignment with the model before changing anything"
      - "Ask explicitly what the redesign costs you in grading time"
      - "Test a draft rubric against two or three real past submissions before you use it"
    donts:
      - "Redesign every assessment at once"
      - "Adopt a redesign whose grading burden you have not counted"
      - "Assume an assignment is resilient because it is hard — difficulty and resistance are different properties"
    prompts:
      - label: "Stress-test an assignment"
        text: |
          Below is an assignment prompt exactly as my students receive it: [paste].
          Attempt it as a strong student would, at the length specified.
          Then tell me, honestly: what grade would this deserve in a [level] [field] course,
          what does it do well, and where would an expert reader see that it is thin?
      - label: "Triage the assessment mix"
        mode: adapt
        text: |
          Here are all the graded components of my course, with weights and prompts: [paste].
          For each, judge how much of the intended learning a student could skip
          by using AI, and sort them into: still works, needs reworking, measures nothing.
          Order the second group by how cheaply I could fix them.
      - label: "Redesign, with the cost named"
        text: |
          This assignment no longer measures what I intended: [paste].
          The learning goal is [state it].
          Propose three redesigns that keep the goal but resist unassisted AI completion.
          For each, state plainly what it costs me in preparation and grading time,
          and what it costs students in workload.
      - label: "Build and calibrate a rubric"
        text: |
          Here is the assignment and the learning goal: [paste].
          Draft an issue-by-issue rubric with point allocations.
          Then apply it to these sample answers: [paste 2-3].
          Tell me where the rubric fails to separate them, and where it rewards
          completeness rather than the thinking I actually care about.
    tools:
      - fn: chat
        label: "Chat & Assistant"

  - id: feedback
    title: "Grading & feedback"
    subtitle: "Responding to student work"
    intro:
      adapt: >-
        Read the caution on this one before anything else: student work is an education
        record, and putting it into a commercial tool discloses it to a third party. Within
        that constraint, the durable gains are in what surrounds grading rather than grading
        itself — building and calibrating rubrics, drafting comment language, and finding
        the patterns across a set once you have marked it.
      build: >-
        Decide your grading workflow before the first submissions arrive, including what you
        will and will not put into a tool. Retrofitting a privacy-safe process in week ten,
        with a stack of papers on your desk, is how mistakes happen.
    keep_yourself:
      - "Every grade, and the judgment behind it"
      - "The substantive comments — the ones responding to what this particular student is trying to do"
      - "Any decision about academic integrity, without exception"
    helps:
      - "Calibrating a rubric against sample answers before you start marking"
      - "Drafting comment language for issues you find yourself explaining every term"
      - "Clustering the patterns across a set you have already graded, so you know what to reteach"
      - "Rephrasing feedback you have written to be more specific or less discouraging"
      - "Producing worked model answers you can release after an assessment"
    risks:
      - "<strong class=\"pink-text\">Student work is an education record.</strong> Do not upload identifiable student submissions to a general-purpose commercial tool. Prefer Penn-licensed and reviewed tools, de-identify first, and confirm current rules with your department. <!-- TODO(verify): Penn-specific guidance -->"
      - "Models are poor and inconsistent judges of quality in specialist work; scores drift between runs on identical text"
      - "Generated feedback converges on generic advice that applies to any paper, which students recognise immediately"
      - "It cannot see the trajectory — that this draft is a substantial improvement for this student"
      - "Bias in generated assessment of writing is documented and difficult to detect in individual cases"
    dos:
      - "Use it on the rubric and the comment language, not on the student's text"
      - "De-identify anything you do put in, and use a Penn-licensed tool"
      - "Grade first, then ask it to help you find the patterns across what you marked"
    donts:
      - "Upload identifiable student work to a consumer AI tool"
      - "Let a model assign or suggest a grade"
      - "Use AI output as evidence in an academic integrity case"
    prompts:
      - label: "Calibrate before you grade"
        text: |
          Here is my rubric and the assignment it grades: [paste].
          Here are three anonymised sample answers I have already marked, with my scores:
          [paste].
          Where does my rubric fail to explain the difference between these scores?
          Which criteria am I applying that are not written down?
      - label: "Sharpen recurring comments"
        text: |
          Every term I write some version of this comment on student work: [paste yours].
          Rewrite it three ways: more specific about what to do next, shorter,
          and framed so a struggling student can act on it rather than shutting down.
          Keep my voice; do not make it warmer than I wrote it.
      - label: "Find the pattern after marking"
        text: |
          I have finished grading. Here are the issues I noted, with rough frequencies,
          and no student identifiers: [paste].
          Which of these cluster into the same underlying misunderstanding?
          For the two most common, what should I reteach, and how?
    tools:
      - fn: chat
        label: "Chat & Assistant"

  - id: evaluation
    title: "Evaluations & iteration"
    subtitle: "Closing the loop for next time"
    intro:
      adapt: >-
        You have evaluations, past exams, and a memory of what did not work. This is the
        cheapest high-value use of AI in teaching: a hundred free-text comments clustered into
        themes in a minute, including the contradictions that reading them one by one tends to
        hide.
      build: >-
        You have no evaluations yet, so most of this waits until the course has run. What you
        can do now is decide what you will collect and when — a short mid-semester check is
        worth more than end-of-term evaluations you receive after the students have gone.
    keep_yourself:
      - "Deciding which criticism to act on and which to set aside — students report symptoms accurately and diagnose causes unreliably"
      - "Judging whether a low rating reflects a problem with the course or with its difficulty"
      - "The choice of what to cut, which is where a course actually gets better"
    helps:
      - "Clustering free-text evaluation comments into themes and surfacing contradictions"
      - "Tracing systematically missed exam questions back to where and how much that material was taught"
      - "Comparing your intended syllabus against what you actually covered, so next term's cuts are deliberate"
      - "Drafting a concrete revision memo you can react to instead of starting from a blank page"
      - "Designing a mid-semester feedback instrument that asks answerable questions"
    risks:
      - "Thematic clustering flattens the outlier comment, which is sometimes the one that matters most — read the raw text too"
      - "Evaluation comments carry known demographic biases; synthesising them can launder those biases into neutral-sounding themes"
      - "Small classes make evaluation text potentially identifying; treat it accordingly"
      - "It will propose changes that make a course more popular, which is not the same as better"
    dos:
      - "Ask for representative verbatim quotes alongside every theme, and read them"
      - "Ask explicitly where students contradict each other, rather than for a consensus"
      - "Cross-check evaluation themes against what exam performance actually shows"
    donts:
      - "Act on synthesised themes without reading the underlying comments"
      - "Treat satisfaction as a measure of learning"
      - "Paste evaluation text from a small seminar into a consumer tool"
    prompts:
      - label: "Cluster the evaluations"
        text: |
          Here are [n] free-text course evaluation comments, with no identifiers: [paste].
          Group them into themes. For each theme give the approximate share of comments,
          two verbatim quotes, and whether it concerns the course design, my teaching,
          or the workload.
          Separately, list every point on which students directly contradict each other.
      - label: "Autopsy the exam"
        text: |
          Here is my exam, the marking scheme, and the per-question performance data: [paste].
          Here is my syllabus with weekly topics: [paste].
          Which questions did students miss most, and where in the term was that material
          taught and for how long?
          Where does the evidence suggest a teaching problem rather than a hard question?
      - label: "Draft the revision memo"
        text: |
          Based on the evaluation themes and exam analysis above, draft a revision memo
          for the next offering: specific changes, each with the reason and the
          expected cost to me.
          Include at least two things to cut. Do not propose adding without removing.
    tools:
      - fn: chat
        label: "Chat & Assistant"

rail_reminders:
  - id: instructor-of-record
    default: true
    title: "You are the instructor of record"
    body: >-
      Everything that reaches your students carries your name, whatever produced the first
      draft. Verify anything factual, and work every generated problem yourself.
  - id: drift
    title: "Watch for quiet drift"
    body: >-
      A model reads your syllabus as a slightly wrong version of the standard course. Where
      it suggests a correction, check whether you are being improved or flattened.
  - id: solve-it
    title: "Solve it before you assign it"
    body: >-
      Generated problems can be subtly ambiguous or unsolvable, and the answer key can be
      confidently wrong. Working it yourself is the only reliable check.
    for_tasks: [materials]
  - id: room
    title: "The room is now your best evidence"
    body: >-
      Time with students is the most reliable signal you have of what they can actually do.
      That is an argument for spending more of it on work and less on delivery.
    for_tasks: [classroom]
  - id: count-the-cost
    title: "Count the grading cost"
    body: >-
      AI-resilient assignments are usually more work to grade. A redesign you cannot sustain
      through week twelve is worse than the assignment you started with.
    for_tasks: [assessment]
  - id: education-record
    title: "Student work is an education record"
    body: >-
      Do not upload identifiable student submissions to a consumer AI tool. De-identify,
      prefer Penn-licensed tools, and confirm current rules with your department.
    for_tasks: [feedback]
  - id: satisfaction
    title: "Satisfaction is not learning"
    body: >-
      Evaluations measure how a course felt. Useful, but not the same question as whether
      students can do what you set out to teach them.
    for_tasks: [evaluation]

# ─────────────────────────────────────────────────────────────
# Tab 3 — AI-resilient assessment
# ─────────────────────────────────────────────────────────────
assessment:
  title: "AI-resilient assessment"
  desc: "Four shifts that protect what an assignment measures, and six worked examples of applying them. None of this is free — each shift moves work onto you, and the cost is named."
  intro: >-
    The aim is not to make assignments impossible to complete with AI. That is unwinnable and
    the wrong target. The aim is to make the parts you care about — the reasoning, the
    judgment, the engagement with this particular course — the parts that have to be visible
    in the work.
  shifts:
    - num: "01"
      from: "Product"
      to: "Process"
      body: >-
        Grade the trajectory, not only the artifact: a proposal, an annotated draft, a
        revision memo explaining what changed and why, a short reflection on the feedback
        received. These are steps a model cannot retroactively fabricate for work it did not
        do, and they make the thinking visible rather than inferred.
      cost: "More submission points to track, and more of your reading spread across the term rather than concentrated at the end."
    - num: "02"
      from: "Take-home"
      to: "Live"
      body: >-
        Some portion of assessment should happen where you can see it: in-class writing,
        a whiteboard problem, a five-minute oral defence of a submitted paper, a lab
        performed rather than described. It need not be high-stakes — a brief viva on
        submitted work verifies authorship far more reliably than any detector.
      cost: "Class time spent assessing rather than teaching, and scheduling burden that scales badly above roughly forty students."
    - num: "03"
      from: "Generic"
      to: "Situated"
      body: >-
        Anchor the task in material a model was never present for: the argument you made in
        Tuesday's lecture, your lab's own dataset, this week's seminar discussion, a local
        archive, the student's own fieldwork or experience. A prompt that could have been set
        by any instructor anywhere is a prompt a model can answer.
      cost: "Assignments have to be rewritten each time you teach the course; they cannot be reused unchanged for a decade."
    - num: "04"
      from: "Detection"
      to: "Disclosure"
      body: >-
        Detectors are unreliable and produce false accusations, disproportionately against
        non-native English speakers. Replace the forensic approach with a structural one:
        a required disclosure statement on each submission, a policy specific enough to
        comply with, and norms of transparency you establish in week one.
      cost: "Requires a real policy and a real conversation with students, rather than a tool that promises to handle it for you."
  makeovers_desc: "Worked examples. These are constructed illustrations, not case studies from real Penn courses — they will be replaced with faculty examples as the department sessions run this term."
  makeovers:
    - id: lit-close-reading
      division: humanities
      course_type: "Seminar"
      before:
        task: "A 2,000-word essay analysing the use of a named literary device in an assigned novel, due at the end of term."
        why_it_breaks: "The novel, the device, and the critical conventions are all thoroughly represented in training data. A model produces a competent, well-organised, entirely unremarkable version of this essay in under a minute."
      after:
        task: "Students select a passage of fewer than 300 words during a seminar in week six, defend the choice orally in two minutes, and submit an essay that must engage with two specific objections raised by classmates that day, quoted and attributed."
        what_it_now_measures: "Close reading of a passage the student chose and justified in front of witnesses, plus the ability to take seriously an objection they did not anticipate."
        cost_to_you: "One seminar spent on passage selection, notes on who objected to what, and essays that can no longer be graded against a single common text."
    - id: history-source
      division: humanities
      course_type: "Lecture with sections"
      before:
        task: "A source-analysis paper on a document from the assigned reader, addressing context, audience, and reliability."
        why_it_breaks: "Canonical documents come with canonical analyses. The model reproduces the standard reading fluently, including the standard caveats."
      after:
        task: "Students work from a digitised item they locate themselves in a specified Penn Libraries or Philadelphia-area collection, submit a photograph of the item alongside the analysis, and include a paragraph on what they could not determine and why."
        what_it_now_measures: "Locating and handling an actual source, and distinguishing what the evidence supports from what it does not."
        cost_to_you: "A library session to set up, and grading a set of papers on thirty different documents rather than one."
    - id: econ-regression
      division: social-sciences
      course_type: "Problem set"
      before:
        task: "Run the specified regression on the provided dataset, report coefficients, and interpret the results."
        why_it_breaks: "The dataset is standard, the specification is given, and the interpretation is formulaic. The model writes the code and the interpretation together."
      after:
        task: "Students receive the same output but with one specification error deliberately introduced, must identify it, explain what it does to the estimates, and produce the corrected analysis with a memo on what changed substantively."
        what_it_now_measures: "Whether the student can read regression output critically rather than transcribe it — which is the actual professional skill."
        cost_to_you: "Building the flawed variants, and a rubric that credits identifying the error even when the correction is imperfect."
    - id: psych-design
      division: social-sciences
      course_type: "Seminar"
      before:
        task: "Write a research proposal on a topic of your choice in the area of the course."
        why_it_breaks: "Proposals are a highly conventional genre. A model produces a plausible hypothesis, method, and analysis plan with no engagement with the course at all."
      after:
        task: "Proposals must extend or challenge a specific finding from a paper on the syllabus, staged across three submissions: a one-page critique in week four, a design memo in week eight responding to peer critique, and the full proposal in week twelve with a changelog explaining what the earlier feedback changed."
        what_it_now_measures: "Sustained engagement with one paper, and the ability to revise a design in response to criticism."
        cost_to_you: "Three review points instead of one, and peer-review logistics to run."
    - id: bio-lab
      division: natural-sciences
      course_type: "Lab report"
      before:
        task: "A standard lab report on a scheduled experiment: introduction, methods, results, discussion."
        why_it_breaks: "The experiment is well documented and the genre is rigid. Given the expected results, a model writes the entire report, and students who ran the bench work badly can still submit a clean one."
      after:
        task: "Reports must use the group's own recorded measurements, including a required section analysing where their data diverged from the expected result and what in their procedure could account for it. Notebook photographs are submitted alongside."
        what_it_now_measures: "Whether students can reason from the data they actually produced, including when it is messy — which is what lab work teaches."
        cost_to_you: "Grading thirty different sets of imperfect data rather than one expected answer, and being explicit that divergence is not penalised."
    - id: math-proof
      division: natural-sciences
      course_type: "Problem set"
      before:
        task: "Prove the stated theorem."
        why_it_breaks: "For standard results, models now produce correct and well-presented proofs. For non-standard ones they produce confident proofs with an error buried mid-argument."
      after:
        task: "Half the problem set is unchanged and ungraded, for practice. The other half asks students to evaluate three supplied proof attempts — one correct, two with subtle errors — identify precisely where each fails, and repair one of them."
        what_it_now_measures: "Whether the student can verify an argument, which is the skill the course is actually building and the one AI makes most valuable."
        cost_to_you: "Writing convincing flawed proofs is genuinely hard and takes real preparation time."

# ─────────────────────────────────────────────────────────────
# Tab 4 — Your course AI policy
# ─────────────────────────────────────────────────────────────
policy:
  title: "Your course AI policy"
  desc: "How to decide what yours should say."
  intro:
    - >-
      This page does not give you policy language to paste into a syllabus, and the omission
      is deliberate. A policy that fits your course has to follow from what your assessments
      are for, and a template short-circuits exactly the thinking that makes it work. Students
      also detect boilerplate immediately, and a policy that is obviously borrowed invites
      the reading that it is not really meant.
    - >-
      What follows is the decision instead: the four broad stances and what each costs, the
      questions any workable policy has to answer, and the ways policies fail in practice.
      Check your department's and Penn's existing requirements first — those bind, and this
      page does not override them.
  stances:
    - id: prohibited
      name: "Prohibited"
      fits_when: "The course exists to build a skill that AI performs — introductory writing, elementary language acquisition, foundational problem-solving. The thing being automated is precisely the thing being learned."
      tradeoff: "Only credible if your assessments are actually resilient. A prohibition attached to a take-home essay is a rule you cannot enforce and students know it."
      watch_out: "Blanket bans get reinterpreted generously. Without specifics, students genuinely do not know whether grammar checking, translation, or looking up a concept falls inside the ban."
    - id: disclosure
      name: "Permitted with disclosure"
      fits_when: "Most upper-level courses, where AI is a legitimate working tool and the learning goal sits above the level it operates at."
      tradeoff: "Depends entirely on the disclosure being specific and habitual. Vague disclosure — 'I used AI for editing' — tells you nothing and gives false comfort."
      watch_out: "Students under-report, not usually from dishonesty but because they are unsure what counts. Say explicitly what a complete disclosure looks like."
    - id: taught
      name: "Encouraged and taught"
      fits_when: "Courses where AI literacy is itself a defensible outcome — professional preparation, research methods, most computational work."
      tradeoff: "Costs real course time. You are adding an outcome, which means something else gets less attention."
      watch_out: "'Encouraged' without instruction leaves weaker students worse off, since the ability to use these tools well is unevenly distributed on arrival."
    - id: varies
      name: "Varies by assignment"
      fits_when: "Most courses, honestly — a course with both skill-building problem sets and a synthesis paper has two different problems and should not pretend otherwise."
      tradeoff: "The hardest to write and the hardest for students to keep track of. Requires the rule to be restated on every assignment, not only in the syllabus."
      watch_out: "Complexity becomes ambiguity. If a student cannot tell from the assignment sheet alone what is permitted, the policy has failed regardless of how carefully the syllabus explains it."
  must_answer:
    - "<strong>Which actions, specifically.</strong> Not 'no AI' but: may a student use it to check grammar, to translate a source, to explain a concept before starting, to debug code, to generate practice questions, to draft an outline, to draft prose? Each of these is a different question and students will resolve any silence in their own favour."
    - "<strong>Why.</strong> A rule with a reason attached survives challenge and gets followed; a rule without one gets treated as arbitrary and reinterpreted. Two sentences is enough."
    - "<strong>What disclosure looks like.</strong> Where it goes, what it has to contain, and whether it is required on every submission or only when AI was used. Show an example of a complete one."
    - "<strong>What happens if the policy is broken</strong>, and how that connects to Penn's <a href=\"https://catalog.upenn.edu/pennbook/code-of-academic-integrity/\" target=\"_blank\" rel=\"noopener\">Code of Academic Integrity</a>. Unauthorised assistance is already covered there; your policy defines what 'authorised' means in your course."
    - "<strong>Whether it varies by assignment</strong>, and if so, where the authoritative statement lives. It should be on the assignment sheet, not only in a syllabus read once in September."
  failure_modes:
    - "<strong>Too general to comply with.</strong> 'Do not use AI to write your assignments' leaves every interesting case unresolved. Students are not looking for loopholes so much as a decision, and in its absence they make their own."
    - "<strong>Prohibition without redesign.</strong> A ban on an assignment a model can complete in seconds does not protect the assignment; it just shifts the failure out of sight and penalises the students who follow the rule."
    - "<strong>One rule for a course with several kinds of work.</strong> Problem sets that build fluency and a term paper that demonstrates synthesis need different rules. A single policy will be wrong for one of them."
    - "<strong>Rules without reasons.</strong> Students comply with policies they understand and route around policies that read as arbitrary. The reasoning is not decoration."
    - "<strong>Relying on detection.</strong> Detectors are unreliable and misflag non-native English speakers disproportionately. Building a policy on the assumption you will catch violations is building it on sand."
  alignment_note: >-
    Your policy is the other half of something students already see. The
    <a href="%BASEURL%/for-students/">AI for Learning</a> page gives students a disclosure
    template and tells them to check the syllabus first, so it is worth confirming that what
    you require and what they are prepared to provide actually match. Where your department,
    programme, or Penn has existing requirements, those come first — this page is a way to
    think the question through, not a substitute for them.
---
