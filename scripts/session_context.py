"""
AIS-OS Session Context Injector
--------------------------------
Called by the UserPromptSubmit hook in .claude/settings.json.

Behavior:
- Fires on every prompt
- If this is a new session (> 30 min since last prompt) AND a domain is active:
  inject the relevant neuron's current_state.md as context
- If same session: output nothing (no repeated injection)
- Always updates last_prompt_time in system_state.json

Output goes to stdout and is injected into Claude's context by the hook.
"""

import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).parent.parent
STATE_FILE = ROOT / "logs" / "system_state.json"
NEURONS_DIR = ROOT / "Agentic_OS" / "wiki" / "neurons"

SESSION_TIMEOUT_SECONDS = 1800  # 30 minutes

DOMAIN_TO_NEURON = {
    "trading": "trading",
    "learning": "trading",
    "software": "coding",
    "coding": "coding",
    "business": "business",
    "os_design": "os_design",
    "automation": "os_design",
    "general": "general",
}

SKIP_DOMAINS = {"system", "none", None}


def load_state() -> dict:
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def save_state(state: dict) -> None:
    STATE_FILE.parent.mkdir(exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2, default=str), encoding="utf-8")


def main() -> None:
    state = load_state()
    now = time.time()
    last_prompt_time = float(state.get("last_prompt_time", 0))
    active_domain = state.get("active_domain")

    # Always update last_prompt_time so next call can detect session boundary
    state["last_prompt_time"] = now
    save_state(state)

    # Skip system domains
    if active_domain in SKIP_DOMAINS:
        return

    # Same session — don't re-inject
    if (now - last_prompt_time) < SESSION_TIMEOUT_SECONDS:
        return

    # New session — find and inject the right neuron
    neuron = DOMAIN_TO_NEURON.get(active_domain, "general")
    current_state_file = NEURONS_DIR / neuron / "current_state.md"

    if not current_state_file.exists():
        return

    content = current_state_file.read_text(encoding="utf-8")

    print("---")
    print(f"AIS-OS: New session detected. Loading {neuron} neuron context.")
    print(f"Active domain: {active_domain}")
    print("---")
    print()
    print(content)
    print()
    print("---")
    print("End of session context. Proceed with the user's request.")
    print("---")


if __name__ == "__main__":
    main()
