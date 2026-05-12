# Folder Architecture

## Root: D:\AI_OS\

This is the AI Operating System root.
All projects inherit from this directory.

---

## Folder Map

```
D:\AI_OS\
│
├── CLAUDE.md                    ← Session boot file. Always load first.
│
├── UNIVERSAL_CONTEXT\           ← Global rules and principles
│   ├── ai_philosophy.md             Why we build this way
│   ├── context_engineering.md       How to load and route context
│   ├── folder_architecture.md       This file — canonical workspace map
│   ├── workflow_routing.md          Task-to-folder routing table
│   ├── writing_constraints.md       Output quality and style rules
│   ├── naming_conventions.md        File naming standards
│   └── universal_ai_workspace_architecture_system.md  Source reference doc
│
├── CORE_SYSTEMS\                ← Technical system mechanics
│   └── token_economy.md             Token optimization rules
│
├── MEMORY\                      ← Session memory and handoff
│   ├── ai_memory_rules.md           How AI handles cross-session memory
│   └── session_handoff.md           Template for closing/resuming sessions
│
├── WORKFLOWS\                   ← Universal pipeline standards
│   ├── workflow_standards.md        Generic production pipeline stages
│   └── project_lifecycle.md         Full project lifecycle from brief to archive
│
├── THINKING_MODELS\             ← Mental models and decision frameworks
│   ├── thinking_frameworks.md       Problem-solving models
│   └── decision_templates.md        Reusable decision structures
│
├── PROJECT_TEMPLATES\           ← Scaffold for every new project
│   ├── _template_project_claude.md  Copy this as CLAUDE.md for any project
│   ├── template_trading_project.md  Trading project folder scaffold
│   ├── template_research_project.md Research project folder scaffold
│   └── template_content_project.md  Content project folder scaffold
│
├── ACTIVE_PROJECTS\             ← Live work only
│   └── [project-name]\              Each project is a self-contained folder
│
├── TRADING_SYSTEMS\             ← Trading intelligence
│   ├── trading_operating_system.md  Trading OS overview and operating rules
│   ├── scanner_development.md       Scanner build workflow
│   ├── journal_system.md            Trading journal structure and templates
│   └── risk_framework.md            Risk rules and position sizing
│
├── AGENT_SYSTEMS\               ← AI agent design
│   ├── agent_design_principles.md   How to design lean, effective agents
│   └── agent_routing_patterns.md    Multi-agent coordination patterns
│
├── CONTENT_SYSTEMS\             ← Content production
│   ├── content_operating_system.md  Content workflow overview
│   ├── voice_constraints.md         Tone, style, and anti-patterns
│   └── content_pillars.md           Content direction and themes
│
├── AUTOMATIONS\                 ← Automation systems
│   └── automation_principles.md     What to automate, how, and when not to
│
├── RESEARCH\                    ← Research and synthesis
│   └── research_workflow.md         Research intake, processing, and output
│
└── PROMPTS\                     ← Reusable prompt components
    └── [prompt files]               Modular prompt building blocks
```

---

## Folder Purpose Summary

| Folder            | Purpose                                      | Audience      |
| ----------------- | -------------------------------------------- | ------------- |
| UNIVERSAL_CONTEXT | Rules that apply everywhere                  | All sessions  |
| CORE_SYSTEMS      | Mechanics: tokens, routing, system design    | Technical     |
| MEMORY            | Cross-session continuity                     | All sessions  |
| WORKFLOWS         | How work moves from idea to output           | All projects  |
| THINKING_MODELS   | How to reason through complex problems       | Analysis work |
| PROJECT_TEMPLATES | Copy-paste scaffolds for new projects        | Project start |
| ACTIVE_PROJECTS   | The actual work being done right now         | Live work     |
| TRADING_SYSTEMS   | All trading-domain context and intelligence  | Trading work  |
| AGENT_SYSTEMS     | Agent architecture and coordination          | Agent builds  |
| CONTENT_SYSTEMS   | Content production rules and structure       | Content work  |
| AUTOMATIONS       | What gets automated and how                  | System builds |
| RESEARCH          | How research is collected and synthesized    | Research work |
| PROMPTS           | Reusable prompt components and templates     | All AI work   |

---

## Project Inheritance Pattern

Every new project in ACTIVE_PROJECTS:
1. Copies `_template_project_claude.md` as its own `CLAUDE.md`
2. References the relevant domain files from AI_OS root
3. Contains only project-specific artifacts inside its own folder
4. Does NOT duplicate global rules — it references them

Projects inherit from the OS. They do not rewrite it.
