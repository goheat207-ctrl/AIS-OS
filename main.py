"""
AIS-OS Central Orchestrator
----------------------------
The runtime control system for Blaine's AI Operating System.

Usage:
    python main.py status
    python main.py scan [TICKER]
    python main.py analyze TICKER [DATE]
    python main.py journal [DATE]
    python main.py research TOPIC
    python main.py ingest FILE_PATH
    python main.py log MESSAGE
    python main.py help

Domains: trading | software | business | learning | automation
"""

import sys
import os
import json
import logging
from datetime import datetime, date
from pathlib import Path

# ─── Paths ────────────────────────────────────────────────────────────────────

ROOT = Path(__file__).parent
LOGS_DIR = ROOT / "logs"
STATE_FILE = ROOT / "logs" / "system_state.json"
DECISIONS_LOG = ROOT / "decisions" / "log.md"
DOMAINS_DIR = ROOT / "domains"
WIKI_INDEX = ROOT / "Agentic_OS" / "wiki" / "index.md"
CONNECTIONS = ROOT / "connections.md"
TOS_STATEMENTS = ROOT / "TOS_Statements"

LOGS_DIR.mkdir(exist_ok=True)

# ─── Logging ─────────────────────────────────────────────────────────────────

log_file = LOGS_DIR / f"aios_{datetime.now().strftime('%Y-%m-%d')}.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(log_file, encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger("aios")


# ─── State ────────────────────────────────────────────────────────────────────

DEFAULT_STATE = {
    "last_run": None,
    "active_domain": None,
    "active_workflows": [],
    "session_count": 0,
    "system_health": "ok",
    "flags": {},
}


def load_state() -> dict:
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return DEFAULT_STATE.copy()
    return DEFAULT_STATE.copy()


def save_state(state: dict) -> None:
    STATE_FILE.write_text(json.dumps(state, indent=2, default=str), encoding="utf-8")


def update_state(**kwargs) -> dict:
    state = load_state()
    state.update(kwargs)
    state["last_run"] = datetime.now().isoformat()
    save_state(state)
    return state


# ─── Safety Layer ─────────────────────────────────────────────────────────────

PROTECTED_PATHS = [
    ROOT / "CLAUDE.md",
    ROOT / "AI_OS",
    ROOT / "Agentic_OS",
    ROOT / "decisions" / "log.md",
    ROOT / ".claude",
    ROOT / ".codex",
]


def safety_check(path: Path, operation: str = "modify") -> bool:
    """Block destructive operations on protected system paths."""
    resolved = path.resolve()
    for protected in PROTECTED_PATHS:
        if resolved == protected.resolve() or str(resolved).startswith(
            str(protected.resolve())
        ):
            logger.warning(
                "SAFETY BLOCK: %s operation on protected path %s", operation, path
            )
            print(f"\n[SAFETY] Cannot {operation} protected path: {path}")
            print("  Log this intent in decisions/log.md and do it manually.\n")
            return False
    return True


# ─── Append to Decisions Log ──────────────────────────────────────────────────

def log_decision(title: str, decision: str, why: str = "") -> None:
    entry = f"\n## {date.today()} — {title}\n\n**Decision:** {decision}\n"
    if why:
        entry += f"\n**Why:** {why}\n"
    entry += "\n**Owner:** Blaine\n"
    with open(DECISIONS_LOG, "a", encoding="utf-8") as f:
        f.write(entry)
    logger.info("Decision logged: %s", title)


# ─── Command Handlers ─────────────────────────────────────────────────────────

def cmd_status(args: list) -> int:
    """Show current AIS-OS system state."""
    state = load_state()
    print("\n=== AIS-OS STATUS ===========================")
    print(f"  Last run:        {state.get('last_run', 'never')}")
    print(f"  Active domain:   {state.get('active_domain', 'none')}")
    print(f"  System health:   {state.get('system_health', 'unknown')}")
    print(f"  Session count:   {state.get('session_count', 0)}")
    workflows = state.get("active_workflows", [])
    print(f"  Active workflows: {len(workflows)}")
    for wf in workflows:
        print(f"    - {wf}")

    print("\n  Domain folders:")
    for domain in ["trading", "software", "business", "learning", "automation"]:
        path = DOMAINS_DIR / domain
        file_count = len(list(path.rglob("*"))) if path.exists() else 0
        print(f"    {domain:<12} {file_count} files")

    print("\n  Wiki: ", "OK" if WIKI_INDEX.exists() else "MISSING")
    print("  Connections: ", "OK" if CONNECTIONS.exists() else "MISSING")
    print("=============================================\n")

    update_state(
        active_domain="system",
        session_count=state.get("session_count", 0) + 1,
    )
    logger.info("Status check completed")
    return 0


def cmd_scan(args: list) -> int:
    """Route a pre-market scan to the trading domain."""
    ticker = args[0].upper() if args else None
    update_state(active_domain="trading")
    logger.info("Pre-market scan requested — ticker: %s", ticker or "watchlist")

    print("\n[TRADING] Pre-market scan")
    if ticker:
        print(f"  Ticker: {ticker}")
        print(f"  Run: Use Claude agent 'pre-market-scan' or 'small-cap-catalyst'")
        print(f"  Command: 'scan {ticker}' in Claude Code session")
    else:
        print("  Run: Ask Claude 'pre-market scan' for today's watchlist")
    print()
    return 0


def cmd_analyze(args: list) -> int:
    """Run TradingAgents multi-agent analysis."""
    if not args:
        print("[ERROR] Usage: python main.py analyze TICKER [DATE]")
        return 1

    ticker = args[0].upper()
    analysis_date = args[1] if len(args) > 1 else str(date.today())
    update_state(active_domain="trading")
    logger.info("TradingAgents analysis: %s on %s", ticker, analysis_date)

    print(f"\n[TRADING] TradingAgents analysis: {ticker} / {analysis_date}")

    trading_agents_dir = ROOT / "TradingAgents"
    runner = ROOT / "scripts" / "run_trading_agents.py"

    if not trading_agents_dir.exists():
        print("[ERROR] TradingAgents not found at expected path.")
        return 1

    print(f"  Running: python {runner} {ticker} {analysis_date}")
    print("  Or use the 'trading-agents-team' Claude agent directly.\n")

    os.system(f'python "{runner}" {ticker} {analysis_date}')
    return 0


def cmd_journal(args: list) -> int:
    """Route a journal review task."""
    target_date = args[0] if args else str(date.today())
    update_state(active_domain="trading")
    logger.info("Journal review for %s", target_date)

    print(f"\n[TRADING] Journal review: {target_date}")

    statement_files = list(TOS_STATEMENTS.glob("*.csv")) if TOS_STATEMENTS.exists() else []
    print(f"  Account statements on file: {len(statement_files)}")
    for f in statement_files:
        print(f"    - {f.name}")

    print("\n  Ask Claude: 'analyze my trades today' or 'analyze trades for [date]'")
    print("  Or use the 'trade-pattern-analyst' agent.\n")
    return 0


def cmd_research(args: list) -> int:
    """Route a research request to the knowledge/learning domain."""
    topic = " ".join(args) if args else None
    if not topic:
        print("[ERROR] Usage: python main.py research TOPIC")
        return 1

    update_state(active_domain="learning")
    logger.info("Research request: %s", topic)

    print(f"\n[LEARNING] Research: {topic}")
    print(f"  Wiki index: {WIKI_INDEX}")
    print("  Steps:")
    print("  1. Read Agentic_OS/wiki/index.md for existing knowledge")
    print(f"  2. Search wiki/topics/ for '{topic}'")
    print("  3. If new source needed: drop file in Agentic_OS/raw/articles/")
    print("  4. Ask Claude to ingest and update wiki\n")
    return 0


def cmd_ingest(args: list) -> int:
    """Log a new source file for wiki ingestion."""
    if not args:
        print("[ERROR] Usage: python main.py ingest FILE_PATH")
        return 1

    file_path = Path(args[0])
    if not file_path.exists():
        print(f"[ERROR] File not found: {file_path}")
        return 1

    update_state(active_domain="learning")
    logger.info("Ingest queued: %s", file_path)

    print(f"\n[LEARNING] Ingest queued: {file_path.name}")
    print("  Next: Ask Claude to ingest this file into the wiki")
    print("  Command: 'ingest [filename]' or drop into Agentic_OS/raw/ and ask Claude\n")
    return 0


def cmd_log(args: list) -> int:
    """Quick-append a note to the decisions log."""
    if not args:
        print("[ERROR] Usage: python main.py log MESSAGE")
        return 1

    message = " ".join(args)
    log_decision("Quick note", message)
    print(f"\n[LOG] Appended to decisions/log.md: {message}\n")
    return 0


def cmd_build(args: list) -> int:
    """Route a build task to the appropriate domain."""
    project = " ".join(args) if args else None
    update_state(active_domain="software")
    logger.info("Build task: %s", project or "unspecified")

    print(f"\n[SOFTWARE] Build: {project or '(unspecified)'}")
    print("  Steps:")
    print("  1. Drop brief into domains/software/ or domains/trading/")
    print("  2. Ask Claude to run workflow: Brief → Spec → Build → Review → Output")
    print("  3. Reference: AI_OS/WORKFLOWS/workflow_standards.md\n")
    return 0


def cmd_help(args: list) -> int:
    """Print usage."""
    print(__doc__)
    return 0


# ─── Command Registry ─────────────────────────────────────────────────────────

COMMANDS: dict = {
    "status": cmd_status,
    "scan": cmd_scan,
    "analyze": cmd_analyze,
    "journal": cmd_journal,
    "research": cmd_research,
    "ingest": cmd_ingest,
    "log": cmd_log,
    "build": cmd_build,
    "help": cmd_help,
}

# Domain routing: which commands belong to which domain
DOMAIN_MAP: dict = {
    "scan": "trading",
    "analyze": "trading",
    "journal": "trading",
    "research": "learning",
    "ingest": "learning",
    "build": "software",
    "log": "system",
    "status": "system",
    "help": "system",
}


# ─── Entry Point ──────────────────────────────────────────────────────────────

def main() -> int:
    args = sys.argv[1:]

    if not args:
        return cmd_help([])

    command = args[0].lower().lstrip("/")
    command_args = args[1:]

    if command not in COMMANDS:
        print(f"\n[ERROR] Unknown command: '{command}'")
        print(f"  Available: {', '.join(sorted(COMMANDS))}\n")
        return 1

    domain = DOMAIN_MAP.get(command, "system")
    logger.info("Command: %s | Domain: %s | Args: %s", command, domain, command_args)

    try:
        return COMMANDS[command](command_args)
    except KeyboardInterrupt:
        logger.info("Interrupted by user")
        return 0
    except Exception as exc:
        logger.error("Command '%s' failed: %s", command, exc, exc_info=True)
        print(f"\n[ERROR] Command failed: {exc}")
        print("  Check logs/ for details.\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
