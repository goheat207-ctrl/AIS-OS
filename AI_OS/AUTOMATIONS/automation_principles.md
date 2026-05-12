# Automation Principles

## Core Question

Before building any automation: is this actually worth automating?

```
Time to build + Time to maintain
         vs.
Time saved × Number of times it runs
```

If the math doesn't favor automation: don't automate.

---

## What to Automate

Good automation candidates:
- Tasks that repeat identically more than weekly
- Tasks where human error is costly and the process is fully defined
- Tasks that are time-sensitive and you won't always be available
- Data collection that runs in the background without your attention

Bad automation candidates:
- Tasks that require judgment each time
- One-off tasks you think might repeat (they often don't)
- Tasks where the process is still being figured out
- Tasks where the automation cost exceeds the gain within a year

---

## Automation Design Rules

### 1. Define the trigger
What starts the automation? Time, event, data condition, or manual trigger?
If you can't define the trigger precisely: the automation isn't ready to build.

### 2. Define the output
What does the automation produce? Where does it go? Who uses it?

### 3. Define the failure mode
What happens when it breaks? Who gets notified?
An automation that fails silently is worse than no automation.

### 4. Build the simplest version first
Start with the most naive implementation that works.
Optimize only after confirming it actually runs and provides value.

### 5. Document it
An undocumented automation is a future mystery.
One-paragraph description: what it does, when it runs, how to turn it off.

---

## Automation vs. Agent

| Factor              | Script / Automation             | AI Agent                        |
| ------------------- | ------------------------------- | ------------------------------- |
| Logic type          | Fully deterministic             | Requires judgment or language   |
| Maintenance         | Low (stable logic)              | Higher (prompt + model drift)   |
| Speed               | Faster, cheaper                 | Slower, more expensive          |
| Best for            | Data pipelines, alerts, CRUD    | Synthesis, routing, analysis    |

Default to scripts for deterministic work.
Use AI agents only where language or judgment is genuinely required.

---

## Anti-Patterns

Avoid:
- Automating a process you don't fully understand yet
- Building automation as a substitute for thinking through the workflow
- Automating something that changes frequently (it will break constantly)
- Running automations you've forgotten about (audit quarterly)
