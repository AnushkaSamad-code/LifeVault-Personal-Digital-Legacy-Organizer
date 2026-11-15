# Module Breakdown and User Workflow

## Team ownership — individual module responsibility

Each member independently develops, tests, and documents their assigned modules.
Do not edit the other member's module implementation. Agree on service/repository
interfaces before integration.

### Anushka Samad — owner of these modules
1. Dashboard — Array for in-memory record collection/statistics.
2. Memory Vault — Circular Linked List for next/previous memory browsing.
3. Life Timeline — Singly Linked List for chronological/history traversal.
4. Memory Connections — Graph using a custom adjacency list; BFS/DFS.
5. Category Manager — General Tree for parent-child categories.

**Anushka's five Data Structures:** Array, Singly Linked List, Circular Linked List, Graph, General Tree.

### Ubaid Raza — owner of these modules
1. Document Vault — document metadata and optional local file paths.
2. Achievement Vault — certificates, awards, and milestones.
3. Smart Search — Binary Search Tree for exact numeric ID search and Hash Table for exact ID lookup.
4. Priority Vault — custom Max Heap / Priority Queue for importance ordering.
5. Archive & Undo — archive/restore workflow and Stack-based undo for supported actions.

**Ubaid's five Data Structures:** Binary Search Tree, Hash Table, Max Heap/Priority Queue, Stack, Queue.

**Queue responsibility:** Ubaid implements the Queue as an internal FIFO pending-task processor (for example, processing record operations in order). It is not assigned as the data structure for the Achievement Vault.

### Shared work — both members
- Agree on database/repository interfaces before either side integrates.
- Integrate independently completed modules.
- Test complete application workflows and persistence.
- Prepare final report, screenshots, user guide, and viva together.



## Navigation
Persistent left sidebar:
1. Dashboard
2. Memory Vault
3. Document Vault
4. Achievement Vault
5. Life Timeline
6. Memory Connections
7. Priority Vault
8. Archive
9. Search
10. Settings / About

## Module 1 — Dashboard (Owner: Anushka)
Purpose: Give a quick overview.
- Cards: total active records, memories, documents, achievements, archived count.
- Recent activity / recently added records.
- Quick action buttons: Add Memory, Add Document, Add Achievement.
- Empty state when no records exist.

## Module 2 — Memory Vault (Owner: Anushka)
Purpose: Manage personal memories.
- Add, view, edit, archive and delete a memory.
- Fields: title, category, date, description, optional file path, importance.
- Browse next/previous memories through Circular Linked List.
- Show memory history using Singly Linked List.

## Module 3 — Document Vault (Owner: Ubaid)
Purpose: Organize document metadata and local file references.
- Add document details and optionally browse for a file.
- Open file only if its path still exists; otherwise show a clear missing-file message.
- Filter by category.
- Do not copy or upload files to any cloud service.

## Module 4 — Achievement Vault (Owner: Ubaid)
Purpose: Keep a record of achievements.
- Add certificates, awards, completed courses and milestones.
- Store title, organization/category, date, description and optional file path.
- Show achievement cards and timeline entries.

## Module 5 — Life Timeline (Owner: Anushka)
Purpose: Display Memory and Achievement records in date order.
- Sort chronologically.
- Allow filtering by record type and date range.
- Timeline sorting may use a clear sorting method; explain if a custom structure is used.

## Module 6 — Memory Connections (Owner: Anushka)
Purpose: Show relationships between records.
- Select a source record and target record.
- Create an undirected relationship.
- Display neighbors of a selected record.
- Prevent self-links and duplicate links.
- Graph data must be built using a custom adjacency-list Graph class.

## Module 7 — Priority Vault (Owner: Ubaid)
Purpose: Display important records first.
- Priority scale: 1 (normal) to 5 (highest).
- Custom max-heap / Priority Queue.
- Explain that changing a record's priority requires rebuilding or updating the heap.

## Module 8 — Archive & Undo (Owner: Ubaid)
Purpose: Keep records out of the active view without permanently deleting them.
- View archived records.
- Restore record.
- Permanently delete only after confirmation.
- Archive is a database status, not a separate copy of the record.

## Module 9 — Smart Search (Owner: Ubaid)
Purpose: Find records.
- Search exact numeric ID using BST and/or Hash Table.
- Search title/category/description using a case-insensitive linear scan.
- Clearly distinguish exact ID lookup from keyword search.
- Show a friendly no-results state.

## Internal Queue workflow (Owner: Ubaid)
Purpose: Process pending record tasks in FIFO order.
- Use the custom Queue for pending tasks such as add/update/archive requests.
- Demonstrate enqueue, dequeue, front/peek, is_empty, and size in a real workflow.

## Main user journey
1. User opens LifeVault.
2. Dashboard loads records from SQLite.
3. Application rebuilds in-memory Data Structures.
4. User adds a memory/document/achievement.
5. Service validates input and writes to SQLite.
6. In-memory indexes are updated or rebuilt.
7. GUI refreshes the affected screen.
8. On restart, SQLite reloads the records and structures are rebuilt.
