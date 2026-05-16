# Daily Operating Workflow
**Think of this as your clock-in checklist. Read it every morning until you don't need to.**
*This file lives in Obsidian. A proper dashboard is coming — for now, this is it.*

---

## WHAT RUNS AUTOMATICALLY (you don't touch these)

| What | When | Where to see it |
|------|------|-----------------|
| Morning Journal Pull | 8:00 AM Mon-Fri | n8n at localhost:5678 |
| Nightly Task Updater | 10:00 PM daily | Agentic_OS/TASKS/CURRENT.md |
| n8n starts on login | When Windows boots | Runs in background silently |
| Brief writer server | When Windows boots | localhost:8765 — writes logs/morning-brief.json |

---

## WEEKEND WORKFLOW — Saturday & Sunday

No market. This time is for building the machine.

### Focus 1 — Feed the Brain (wiki ingest)
The wiki only gets smarter if you put things in it. Weekends are ingest time.

- [ ] Open YouTube — watch 1-2 trading/building videos with intention, not passively
- [ ] After each video: open Claude Code, run `/wiki-ingest` — paste the transcript or key notes
- [ ] Check Obsidian Web Clipper for anything you clipped during the week — ingest each one
- [ ] Run `/wiki-search [topic]` to see if the new content fills a known gap
- [ ] Optional: run `lint the wiki` in Claude Code — finds orphan files and stale claims

> Target: 2-3 quality ingests per weekend. Quantity is secondary to quality.

### Focus 2 — Dashboard (build the UI)
The HTML dashboard at `dashboards/blaine-os.html` is the target surface. Build one panel per session.

- [ ] Open `dashboards/blaine-os.html` in browser — note what's broken or missing
- [ ] Pick ONE panel to work on this session (trade metrics, task list, or system status)
- [ ] Connect it to real data: `logs/morning-brief.json`, `TASKS/CURRENT.md`, or the journal API
- [ ] Test it with real data before closing — does the number actually match what you expect?
- [ ] Commit when the panel works: `git commit -m "dashboard: [panel name] connected"`

> Rule: never ship a panel that shows fake or hardcoded data.

### Focus 3 — Agent Improvement
Agents are only as good as the rules you give them. Weekends are for tightening the brief.

- [ ] Pick ONE agent to improve this session (pre-market-scan, small-cap-catalyst, or trade-pattern-analyst)
- [ ] Read its current `.claude/agents/{name}.md` — what's vague, what's missing?
- [ ] Add or sharpen: stock filters, dilution mechanics, catalyst keywords, entry/exit criteria
- [ ] Test it: run the agent, does the output reflect your rules? If not, iterate.
- [ ] Commit the improved agent file

> Agents don't know your rules unless you write them down. Every edit makes them smarter.

### End of weekend — 5 min close-out
- [ ] Commit and push everything: `git add -A && git commit -m "weekend build" && git push`
- [ ] Note one thing that's better than Friday in `decisions/log.md`

---

## BEFORE MARKET OPEN — 8:00 to 9:30 AM

### Step 1 — Open your apps (do this first, every time)
- [ ] Open **ThinkOrSwim** — let it fully load before you do anything else
- [ ] Open **Obsidian** — this file should be your home tab
- [ ] Open **Claude Code** — type `claude` in your terminal or open the desktop app

### Step 2 — Check the morning brief (2 min)
The n8n workflow already pulled your journal data at 8AM.
- [ ] Open browser → go to **localhost:5678**
- [ ] Click the **Morning Journal Pull** workflow → look at the last execution output
- [ ] Scan the metrics: P&L summary, top 3 winners, top 3 losers, Q2 status

> If n8n shows no recent execution: click the workflow and hit **Execute Workflow** manually.
> If the Save Brief node fails: the brief writer server may not be running. Fix: open a terminal and run `python D:/AIS-OS/scripts/brief_writer_server.py`

### Step 3 — Start your Claude Code session (1 min)
- [ ] In Claude Code, type: `/startup trading`
- [ ] Wait for the context confirmation — it loads your trading neuron automatically
- [ ] You're ready. Claude now knows your full trading context for this session.

### Step 4 — Pre-market scan (5-10 min)
- [ ] In Claude Code, type: `run pre-market scan` or use the pre-market-scan agent
- [ ] Review gappers: gap %, float, catalyst. **You decide the tier — not the AI.**
- [ ] Set your watchlist in thinkorswim based on what you see

---

## MARKET HOURS — 9:30 AM to 4:00 PM

### Every trade — do this while it's fresh
- [ ] **Before entry:** know your max loss. If you don't know it, don't enter.
- [ ] **After each trade:** log it in the trade journal (thinkorswim or manually)
- [ ] **Target:** keep per-trade losses at 0.25-0.33% of account. This is Q2's #1 goal.

### If you want Claude's help on a live setup
- [ ] Describe the setup in Claude Code — ask for a quick read, not a decision
- [ ] You make the call. AI confirms or pushes back. Never trades for you.

---

## AFTER MARKET — 4:00 PM onward

### Step 1 — Post-session review (10-15 min)
- [ ] In Claude Code, type: `run trade-pattern-analyst` or ask Claude to review today's trades
- [ ] Pull data from the journal API at **goheat207.pythonanywhere.com**
- [ ] Identify: what worked, what didn't, what to repeat or avoid tomorrow

### Step 2 — Save anything worth keeping
- [ ] If you learned something new → ask Claude to ingest it: `/wiki-ingest`
- [ ] If you made a decision (setup rules, risk rules, process changes) → Claude logs it automatically to `decisions/log.md`

### Step 3 — End-of-session commit and push (2 min)
```
git add [files you changed]
git commit -m "Brief description of what you did today"
git push origin main
```
> Or just tell Claude "commit and push everything from today" and it handles it.

---

## BEFORE BED — Quick check

- [ ] Nightly task runner fires at **10:00 PM** automatically — no action needed
- [ ] It updates CURRENT.md and BACKLOG.md for tomorrow
- [ ] Check **Agentic_OS/TASKS/CURRENT.md** in the morning to see what's next

---

## TROUBLESHOOTING — Quick fixes

| Problem | Fix |
|---------|-----|
| n8n didn't run this morning | Open localhost:5678, run the workflow manually |
| n8n won't open | Search Windows → Task Scheduler → find "AIS-OS n8n Startup" → Run it |
| Morning brief not saving | Brief writer server is down — run `python D:/AIS-OS/scripts/brief_writer_server.py` in a terminal |
| Claude Code has no context | Type `/startup trading` — this reloads everything |
| git push fails | Ask Claude "why is git push failing" before doing anything else |
| Trade journal shows no data | Check goheat207.pythonanywhere.com directly in browser |

---

## QUICK REFERENCE — Commands you'll use daily

|      What you want       | What to type in Claude Code |     When     |
| :----------------------: | :-------------------------: | :----------: |
|   Load trading context   |     `/startup trading`      |    Daily     |
|     Pre-market scan      |    `run pre-market scan`    |    Daily     |
|    Analyze my trades     | `run trade-pattern-analyst` |    Daily     |
| Save a note to the wiki  |       `/wiki-ingest`        | Periodically |
| Weekly automation review |         `/level-up`         |    Sunday    |
|   System health check    |          `/audit`           |  As needed   |

---

*Last updated: 2026-05-14 | Replace this file with the UI dashboard when it's built.*
