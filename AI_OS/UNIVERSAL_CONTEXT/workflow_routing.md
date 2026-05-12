# Workflow Routing

## Purpose

This file defines which context files to load for each task type.
Follow this table at the start of every session.
Do NOT load files outside the relevant domain.

---

## Primary Routing Table

| Task Type              | Primary Files                                      | Optional Add-ons              |
| ---------------------- | -------------------------------------------------- | ----------------------------- |
| Trading analysis       | trading_operating_system.md, risk_framework.md     | journal_system.md             |
| Scanner development    | scanner_development.md, workflow_standards.md      | thinking_frameworks.md        |
| Journal review         | journal_system.md, thinking_frameworks.md          | risk_framework.md             |
| Research synthesis     | research_workflow.md, thinking_frameworks.md       | decision_templates.md         |
| Content writing        | content_operating_system.md, voice_constraints.md  | content_pillars.md            |
| Script / video         | voice_constraints.md, content_pillars.md           | content_operating_system.md   |
| Agent design           | agent_design_principles.md, context_engineering.md | agent_routing_patterns.md     |
| Automation build       | automation_principles.md, workflow_standards.md    | agent_design_principles.md    |
| New project setup      | folder_architecture.md, _template_project_claude.md| workflow_standards.md         |
| System design          | context_engineering.md, ai_philosophy.md           | folder_architecture.md        |
| General reasoning      | ai_philosophy.md, thinking_frameworks.md           | decision_templates.md         |
| Memory / session end   | ai_memory_rules.md, session_handoff.md             | —                             |

---

## Dynamic Role Assignment

The AI assumes a role based on the domain loaded:

| Domain Loaded         | AI Operating Role    |
| --------------------- | -------------------- |
| TRADING_SYSTEMS       | Market analyst       |
| CONTENT_SYSTEMS       | Writer and editor    |
| AGENT_SYSTEMS         | Systems architect    |
| RESEARCH              | Research synthesizer |
| AUTOMATIONS           | Automation engineer  |
| THINKING_MODELS       | Strategic advisor    |

Roles are dynamic. They are loaded with context. They are not permanent.

---

## Cross-Domain Work

If a task touches two domains (e.g., trading content creation):
1. Identify the primary domain (what is the OUTPUT?)
2. Load primary domain files first
3. Load secondary domain files only for specific constraints needed
4. Do not merge domain rules — keep them separate in reasoning

Example: Writing a trading education YouTube script
- Primary: content_operating_system.md + voice_constraints.md
- Secondary: trading_operating_system.md (for accuracy)
- Do NOT merge into one context block

---

## Anti-Patterns

Never do this:
- Load all files "just in case"
- Combine trading + content + agent context in one session
- Use this routing table as a checklist to load everything on it
- Skip routing because the task "seems simple"

Routing discipline is how the workspace stays fast and accurate.
