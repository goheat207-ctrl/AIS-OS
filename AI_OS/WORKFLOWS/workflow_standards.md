# Workflow Standards

## Universal Production Pipeline

Every project moves through these stages:

```
Brief → Spec → Build → Review → Output → Archive
```

Not every project needs every stage.
Skip stages explicitly — don't drift past them accidentally.

---

## Stage Definitions

### Brief
What we are doing and why.
- Goal of the project
- Audience or user
- Constraints and requirements
- Success criteria

Output: a clear statement of intent, not a document.

---

### Spec
How we are going to do it.
- Structure and approach
- Technical dependencies
- Sequence of work
- What good looks like

Output: a plan specific enough to execute without re-asking.

---

### Build
Doing the work.
- Execute the spec
- Stay in scope
- Surface blockers early
- Do not redesign during build

Output: a working draft or functional artifact.

---

### Review
Is this right?
- Check against the brief
- Apply domain constraints
- Identify gaps
- Validate quality

Output: revised artifact or specific list of changes needed.

---

### Output
Final form, ready for use.
- Formatted correctly
- Named correctly (see naming_conventions.md)
- Stored in the right folder

Output: the deliverable, archived correctly.

---

### Archive
Done.
- Move to the correct archive location
- Update session_handoff.md if relevant
- Update any context files that changed

---

## Stage Anti-Patterns

Brief stage failures:
- Starting build before goal is clear
- Treating a vague idea as a brief

Spec stage failures:
- Over-speccing to avoid starting
- Skipping spec because the task "seems simple"

Build stage failures:
- Redesigning the brief during build
- Adding scope without updating the spec

Review stage failures:
- Reviewing against personal preference instead of the brief
- Calling "looks good" without checking constraints

---

## Minimum Viable Pipeline

For small tasks:
```
Brief (clear intent) → Build → Output
```

For medium tasks:
```
Brief → Spec → Build → Review → Output
```

For large or complex tasks:
```
Brief → Spec → Build (iterative) → Review → Output → Archive
```

Match the pipeline to the task. Don't over-engineer small work.
