# AIS-OS — Task Backlog

Prioritized build queue. Updated nightly at 10PM automatically.
P0 = blocking / immediate. P3 = future / low urgency.

---

## P0 — Immediate (do next session)

- [ ] **Populate morning-brief.json with real data** — currently contains `{"": ""}` (test data from curl). n8n workflow needs to be run manually once against the live journal API to confirm end-to-end. Check `logs/morning-brief.json` date field after run.
- [ ] **Confirm nightly task updater is scheduled** — `schtasks` returned nothing. Verify Task Scheduler has "AIS-OS Nightly Task Updater" registered or re-register it.

---

## P1 — High (next 1-2 weeks)

- [ ] **Write Blaine's Trading Criteria doc** — single source of truth all agents inherit from. Stock filters, dilution mechanics, catalyst keywords, entry/exit rules, hard no list. File: `AI_OS/TRADING_SYSTEMS/blaine_trading_criteria.md`.
- [ ] **Rebuild pre-market scan agent** — strip A/B/C tier buy recommendations. Output is data only — float, gap %, catalyst text, rel. volume. Blaine decides the tier. Ref: `.claude/agents/pre-market-scan.md`.
- [ ] **Dashboard — trade metrics panel** — one working panel in `dashboards/blaine-os.html` connected to `logs/morning-brief.json`. No hardcoded data. Requires P0 morning-brief fix first.
- [ ] **Ingest raw/ backlog** — 10+ articles and notes in `Agentic_OS/raw/articles/` unprocessed. Run `/wiki-ingest` on each this weekend.

---

## P2 — Medium (next month)

- [ ] **Update small-cap-catalyst agent** — add dilution mechanics, S-1 red flags, float rotation, halt patterns. Ref: `.claude/agents/small-cap-catalyst.md`. Requires Trading Criteria doc first.
- [ ] **Dashboard — tasks panel** — second panel connected to `Agentic_OS/TASKS/CURRENT.md`. Shows open tasks. Requires trade metrics panel first.
- [ ] **n8n workflow — pre-market catalyst pull** — SEC EDGAR 8-K overnight filings at 7AM Mon-Fri. Save to `logs/catalyst-brief.json`. Export JSON to `workflows/`.
- [ ] **Add reference guides for connected tools** — `references/edgar-api.md`, `references/yfinance-api.md`, `references/tradingagents-api.md`. Research once, save forever.
- [ ] **Build templates folder** — `.claude/templates/` with at least 1 starter template. Easy +5 pts on next audit Cadence score.
- [ ] **YouTube → wiki ingest habit** — 2-3 ingests per weekend minimum. Track in `Agentic_OS/wiki/log.md`.

---

## P3 — Low (Q3 2026 / when ready)

- [ ] **ThinkScript scanner development** — dilution tracker + watchlist scan filters in TOS. Q2 priority but needs dedicated TOS time.
- [ ] **TOS strategy backtester** — needs ThinkScript scanner knowledge first.
- [ ] **Dilution tracker** — standalone tool feeding into pre-market scan agent.
- [ ] **n8n weekly pattern review trigger** — auto-trigger trade-pattern-analyst every Sunday evening.
- [ ] **Vector/RAG retrieval** — needs 500+ quality wiki entries before semantic search adds value. Don't build yet.
- [ ] **External-facing trader tools** — after your own tools are proven. Not yet.
- [ ] **Dashboard — system status panel** — third panel: wiki entry count, connections health, nightly runner status.

---

## COMPLETED — This session (2026-05-15)

- [x] **TOS_Statements/ excluded from git** — `.gitignore` updated, 2 CSVs untracked via `git rm --cached`, files preserved on disk.
- [x] **/wiki-search skill** — grep-based keyword search across all wiki files. `.claude/skills/wiki-search/SKILL.md`. Registered in README.
- [x] **Memory files added** — `project_n8n.md` and `project_skills_registry.md`. Memory count now 4 (was 2).
- [x] **Morning brief persistence fixed** — `scripts/brief_writer_server.py` on port 8765. n8n POSTs JSON, Python writes `logs/morning-brief.json`. Added to Windows Startup folder.
- [x] **n8n startup restored** — `start-n8n.bat` in Windows Startup folder.
- [x] **n8n workflow fixed** — sequential chain, JSON valid, executeCommand node removed (unsupported in v2.20).
- [x] **DAILY_WORKFLOW.md** — weekend workflow section, AIS-OS operating workflow (universal + deep reference) added.
- [x] **Kanban board** — `Agentic_OS/TASKS/AIS-OS Board.md` created with full P1/P2/P3 breakdown.
- [x] **decisions/log.md** — 6 session decisions logged.
- [x] **Weekend workflow added to DAILY_WORKFLOW.md** — Focus 1 (wiki), Focus 2 (dashboard), Focus 3 (agents).

---

*Last updated: 2026-05-15 (manual end-of-session audit) | Next auto-update: 10PM nightly*
