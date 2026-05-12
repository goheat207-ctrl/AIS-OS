# Agent Routing Patterns

## Purpose

How to coordinate multiple AI agents without building unnecessary complexity.

---

## Pattern 1 — Sequential Pipeline

Use when: each step depends on the output of the previous step.

```
Input → Agent A → Output A → Agent B → Output B → Final Output
```

Example: Research → Summarize → Format → Publish

Rules:
- Each agent gets only the output of the prior step plus its own context
- Do not pass the full pipeline history to every agent
- Validate output before passing to next stage

---

## Pattern 2 — Parallel Gather

Use when: multiple independent sub-tasks need to complete before synthesis.

```
Input ──→ Agent A → Output A ──┐
       └→ Agent B → Output B ──┼→ Synthesis Agent → Final Output
       └→ Agent C → Output C ──┘
```

Example: Research three companies simultaneously, then compare.

Rules:
- Agents in the parallel step should be identical in structure
- Synthesis agent receives all parallel outputs plus a synthesis prompt
- Do not let parallel agents "know about" each other

---

## Pattern 3 — Router + Specialist

Use when: input type varies and different inputs need different handling.

```
Input → Router Agent → identifies type
                    → if Type A: Specialist A
                    → if Type B: Specialist B
                    → if Type C: Specialist C
```

Example: Inbound query goes to trading agent or content agent based on topic.

Rules:
- Router has no specialist logic — it only routes
- Specialists have no routing logic — they only execute
- Keep routing rules explicit and in a routing context file

---

## Pattern 4 — Critic Loop

Use when: output quality must meet a defined standard before continuing.

```
Generator Agent → Output → Critic Agent → Score
                                       → if pass: continue
                                       → if fail: Generator Agent (revised context)
```

Rules:
- Critic must have explicit, objective criteria
- Set a maximum iteration count (2-3 loops maximum)
- If max iterations reached without pass: surface to human, do not loop indefinitely

---

## Coordination Anti-Patterns

Avoid:
- Agents that talk to each other without a defined output format
- Infinite loops without human checkpoints
- Context accumulation across many hops (each hop gets only what it needs)
- Building routing logic inside every agent
