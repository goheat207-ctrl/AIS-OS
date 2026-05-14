You want **safe refactor prompts** (not a full system prompt) that your AI code bot can execute step-by-step without breaking your current AIS-OS.

Below are **clean, structured prompts you can run in sequence**. Each one is designed to be:

- non-destructive
    
- incremental
    
- reversible
    
- dependency-aware
    
- safe for live systems
    

---

# ⚙️ PHASE 0 — SAFETY CHECK (RUN FIRST)

```text
Analyze the entire AIS-OS directory at D:\AIS-OS.

Your only task:
1. Map the full folder structure
2. Identify all active systems (agents, commands, trading tools, wiki, dashboards, scripts)
3. Identify any duplicate folders or overlapping responsibilities
4. Identify high-risk dependencies (anything referenced by multiple systems)

DO NOT change, move, rename, or delete anything.

Output:
- Full system map
- Dependency risks
- Overlapping systems
- Recommended safe refactor order
```

---

# 🧠 PHASE 1 — ARCHITECTURE GROUPING (NO CHANGES YET)

```text
Based on the full AIS-OS structure, categorize every folder and file into logical groups:

Use ONLY these categories:
1. core system (orchestration, memory, routing, logging)
2. personality layer (user-specific logic, trading behavior, preferences)
3. domains (trading, business, software, learning, automation)
4. agents (AI workers)
5. workflows (multi-step processes)
6. builders (tools that generate apps/UI/dashboards)
7. integrations (external APIs/services)
8. knowledge system (Obsidian/wiki/raw/syntheses)
9. UI/dashboards
10. logs/system telemetry
11. sandbox/experimental
12. archives/legacy
13. unclear/needs review

DO NOT modify anything.

Output:
- Every folder mapped to one category
- List anything ambiguous or misclassified
```

---

# 🧩 PHASE 2 — CLEAN TARGET STRUCTURE PROPOSAL

```text
Design a cleaned, optimized folder structure for AIS-OS based on the current system.

Rules:
- Must NOT remove functionality
- Must preserve ALL current features
- Must support personal-first system (Blaine-specific)
- Must support future multi-user deployments
- Must be modular and scalable

Output ONLY:
1. Proposed final folder structure
2. Explanation of why each top-level folder exists
3. Migration safety notes (what could break if moved incorrectly)
```

---

# 🔒 PHASE 3 — SAFE MIGRATION PLAN (NO EXECUTION)

```text
Create a step-by-step SAFE migration plan to move the current AIS-OS into the proposed structure.

Constraints:
- No breaking changes allowed
- Must use staged migration
- Must preserve all imports, paths, and references
- Must prioritize system stability over cleanliness

Output:
1. Phase 1 (safe folder creation only)
2. Phase 2 (non-critical moves)
3. Phase 3 (core system migration)
4. Phase 4 (cleanup + consolidation)

Also include:
- rollback strategy
- risk points
```

---

# 🧱 PHASE 4 — SAFE FOLDER CREATION ONLY

```text
Create ONLY the new folder structure needed for the future AIS-OS architecture.

Rules:
- DO NOT move any files
- DO NOT delete anything
- DO NOT rename anything
- ONLY create empty folders
- Ensure no conflicts with existing structure

After creation, output:
- list of new folders created
- confirmation that nothing was modified
```

---

# 🔄 PHASE 5 — NON-BREAKING FILE MIGRATION (LOW RISK ONLY)

```text
Move ONLY low-risk, non-dependent files into the new structure.

Rules:
- Do NOT move core system, agents, or commands yet
- Do NOT move anything referenced by CLAUDE.md or active scripts
- Only move:
  - dashboards (HTML/UI files)
  - sandbox/experimental code
  - clearly isolated utilities
  - archives/legacy-safe files

For each move:
- explain why it is safe
- confirm no dependencies are affected

Output:
- list of moved files
- list of files NOT moved and why
- risk report
```

---

# 🧠 PHASE 6 — DEPENDENCY VALIDATION (IMPORTANT)

```text
Verify that no broken references exist after recent structural changes.

Check:
- Python imports
- script paths
- agent references
- command routing
- wiki ingestion paths
- dashboard file links

Output:
- any broken references
- suggested fixes (DO NOT auto-fix yet)
- system health status
```

---

# 🧭 PHASE 7 — FINAL CONSOLIDATION CHECK

```text
Evaluate the current AIS-OS structure after refactor steps.

Provide:
1. New system architecture summary
2. What improved
3. What still needs work
4. Any technical debt introduced
5. Recommended next improvement step

Do NOT modify anything.
```

---

# ⚠️ HOW TO USE THESE (IMPORTANT)

Run them **in this order only**:

1 → Phase 0 (map system)  
2 → Phase 1 (classification)  
3 → Phase 2 (target design)  
4 → Phase 3 (migration plan)  
5 → Phase 4 (create folders only)  
6 → Phase 5 (safe moves only)  
7 → Phase 6 (validation)  
8 → Phase 7 (review)

---

# 🧠 WHY THIS WORKS (CRITICAL INSIGHT)

This avoids the biggest failure mode in AI OS builds:

> “refactoring while simultaneously redesigning and moving logic”

Instead it enforces:

- map first
    
- understand second
    
- design third
    
- plan fourth
    
- build structure fifth
    
- migrate slowly sixth
    
- validate constantly
    

That is how real production systems are refactored.

---

