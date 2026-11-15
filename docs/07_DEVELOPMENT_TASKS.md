# Development Tasks — Execute in Order

## Team ownership rules
- Anushka independently owns: Dashboard, Memory Vault, Life Timeline, Memory Connections, Category Manager.
- Ubaid independently owns: Document Vault, Achievement Vault, Smart Search, Priority Vault, Archive & Undo, and the internal FIFO Queue workflow.
- Anushka implements/tests: Array, Singly Linked List, Circular Linked List, Graph, General Tree.
- Ubaid implements/tests: Binary Search Tree, Hash Table, Stack, Queue, Max Heap/Priority Queue.
- Both members jointly agree on database/repository interfaces, integration contracts, end-to-end testing, and final deliverables.
- Each member must develop and test their own modules; do not assign one member to implement the other's modules.



## Phase 0 — Documentation review
- Read all project docs.
- Summarize scope and architecture.
- Identify contradictions.
- Ask for approval before coding.

## Phase 1 — Project foundation
- Create folder structure.
- Create requirements.txt and README.md.
- Create virtual-environment instructions.
- Create minimal CustomTkinter app shell with navy/lavender theme and sidebar.
- Verify the app launches.
- Do not implement all screens yet.

## Phase 2 — Data Structures
Implement each of the ten classes exactly as specified in `03_DATA_STRUCTURES_SPEC.md`.
For each:
- implement methods,
- test empty and normal cases,
- test boundary cases,
- document time complexity,
- run unit tests.
Do not continue until all ten structure tests pass.

## Phase 3 — Database
- Implement SQLite connection and schema.
- Implement repositories for records and connections.
- Add validation, foreign keys and transactions.
- Test add/get/update/archive/restore/delete and relationship persistence.

## Phase 4 — Services and integration
- Implement record service and input validation.
- Build/rebuild custom structures from repository data.
- Integrate search, priority, categories, circular navigation, graph and undo.
- Ensure Queue has a real workflow.
- Add service tests.

## Phase 5 — GUI foundations
- Create reusable sidebar, page header, cards, form fields, dialogs and record rows.
- Implement navigation and dashboard.
- Test empty database and populated database.

## Phase 6 — Core record modules
Build in this order:
1. Memory Vault
2. Document Vault
3. Achievement Vault
Each must support create, read, update, archive and validation.

## Phase 7 — Advanced modules
Build in this order:
1. Search and filters
2. Archive and restore
3. Timeline
4. Memory circular navigation
5. Category tree view
6. Graph connections
7. Priority Vault
8. Undo history
9. Data Structure demo screen

## Phase 8 — Integration and QA
- Test complete user journeys.
- Test persistence after restart.
- Test invalid inputs and missing files.
- Test empty states.
- Fix errors before adding cosmetic enhancements.

## Phase 9 — Final deliverables
- Final README and setup guide.
- Updated architecture and Data Structures documentation.
- Screenshots of actual working screens.
- Test report with real results.
- User guide.
- Viva questions and answers based on actual implementation.
- Presentation outline.

## Antigravity phase prompt template
"Read the relevant LifeVault documentation. Implement Phase [NUMBER] only. Do not start later phases. Before coding, state the files you will create/change and the approach. After coding, run the relevant tests, report exact outcomes, explain the code in beginner-friendly language, and list remaining work. Do not claim untested features work."
