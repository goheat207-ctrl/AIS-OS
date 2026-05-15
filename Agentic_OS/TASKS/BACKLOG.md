# AIS-OS — Task Backlog

Prioritized build queue. Updated by Claude at the end of every session.
P0 = blocking / immediate. P3 = future / low urgency.

---

## P0 — Immediate (do next session)

- [ ] **Fix git push** — run `git push origin main` from your own terminal (not via Claude Code). gh auth is already done, just needs a direct terminal run.
- [ ] **Set n8n as Windows startup service** — so Morning Journal Pull fires at 8AM automatically without you starting n8n manually. ~10 min job.
- [x] **Nightly task updater** — `scripts/update_tasks.py` + Windows Task Scheduler at 10PM. CURRENT.md, COMPLETED.md, BACKLOG.md auto-update every night.
- [ ] **Run `/startup [domain]` at the start of every session** — habit, not a build task. The hook is live, just needs to be used.

---

## P1 — High (next 1-2 weeks)

- [ ] **Reframe pre-market scan agent** — strip A/B/C tier buy recommendations. Make it a data aggregation tool (gap %, float, catalyst text, volume). You decide the tier. This makes the agent usable again.
- [ ] **Wire n8n morning brief to save to file** — `logs/morning-brief.json` persists between sessions. `scripts/save_morning_brief.py` is already written, just needs to be connected. Replace the Execute Command node issue with a Write Binary File node or webhook approach.
- [ ] **Wiki keyword search skill** — simple grep-based `/wiki-search` skill. Even basic search is better than manually navigating 80+ files.
- [ ] **Add 1+ memory files** — currently 2 memory files. Need >3 to hit the Context score threshold on the next audit. Add `memory/project_n8n.md` or `memory/feedback_session1.md`.

---

## P2 — Medium (next month)

- [ ] **Wire Gmail as first tier-1 domain** — highest leverage connection gap. `claude mcp add gmail` or Python script + `references/gmail-api.md`. Jumps audit Connections score by ~6 pts.
- [ ] **Add reference guides for connected tools** — SEC EDGAR, yfinance, TradingAgents each need a `references/{tool}-api.md`. Research once, save forever. Currently 8 of 9 active connections have no guide.
- [ ] **Build templates folder** — `.claude/templates/` with at least 1 file. Easy +5 pts on next audit Cadence score.
- [ ] **Ingest raw/ backlog** — 2 articles and 1 note sitting in `Agentic_OS/raw/` unprocessed. Run `/wiki-ingest` on each.
- [ ] **n8n second workflow** — pre-market catalyst pull (SEC EDGAR 8-K overnight filings). Runs at 7AM, feeds the trading neuron.
- [ ] **Update connections.md** — add n8n as a connection entry. Document workflow ID and what it does.

---

## P3 — Low (Q3 2026 / when ready)

- [ ] **ThinkScript scanner development** — Dilution tracker + watchlist scan filters. Q2 priority but needs TOS time.
- [ ] **TOS strategy backtester** — Q2 priority. Needs ThinkScript knowledge first.
- [ ] **Dilution tracker** — standalone tool. Feeds into the pre-market scan agent.
- [ ] **n8n additional workflows** — weekly pattern review auto-trigger, wiki ingest queue checker.
- [ ] **Vector/RAG retrieval** — needs 500+ quality wiki entries before semantic search adds value. Don't build yet.
- [ ] **Gmail integration** — after reference guide is written and API is understood.
- [ ] **External-facing trader tools** — after your own tools are proven. Not yet.

---

*Last updated: 2026-05-14 (auto) | Updated by nightly task runner.*