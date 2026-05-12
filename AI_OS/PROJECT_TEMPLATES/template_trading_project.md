# Trading Project Template

## Folder Structure

```
ACTIVE_PROJECTS\[project-name]\
├── CLAUDE.md              ← Copy from _template_project_claude.md, fill in
├── brief.md               ← What we're trading and why
├── scanners\
│   └── [scanner_name].md  ← Scanner logic, ThinkScript, or criteria
├── journals\
│   └── YYYY-MM-DD_journal.md
├── research\
│   └── [ticker_or_topic].md
└── outputs\
    └── [analysis or recap files]
```

---

## CLAUDE.md Additions for Trading Projects

Add these sections to the project CLAUDE.md:

```
## Trading Context

Instrument: [small cap / options / futures / crypto / etc.]
Timeframe: [intraday / swing / position]
Strategy Type: [momentum / reversal / catalyst / etc.]

## Inherit From

- D:\AI_OS\TRADING_SYSTEMS\trading_operating_system.md
- D:\AI_OS\TRADING_SYSTEMS\risk_framework.md
- D:\AI_OS\TRADING_SYSTEMS\journal_system.md [if journaling]
- D:\AI_OS\TRADING_SYSTEMS\scanner_development.md [if building scanners]
```

---

## Session Startup (Trading)

1. Read project CLAUDE.md
2. Read trading_operating_system.md
3. Read risk_framework.md
4. If scanner work: read scanner_development.md
5. If journal review: read journal_system.md + thinking_frameworks.md

---

## Output Standards for Trading Projects

Journal entries:
- Named: `YYYY-MM-DD_journal.md`
- Contains: tickers, setups, executions, mistakes, lessons

Scanner files:
- Named: `[setup-type]_scanner.md` or `.ts` for ThinkScript
- Contains: criteria, logic, rationale

Research files:
- Named: `YYYY-MM-DD_[ticker]_research.md`
- Contains: catalyst, float, dilution risk, levels, thesis
