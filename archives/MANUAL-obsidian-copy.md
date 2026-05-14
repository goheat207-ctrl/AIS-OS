# AIS-OS Complete User Manual

**Last updated:** 2026-05-13
**For:** Blaine
**Location:** D:\AIS-OS

---

## The Big Picture — What Is All This?

Your AIS-OS is a **personal AI operating system** built on top of Claude Code. Think of it like a custom control panel that gives Claude a brain, a memory, tools, and rules specific to YOU.

Three layers:

```
Layer 1 — System Brain     (AI_OS folder)
Layer 2 — Your Knowledge   (Agentic_OS/wiki folder)
Layer 3 — Tools & Skills   (.claude folder)
```

Everything in this repo works TOGETHER. You don't need to touch most of it. You just need to know what to TYPE and what to OPEN.

---

## Part 1 — Claude Code (Your Main Interface)

Claude Code is the app/CLI you use to talk to your AI OS. It's what you're using right now.

**How to start a session:**
1. Open Claude Code in VS Code or your terminal
2. Navigate to `D:\AIS-OS`
3. Type your request. Claude reads `CLAUDE.md` automatically and knows your whole setup.

That's it. You don't need to say "hey you're my AI OS" every time. It already knows from `CLAUDE.md`.

---

## Part 2 — Your 3 Core Skills (Slash Commands)

These are your most important tools. Type them exactly as shown.

### `/onboard`
**What it does:** Runs a 7-question setup interview. Fills in `context/about-me.md`, `context/about-business.md`, `context/priorities.md`.

**When to use it:**
- When things change (new goals, new business direction)
- When Claude seems out of date about who you are

**How it works:** Claude asks you 7 questions. You answer. It writes/updates your context files. Done.

---

### `/audit`
**What it does:** Runs a "Four Cs" health check on your OS. Grades it like a report card.

**The Four Cs:**
- **Context** — Does Claude know enough about you?
- **Connections** — What tools are wired in vs. missing?
- **Capabilities** — What can your OS actually do right now?
- **Cadence** — Are you using it consistently?

**When to use it:**
- Day 7 after setup
- Every week after that
- Any time something feels broken or stale

**Output:** A gap report showing where you're weak and what to fix next.

---

### `/level-up`
**What it does:** A weekly Three Ms interview. Finds ONE thing to automate and ships it.

**The Three Ms:**
- **Mindset** — How you're thinking about AI
- **Method** — How you're deciding what to automate
- **Machine** — How you're building it

**When to use it:** Once a week. Every week. Non-negotiable if you want to get better.

**Output:** One shipped automation, script, or improvement each time.

---

## Part 3 — Your Agents (Pre-Built AI Tools)

These are specialized AI agents that do specific trading tasks. They live in `.claude/agents/`.

### `pre-market-scan`
**What it does:** Morning market watchlist. Screens for small-cap gappers with catalyst and volume. Scores setups. Gives you a ranked list before market open.

**How to use it:** Type any of these:
- `pre-market scan`
- `what's gapping today`
- `give me my watchlist`
- `morning brief`

**Best time:** 7:00–9:30 AM ET

---

### `small-cap-catalyst`
**What it does:** Deep dives on a specific stock before you trade it. Pulls SEC 8-K filings, FDA decisions, float/short interest, dilution risk.

**How to use it:** Type any of these:
- `pull catalyst research on [TICKER]`
- `what's the news on HTCO`
- `check float on [TICKER]`
- `is this dilution risk? [TICKER]`

---

### `trade-pattern-analyst`
**What it does:** Analyzes your trade journal data. Finds patterns — what's working, what's not, where you're losing money.

**How to use it:** Type any of these:
- `analyze my trades`
- `what's my win rate on [strategy]`
- `where am I losing money`
- `P&L review`

**Pulls from:** Your live trade journal at `goheat207.pythonanywhere.com`

---

### `trading-agents-team`
**What it does:** Runs a full 10-agent AI analysis on any stock. Bull researchers, bear researchers, risk debaters, portfolio manager — all automated.

**How to use it:** Type: `run trading agents on [TICKER]`

**Warning:** This is slow and costs API tokens. Use it for A-tier setups only, not for scanning.

---

## Part 4 — Your Dashboards (HTML Files)

These are standalone HTML files you open in a browser. They don't connect to live data — they're reference and planning tools.

| File | Where | What it's for |
|------|-------|---------------|
| `blaine-os.html` | Root folder | Main OS overview dashboard |
| `AI_OS/mission-control.html` | AI_OS folder | Status and metrics view |
| `AI_OS/skillsilverplatter.html` | AI_OS folder | Skills reference guide |
| `AI_OS/the-3ms-framework-html.html` | AI_OS folder | Three Ms framework breakdown |
| `AI_OS/four-cs.html` | AI_OS folder | Four Cs architecture |
| `Visual blueprints/small-cap-trading-dashboard.html` | Visual blueprints | Trading dashboard template |
| `Visual blueprints/Tech Builder Blueprint — Year 1.html` | Visual blueprints | Year 1 roadmap |

**How to open:** Double-click the file in Windows Explorer. Opens in your browser.

**These are NOT live.** They're visual references, not connected apps.

---

## Part 5 — Your Second Brain (Obsidian Wiki)

Your wiki lives at `D:\AIS-OS\Agentic_OS\`. It's a folder of markdown files you can open in Obsidian.

**What's in it:**

```
wiki/
├── index.md          <- Start here. Table of contents.
├── entities/         <- Core things (you, tools, platforms)
├── topics/           <- Knowledge areas (strategies, psychology, playbooks)
├── sources/          <- Things you've ingested (articles, prompts)
└── syntheses/        <- AI-generated summaries (empty, ready for use)

raw/                  <- Drop new stuff here to be ingested
├── books/            <- Trading playbooks (already loaded)
├── articles/         <- Articles to read
├── data/             <- CSV/JSON data
└── notes/            <- Loose notes
```

**How to use it with Claude:**
1. Drop a source (article, screenshot, notes) into `Agentic_OS/raw/`
2. Tell Claude: `ingest the file in raw/`
3. Claude reads it, writes it to `wiki/sources/`, updates relevant topic pages, updates the index

**How to browse it in Obsidian:**
1. Open Obsidian
2. Open the vault at `D:\AIS-OS\Agentic_OS\`
3. Browse like a normal Obsidian vault
4. Start at `wiki/index.md`

---

## Part 6 — What's Connected (and What Isn't Yet)

### Connected and working right now:

| Tool | What it does | How Claude uses it |
|------|-------------|-------------------|
| Trade Journal API | Your trades from TOS | Fetches from `goheat207.pythonanywhere.com` |
| yfinance | Stock price/volume data | Python script via `fincept_tools` |
| SEC EDGAR | 10K, 10Q, 8K, insider filings | Python script via `fincept_tools` |
| 40+ Technical Indicators | RSI, VWAP, MACD, etc. | Python script via `fincept_tools` |
| Backtesting engine | Strategy backtesting | Python via `fincept_tools` |
| TradingAgents | 10-agent multi-agent analysis | Python package |
| Obsidian wiki | Second brain | Local markdown files |

### NOT yet connected (still manual):

| Tool | What's needed |
|------|--------------|
| Gmail | Google API key + OAuth setup |
| Google Calendar | Same as Gmail |
| thinkorswim/TD Ameritrade | CSV export pipeline (easiest) |
| Twitter/X | X API key |
| Discord | Discord bot token |
| PayPal | PayPal API key |

Don't stress about these yet. Wire them one at a time when you actually need them. Update `connections.md` each time you add one.

---

## Part 7 — Your Key Files (The Ones That Matter)

| File | Why it matters |
|------|---------------|
| `CLAUDE.md` | Claude reads this every session. It's your OS rules. Don't break this. |
| `aios-intake.md` | Your Q&A intake. Edit this when things change, then re-run `/onboard`. |
| `connections.md` | Registry of every tool. Update whenever you wire something new. |
| `decisions/log.md` | Your decision log. Append entries whenever you make a real decision. |
| `context/about-me.md` | Who you are. Auto-filled by `/onboard`. |
| `context/priorities.md` | Your Q2 goals. Auto-filled by `/onboard`. |
| `references/voice.md` | Your writing voice. Claude uses this for content. |
| `references/3ms-framework.md` | The Three Ms framework. Reference during `/level-up`. |
| `references/trade-journal-api.md` | API endpoints for your trade journal. |
| `EXPANSIONS.md` | What to add as you grow. Read before adding anything new. |
| `MANUAL.md` | This file. |

---

## Part 8 — Your Q2 Goals and How to Work on Them

### Goal 1: Fix the P&L — cut per-trade losses to 0.25–0.33%

How to work on it:
- Run the `trade-pattern-analyst` agent
- Ask: `analyze my trades from the last 30 days, find my biggest loss patterns`
- Ask: `what mistakes am I making most often based on my journal data`
- Use that data to change ONE behavior at a time

---

### Goal 2: Finish the Trade Journal / Backtest Prototype

Your journal is already live at `goheat207.pythonanywhere.com`. For next steps:
- Ask Claude: `what's the current state of my trade journal? what features are missing?`
- The GitHub repo is at `github.com/goheat207-ctrl/backtest_project`
- For coding work, describe what you want in plain English. Claude scopes it, then builds it.

---

### Goal 3: TOS Strategy Backtester with Dilution Tracker, Learning System, and Thinkscript scan filters

This is the biggest one. Break it into pieces:
- Week 1: Ask Claude: `help me scope out the TOS backtester — what are the 3-5 required features for v1?`
- Use `/level-up` each week to ship one piece
- Don't try to build it all at once

---

## Part 9 — Daily and Weekly Workflow

### Morning (pre-market, 7–9:30 AM ET)
1. Open Claude Code in `D:\AIS-OS`
2. Type: `pre-market scan` — get your watchlist
3. Pick a name — type: `pull catalyst on [TICKER]`
4. Trade your plan

### After market close
1. Type: `analyze my trades today`
2. Review patterns, note what went wrong
3. Log any big decisions: `log a decision: [what and why]`

### Weekly (pick one day, keep it consistent)
1. Run `/audit` — see your OS health score
2. Run `/level-up` — find one thing to ship
3. Glance at `connections.md` — anything new to wire?

---

## Part 10 — Common Tasks (How to Do X)

**Look up a stock:**
→ `research [TICKER]` or `run trading agents on [TICKER]`

**See how you've been trading:**
→ `analyze my last 30 days of trades` or `what's my win rate by strategy`

**Save a new article or source:**
→ Drop it in `Agentic_OS/raw/articles/` then tell Claude: `ingest the new file in raw/articles`

**Update your goals:**
→ Edit `aios-intake.md` then tell Claude: `run /onboard`

**Something broke:**
→ Describe what broke. Claude will diagnose it.

**Build something new:**
→ Describe it in plain English. Claude scopes it, then builds it (or hands off to Codex for code).

**Log a decision:**
→ Tell Claude: `log this decision: [what you decided and why]`

**Add a new tool connection:**
→ Wire it → Update `connections.md` → Save a `references/{tool}-api.md` file

**Check on your P&L patterns:**
→ `P&L review` or `show me where I'm losing money`

**Get a weekly report on your trading:**
→ `weekly trading review` or `summarize my trades this week`

---

## Part 11 — What NOT to Touch

- **Don't edit `CLAUDE.md` without knowing what you're doing.** It controls how Claude behaves. Ask Claude to help edit it if needed.
- **Don't delete anything from `AI_OS/`.** Move old stuff to `archives/` instead.
- **Don't add `notes/`, `tmp/`, `misc/` folders.** See `EXPANSIONS.md` for why.
- **Don't run `/level-up` more than once a week.** It's a weekly rhythm, not a dump session.
- **Don't commit API keys or `.env` files to git.** They stay local only.
- **Don't edit wiki files manually unless you know the schema.** Let Claude do it via the ingest flow.

---

## Part 12 — Your Folder Map (Quick Reference)

```
D:\AIS-OS\
├── CLAUDE.md               <- OS rules. Claude reads this first.
├── AGENTS.md               <- Codex rules.
├── MANUAL.md               <- This file.
├── aios-intake.md          <- Your intake Q&A. Edit here, then /onboard.
├── connections.md          <- Tool registry. Always keep up to date.
├── EXPANSIONS.md           <- Growth guide. Read before adding stuff.
├── blaine-os.html          <- Main dashboard. Open in browser.
│
├── context/                <- About you (auto-filled by /onboard)
├── references/             <- Frameworks, voice, API guides
├── decisions/              <- Decision log (append-only)
├── archives/               <- Old stuff. Don't delete, move here.
│
├── AI_OS/                  <- System brain
│   ├── UNIVERSAL_CONTEXT/  <- Rules, philosophy, routing
│   ├── TRADING_SYSTEMS/    <- Trading OS, risk, scanners, journal rules
│   │   └── fincept_tools/  <- Data + backtesting Python library
│   ├── AGENT_SYSTEMS/      <- Agent design patterns
│   └── [dashboards]        <- Reference HTML files
│
├── Agentic_OS/             <- Your second brain (Obsidian wiki)
│   ├── wiki/               <- Curated knowledge
│   └── raw/                <- Drop sources here to ingest
│
├── .claude/                <- Claude Code config
│   ├── agents/             <- Pre-built trading agents
│   └── skills/             <- /onboard, /audit, /level-up
│
├── TradingAgents/          <- 10-agent trading framework (Python)
├── scraper-agent/          <- Web scraper
├── scripts/                <- Python scripts
└── TOS_Statements/         <- Raw trade statement CSVs
```

---

## Quick Start Checklist

If you're starting fresh, do these in order:

- [ ] 1. Open Claude Code in `D:\AIS-OS`
- [ ] 2. Run `/onboard` — answer 7 questions to sync your context
- [ ] 3. Open `blaine-os.html` in your browser — bookmark it
- [ ] 4. Run `pre-market scan` before tomorrow's open
- [ ] 5. After your first trading day, run `analyze my trades today`
- [ ] 6. On Day 7, run `/audit` — see your gap score
- [ ] 7. Once a week, run `/level-up` — ship one automation

That's your whole system in 7 steps.

---

## Glossary

| Term | What it means |
|------|--------------|
| AIOS | AI Operating System — this whole thing |
| Claude Code | The app/CLI you type into |
| CLAUDE.md | The file Claude reads at every session start |
| Skill / slash command | A pre-built task you trigger with `/command` |
| Agent | A specialized AI worker for a specific job |
| fincept_tools | Python library for market data and backtesting |
| TradingAgents | 10-agent framework for deep stock analysis |
| wiki | Your Obsidian second brain at Agentic_OS/wiki/ |
| ingest | The process of adding a source to your wiki |
| connections.md | The registry of every tool wired to your OS |
| Three Ms | Mindset, Method, Machine — the AI framework from Nate Herk |
| Four Cs | Context, Connections, Capabilities, Cadence — audit framework |
| Codex | AI coding agent, implementation partner for building things |
