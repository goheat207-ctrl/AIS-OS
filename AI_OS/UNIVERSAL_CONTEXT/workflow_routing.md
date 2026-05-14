# Workflow Routing

## Purpose

This file defines which context files to load for each task type.
Follow this table at the start of every session.
Do NOT load files outside the relevant domain.

This system covers five domains: trading, software, business, learning, automation.
Default to identifying the domain BEFORE loading any files.

---

## Step 1 — Identify the Domain

| The task is about... | Domain |
|---------------------|--------|
| Trades, scanners, journal, TOS, risk | trading |
| Building apps, scripts, tools, APIs | software |
| Client work, local business, revenue | business |
| Playbooks, research, skill building | learning |
| Workflows, agents, n8n, scraping | automation |
| Content, writing, social media | content |
| AIS-OS structure, memory, routing | system |

---

## Step 2 — Load the Right Files

| Task Type | Primary Files | Optional Add-ons |
|-----------|---------------|-----------------|
| Trading analysis | trading_operating_system.md, risk_framework.md | journal_system.md |
| Scanner development | scanner_development.md, workflow_standards.md | thinking_frameworks.md |
| Journal review | journal_system.md, thinking_frameworks.md | risk_framework.md |
| Software build | workflow_standards.md, agent_design_principles.md | folder_architecture.md |
| Business task | context/about-business.md, workflow_standards.md | decision_templates.md |
| Research / learning | research_workflow.md, thinking_frameworks.md | decision_templates.md |
| Automation build | automation_principles.md, workflow_standards.md | agent_design_principles.md |
| Content writing | content_operating_system.md, voice_constraints.md | content_pillars.md |
| Agent design | agent_design_principles.md, context_engineering.md | agent_routing_patterns.md |
| New project setup | folder_architecture.md, _template_project_claude.md | workflow_standards.md |
| General reasoning | ai_philosophy.md, thinking_frameworks.md | decision_templates.md |
| Memory / session end | ai_memory_rules.md, session_handoff.md | — |

---

## Step 2b — Add Wiki Context for Knowledge Tasks

For any task involving decisions or domain knowledge, ALSO check the wiki:

1. Read `Agentic_OS/wiki/index.md`
2. Filter entries by the task's domain
3. Load pages with `relevance: high` only

Do NOT load the full wiki. Domain-filter first, then relevance-filter.

---

## Dynamic Role Assignment

| Domain Loaded | AI Operating Role |
|---------------|-------------------|
| TRADING_SYSTEMS | Market analyst |
| CONTENT_SYSTEMS | Writer and editor |
| AGENT_SYSTEMS | Systems architect |
| RESEARCH | Research synthesizer |
| AUTOMATIONS | Automation engineer |
| THINKING_MODELS | Strategic advisor |
| wiki trading pages | Trading decision support |
| wiki learning pages | Knowledge retrieval |

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
- Secondary: trading_operating_system.md (for accuracy only)

---

## Anti-Patterns

Never do this:
- Load all files without identifying domain first
- Combine trading + content + agent context in one session
- Load all wiki pages instead of filtering by domain + relevance
- Skip routing because the task "seems simple"

Routing discipline is how the workspace stays fast and accurate.
