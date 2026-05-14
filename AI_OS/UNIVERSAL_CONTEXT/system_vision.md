# AIS-OS System Vision

## What This System Is

AIS-OS is a personal AI operating system for Blaine.

It is NOT a trading tool.
It is NOT a single-purpose assistant.

It is a multi-domain execution engine that supports:
- trading systems
- software and tool development
- business building and client work
- learning and research
- automation and productivity
- idea-to-execution workflows

Trading is one module. The OS is the foundation.

---

## Architecture Layers

```
┌─────────────────────────────────────────────────────┐
│                    CLAUDE.md                        │  ← Session entry point
├─────────────────────────────────────────────────────┤
│               PERSONALITY LAYER                     │  ← context/, references/
│         Blaine-specific behavior, voice,            │
│         decision logic, priorities                  │
├─────────────────────────────────────────────────────┤
│               CORE ENGINE                           │  ← AI_OS/
│   Routing, memory, token economy, workflows,        │
│   agent design, thinking models, templates          │
├────────┬────────┬──────────┬──────────┬─────────────┤
│TRADING │SOFTWARE│ BUSINESS │ LEARNING │ AUTOMATION  │  ← domains/
│module  │module  │  module  │  module  │   module    │
├────────┴────────┴──────────┴──────────┴─────────────┤
│               KNOWLEDGE SYSTEM                      │  ← Agentic_OS/wiki/
│   Obsidian second brain: entities, topics,          │
│   sources, syntheses, decision intelligence         │
├─────────────────────────────────────────────────────┤
│               AGENTS LAYER                          │  ← .claude/agents/
│   Pre-market scan, catalyst research,               │
│   trade analysis, TradingAgents team                │
├─────────────────────────────────────────────────────┤
│               INTEGRATIONS                          │  ← connections.md
│   TOS, yfinance, EDGAR, TradingAgents,              │
│   scraper, n8n, Obsidian, Gmail (future)            │
├─────────────────────────────────────────────────────┤
│               EXECUTION RUNTIME                     │  ← main.py
│   Command routing, state management,                │
│   agent dispatch, logging, safety layer             │
└─────────────────────────────────────────────────────┘
```

---

## Domain Modules

Each domain lives in `domains/` and is self-contained:

| Domain | Purpose | Current State |
|--------|---------|---------------|
| `domains/trading/` | Scanners, journal, backtester, risk tools | Active — Q2 priority |
| `domains/software/` | Dev projects for self and local businesses | Starting |
| `domains/business/` | Client work, local app builds, consulting | Planned |
| `domains/learning/` | Research intake, skill dev, playbook study | Active via wiki |
| `domains/automation/` | n8n workflows, scraper, pipeline agents | Active — scraper running |

---

## Design Principles

**Personal-first.** Built for Blaine now. Generalized later.

**Modular.** Adding a new domain does not touch existing domains.

**Personality isolated.** Blaine-specific logic lives only in `context/` and `references/`. The engine is generic.

**Stable before clean.** Functionality is never sacrificed for structural elegance.

**One next step.** The system reduces cognitive load. Never adds to it.

---

## Future Multi-User Path

When this system needs to support other users:
1. Fork the repo
2. Replace `context/` files with that user's intake
3. Replace `references/voice.md` with their voice
4. Adjust `domains/` based on what they're building
5. Keep AI_OS/ core unchanged

The core engine is already user-agnostic.
Only the personality layer is Blaine-specific.

---

## Q2 2026 Focus (End of July)

1. Trading module: finish journal + backtester + TOS scan filters
2. Software module: scaffold first local business app
3. Automation module: n8n workflows for pre-market research
4. Knowledge system: full ingest pipeline live

The vision is long-term. The next step is always small.
