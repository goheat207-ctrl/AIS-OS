# main.py — AIS-OS Orchestrator Design

## What It Is

`main.py` is the Python execution runtime for AIS-OS.

It handles the code-execution side of the OS:
- receiving commands from CLI, Claude, or agents
- routing to the right domain and handler
- maintaining system state between runs
- logging all actions to `logs/`
- enforcing safety on destructive operations

It does NOT replace Claude Code. Claude handles intelligence, judgment, and conversation. `main.py` handles execution, routing, and state.

---

## Architecture

```
python main.py <command> [args]
        |
        v
  Command Registry
  (COMMANDS dict)
        |
        v
  Domain Router          ← maps command to domain (trading/software/etc)
  (DOMAIN_MAP dict)
        |
        v
  Handler Function       ← executes logic, calls tools, prints output
        |
        v
  State Update           ← writes logs/system_state.json
        |
        v
  Log Entry              ← appends to logs/aios_YYYY-MM-DD.log
```

---

## Command Registry

| Command | Domain | Handler | What it does |
|---------|--------|---------|--------------|
| `status` | system | cmd_status | Print system state, domain health |
| `scan [TICKER]` | trading | cmd_scan | Route pre-market scan |
| `analyze TICKER [DATE]` | trading | cmd_analyze | Run TradingAgents pipeline |
| `journal [DATE]` | trading | cmd_journal | Route journal review |
| `research TOPIC` | learning | cmd_research | Route research request |
| `ingest FILE` | learning | cmd_ingest | Queue file for wiki ingest |
| `log MESSAGE` | system | cmd_log | Append to decisions/log.md |
| `build [PROJECT]` | software | cmd_build | Route build task |
| `help` | system | cmd_help | Print usage |

Adding a command: add handler function + entry to `COMMANDS` + entry to `DOMAIN_MAP`.

---

## State Model

Stored in `logs/system_state.json`:

```json
{
  "last_run": "2026-05-13T10:00:00",
  "active_domain": "trading",
  "active_workflows": [],
  "session_count": 12,
  "system_health": "ok",
  "flags": {}
}
```

`flags` is a freeform dict for feature toggles or temporary markers.

---

## Safety Layer

`safety_check(path, operation)` blocks writes to protected paths:

Protected: `CLAUDE.md`, `AI_OS/`, `Agentic_OS/`, `decisions/log.md`, `.claude/`, `.codex/`

If blocked: prints a message, logs a warning, returns False. Does NOT raise an exception. Never silently fails.

---

## Logging Structure

All logs go to `logs/aios_YYYY-MM-DD.log`.

Format: `2026-05-13 09:30:00 [INFO] Command: scan | Domain: trading | Args: [AAPL]`

Log levels used:
- INFO: normal execution, state changes
- WARNING: safety blocks, unexpected but non-fatal states
- ERROR: command failures with full traceback

---

## Extending main.py

To add a new command:

```python
def cmd_mycommand(args: list) -> int:
    # args is a list of strings from CLI
    # return 0 for success, 1 for error
    update_state(active_domain="my_domain")
    logger.info("My command: %s", args)
    print("[MY_DOMAIN] ...")
    return 0

COMMANDS["mycommand"] = cmd_mycommand
DOMAIN_MAP["mycommand"] = "my_domain"
```

---

## What main.py Does NOT Do

- Does not make AI decisions (that's Claude's job)
- Does not contain domain logic (that lives in domain handlers or Python packages)
- Does not manage Obsidian (wiki operations stay in Claude sessions)
- Does not store secrets (use .env files)
