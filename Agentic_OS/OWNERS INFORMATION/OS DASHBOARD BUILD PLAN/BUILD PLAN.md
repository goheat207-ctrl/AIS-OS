 Plan: Wire Blaine OS Dashboard to Local FastAPI Server                                                                                                                                                                                                                                     
 Context

 The blaine-os.html dashboard looks operational but is almost entirely fake:
 - Metrics (win rate 30.6%, 242 trades, -$141.81 P&L) are hardcoded HTML
 - Integration status dots are hardcoded CSS classes
 - The RUN button copies to clipboard — it does not execute anything
 - The Run Log only tracks clipboard copies in localStorage (resets context between sessions)
 - The AUDIT_LOG array is hardcoded in the HTML and only updated by manually editing the file
 - The War Room is a scripted theatre piece with no real agents
 - The ONE real connection is fetchTodayTrades() → goheat207.pythonanywhere.com/api/trades

 Goal: Build a local FastAPI server that the dashboard can fetch() from, making the Run Log, metrics, integrations, and audit history
 genuinely live. Keep it scoped — one afternoon of work.

 ---
 What We Are NOT Fixing

 - War Room (scripted UI, out of scope)
 - Making RUN actually execute Claude (requires Claude API integration, separate project)
 - Connecting Gmail, Discord, social accounts (connections gap, separate project)

 ---
 Architecture

 blaine-os.html  ←→  http://localhost:8765  ←→  local files + trade journal API

 Server runs as a background process. Dashboard detects if it's up on load. If offline, shows stale data with an "OFFLINE" badge. If live,
 replaces hardcoded values with fetched data.

 Port: 8765 (avoids conflict with journal server on 5000, TradingAgents on 8000)

 ---
 Files to Create

 1. D:/AIS-OS/server/aios_server.py

 Single-file FastAPI app. Endpoints:

 ┌────────┬───────────────────────┬────────────────────────────────────────────────────────────────────────┐
 │ Method │         Path          │                                  Does                                  │
 ├────────┼───────────────────────┼────────────────────────────────────────────────────────────────────────┤
 │ GET    │ /api/health           │ Returns {status: "ok", timestamp} — dashboard polls this               │
 ├────────┼───────────────────────┼────────────────────────────────────────────────────────────────────────┤
 │ GET    │ /api/run-log          │ Reads audits/run-log.json, returns array of audit entries              │
 ├────────┼───────────────────────┼────────────────────────────────────────────────────────────────────────┤
 │ POST   │ /api/run-log          │ Appends new audit entry to audits/run-log.json                         │
 ├────────┼───────────────────────┼────────────────────────────────────────────────────────────────────────┤
 │ GET    │ /api/audit/{filename} │ Serves raw markdown from audits/ folder as text                        │
 ├────────┼───────────────────────┼────────────────────────────────────────────────────────────────────────┤
 │ GET    │ /api/metrics          │ Proxies goheat207.pythonanywhere.com/api/metrics, caches 5min          │
 ├────────┼───────────────────────┼────────────────────────────────────────────────────────────────────────┤
 │ GET    │ /api/skill-runs       │ Returns last 100 skill runs from server/skill-runs.json                │
 ├────────┼───────────────────────┼────────────────────────────────────────────────────────────────────────┤
 │ POST   │ /api/skill-run        │ Appends a skill run entry to server/skill-runs.json                    │
 ├────────┼───────────────────────┼────────────────────────────────────────────────────────────────────────┤
 │ GET    │ /api/connections      │ Parses connections.md, returns array with {name, status, last_checked} │
 └────────┴───────────────────────┴────────────────────────────────────────────────────────────────────────┘

 CORS: allow all origins (localhost file:// use case).

 Metrics caching: store last fetch timestamp + result in memory. If < 5min old, return cached. Prevents hammering the trade journal API on
 every dashboard load.

 2. D:/AIS-OS/server/requirements.txt

 fastapi==0.115.0
 uvicorn==0.30.0
 httpx==0.27.0

 3. D:/AIS-OS/server/start.bat

 Windows batch file. Double-click to start server:
 @echo off
 cd /d D:\AIS-OS
 pip install -r server/requirements.txt -q
 uvicorn server.aios_server:app --host 127.0.0.1 --port 8765 --reload
 pause

 4. D:/AIS-OS/audits/run-log.json

 Machine-readable version of the run log. Seed with today's audit:
 [
   {
     "date": "2026-05-13",
     "score": "71/100",
     "stage": "Stage 2: Compounding",
     "file": "audit-2026-05-13.md"
   }
 ]

 5. D:/AIS-OS/server/skill-runs.json

 Persisted skill run history (created empty, populated by dashboard):
 []

 ---
 Files to Modify

 6. D:/AIS-OS/dashboards/blaine-os.html

 On page load — server detection:
 Add initDashboard() call that pings /api/health. If 200: set window.SERVER_LIVE = true and fetch live data. If fail: set window.SERVER_LIVE =
  false, add an "OFFLINE" badge to the header, keep hardcoded values.

 Metrics section (lines 322-341) — replace hardcoded values:
 Fetch GET /api/metrics. Response from trade journal API includes: win_rate, total_trades, net_pnl, current_streak. Update the DOM elements
 .m-val and .m-sub for win rate and trade count cards.

 Integration dots (lines 352-368) — make status live:
 Fetch GET /api/connections. Server returns each connection's status from connections.md. Add/remove .pending class dynamically instead of
 hardcoding it.

 Run Log tab (lines 768-775) — replace localStorage with server:
 - On tab open: fetch GET /api/skill-runs, render the list
 - On doRun(): also POST /api/skill-run with {name, time, preview}
 - Remove the localStorage dependency (or keep as fallback when offline)

 Audit History section (line 776) — remove hardcoded AUDIT_LOG:
 On page load: fetch GET /api/run-log, populate #auditLog dynamically. Remove the hardcoded AUDIT_LOG const from JS. The VIEW → buttons will
 link to /api/audit/{filename} so the server serves the markdown.

 Trade Journal tab (lines 892-923) — already works, no change needed.
 fetchTodayTrades() already hits the real API. Leave it.

 Chart data (lines 1658-1690) — optionally make live:
 Could fetch equity curve from /api/metrics → /api/equity-curve proxy. Defer this — it's cosmetic. Mark as Phase 2.

 7. D:/AIS-OS/.claude/skills/audit/SKILL.md

 Replace Step 5c (which currently edits the HTML file directly — fragile) with:

 5c. After writing the markdown file and appending to run-log.md, also:
 - Write/update audits/run-log.json by reading the existing file, prepending the new entry, and writing back
 - Optionally: POST http://localhost:8765/api/run-log with {date, score, stage, file} if the server is running (fire-and-forget, do not fail
 if server is offline)
 - Remove the step that edits blaine-os.html's AUDIT_LOG array directly (dashboard now fetches from server)

 8. D:/AIS-OS/connections.md

 Add row for the AIOS local server:
 | 16 | AIOS Local Server | FastAPI (aios_server.py) | script (server/start.bat → uvicorn) | local | 2026-05-13 |

 ---
 Implementation Order

 9. Create server/aios_server.py — get the server running and testable first
 10. Create audits/run-log.json — seed with today's audit entry
 11. Create server/skill-runs.json — empty array
 12. Create server/requirements.txt and server/start.bat
 13. Update dashboard — wire all fetch() calls
 14. Update audit skill — swap HTML-edit step for JSON-write step
 15. Update connections.md
 16. Start server + reload dashboard + verify

 ---
 Verification

 17. Run server/start.bat — terminal should show Uvicorn running on http://127.0.0.1:8765
 18. Open browser → http://127.0.0.1:8765/api/health → should return {"status":"ok"}
 19. Open browser → http://127.0.0.1:8765/api/run-log → should return the audit entry array
 20. Open dashboards/blaine-os.html in browser:
   - Header should show "LIVE" indicator (not "OFFLINE")
   - Win rate metric should update from trade journal API
   - Run Log tab → Audit History should show today's entry with working VIEW → link
 5. Click a skill button → click RUN → check http://127.0.0.1:8765/api/skill-runs → new entry should appear
 6. Run /audit again → new entry appears in audits/run-log.json → dashboard Audit History updates on next load

 ---
 What This Does NOT Do

 - Does not make RUN execute Claude (clipboard copy behavior stays — that's a separate Claude API integration)
 - Does not make War Room agents real
 - Does not connect Gmail/Discord (those are separate connections tasks)
 - Does not require always-on — dashboard gracefully degrades when server is offline