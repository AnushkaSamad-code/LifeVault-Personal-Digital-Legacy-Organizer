# LifeVault — Antigravity Project Instructions

## Project identity
- **Project:** LifeVault — Personal Digital Legacy Organizer
- **Team:** Anushka Samad (CSC-25F-083), Ubaid Raza (CSC-25F-013)
- **Course:** Data Structures
- **Language:** Python
- **GUI:** CustomTkinter
- **Storage:** Local SQLite
- **Complexity:** Medium
- **Theme:** Navy with lavender accents

## How Antigravity must work
Read all Markdown files in this folder before changing or generating code. Treat `PROJECT_REQUIREMENTS.md` and `DATA_STRUCTURES_SPEC.md` as the source of truth.

Build the application in small, reviewable phases. Do not generate the entire application in one step. At the end of each phase:
1. Summarize files created or changed.
2. Explain the implementation in beginner-friendly language.
3. Run relevant tests and report actual results.
4. List known issues and the next phase.
5. Wait for the user's approval before moving to the next phase.

Do not claim a feature works unless it has been run and tested.

## Non-negotiable engineering rules
1. Implement all ten required Data Structures manually in separate Python classes.
2. Do not replace required custom structures with Python `dict`, `set`, `list`, `queue.Queue`, or `heapq` for the core algorithm. Python lists may be used for GUI display, test fixtures, or temporary presentation data where clearly appropriate.
3. SQLite is the persistent source of truth. Custom Data Structures are in-memory indexes/algorithms and must be rebuilt from database records on application startup.
4. Keep GUI, business logic, Data Structures, and database code separate.
5. Use parameterized SQL queries.
6. Validate user input and handle missing files and database errors gracefully.
7. Do not store actual sensitive personal documents during demos. Use sample records.
8. Do not add cloud sync, AI features, authentication services, inheritance transfer, or legal claims. They are outside this medium-complexity scope.
9. Do not silently change project scope or technology choices. Ask first.
10. Keep code readable, commented where helpful, and suitable for a BSCS Data Structures viva.

## Required development order
Phase 0: Read documentation and confirm understanding.
Phase 1: Project setup, environment, folder structure, app shell.
Phase 2: Implement and test all ten Data Structures independently.
Phase 3: SQLite schema and repository/data-access layer.
Phase 4: Service layer integrating database and custom structures.
Phase 5: GUI shell, navigation, dashboard and reusable components.
Phase 6: Memory, Document and Achievement modules.
Phase 7: Search, category tree, timeline, graph connections, priority view, archive and undo.
Phase 8: Integration, validation, error handling and full testing.
Phase 9: Final documentation, screenshots, demo data and presentation support.

## First instruction
Start with **Phase 0 only**. Read all project Markdown documents and return:
- a concise understanding of the project,
- the ten Data Structures and their planned responsibilities,
- the proposed folder architecture,
- a list of ambiguities or conflicts, if any,
- the exact Phase 1 tasks.

Do not write application code until the user approves Phase 1.
