# Agent Design Principles

## Core Principle

Build the minimum agent that accomplishes the job.
Complexity is not intelligence.

---

## When to Build an Agent

Build an agent when:

- A task repeats frequently enough to justify automation
- The task has a well-defined input → output structure
- The task can be broken into discrete steps
- A human checking the output is practical

Do NOT build an agent when:

- You could do it with a single well-structured prompt
- The task requires too much judgment to automate reliably
- The maintenance cost will exceed the time saved

---

## Agent Architecture Principles

### 1. Single Responsibility

One agent does one thing.
An agent that does "research and then writes and then posts" is three agents poorly combined.

### 2. Clear Input/Output Contract

Before building: define exactly what the agent receives and exactly what it produces.
If you can't state the contract in 2 sentences, the design is unclear.

### 3. Fail Loudly

Agents should surface errors and ambiguity — not guess and continue silently.
A bad output delivered confidently is worse than no output.

### 4. Human in the Loop for Judgment

Automate execution. Do not automate judgment.
Agents should flag edge cases for human review, not override them.

### 5. Stateless When Possible

Agents that don't carry state between runs are easier to debug, test, and maintain.
State should live in files or databases — not inside the agent.

---

## Agent Context Loading

When building an agent prompt:

- Load only the context the agent's specific task requires
- Do not dump the full workspace into the agent prompt
- Use the workflow_routing.md routing table to determine what the agent needs
- Apply token_economy.md principles to the agent's context design

---

## Anti-Patterns

Avoid:

- Mega-agents that do everything
- Agents with no defined output format
- Agents that can't explain what they did
- Agents that run indefinitely without human checkpoints
- Building agents to avoid thinking through a workflow

---

## Agent vs. Workflow Decision

| Situation                          | Use                      |
| ---------------------------------- | ------------------------ |
| Task repeats daily, same structure | Agent                    |
| Task is complex but happens once   | Structured workflow      |
| Task requires judgment each time   | Human + AI collaboration |
| Task is fully deterministic        | Script (not AI at all)   |
