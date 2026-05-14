---
name: startup
description: Initialize a domain session. Loads the right neuron context, sets the active domain in system state, and gives a focused briefing for the session ahead.
trigger: manual — run at the start of any work session
---

# /startup

Sets the active domain for this session and loads the relevant neuron context.

## Usage

```
/startup trading
/startup coding
/startup business
/startup os
/startup general
```

If no domain is given, ask which one.

---

## What this skill does

### Step 1 — Set the domain

Map the user's input to one of the five neurons:

| Input | Neuron |
|-------|--------|
| `trading`, `trade`, `market`, `stocks` | trading |
| `coding`, `code`, `build`, `software`, `dev` | coding |
| `business`, `clients`, `biz` | business |
| `os`, `os_design`, `agents`, `skills`, `system` | os_design |
| `general`, `research`, `learning` | general |

### Step 2 — Update system state

Write the active domain to `logs/system_state.json`:

```json
{
  "active_domain": "{neuron_name}",
  "last_prompt_time": 0
}
```

Setting `last_prompt_time` to 0 forces the hook to inject context on the very next prompt, even within the same session. This is the reset mechanism.

Use `main.py` via Bash to update state:

```bash
python D:/AIS-OS/main.py status
```

Or directly update the JSON if main.py doesn't expose a domain-set command yet.

### Step 3 — Load and display the neuron

Read and output the full contents of:
```
Agentic_OS/wiki/neurons/{neuron}/current_state.md
```

Present it clearly. This is the domain briefing.

### Step 4 — Session brief

After loading the neuron, give a 3-line session brief:

```
Domain: {neuron}
Last updated: {date from current_state.md}
Focus: {top priority or known gap from the neuron's content}
```

---

## What changes in the OS

- `logs/system_state.json` → active_domain updated
- `last_prompt_time` → reset to 0 so hook fires on next prompt

No other files are modified.

---

## Examples

**`/startup trading`**
→ Loads neurons/trading/current_state.md
→ Sets active_domain: trading
→ Brief: what you currently know, what tools are active, what the Q2 focus is

**`/startup coding`**
→ Loads neurons/coding/current_state.md
→ Sets active_domain: coding (software)
→ Brief: active projects, languages in use, known gaps

**`/startup os`**
→ Loads neurons/os_design/current_state.md
→ Sets active_domain: os_design
→ Brief: current audit score, active agents/skills, known gaps
