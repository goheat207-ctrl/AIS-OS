# Wiki Intelligence Guide

How the Obsidian knowledge system connects to AIS-OS decisions.

This file turns the wiki from passive notes into an active decision layer.

---

## The Core Idea

Every decision Blaine makes belongs to a domain.
Every domain has knowledge pages in the wiki.
Before making a decision, load the relevant high-relevance pages first.

```
Question / Task
     |
     v
Identify domain (trading / software / business / learning / automation)
     |
     v
Load wiki/index.md → filter by domain
     |
     v
Read high-relevance pages
     |
     v
Surface relevant rules, past decisions, contradictions
     |
     v
Present options with evidence
     |
     v
Blaine decides → log in decisions/log.md
```

---

## Domain Knowledge Maps

### Trading Decisions

Before any trade analysis or rule change, check:
- `wiki/topics/trading_context.md` — current setup and constraints
- `wiki/topics/q2_goals.md` — what's being optimized for
- Any relevant strategy page (e.g., `small_cap_breakout`, `tape_reading`)
- Recent syntheses tagged `domain: trading`

Key questions the wiki should answer:
- What are my current entry/exit rules for this setup?
- What did past similar trades look like?
- What rule am I most likely to break here?

### Software / Build Decisions

Before starting a build:
- `wiki/entities/codex.md` — how to work with the implementation partner
- Any prior build notes in `wiki/topics/`
- `references/` for API guides already researched

Key questions:
- Has this been tried before?
- What broke last time?
- What's the simplest version that works?

### Learning Decisions

Before researching a topic:
- Check `wiki/index.md` — does this knowledge already exist?
- If yes: update the existing page
- If no: drop source in `raw/` and run ingest

Key question: Is this net-new knowledge or reinforcement of something already captured?

---

## Connecting Wiki to main.py

`python main.py research TOPIC` routes to the learning domain and prompts:
1. Check wiki index for existing coverage
2. If covered: load and summarize
3. If not covered: queue for ingest

`python main.py analyze TICKER` routes trading analysis and wiki should be checked for:
- Existing ticker entity page (`wiki/entities/ticker_XXXX.md`)
- Relevant strategy pages for the pattern being traded

---

## Knowledge Gaps as Action Items

Gaps flagged in `wiki/index.md` are not passive notes. They are build queue items.

When a gap is flagged:
1. Is there a raw source that would fill it? Drop it in `raw/` and ingest.
2. Is it a synthesis gap? Run a synthesis after enough sources exist.
3. Is it a "hasn't happened yet" gap? Note it in `decisions/log.md` as future work.

Current gaps (from index.md) → see `wiki/index.md` Gaps section.

---

## Synthesis Triggers

Create a synthesis (`wiki/syntheses/synth_*.md`) when:
- 3+ sources on the same topic have been ingested
- A recurring question keeps coming up without a clean answer
- A decision was made that required research — capture the conclusion
- A pattern was identified across multiple trade reviews

Syntheses are the highest-value pages in the wiki.
One good synthesis saves hours of re-researching the same question.

---

## Keeping the Wiki Alive

| Trigger | Action |
|---------|--------|
| New article saved in raw/ | Run ingest workflow |
| New trade taken | Update trading_context.md if rules changed |
| Decision made | Log in decisions/log.md, update any wiki page the decision affects |
| Weekly /level-up | Check for new synthesis opportunities |
| Monthly | Run lint — find orphans, stale pages, gaps |
| Q2 end | Archive low-relevance pages, upgrade syntheses |

---

## Anti-Patterns

- Don't add to the wiki without adding to `index.md` — orphan pages are invisible
- Don't update a topic page without checking for contradictions with existing claims
- Don't create a synthesis page with only one source — that's just a source page
- Don't keep `relevance: high` on pages you haven't looked at in 60+ days
- Don't duplicate knowledge from `AI_OS/` — that's the OS; this is the knowledge
