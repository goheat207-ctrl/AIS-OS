# Wiki Schema

This file governs how the wiki is built and maintained. I read this before any wiki operation. The wiki is a persistent, LLM-maintained knowledge base — not a chat log, not raw notes. Every page is a compiled artifact that gets richer over time.

---

## Directory layout

```
Agentic_OS/
├── raw/                  — source documents (immutable — LLM reads, never writes)
│   ├── articles/         — clipped web articles, saved as markdown
│   ├── notes/            — voice memos, journal entries, meeting notes
│   ├── data/             — CSVs, trade logs, exported data
│   └── books/            — chapter notes, highlights, book summaries
├── wiki/
│   ├── SCHEMA.md         — this file
│   ├── index.md          — catalog of every wiki page (read first on every query)
│   ├── log.md            — append-only activity log
│   ├── entities/         — pages about specific people, tools, companies, tickers
│   ├── topics/           — concept and theme pages (ideas, strategies, frameworks)
│   ├── sources/          — one-page summaries of raw source documents
│   └── syntheses/        — analysis, comparison, and conclusion pages
```

---

## Page frontmatter

Every wiki page starts with YAML frontmatter:

```yaml
---
title: Human-readable title
type: entity | topic | source | synthesis
tags: [tag1, tag2]
source_count: 0
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

---

## Naming conventions

- All files: `snake_case.md`
- Entities: `person_name.md`, `tool_name.md`, `company_name.md`
- Topics: descriptive noun phrase — `small_cap_trading.md`, `risk_management.md`
- Sources: `src_YYYYMMDD_short_title.md`
- Syntheses: `synth_topic_focus.md`

---

## Cross-linking rules

- Use `[[filename_without_extension]]` Obsidian wiki-link format throughout
- Every entity or topic mentioned in body text should link to its page
- If the page doesn't exist yet, still write the link — it marks a gap for lint to catch
- Cross-links are how the wiki compounds. Link liberally.

---

## Ingest workflow

When a new source lands in `raw/`:

1. Read the source fully
2. Discuss key takeaways (Blaine directs emphasis)
3. Write `wiki/sources/src_YYYYMMDD_title.md` — summary page
4. Update all relevant entity and topic pages — a single source may touch 5-15 pages
5. Add the source entry to `index.md`
6. Append to `log.md`: `## [YYYY-MM-DD] ingest | Source Title`

Never synthesize during intake. Capture first, revise entity/topic pages second.

---

## Query workflow

When Blaine asks a question:

1. Read `index.md` to find relevant pages
2. Read those pages
3. Answer with `[[citations]]` linked to wiki pages
4. If the answer is non-trivial and reusable, file it as `wiki/syntheses/synth_topic.md`
5. Update `index.md` and `log.md` if a new page was created

---

## Lint workflow

Run on request (`/lint` or "lint the wiki"):

- Orphan pages — pages with no inbound `[[links]]`
- Stale claims — older pages that newer sources may have superseded
- Missing pages — concepts linked but no page exists yet
- Contradictions — claims on two pages that conflict
- Data gaps — important questions not yet answered by any source

---

## index.md format

```markdown
## Entities
- [[entity_name]] — one-line description

## Topics
- [[topic_name]] — one-line description

## Sources
- [[src_YYYYMMDD_title]] — Source Title (date ingested)

## Syntheses
- [[synth_topic_focus]] — what question it answers
```

---

## log.md format

```markdown
## [YYYY-MM-DD] {type} | {title}
{one-line summary of what happened / what changed}
```

Entry types: `setup` | `ingest` | `query` | `update` | `lint`

---

## What the wiki is NOT

- Not a chat transcript
- Not a place to dump raw notes unprocessed
- Not a to-do list (use `decisions/log.md` for decisions, AIOS tasks for tasks)
- Not duplicating `AI_OS/` content — that's the operating system; this is the knowledge base
