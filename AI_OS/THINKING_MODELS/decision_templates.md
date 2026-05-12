# Decision Templates

## Purpose

Reusable structures for making and recording decisions.
Use these to avoid decision debt — choices made implicitly that become hard to revisit.

---

## Template 1 — Simple Decision Record

Use for: any decision that will affect future work.

```
Decision: [what was decided]
Date: YYYY-MM-DD
Context: [what situation prompted this]
Options Considered:
  - [option A] — [tradeoff]
  - [option B] — [tradeoff]
Chosen: [option] because [reason]
Revisit if: [condition that would make this worth reconsidering]
```

---

## Template 2 — Build vs. Buy vs. Borrow

Use for: evaluating whether to build something custom, use a tool, or leverage an existing system.

```
Need: [what capability do we actually need?]

Build:
  - Benefit: [what we gain]
  - Cost: [time + maintenance + complexity]
  - Risk: [what could go wrong]

Buy / Use existing tool:
  - Benefit: [speed, reliability]
  - Cost: [dependency, limitations]
  - Risk: [vendor lock, feature gaps]

Borrow (adapt something existing):
  - Benefit: [lower effort than full build]
  - Cost: [adaptation effort]
  - Risk: [fit may not be perfect]

Verdict: [which, and why]
```

---

## Template 3 — Scope Gate

Use before starting a build to prevent scope creep.

```
Project: [name]
In scope:
  - [item]
  - [item]

Out of scope (explicitly):
  - [item]
  - [item]

Done looks like: [specific, testable description]
```

If something not on the "in scope" list comes up during build:
- Stop
- Decide if it changes the scope
- Update this document before proceeding

---

## Template 4 — Quick Prioritization

Use when facing multiple options and needing to choose one.

```
Options: [list them]

Score each on:
  Impact (1-5):    [how much does it move the goal?]
  Effort (1-5):    [how much work is it? 1=low, 5=high]
  Reversibility:   [easy / hard to undo]

Priority = Impact / Effort

Choose highest priority reversible option first.
```

---

## When to Document a Decision

Document when:
- The choice was non-obvious
- Future work will be constrained by this choice
- A different person (or a future you) would make a different call without this context
- You spent more than 5 minutes deciding

Do not document:
- Trivial formatting choices
- Things already clear from the code or output
- Decisions that will be superseded in hours
