# Wiki Schema — Intelligence Layer

This file governs how the wiki is built and maintained. I read this before any wiki operation.

The wiki is NOT passive note storage. It is a structured knowledge + decision intelligence engine.
Every page is a compiled artifact that gets richer over time. The goal is actionable retrieval, not archiving.

---

## Directory Layout

```
Agentic_OS/
├── raw/                    — source documents (immutable — LLM reads, never writes here)
│   ├── articles/           — web clips, X posts, saved markdown
│   ├── notes/              — voice memos, journal entries, meeting notes
│   ├── data/               — CSVs, trade logs, exported data, screenshots
│   └── books/              — playbooks, PDFs, chapter notes
├── wiki/
│   ├── SCHEMA.md           — this file (read before any wiki op)
│   ├── index.md            — catalog of every wiki page (read first on every query)
│   ├── log.md              — append-only activity log
│   ├── INTELLIGENCE_GUIDE.md — how the wiki connects to decisions
│   ├── entities/           — tools, people, tickers, platforms
│   ├── topics/             — concepts, strategies, frameworks, systems
│   ├── sources/            — one-page digests of raw source documents
│   └── syntheses/          — cross-source analysis and actionable conclusions
```

---

## Domain Classification

Every page belongs to exactly ONE domain. This determines which context loads it.

| Domain | Use for |
|--------|---------|
| `trading` | Strategies, entries/exits, scanners, risk, tape reading |
| `software` | Dev tools, code patterns, app architecture |
| `business` | Client work, local business tools, revenue models |
| `learning` | Meta-learning, skill frameworks, habit systems |
| `automation` | Workflows, agents, scraping, pipelines |
| `system` | AIS-OS structure, wiki ops, memory rules |

---

## Page Frontmatter (REQUIRED)

Every wiki page starts with YAML frontmatter:

```yaml
---
title: Human-readable title
type: entity | topic | source | synthesis
domain: trading | software | business | learning | automation | system
tags: [tag1, tag2]
relevance: high | medium | low
source_count: 0
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

**Fields explained:**
- `domain` — routes this page to the right AIS-OS context (see table above)
- `relevance` — how actionable this knowledge is right now (high = use in decisions today)
- `source_count` — number of raw sources that back the claims on this page

---

## Page Types

### entity
A specific person, tool, ticker, company, or platform.
- Always has a "Current Role" section explaining why it matters to Blaine now
- Examples: `thinkorswim.md`, `blaine.md`, `codex.md`

### topic
A concept, strategy, framework, or system.
- Should answer: "What is this?" and "How does Blaine use it?"
- Examples: `risk_management.md`, `tape_reading.md`, `dilution_tracking.md`

### source
A one-page digest of a single raw source.
- Never synthesizes across sources — capture only
- Filename: `src_YYYYMMDD_short_title.md`

### synthesis
Cross-source analysis that reaches a conclusion or decision recommendation.
- Connects multiple sources and topics into one actionable insight
- Filename: `synth_topic_focus.md`
- Lives in `wiki/syntheses/`

---

## Naming Conventions

- All files: `snake_case.md`
- Entities: `tool_name.md`, `person_name.md`, `ticker_XXXX.md`
- Topics: descriptive noun phrase — `small_cap_breakout.md`, `risk_per_trade.md`
- Sources: `src_YYYYMMDD_short_title.md`
- Syntheses: `synth_topic_focus.md`

---

## Cross-Linking Rules

- Use `[[filename_without_extension]]` Obsidian wiki-link format throughout
- Every entity or topic mentioned in body text should link to its page
- If the page doesn't exist yet, still write the link — it marks a gap for lint to catch
- Cross-links are how the wiki compounds over time. Link liberally.

---

## Ingest Workflow

When a new source lands in `raw/`:

1. Read the source fully
2. Identify its domain (trading / software / business / learning / automation)
3. Write `wiki/sources/src_YYYYMMDD_title.md` with correct frontmatter + domain
4. Update all relevant entity and topic pages — one source may touch 5-15 pages
5. Add source entry to `index.md` under the correct domain section
6. Append to `log.md`: `## [YYYY-MM-DD] ingest | domain | Source Title`

Never synthesize during ingest. Capture first. Synthesize in a separate step.

---

## Query Workflow

When Blaine asks a question:

1. Read `index.md` to find relevant pages
2. Filter by domain first (trading question = load trading pages only)
3. Read those pages
4. Answer with `[[citations]]` linked to wiki pages
5. If the answer is non-trivial and reusable: file as `wiki/syntheses/synth_topic.md`
6. Update `index.md` and `log.md` if a new page was created

---

## Decision Support Workflow

When a decision needs to be made (trade, build, business):

1. State the decision: "Should I take this trade?" / "Should I build X?"
2. Load wiki pages by domain + `relevance: high`
3. Surface any contradictions, recent updates, or relevant syntheses
4. Present 2-3 options with wiki evidence
5. Blaine decides. Log in `decisions/log.md`.
6. If decision reveals a knowledge gap: flag it in `index.md` Gaps section

---

## Lint Workflow

Run on request ("lint the wiki"):

- Orphan pages — pages with no inbound `[[links]]`
- Stale claims — `relevance: high` pages not updated in 30+ days
- Missing pages — concepts linked but no page exists yet
- Contradictions — claims on two pages that conflict
- Domain gaps — domains with fewer than 3 topic pages (weak coverage)
- Missing frontmatter — pages without required fields

---

## Index Format

```markdown
## Entities
- [[entity_name]] — one-line description | domain: X

## Topics by Domain

### Trading
- [[topic_name]] — one-line description

### Software
- [[topic_name]] — one-line description

### Learning
...

## Sources
- [[src_YYYYMMDD_title]] — Source Title (domain | date ingested)

## Syntheses
- [[synth_topic_focus]] — what question it answers | domain: X

## Gaps Flagged
- [description of missing knowledge]
```

---

## Log Format

```markdown
## [YYYY-MM-DD] {type} | {domain} | {title}
{one-line summary of what happened}
```

Types: `setup` | `ingest` | `query` | `update` | `lint` | `synthesis` | `decision`

---

## Relevance Scoring Guide

| Score | Meaning | Review cadence |
|-------|---------|----------------|
| `high` | Used in daily/weekly decisions | Review if >30 days since update |
| `medium` | Useful for context, referenced occasionally | Review if >90 days |
| `low` | Background knowledge, historical reference | No required review |

Downgrade `relevance` when a newer source supersedes a claim. Never delete — mark stale.

---

## What the Wiki Is NOT

- Not a chat transcript
- Not a place to dump raw notes unprocessed
- Not a to-do list (use `decisions/log.md` for decisions)
- Not duplicating `AI_OS/` content — that's the OS; this is the knowledge base
- Not a replacement for real-time data (price data, live news stays in tools)
