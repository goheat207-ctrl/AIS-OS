"""
AIS-OS Nightly Task Updater
----------------------------
Called by n8n at 10PM every night.
Reads system state, git log, and audit history.
Updates Agentic_OS/TASKS/CURRENT.md, BACKLOG.md, and COMPLETED.md.
"""

import json
import subprocess
import sys
from datetime import datetime, date
from pathlib import Path

ROOT = Path(__file__).parent.parent
TASKS_DIR = ROOT / "Agentic_OS" / "TASKS"
STATE_FILE = ROOT / "logs" / "system_state.json"
AUDIT_LOG = ROOT / "audits" / "run-log.md"
DECISIONS_LOG = ROOT / "decisions" / "log.md"
CURRENT = TASKS_DIR / "CURRENT.md"
BACKLOG = TASKS_DIR / "BACKLOG.md"
COMPLETED = TASKS_DIR / "COMPLETED.md"

TODAY = date.today().isoformat()
NOW = datetime.now().strftime("%Y-%m-%d %H:%M")


def load_state() -> dict:
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def get_todays_commits() -> list[str]:
    """Return list of today's commit messages."""
    try:
        result = subprocess.run(
            ["git", "log", "--oneline", "--since=midnight", "--format=%s"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=10,
        )
        lines = [l.strip() for l in result.stdout.strip().splitlines() if l.strip()]
        return lines
    except Exception:
        return []


def get_latest_audit() -> str:
    """Return the latest audit score line from run-log.md."""
    if not AUDIT_LOG.exists():
        return "No audit on file."
    lines = AUDIT_LOG.read_text(encoding="utf-8").splitlines()
    data_lines = [l for l in lines if l.startswith("|") and "Score" not in l and "---" not in l and "Date" not in l]
    return data_lines[-1] if data_lines else "No audit on file."


def get_completed_today() -> list[str]:
    """Pull today's commits as completed items."""
    commits = get_todays_commits()
    if not commits:
        return []
    return [f"- [x] {c}" for c in commits]


def read_backlog_tasks() -> tuple[list[str], list[str], list[str], list[str]]:
    """Parse existing backlog into P0/P1/P2/P3 buckets. Returns unchecked tasks only."""
    if not BACKLOG.exists():
        return [], [], [], []

    content = BACKLOG.read_text(encoding="utf-8")
    p0, p1, p2, p3 = [], [], [], []
    current_bucket = None

    for line in content.splitlines():
        if "## P0" in line:
            current_bucket = p0
        elif "## P1" in line:
            current_bucket = p1
        elif "## P2" in line:
            current_bucket = p2
        elif "## P3" in line:
            current_bucket = p3
        elif line.strip().startswith("- [ ]") and current_bucket is not None:
            current_bucket.append(line.strip())

    return p0, p1, p2, p3


def update_current() -> None:
    state = load_state()
    active_domain = state.get("active_domain", "unknown")
    session_count = state.get("session_count", 0)
    last_run = state.get("last_run", "unknown")
    commits = get_todays_commits()
    audit = get_latest_audit()

    p0, p1, _, _ = read_backlog_tasks()
    next_task = p0[0] if p0 else (p1[0] if p1 else "See BACKLOG.md")

    built_today = "\n".join(f"- {c}" for c in commits) if commits else "- No commits recorded today."

    content = f"""# AIS-OS — Current Focus

What's actively being worked on right now. Updated nightly at 10PM automatically.

---

## Last Session: {TODAY}

**Active domain:** {active_domain}
**Session count:** {session_count}
**Last activity:** {last_run}

**Built / committed today:**
{built_today}

**Latest audit:** {audit.strip()}

---

## Next Session: Start Here

1. Run `git push origin main` from your terminal if there are unpushed commits
2. Run `/startup [domain]` to load the right neuron context
3. Pick the top P0 task from BACKLOG.md

**Next recommended task:**
{next_task}

---

*Auto-updated: {NOW}*
"""
    CURRENT.write_text(content, encoding="utf-8")
    print(f"[OK] CURRENT.md updated")


def update_completed() -> None:
    commits = get_todays_commits()
    if not commits:
        print("[SKIP] No commits today — COMPLETED.md unchanged.")
        return

    existing = COMPLETED.read_text(encoding="utf-8") if COMPLETED.exists() else "# AIS-OS — Completed Work\n\nAppend-only log. Newest at top.\n\n---\n"

    # Check if today's date already has an entry
    if f"## {TODAY}" in existing:
        print("[SKIP] Today's entry already exists in COMPLETED.md.")
        return

    items = "\n".join(f"- [x] {c}" for c in commits)
    new_entry = f"""## {TODAY}

{items}

---

"""
    # Insert after the header block
    insert_after = "Newest at top.\n\n---\n"
    if insert_after in existing:
        updated = existing.replace(insert_after, insert_after + "\n" + new_entry)
    else:
        updated = existing + "\n" + new_entry

    updated += f"\n*Auto-updated: {NOW}*"
    COMPLETED.write_text(updated, encoding="utf-8")
    print(f"[OK] COMPLETED.md updated with {len(commits)} commit(s).")


def update_backlog() -> None:
    """Append last-updated timestamp to bottom of BACKLOG.md."""
    if not BACKLOG.exists():
        print("[SKIP] BACKLOG.md not found.")
        return

    content = BACKLOG.read_text(encoding="utf-8")

    # Update the last-updated line
    lines = content.splitlines()
    updated_lines = []
    for line in lines:
        if line.startswith("*Last updated:"):
            updated_lines.append(f"*Last updated: {TODAY} (auto) | Updated by nightly task runner.*")
        else:
            updated_lines.append(line)

    BACKLOG.write_text("\n".join(updated_lines), encoding="utf-8")
    print(f"[OK] BACKLOG.md timestamp updated.")


def main() -> None:
    TASKS_DIR.mkdir(parents=True, exist_ok=True)
    print(f"[AIS-OS] Nightly task update — {NOW}")

    update_current()
    update_completed()
    update_backlog()

    print("[AIS-OS] Task update complete.")


if __name__ == "__main__":
    main()
