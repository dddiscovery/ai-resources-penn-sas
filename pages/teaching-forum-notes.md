---
# ── Invitation-only ────────────────────────────────────────────────────────────
# This page is deliberately not linked from anywhere on the site. `private: true` does
# two things: _layouts/default.html emits <meta name="robots" content="noindex, nofollow">
# and the layout shows the "shared by invitation" chip. The permalink carries a random
# suffix so the address cannot be guessed from the site. Anyone who reads this repository
# can still see it, which the team has accepted.
#
# There is intentionally no robots.txt Disallow for this address: robots.txt is a public
# file that crawlers and people read first, so listing the URL there would publish it,
# and a Disallow also stops crawlers from ever seeing the noindex tag.
#
# To make the forum public: set `private: false`, change the permalink to /teaching-forum/,
# and set `published: false` on pages/teaching-forum.md (the request page). The nav already
# points at /teaching-forum/, so nothing else has to move. Drop any `attendees:` lines first.
private: true
layout: forum
title: "Teaching Forum notes | AI Resources for Penn Arts & Sciences"
description: "Notes from Teaching Forum sessions."
permalink: /teaching-forum/notes-6da5be14/
css: [/assets/css/forum.css]

labels:
  private_chip: "Internal · shared by invitation"
  sessions_label: "Sessions"
  themes_label: "What came up"
  questions_label: "To discuss"
  followups_label: "Follow-ups"
  attendees_label: "In the room"

header:
  eyebrow: "Teaching Forum"
  heading: "Notes from the room"
  subtext: "What Penn instructors said when they sat down together to talk about teaching with AI. Pick a month; the newest is first."

# (No opening paragraph. The layout renders an `about:` list of paragraphs if one is added.)

# ── Sessions ───────────────────────────────────────────────────────────────────
# One entry per month, newest first; no exact dates anywhere, by design. `date` is the
# month as shown on the tab and in the session header. `id` is the tab's anchor (it shows
# in the URL as #id, so a link can open a given month) and must be unique.
# Under each theme, `body` is one paragraph or `paras` is several; `questions` lists what
# was left to discuss on that theme. `followups` holds the session's action items.
# `attendees` and `source` (who took the notes this summary is based on) are optional free
# text; leave them out of anything that may go public.
sessions:
  - id: 2026-10
    date: "October 2026"
    title: "What is actually happening in our courses"
    themes:
      - heading: "AI policy consistency"
        body: "Some schools are working toward a unified AI policy through their curriculum committees; others leave it to individual instructors. The sense in the room was that whether AI belongs in a course depends on the course's goals and level, so shared principles may serve better than one rigid rule."
      - heading: "Assessment"
        body: "In introductory computer science and mathematics, problem sets can now be completed almost entirely by AI. Students who lean on it for homework then struggle on no-AI exams, which produces a bimodal grade distribution with a sizeable group near failing. Oral assessments and asking students to explain their reasoning came up as alternatives, with the caveat that they fit some disciplines, engineering for one, more naturally than others."
      - heading: "Scaling"
        body: "The alternatives above work in small classes and are hard to scale."
        questions:
          - "How do we train TAs to run oral assessments fairly and consistently once the class is large?"
      - heading: "Student motivation and culture"
        body: "Fewer students come to office hours or stay after class, and grade pressure pushes them toward shortcuts. People talked about making practice problems more engaging and about keeping learning recognizably human."
      - heading: "TA logistics"
        body: "There was some confusion about who can be hired as a TA for this project and how, since under the new collective bargaining agreement TA positions have to be formally posted."
        questions:
          - "Who can be hired as a TA for this project, and what does the posting process under the new collective bargaining agreement look like?"
    # attendees: "Four instructors and two DDDI staff"

  - id: 2026-09
    date: "September 2026"
    title: "Training the trainers: where four schools stand"
    attendees: "Colleagues from Penn Vet (pathobiology), Penn Nursing, Philosophy and Penn Carey Law, with DDDI"
    source: "Summarized from notes taken by Miryl Hilibrand."
    themes:
      - heading: "Where each school starts from"
        paras:
          - "<strong>Philosophy.</strong> Interest is broad but runs the whole range, from faculty committed to using AI to skeptics who want to protect the teaching mission. A small department, sixteen faculty and about twenty-five with graduate students, teaching everything from 150-person intros to six-person seminars. Keen to borrow from what Law has done, take materials back, and survey faculty on what they would actually want to learn."
          - "<strong>Vet Medicine (pathobiology).</strong> Around thirty faculty. The vice dean for research has asked for a program and left the scope open. Two very different populations: PhD students, who are in classes for two years and then training in the lab, and vet students, who are in class all day. When faculty are polled, most care more about how AI changes the training of PhD students than about classroom use."
          - "<strong>Nursing.</strong> The dean wants every faculty member to have a basic understanding. A needs assessment and a half-day workshop have already happened; one working group built a Canvas course of resources, policies and recordings, another wrote an RFP for mini-grants, and a separate group looks at AI and research. The school is large, sixty-one standing and sixty-two associate faculty plus some 360 academic-support staff, many of them at clinical sites. The dean's charge is informal but can be shared."
          - "<strong>Law.</strong> Decided early not to set a uniform policy and to invest in faculty fluency instead, then let each instructor decide. The spread now runs from courses with virtual TAs and home-built tools that grade midterm essays with richer feedback, to faculty who want nothing to do with it. Everyone is accommodated."
      - heading: "What format works"
        paras:
          - "A two-hour session may be harder to make useful than a half or full day. Vet leans toward longer sessions with hands-on exercises, perhaps a series of day-long workshops each on one topic, in the style of earlier software workshops that brought in outside experts; postdocs would want a full day. Law's experience is that attention, not time, is the constraint: reach faculty often with short, specific sessions. Monthly lunch workshops on one concrete task (fact scenarios, multiple-choice questions, how to turn off training, a bring-your-laptop session with Claude), office hours, a newsletter every few months, and a web portal of resources and candidate policies that a Claude agent keeps current each week. Faculty listen most readily to someone in their own department."
          - "A half-day outline sketched in the room: an intro to the tools, the landscape and how fast it is changing; then classroom use, especially with grounded tools such as NotebookLM where hallucination is less of a worry."
        questions:
          - "Teach with a frontier model, or with a small local model that students can take apart to build understanding?"
      - heading: "What actually engages faculty"
        body: "Being specific and practical about use cases: here is what you can do with it, and what it does well. Spend time showing that it is not the error-prone tool of three years ago. Most faculty who have used it have done nothing beyond the chat box, so nuts and bolts matter. Faculty are not naturally excited about any of this; the first job is to get everyone fluent enough that the real conversation, about what we should now be teaching, can start."
      - heading: "Nobody knows what students are doing"
        body: "A shared sense of “we have no clue,” and a suggestion that one goal of the training should be to share what we do know. One data point: in a class of 160, three students had heard of NotebookLM and one had used it, which is probably not representative of undergraduates. PennChat has no NotebookLM-style closed mode, and private data should not go into it."
        questions:
          - "How widely is PennChat actually used, and by whom?"
      - heading: "Assessment"
        body: "Law has assessed with written final exams for hundreds of years; in an informal test the model came first in nine of ten cases and second in the tenth. Take-home problem sets and essays are where the pressure is, and making assignments AI-resilient came up again. Philosophy named assignments as the thing it most wants to think through. For coding and mathematics, where the technology cannot be banned: run the first part of a course tech-free and allow AI in the second; many intro CS and engineering courses stay tech-free; scaffold AI use over time."
        questions:
          - "Which take-home assignments still measure what we think they measure, and what replaces the rest?"
      - heading: "Socratic dialogue, reading, and guardrails"
        body: "Law and Philosophy both depend on Socratic dialogue and worry about what instant answers do to it. Philosophy already struggles to get students through hard texts and is not sure they read much any more, and being able to is essential. Nursing frames the question as workload and responsible use with guardrails: journals require disclosure, so students should always be facing that question. When and how students should use these tools has mostly come up at faculty retreats rather than in training sessions."
        questions:
          - "When, and how, is it best for students to use these tools?"
    followups:
      - "Send the slides to Nursing, who asked for them."
      - "Nursing to share the dean's charge and the Canvas course."
      - "Philosophy to survey faculty on what they would want to learn."
      - "Vet to raise AI resources at a faculty meeting and bring back feedback."
      - "DDDI offered to co-develop sessions, consult, or simply hand over the materials."
---
