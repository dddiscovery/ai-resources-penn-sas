---
layout: tools
title: AI Tools Matrix
# description: Compare AI and LLM tools by function and company, with Penn Arts & Sciences access status.
permalink: /tools/
css: /assets/css/tools.css

# access_key:
#   label: "Penn Arts & Sciences Access:"
#   chips:
#     - type: "app"
#       label: "By application"
#     - type: "uni"
#       label: "University-wide"
#   # note: "— Updated as agreements are made. Contact DDDI."

columns:
  - "Anthropic"
  - "OpenAI"
  - "Google"
  - "Microsoft"
  - "Cursor"
  - "Grammarly"

filters:
  - id: "all"
    label: "All"
  - id: "chat"
    label: "Chat & Assistant"
  - id: "coding"
    label: "Coding"
  - id: "api"
    label: "API / Dev"
rows:
  - fn: "chat"
    label: "Chat & Assistant"
    desc: "Conversational interfaces for asking questions, drafting text, summarizing documents, and general-purpose AI assistance."
    cells:
      - name: "Claude.ai"
        url: "https://claude.ai"
        desc: "Long context, file uploads, deep reasoning"
      - name: "ChatGPT Edu"
        url: "https://openai.com/chatgpt/education/"
        # chip: "app"
        # chip_label: "By application"
        price: "$13/month — faculty & staff"
        link_label: "Contact IT Support Provider"
        link_url: "https://isc.upenn.edu/get-it-help"
        highlight: true
      - name: "Gemini"
        url: "https://gemini.google/about/"
        # chip: "app"
        # chip_label: "By application"
        price: "$20 or $30/month — ASC, SEAS & Wharton"
        link_label: "Contact IT Support Provider"
        link_url: "https://isc.upenn.edu/get-it-help"
      - highlight: true
        items:
          - name: "Copilot Chat (Basic)"
            url: "https://isc.upenn.edu/resources/activate-microsoft-copilot-chat"
            # chip: "uni"
            # chip_label: "University-wide"
            price: "Free with M365"
            link_label: "Activate here"
          - name: "M365 Copilot (Premium)"
            url: "https://www.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot"
            # chip: "app"
            # chip_label: "By application"
            price: "$16.50/month — faculty & staff"
            link_label: "Contact IT Support Provider"
            link_url: "https://isc.upenn.edu/get-it-help"
      - empty: true
      - name: "Grammarly"
        url: "https://www.grammarly.com/"
        # chip: "app"
        # chip_label: "By application"
        price: "$87/year — Penn affiliates (annual commitment)"
        link_label: "Contact IT Support Provider"
        link_url: "https://isc.upenn.edu/get-it-help"
        highlight: true

      

  - fn: "coding"
    label: "Coding"
    desc: "AI-assisted programming — writing, explaining, and debugging code across languages. Includes sandbox environments for running scripts."
    cells:
      - name: "Claude Code"
        url: "https://code.claude.com/docs/en/overview"
        chip: "none"
        chip_label: "Paid"
        desc: "Agentic coding, full codebase context"
        tags:
          - label: "Terminal / CLI"
            desc: "Type commands in your terminal to let Claude autonomously read, edit, and run code across your entire project"
          - label: "Desktop app"
            desc: "A dedicated macOS/Windows application with a visual interface for managing parallel coding sessions"
          - label: "Web"
            desc: "Browser-based access that connects to your GitHub repos without installing anything locally"
          - label: "IDE extension"
            desc: "Claude embedded directly inside VS Code, Cursor, or JetBrains so you never leave your editor"
      - name: "Codex"
        url: "https://chatgpt.com/codex/"
        chip: "none"
        chip_label: "Paid"
        desc: "Runs Python in sandbox, EDA"
        tags:
          - label: "Web (ChatGPT)"
            desc: "Access Codex as an agent directly inside ChatGPT without any separate installation"
          - label: "Desktop app"
            desc: "A standalone app that runs coding tasks in isolated cloud sandboxes, keeping your local files untouched"
          - label: "CLI"
            desc: "Terminal-based interface for developers who prefer command-line control over the agent"
          - label: "Mobile"
            desc: "Monitor and approve running agent tasks from your phone while the work happens in the cloud"
      - name: "Gemini Code Assist"
        url: "https://codeassist.google"
        chip: "none"
        chip_label: "Free tier"
        desc: "VSCode extension, inline suggestions"
        tags:
          - label: "IDE extension"
            desc: "Available in VS Code, JetBrains, and Android Studio for inline completions, code generation, and chat"
          - label: "CLI (Gemini CLI)"
            desc: "Terminal-based agent mode for agentic coding workflows beyond the editor"
          - label: "Google Cloud"
            desc: "Embedded across Firebase, BigQuery, Cloud Run, and other Google Cloud products, making it more platform-like than a standalone tool"
      - name: "GitHub Copilot"
        url: "https://github.com/features/copilot"
        # chip: "app"
        # chip_label: "By application"
        desc: "Deep IDE integration, PR reviews"
        tags:
          - label: "IDE extension"
            desc: "Works across VS Code, JetBrains, Neovim, Visual Studio, and Xcode for inline completions and chat"
          - label: "CLI"
            desc: "Integrated with the GitHub CLI for natural language command suggestions and agentic workflows directly in the terminal"
          - label: "Desktop app"
            desc: "A standalone agentic client for macOS, Windows, and Linux, currently in technical preview"
          - label: "Web (github.com)"
            desc: "Copilot Chat and the coding agent accessible directly on GitHub, integrated with your repos, issues, and pull requests"
      - name: "Cursor (full IDE)"
        url: "https://cursor.com"
        chip: "none"
        chip_label: "Free / Paid"
        desc: "Built on VSCode, most AI-native"
        tags:
          - label: "Desktop IDE"
            desc: "A full VS Code-based editor combining fast autocomplete, autonomous multi-file agents, and native browser control in one app (macOS, Windows, Linux). Powered by Cursor, embedded with your choice of models."
      - empty: true

  - fn: "api"
    label: "API / Dev"
    desc: "Programmatic access to AI models for building applications, automating workflows, and integrating AI into research pipelines."
    cells:
      - name: "Claude API"
        url: "https://platform.claude.com/docs/en/home"
        chip: "none"
        chip_label: "Paid by usage"
        desc: "200k context window"
      - name: "OpenAI API"
        url: "https://openai.com/api/"
        chip: "none"
        chip_label: "Paid by usage"
        desc: "Most widely documented"
      - name: "Gemini API"
        url: "https://ai.google.dev/gemini-api/docs"
        chip: "none"
        chip_label: "Free tier + Paid"
        desc: "Generous free tier for prototyping"
      - name: "M365 Copilot API"
        url: "https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/copilot-apis-overview"
        chip: "none"
        chip_label: "Paid"
        desc: "Enterprise-grade, HIPAA-eligible"
      - empty: true
      - empty: true

---

<div class="open-models-section container">
  <div class="open-models-header">
    <span class="fn-label">Open Models</span>
    <p class="fn-desc">Publicly released model weights you can download and run locally — no data sent to external servers, full control over your environment. Deploy via <a href="https://ollama.com" target="_blank" rel="noopener">Ollama</a> (free, self-hosted).</p>
  </div>
  <div class="open-models-grid">
    <a class="open-model-card" href="https://ollama.com" target="_blank" rel="noopener">
      <span class="tool-name">LLaMA 3 / Mistral</span>
      <span class="chip chip-none chip-inline">Open weights</span>
      <div class="tool-desc">Best open models for general use; run via Ollama</div>
    </a>
    <a class="open-model-card" href="https://ollama.com/library/codellama" target="_blank" rel="noopener">
      <span class="tool-name">CodeLlama</span>
      <span class="chip chip-none chip-inline">Open weights</span>
      <div class="tool-desc">Fine-tuned for code generation and completion</div>
    </a>
    <a class="open-model-card" href="https://ai.google.dev/gemma" target="_blank" rel="noopener">
      <span class="tool-name">Gemma 3</span>
      <span class="chip chip-none chip-inline">Open weights</span>
      <div class="tool-desc">Efficient; runs on a laptop</div>
    </a>
  </div>
</div>
