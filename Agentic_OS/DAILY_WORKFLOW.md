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




---

## AIS-OS OPERATING WORKFLOW — How to Run This System

This section is domain-agnostic. It applies whether you're trading, building software, running a client project, or learning something new. The sections above are trading-specific. This one is about operating the OS itself.

---

### EVERY SESSION — Universal Start (2 min)

No matter what domain you're working in, do this first:

- [ ] Open Claude Code — `claude` in terminal or desktop app
- [ ] Tell Claude what domain you're in: `/startup [trading | software | business | learning | automation]`
- [ ] Check today's tasks: open `Agentic_OS/TASKS/CURRENT.md` or ask Claude "what's on deck today?"
- [ ] Pick ONE focus for this session — write it down before you start

> If you skip the startup, Claude has no context and gives generic answers. The 30 seconds are worth it.

**Domain routing cheat sheet:**

| What you're doing | Startup command |
|---|---|
| Trading / pre-market / journal review | `/startup trading` |
| Building a tool, script, or dashboard | `/startup software` |
| Client work, local business app | `/startup business` |
| Reading, research, learning | `/startup learning` |
| n8n, agents, automation pipelines | `/startup automation` |
| AIS-OS maintenance, skills, wiki | `/startup automation` |

---

### EVERY SESSION — Universal Close (3 min)

Before you close Claude Code:

- [ ] **Log any decision you made** — if you chose one approach over another, tell Claude to log it: "log this decision" and it writes to `decisions/log.md`
- [ ] **Ingest anything worth keeping** — if you learned something during the session: `/wiki-ingest`
- [ ] **Commit and push** — even a one-liner commit is better than nothing:
  ```
  git add -A && git commit -m "brief description" && git push
  ```
  Or just tell Claude: "commit and push everything" and it handles it.

> The OS only gets smarter if you put things back in. Close-out is where the compounding happens.

---

### WEEKLY CADENCE — Sunday (30–45 min)

Run these two skills back to back every Sunday. They're the engine that keeps the OS improving.

**Step 1 — `/audit` (15 min)**
Four-Cs gap report. Tells you what's weak in the system architecture.
- [ ] Run `/audit` in Claude Code
- [ ] Read the gap report — where is the score lowest?
- [ ] Pick ONE gap to close this week. Write it as a task.

**Step 2 — `/level-up` (20 min)**
Three Ms interview. Surfaces one automation worth building.
- [ ] Run `/level-up` in Claude Code
- [ ] Answer the interview honestly — don't shortcut it
- [ ] Scope the one automation that comes out of it
- [ ] Add it to the Kanban board (`TASKS/AIS-OS Board.md`) under P1 or P2

> `/audit` asks "is the OS built right?" `/level-up` asks "what leverage am I missing?" Run them in this order — fix structure first, then capability planning makes sense.

---

### WHEN YOU HAVE SOMETHING NEW TO ADD

**New knowledge (article, video, notes):**
→ `/wiki-ingest` — drops it into the right neuron in the second brain

**New decision (rule change, process change, trade rule):**
→ Tell Claude: "log this decision" — writes to `decisions/log.md` with the why

**New tool or connection:**
→ Add it to `connections.md` — one line, what it does, how to access it

**New skill to build:**
→ Add a card to the Kanban board P2 column, then build it on a weekend

**New agent to build:**
→ Create `.claude/agents/{name}.md` — follow the format in any existing agent file. Test it before relying on it.

**New n8n workflow:**
→ Build it in n8n, export JSON to `workflows/`, commit. Document in `connections.md`.

---

### MEMORY — How the OS Remembers Things

The OS has two memory layers:

| Layer | Where | What it's for | How to update |
|---|---|---|---|
| **Session context** | CLAUDE.md + wiki neurons | What Claude loads at the start of each session | Edit CLAUDE.md or run `/onboard` to refresh |
| **Persistent memory** | `memory/*.md` files | Facts that carry across every session forever | Tell Claude "remember this" and it writes a memory file |

**When to explicitly ask Claude to remember something:**
- A preference about how you like to work ("don't use bullet points for X")
- A key fact that changes how it should respond ("I'm in drawdown, be conservative")
- A decision you made that should never be revisited ("we're not using X tool")

**When NOT to use memory:**
- Current task state (use TASKS/)
- Code or file content (use the codebase)
- Things already in the wiki

---

### OS HEALTH INDICATORS

**Healthy signs:**
- Claude answers domain questions without you re-explaining context
- `/wiki-search` finds things you put in weeks ago
- The Kanban board has cards moving from P1 → In Progress → Done
- `decisions/log.md` has entries from this week
- `logs/morning-brief.json` has today's date

**Warning signs — address these:**
- Claude asks you to explain your trading rules again → update the trading criteria doc
- Pre-market scan returns irrelevant tickers → agent needs a rules update
- Kanban board hasn't moved in 2 weeks → run `/level-up`, something is blocking
- `logs/morning-brief.json` is stale → brief writer server is down
- You're copy-pasting the same information into Claude every session → that belongs in a memory file or context file

**Critical signs — fix immediately:**
- `git push` fails → stop everything and debug before more commits stack up
- n8n is not running → check startup folder, relaunch manually
- Wiki has no new entries in 3 weeks → ingest backlog is building up, spend 30 min on it

---

---

## AIS-OS OPERATING WORKFLOW

How to actually run this system. Every file and command below is real and in the repo.

---

### THE LAYER MAP — What lives where

Before you can operate the OS, you need to know what each layer is for.

| Layer | Folder | What it does |
|---|---|---|
| **Boot file** | `CLAUDE.md` | Claude reads this every session — the master config |
| **Your context** | `context/` | Who you are, your business, your priorities |
| **Frameworks** | `references/` | 3Ms, voice guide, API references |
| **Intelligence** | `AI_OS/` | Routing logic, trading OS, agent design, memory rules |
| **Domain work** | `domains/` | Where actual work output lives (trading, software, etc.) |
| **Second brain** | `Agentic_OS/wiki/` | Everything you've learned, filed by neuron |
| **Agents** | `.claude/agents/` | Autonomous agents you can run by name |
| **Skills** | `.claude/skills/` | Slash commands that trigger multi-step workflows |
| **Scripts** | `scripts/` | Python automation that runs on a schedule or on demand |
| **Tasks** | `Agentic_OS/TASKS/` | What's next, what's in progress, what's done |
| **Decisions** | `decisions/log.md` | Append-only record of every significant choice |
| **Logs** | `logs/` | Live system output — morning brief, session state |
| **Dashboards** | `dashboards/` | HTML views of the system |

---

### SESSION START — Any domain (2 min)

1. Open Claude Code
2. Run `/startup [domain]` — this triggers `scripts/session_context.py` and loads the right files from `AI_OS/`

   | You're working on | Command |
   |---|---|
   | Trading / pre-market | `/startup trading` → loads `AI_OS/TRADING_SYSTEMS/` |
   | Building a script or tool | `/startup software` → loads `AI_OS/AGENT_SYSTEMS/` + `AI_OS/WORKFLOWS/` |
   | Client or business work | `/startup business` → loads `context/about-business.md` + `AI_OS/WORKFLOWS/` |
   | Research or learning | `/startup learning` → loads `AI_OS/RESEARCH/` + `Agentic_OS/wiki/index.md` |
   | n8n, agents, automation | `/startup automation` → loads `AI_OS/AUTOMATIONS/` + `AI_OS/AGENT_SYSTEMS/` |

3. Check today's tasks: `Agentic_OS/TASKS/CURRENT.md`
4. Pick ONE thing to ship this session

---

### SESSION END — Any domain (3 min)

**Every single session, no exceptions:**

- [ ] **Log decisions** → tell Claude "log this decision" → writes to `decisions/log.md`
- [ ] **Ingest anything worth keeping** → `/wiki-ingest` → files to `Agentic_OS/wiki/neurons/{domain}/`
- [ ] **Commit and push:**
  ```
  git add -A && git commit -m "description" && git push
  ```

---

### THE FILES YOU'LL ACTUALLY TOUCH

**When something about you changes** (new priority, new focus, new tool):
→ Edit `context/priorities.md` or `context/about-me.md`
→ Then tell Claude: "re-read my context" or run `/onboard`

**When you wire a new tool or connection:**
→ Add it to `connections.md` (one line — what it is, how to reach it, what it does)

**When you make a decision that should never be re-litigated:**
→ Tell Claude to log it → `decisions/log.md`

**When you learn something worth keeping:**
→ `/wiki-ingest` → routes to `Agentic_OS/wiki/neurons/[trading|coding|business|os_design|general]/`

**When you want to find something in the wiki:**
→ `/wiki-search [keyword]` → grep across all 80+ wiki files

**When you want to know what's broken in the OS:**
→ `/audit` → reads against `references/3ms-framework.md`, scores Four-Cs

**When you want to find the next thing worth building:**
→ `/level-up` → Three Ms interview, produces one scoped automation

---

### WEEKLY CADENCE — Sunday

| Time | What | File it touches |
|---|---|---|
| 15 min | `/audit` | Reads `context/`, `connections.md`, `AI_OS/` — scores Four-Cs |
| 20 min | `/level-up` | Reads `references/3ms-framework.md` — surfaces one automation |
| 10 min | Kanban review | `Agentic_OS/TASKS/AIS-OS Board.md` — move cards, reprioritize |
| 10 min | Wiki lint | Tell Claude "lint the wiki" → checks `Agentic_OS/wiki/` for gaps |

---

### THE AGENTS — Run these by name

These live in `.claude/agents/` and run autonomously when called:

| Agent | How to run | What it does |
|---|---|---|
| `pre-market-scan` | "run pre-market scan" | Gappers, float, catalyst, rel. volume — your watchlist |
| `small-cap-catalyst` | "run small-cap-catalyst [TICKER]" | Deep dive: SEC filings, dilution, float, catalyst quality |
| `trade-pattern-analyst` | "run trade-pattern-analyst" | Pulls from `goheat207.pythonanywhere.com` — what's working |
| `trading-agents-team` | "run trading-agents-team [TICKER]" | Full BUY/HOLD/SELL pipeline, multi-agent |

---

### THE SCRIPTS — What runs and when

These live in `scripts/` and run automatically or on demand:

| Script | When it runs | What it does |
|---|---|---|
| `session_context.py` | Every time you submit a prompt | Injects date and session state into context |
| `update_tasks.py` | 10PM nightly (Task Scheduler) | Updates `TASKS/CURRENT.md` and `TASKS/BACKLOG.md` |
| `brief_writer_server.py` | On login (Startup folder) | Listens on `localhost:8765` — receives morning brief from n8n |
| `save_morning_brief.py` | Called by n8n at 8AM | Writes `logs/morning-brief.json` |
| `run_trading_agents.py` | On demand | Launches the TradingAgents team pipeline |

**If a script stops working:**
- `brief_writer_server.py` down → run it manually: `python D:/AIS-OS/scripts/brief_writer_server.py`
- `update_tasks.py` not running → check Task Scheduler for "AIS-OS Nightly Task Updater"
- `session_context.py` failing → check `.claude/settings.json` hooks section

---

### THE INTELLIGENCE FILES — Read these when you need to think

These live in `AI_OS/` and are the reasoning backbone of the system. Claude reads them selectively — you can too:

| File | Read it when... |
|---|---|
| `AI_OS/UNIVERSAL_CONTEXT/system_vision.md` | You need to remember what this whole thing is for |
| `AI_OS/UNIVERSAL_CONTEXT/workflow_routing.md` | You're not sure which domain/files to load |
| `AI_OS/TRADING_SYSTEMS/trading_operating_system.md` | You're rethinking your trading process |
| `AI_OS/TRADING_SYSTEMS/risk_framework.md` | You're reviewing or changing your risk rules |
| `AI_OS/AGENT_SYSTEMS/agent_design_principles.md` | You're building or improving an agent |
| `AI_OS/MEMORY/ai_memory_rules.md` | You want to understand what Claude remembers and how |
| `AI_OS/THINKING_MODELS/thinking_frameworks.md` | You're stuck on a decision and need a framework |
| `AI_OS/WORKFLOWS/workflow_standards.md` | You're building a new automation or n8n workflow |
| `references/3ms-framework.md` | Before any `/level-up` session |

---

*Last updated: 2026-05-15 | Replace this file with the UI dashboard when it's built.*
