# Decisions Log

Append-only record of meaningful decisions and why they were made. `/level-up` Phase 2 (Method interview) writes scoped automation specs here. You can also append manually whenever you decide something worth remembering.

**Format per entry:**

```
## YYYY-MM-DD — Short title

**Decision:** what was decided.

**Why:** the reasoning, constraints, and what would change your mind.

**Alternatives considered:** what else was on the table.

**Owner:** who's accountable.
```

Keep it terse. Future-you will thank present-you for capturing the *why*, not just the *what*.

---

## 2026-05-11 — AIOS Day 1 setup

**Decision:** Set up AIS-OS with AIS-OS starter kit + AI_OS workspace. Not focused on selling yet — building trading tools and local apps first.

**Why:** Blaine's Q2 priorities are P&L improvement, trade journal prototype, and TOS backtester. The OS needs to support those before anything else.

**Alternatives considered:** Starting with selling/monetization first. Rejected — not ready and not the priority.

**Owner:** Blaine

## 2026-05-11 - Add Codex to AIS-OS

**Decision:** Add Codex as the AIS-OS implementation partner with a root `AGENTS.md`, a standing role file, and a wiki entity.

**Why:** Blaine needs low-friction execution support that turns ideas into working files, scripts, dashboards, and systems without adding cognitive load.

**Alternatives considered:** Leave Codex as an external chat tool only. Rejected because the OS should preserve how Codex should operate inside this workspace.

**Owner:** Blaine

## 2026-05-13 — Quick note

**Decision:** Testing main.py orchestrator - all commands working

**Owner:** Blaine

## 2026-05-14 — Neuron Architecture + wiki-ingest skill

**Decision:** Redesign the second brain around five isolated domain neurons (trading, coding, business, os_design, general). Each neuron has a `current_state.md` (what I currently know in this domain) and an `index.md` (registry of filed entries). Built `/wiki-ingest` skill to route new knowledge into the correct neuron with AI classification + human review before filing.

**Why:** The existing wiki was a flat pile — all topics mixed together. AI was loading undifferentiated context or the wrong domain entirely. Car mechanics knowledge doesn't help you cook. The neuron structure lets AI load ONLY the relevant domain per session, cutting cognitive overhead and making context actually useful.

**Autonomy level:** L2 — AI drafts and classifies, Blaine reviews and approves before filing. Advance to L3 after 10 validated entries.

**KPI:** Cut costs (cognitive overhead). Metric: sessions where AI loads correct domain context without re-explanation — target 80%+ within 2 weeks of use.

**Alternatives considered:** Continuing with flat topics/ structure. Rejected — it's the root cause of AI context failures.

**Bike Method Phase:** 1 — run manually, review every output.

**Owner:** Blaine

---

## 2026-05-15 — TOS_Statements/ excluded from git

**Decision:** Added `TOS_Statements/` and `*.csv` to `.gitignore`. Untracked two already-committed CSVs via `git rm --cached` (files preserved on disk).

**Why:** Financial data has no business in a git repo. Size hygiene and privacy. Caught before more CSVs accumulated.

**Alternatives considered:** Scoping to `TOS_Statements/*.csv` only instead of global `*.csv`. Left global for now — no other CSVs in the repo that need tracking.

**Owner:** Blaine

---

## 2026-05-15 — /wiki-search skill added

**Decision:** Built a grep-based `/wiki-search` skill at `.claude/skills/wiki-search/SKILL.md`. No embeddings, no vector DB — just ripgrep wrapped in a clean skill interface.

**Why:** 80+ wiki files with no search is ADHD-hostile. Grep is fast, zero infrastructure, and sufficient for the current wiki size. Vector/RAG can come later when there are 500+ entries.

**Alternatives considered:** Semantic/vector search. Rejected for now — overkill at current wiki size, adds infrastructure cost and complexity.

**Owner:** Blaine

---

## 2026-05-15 — Morning brief persistence via local HTTP server

**Decision:** Built `scripts/brief_writer_server.py` — a local Python HTTP server on port 8765. n8n POSTs the morning brief JSON to it; the server writes `logs/morning-brief.json`. Added to Windows Startup folder alongside n8n.

**Why:** Three approaches failed before this one. (1) Execute Command node — broken on Windows, removed in n8n v2.20. (2) Write Binary File node — "not writable" error, unreliable. (3) `fs.writeFileSync` in Code node — n8n sandboxes `require`, `fs` disallowed. Local HTTP server bypasses all three. Port 5679 was blocked by Windows; switched to 8765.

**Alternatives considered:** Write Binary File node, Execute Command node, fs in Code node — all tried and failed. Documented in git history commits `fix:`.

**Owner:** Blaine

---

## 2026-05-15 — n8n workflow restructured to sequential chain

**Decision:** Replaced parallel branch architecture (two HTTP nodes merging into one Code node) with a sequential chain: Schedule → Get Metrics → Get Per-Symbol → Format Brief → Save Brief.

**Why:** n8n v2.x Code node doesn't reliably handle two simultaneous inputs. Parallel branches caused "node hasn't been executed" errors. Sequential chain is simpler, no merge ambiguity.

**Alternatives considered:** Merge node before Code node. Rejected — adds complexity without benefit when sequential ordering works fine.

**Owner:** Blaine

---

## 2026-05-15 — Kanban board added to Obsidian

**Decision:** Created `Agentic_OS/TASKS/AIS-OS Board.md` as the primary task management surface using the obsidian-kanban plugin. Columns: P1 This Weekend, P2 This Month, P3 Q3 2026, OS Maintenance Recurring, In Progress (max 3), Done.

**Why:** BACKLOG.md and CURRENT.md are good for automation but bad for visual prioritization. The Kanban board gives a drag-and-drop view across three milestones. ADHD-friendly — see everything at once without reading a flat list.

**Alternatives considered:** Markdown task files only. Rejected — no visual overview, hard to reprioritize quickly.

**Owner:** Blaine

---

## 2026-05-15 — DAILY_WORKFLOW.md expanded to full OS operating manual

**Decision:** Extended `Agentic_OS/DAILY_WORKFLOW.md` with three new sections: Weekend Workflow (wiki ingest, dashboard build, agent improvement), AIS-OS Operating Workflow — universal session start/close/cadence/memory/health indicators, and AIS-OS Operating Workflow — Deep Reference with real file paths, layer map, agents table, scripts table, and intelligence files.

**Why:** The existing workflow was trading-only. The OS covers five domains and needs operating instructions that apply regardless of domain. Grounded in actual repo files — not generic advice.

**Alternatives considered:** Separate file per workflow type. Rejected — one file is easier to open in Obsidian and keeps the full operating picture in one place.

**Owner:** Blaine
