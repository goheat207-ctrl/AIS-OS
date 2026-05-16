---

kanban-plugin: board

---

## 🔴 P1 — This Weekend

- [ ] **Write Blaine's Trading Criteria Doc** #trading #agents #p1
	
	  Single source of truth all agents inherit from. Stock filters, dilution mechanics, catalyst keywords, entry/exit rules, hard no list.
	  
	  📅 2026-05-18
	  **Est:** 45 min | **WIP:** Do this alone first — unlocks every agent task below
	  
	  **Safety Gate:** Read it back. If a stranger could trade your rules from it without asking you a question, it's done.
	  
	  - [ ] Git snapshot before starting
	  - [ ] Stock universe filters (market cap, float, price, avg volume, exchanges)
	  - [ ] Dilution mechanics (S-1 shelf, ATM, warrant overhangs, toxic notes, float rotation)
	  - [ ] Catalyst keywords (FDA, earnings, 8-K types, PR keywords, halt history)
	  - [ ] Entry criteria (price action, tape, relative volume threshold)
	  - [ ] Exit criteria (max loss %, trail method, time-based)
	  - [ ] Hard no list (OTC pinks, sub-$1, no catalyst, etc.)
	  - [ ] Commit: `feat: blaine trading criteria doc — agent source of truth`
- [ ] **Rebuild Pre-Market Scan Agent** #agents #trading #p1
	  Strip all buy/tier language. Add Blaine's actual filters. Output is data — he decides the tier.
	  📅 2026-05-18
	  **Est:** 45 min | **WIP:** Do AFTER Trading Criteria doc is done
	  **Safety Gate:** Run the agent on a day you remember well. Does it surface what you actually watched? If it misses your setup, filters are wrong.
	  - [ ] Git snapshot
	  - [ ] Read current `.claude/agents/pre-market-scan.md` in full
	  - [ ] Strip all buy/tier recommendation language
	  - [ ] Add stock filters from criteria doc (float, cap, price)
	  - [ ] Add catalyst keyword filter — only surface real catalysts
	  - [ ] Add dilution red flag check (recent S-1, toxic history)
	  - [ ] Add relative volume threshold
	  - [ ] Test against 3 real setups you remember
	  - [ ] Commit: `feat: pre-market-scan rebuilt with Blaine's trading criteria`
- [ ] **Dashboard — Trade Metrics Panel** #dashboard #p1
	  One working panel connected to `logs/morning-brief.json`. Win rate, expectancy, P&L, top 3 winners/losers. No fake data.
	  📅 2026-05-18
	  **Est:** 1 hr | **WIP:** Max 2 in progress total
	  **Safety Gate:** Every number on screen must match the raw JSON. If anything is hardcoded, it's not done.
	  - [ ] Git snapshot
	  - [ ] Open `dashboards/blaine-os.html` — note what's hardcoded vs live
	  - [ ] Add JS `fetch()` to read `logs/morning-brief.json` at page load
	  - [ ] Render: win rate, expectancy, profit factor, avg win, avg loss, streak
	  - [ ] Render: top 3 winners and top 3 losers as a table
	  - [ ] Add "Last updated: {generated_at}" timestamp
	  - [ ] Test every number against the raw JSON
	  - [ ] Commit: `feat: dashboard trade metrics panel connected to morning-brief.json`
- [ ] **Add Weekend Workflow to DAILY_WORKFLOW.md** #system #p1
	  Done ✅ (completed 2026-05-15)


## 🟡 P2 — This Month

- [ ] **Update Small-Cap-Catalyst Agent** #agents #trading #p2
	  
	Add dilution mechanics knowledge, S-1 red flags, float rotation, halt patterns, warrant overhangs.
	  **Est:** 1 hr | **WIP:** Max 2 in progress
	  **Safety Gate:** Run it on a stock that burned you. Does it flag the thing that burned you? If not, add that pattern.
	  - [ ] Trading Criteria doc must be done first
	  - [ ] Git snapshot
	  - [ ] Add dilution section (S-1, S-3, 424B filings — what to pull, what to flag)
	  - [ ] Add float section (shares outstanding vs float, insider sells, lockup expiry)
	  - [ ] Add halt history check (flag stocks with multiple consecutive halts)
	  - [ ] Add catalyst quality check (real move vs PR fluff)
	  - [ ] Test on 2 real tickers you traded recently
	  - [ ] Commit: `feat: small-cap-catalyst agent updated with dilution and float logic`
- [ ] **Dashboard — Tasks Panel** #dashboard #p2
	  Second panel showing open tasks from `TASKS/CURRENT.md`. Replaces opening Obsidian just to check what's next.
	  **Est:** 45 min | **WIP:** Max 2 in progress
	  **Safety Gate:** Cross-check 3 tasks between dashboard and CURRENT.md — all must match.
	  - [ ] Trade metrics panel from P1 must be working first
	  - [ ] Parse `TASKS/CURRENT.md` — extract unchecked `[ ]` items
	  - [ ] Render as checklist in dashboard
	  - [ ] Add last-modified timestamp (shows when nightly updater last ran)
	  - [ ] Test: compare dashboard task list to actual CURRENT.md
	  - [ ] Commit: `feat: dashboard tasks panel connected to CURRENT.md`
- [ ] **YouTube → Wiki Ingest — First 3 Runs** #wiki #learning #p2
	  Build the ingest habit before building the automation. 2-3 quality ingests per weekend.
	  **Est:** 30 min per video | **WIP:** Max 1 at a time
	  **Safety Gate:** After filing each, run `/wiki-search [topic]` — if it doesn't surface the file, the ingest didn't land right.
	  - [ ] Pick a trading or system-building video
	  - [ ] Watch with Claude Code open — pause and note key ideas
	  - [ ] Run `/wiki-ingest` with your notes or transcript
	  - [ ] Approve draft, file to the right neuron
	  - [ ] Repeat 2 more times this weekend
	  - [ ] Verify with `/wiki-search` after each
- [ ] **n8n Workflow — Pre-Market Catalyst Pull** #n8n #automation #p2
	  SEC EDGAR 8-K overnight filings at 7AM Mon-Fri. Feeds the trading neuron before market open.
	  **Est:** 1.5 hr | **WIP:** Max 2 in progress
	  **Safety Gate:** Run manually first. Confirm it returns real filings before enabling the schedule.
	  - [ ] Git snapshot
	  - [ ] Research EDGAR full-text search API (efts.sec.gov)
	  - [ ] Build n8n workflow: Schedule (7AM Mon-Fri) → EDGAR API → filter by keywords → save to `logs/catalyst-brief.json`
	  - [ ] Test manually on a day with known filings
	  - [ ] Export workflow JSON to `workflows/`
	  - [ ] Commit: `feat: pre-market catalyst pull workflow (EDGAR 8-K)`
- [ ] **Update connections.md** #system #p2
	  Document brief_writer_server, workflow IDs, what each n8n workflow does.
	  **Est:** 15 min | **WIP:** Can pair with any session
	  - [ ] Open `connections.md`
	  - [ ] Add entry: brief_writer_server (localhost:8765, writes logs/morning-brief.json)
	  - [ ] Add entry: Morning Journal Pull (workflow ID, schedule, output file)
	  - [ ] Add entry: EDGAR workflow when built
	  - [ ] Commit: `docs: update connections.md with n8n and brief writer`
- [ ] **Add Reference Guides for Connected Tools** #system #p2
	  SEC EDGAR, yfinance, TradingAgents each need a `references/{tool}-api.md`. Research once, save forever.
	  **Est:** 30 min per tool | **WIP:** Max 1 tool per session
	  - [ ] `references/edgar-api.md` — EDGAR full-text search, 8-K endpoints, rate limits
	  - [ ] `references/yfinance-api.md` — available data, common calls, limitations
	  - [ ] `references/tradingagents-api.md` — how TradingAgents works, input/output format


## 🔵 P3 — Q3 2026

- [ ] **ThinkScript Scanner Development** #trading #thinkscript #p3
	  Dilution tracker + watchlist scan filters in TOS. Needs dedicated TOS time.
	  **Est:** 4-6 hr (multiple sessions) | **WIP:** Weekend only
	  - [ ] Study ThinkScript scanner syntax
	  - [ ] Build dilution flag scan (ATM offering keywords in news, share count changes)
	  - [ ] Build float/volume filter scan
	  - [ ] Test against known setups
	  - [ ] Document in wiki
- [ ] **TOS Strategy Backtester** #trading #thinkscript #p3
	  Q2 priority. Needs ThinkScript scanner knowledge first.
	  **Est:** 8+ hr | **WIP:** After scanner is done
	  - [ ] Define what "backtest" means in TOS context
	  - [ ] Identify which strategies to test first
	  - [ ] Build ThinkScript study or strategy script
	  - [ ] Document results in wiki
- [ ] **Dashboard — System Status Panel** #dashboard #p3
	  Third panel: wiki entry count, last ingest date, connections health, nightly runner status.
	  **Est:** 45 min | **WIP:** After first two panels are solid
	  - [ ] Count wiki files dynamically
	  - [ ] Show last modified date of key files
	  - [ ] Show brief writer server status (ping localhost:8765)
	  - [ ] Commit: `feat: dashboard system status panel`
- [ ] **Vector/RAG Retrieval for Wiki** #system #p3
	  Don't build until 500+ quality wiki entries. Grep is enough until then.
	  **Est:** 4+ hr | **WIP:** Q3 only
	  - [ ] Gate: run `/wiki-search` and count results — if grep is slow, it's time
	  - [ ] Evaluate: ChromaDB vs Qdrant vs simple sqlite-vec
	  - [ ] Build ingest pipeline from wiki/ folder
	  - [ ] Replace grep in /wiki-search with vector query
- [ ] **n8n Weekly Pattern Review Trigger** #automation #p3
	  Auto-trigger trade-pattern-analyst every Sunday evening. Sends summary to a file or dashboard.
	  **Est:** 1 hr | **WIP:** After EDGAR workflow is stable
	  - [ ] Build n8n workflow: Schedule (Sunday 6PM) → journal API → format weekly summary → save file
	  - [ ] Wire to dashboard or Obsidian note
	  - [ ] Commit: `feat: weekly pattern review n8n workflow`


## ⚙️ OS Maintenance — Recurring

- [ ] **Weekly /audit + /level-up ritual** #system #recurring
  Every Sunday. /audit finds structural gaps. /level-up surfaces one automation to ship. Run back to back, in that order.
  **Est:** 30-45 min | **Cadence:** Every Sunday
  - [ ] Run `/audit` — read the Four-Cs gap report
  - [ ] Pick ONE gap to close this week, add it as a task
  - [ ] Run `/level-up` — answer the Three Ms interview
  - [ ] Scope the one automation that comes out of it
  - [ ] Add scoped task to P1 or P2 column on this board

- [ ] **Wiki lint + ingest backlog check** #wiki #recurring
  Every 2 weeks. Find orphan files, stale claims, and anything sitting in raw/ unprocessed.
  **Est:** 20 min | **Cadence:** Every other Sunday
  - [ ] Tell Claude: "lint the wiki" — checks for orphans and broken links
  - [ ] Check `Agentic_OS/raw/` — anything unprocessed? Run `/wiki-ingest` on each
  - [ ] Check `wiki/log.md` — last ingest should be within 2 weeks
  - [ ] Run `/wiki-search [recent topic]` — confirm new entries are findable

- [ ] **Monthly OS health check** #system #recurring
  First Sunday of each month. Review connections, memory files, and decision log for staleness.
  **Est:** 20 min | **Cadence:** Monthly
  - [ ] Open `connections.md` — any tools added this month that aren't documented?
  - [ ] Check `memory/*.md` — any stale facts to update or remove?
  - [ ] Review `decisions/log.md` — are last month's decisions still holding? Any to revisit?
  - [ ] Check Kanban Done column — archive anything older than 30 days

---

## 🔄 In Progress



## ✅ Done

- [x] **End-of-session audit** — BACKLOG.md consolidated, connections.md updated, CURRENT.md refreshed, decisions/log.md written (6 entries). All task lists current. *(2026-05-15)*
- [x] **AIS-OS operating workflow in DAILY_WORKFLOW.md** — Universal session start/close/cadence/memory/health + Deep Reference with real file paths, layer map, agents table, scripts table. *(2026-05-15)*
- [x] **Kanban board in Obsidian** — AIS-OS Board.md with P1/P2/P3/Recurring columns. Drag-and-drop task management in Obsidian. *(2026-05-15)*
- [x] **Add TOS_Statements/ to .gitignore** — financial data excluded from repo. CSVs untracked, files preserved on disk. *(2026-05-15)*
- [x] **Wire morning brief to save to file** — brief_writer_server.py on port 8765. n8n POSTs, Python writes logs/morning-brief.json. *(2026-05-15)*
- [x] **Wiki keyword search skill** — `/wiki-search` grep-based skill. Returns matching files and snippets. *(2026-05-15)*
- [x] **Add 3+ memory files** — project_n8n.md, project_skills_registry.md added. Memory count now 4. *(2026-05-15)*
- [x] **Set n8n as Windows startup service** — start-n8n.bat in Windows Startup folder. *(2026-05-15)*
- [x] **Nightly task updater** — scripts/update_tasks.py + Task Scheduler at 10PM. *(2026-05-15)*




%% kanban:settings
```
{"kanban-plugin":"board","list-collapse":[null,null]}
```
%%