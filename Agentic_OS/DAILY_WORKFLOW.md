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
