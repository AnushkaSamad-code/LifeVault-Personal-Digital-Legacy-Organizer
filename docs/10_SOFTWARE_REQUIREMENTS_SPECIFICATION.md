# Software Requirements Specification (SRS)
## LifeVault – Personal Digital Legacy Organizer

**Course:** Data Structures (BSCS)  
**Academic Level:** Undergraduate / University Level  
**Project Complexity:** Medium  
**Application Type:** Standalone Local Desktop Application  
**Document Status:** Baseline Requirements Specification (Submission-Ready)  

---

### Project Team & Module Ownership
* **Anushka Samad** (Student ID: `CSC-25F-083`)  
  *Modules:* Dashboard, Memory Vault, Life Timeline, Memory Connections, Category Manager  
  *Data Structures:* Dynamic Array, Singly Linked List, Circular Linked List, Graph, General Tree  
* **Ubaid Raza** (Student ID: `CSC-25F-013`)  
  *Modules:* Document Vault, Achievement Vault, Smart Search, Priority Vault, Archive & Undo, Internal Task Queue Pipeline  
  *Data Structures:* Binary Search Tree, Hash Table, Max-Heap / Priority Queue, Stack, Queue  

---

## 1. Introduction

### 1.1 Purpose of the SRS
This Software Requirements Specification (SRS) establishes the formal functional, non-functional, interface, and data requirements for the **LifeVault – Personal Digital Legacy Organizer** desktop application. LifeVault is proposed as an offline, single-user desktop software application engineered in Python to catalog, preserve, index, and interlink personal memories, milestone achievements, and important documents.

In addition to fulfilling its operational role as an intuitive desktop organizer, LifeVault is architected specifically as a curriculum demonstration project for an undergraduate Data Structures course. This document defines the system's structural boundaries, manual data structure implementations, dual-state synchronization rules, error-handling behaviors, and objective acceptance criteria. It serves as the baseline for implementation, verification, and academic evaluation.

### 1.2 Project Scope
LifeVault will provide a private, local-first repository for organizing personal historical records categorized into three distinct types:
* **Memories:** Narrative recollections of life experiences with associated dates, emotional significance, and optional local media file references.
* **Documents:** Metadata records and filesystem path references for vital educational, career, personal, and medical files located on the user's local disk.
* **Achievements:** Milestone records such as awards, honors, certifications, completed courses, and degrees.

The application pairs a persistent SQLite database with ten custom-implemented in-memory data structures. To ensure technical correctness, the in-memory data structures are categorized by their operational roles:
1. **Persistent Runtime Indexes and Algorithmic Views:** Reconstructed from SQLite upon application startup:
   * *Dynamic Array:* Indexes active records for dashboard metric computations and sequential iteration.
   * *Circular Linked List:* Maintains active memory records for cyclical carousel browsing.
   * *Singly Linked List:* Maintains chronologically sorted active records for timeline traversal.
   * *Category Tree (General N-ary Tree):* Reconstructed from the hierarchical category paths stored across active records in `records.category`.
   * *Graph (Adjacency List):* Reconstructed from the `record_connections` table to represent semantic record networks.
   * *Binary Search Tree (BST):* Indexes active records by integer record ID for ordered lookups.
   * *Hash Table (Separate Chaining):* Indexes active records by integer record ID for fast key lookup.
   * *Priority Queue (Binary Max-Heap):* Arranges active records in non-increasing order of importance.
2. **Transient Operational Structures:** Session-bound structures initialized empty at startup:
   * *Stack:* Captures recent reversible commands in memory to support multi-step undo operations during the active user session.
   * *Queue:* Manages an internal synchronous FIFO pending-task buffer for sequencing record mutation operations.

**System Boundaries:**
* **Included:** Local CRUD operations on records; local file path validation and native launching; chronological event sequencing; associative graph networking; category taxonomy browsing; exact numeric and text-based searching; priority triage; transactional undo history for supported actions; synchronous FIFO task queuing; and a dedicated viva diagnostics screen.
* **Excluded:** Cloud synchronization; remote backups; network communications; multi-user accounts or authentication; automated AI/ML tagging or classification; optical character recognition (OCR); direct storage of large binary files in SQLite; and legal will or estate execution.

### 1.3 Intended Audience
This specification is addressed to:
* **Academic Evaluators and Course Instructors:** To evaluate the architectural integrity, algorithmic rigor, and manual data structure implementations against university curriculum standards.
* **Project Authors (Anushka Samad and Ubaid Raza):** To guide individual module development, define clear component interfaces, enforce persistence workflows, and steer pytest test suite construction.

### 1.4 Definitions, Acronyms, and Abbreviations
* **ADT:** Abstract Data Type. A mathematical specification of a data structure defining its behavior and operations independently of implementation details.
* **BFS:** Breadth-First Search. A layer-by-layer graph traversal algorithm.
* **BST:** Binary Search Tree. A node-based binary tree maintaining the invariant $Key_{Left} < Key_{Node} < Key_{Right}$.
* **CRUD:** Create, Read, Update, Delete. The core lifecycle operations of persistent records.
* **CustomTkinter:** A modern Python UI library extending `tkinter` with styled, high-DPI scaled widgets.
* **DFS:** Depth-First Search. A branch-first graph traversal algorithm.
* **FIFO:** First-In, First-Out. An access ordering principle where elements are dequeued in the exact order they were enqueued (Queue).
* **FK:** Foreign Key. A relational database constraint linking related tables.
* **GUI:** Graphical User Interface.
* **LIFO:** Last-In, First-Out. An access ordering principle where the most recently pushed element is popped first (Stack).
* **N-ary Tree:** A general tree data structure wherein each node maintains an arbitrary number of child node references.
* **PK:** Primary Key. A unique identifier for a database row.
* **pytest:** The automated testing framework used to verify custom data structures and service logic via `python -m pytest`.
* **SQLite:** An embedded, serverless, transactional SQL relational database engine.
* **SRS:** Software Requirements Specification.

### 1.5 Document Overview
The remainder of this document is organized as follows:
* **Section 2:** Overall Description (product perspective, decoupled architecture, user characteristics, operating environment, design constraints).
* **Section 3:** System Features and Functional Requirements (detailed requirements for all ten modules and the internal queue processor, containing exactly 62 functional requirements).
* **Section 4:** External Interface Requirements (UI design system, hardware, software, communications).
* **Section 5:** Non-Functional Requirements (performance, reliability, usability, security, maintainability, portability, data integrity, offline operation, containing exactly 22 non-functional requirements).
* **Section 6:** Data Requirements and SQLite Database Schema (approved tables, dual-state data flows, category tree reconstruction, operational structures).
* **Section 7:** Use Case Specifications (formal specifications for ten primary workflows).
* **Section 8:** System Constraints and Boundaries.
* **Section 9:** Objective Acceptance Criteria (criteria AC-01 through AC-11).
* **Section 10:** Requirements Traceability Matrix (mapping all 62 functional requirements).
* **Section 11:** Assumptions, Dependencies, and Explicitly Identified Design Decisions.

---

## 2. Overall Description

### 2.1 Product Perspective
LifeVault is an autonomous desktop software system designed for local deployment. It operates within the user's local operating system environment and maintains absolute independence from external servers or network services. 

The software strictly adheres to a decoupled 4-layer architecture:

```
+--------------------------------------------------------------------------+
|                     1. PRESENTATION LAYER (GUI)                          |
|    CustomTkinter Navigation Sidebar, Content Panes, Cards, and Dialogs   |
+--------------------------------------------------------------------------+
                                    |
                                    v
+--------------------------------------------------------------------------+
|                       2. SERVICE LAYER (LOGIC)                           |
|      Validation, State Orchestration, Dual-State Sync, Undo Logging      |
+--------------------------------------------------------------------------+
                   /                                      \
                  v                                        v
+-----------------------------------+    +---------------------------------+
| 3. DATA STRUCTURES LAYER (MEMORY) |    | 4. PERSISTENCE LAYER (STORAGE)  |
| 10 Custom Python Data Structures  |    | SQLite Database & Repositories  |
| - Fast in-memory indexing         |    | - Single persistent truth       |
| - Algorithmic traversal & search  |    | - Parameterized relational SQL  |
+-----------------------------------+    +---------------------------------+
```

#### Architectural Interaction Rules:
1. **Presentation Layer Isolation:** The GUI never communicates directly with SQLite. GUI event handlers invoke Service Layer methods exclusively.
2. **Service Layer Orchestration:** The Service Layer validates user input, coordinates repository operations, and enforces the dual-state synchronization protocol.
3. **Database Precedence (Source of Truth):** Persistent state modifications are committed to SQLite first. Only upon successful transaction commit does the Service Layer update or rebuild affected in-memory data structures. If a database transaction fails, the in-memory state remains unmodified, preventing state drift.
4. **Data Structures Layer Isolation:** Custom data structure classes contain no database access logic or GUI references; they operate strictly as in-memory data managers.

### 2.2 Product Functions
LifeVault provides the following primary functions:
* **Dashboard Summary:** Aggregating record metrics and surfacing recently registered items.
* **Record Vault Management:** Creating, viewing, editing, archiving, restoring, and permanently deleting records across three entity types (Memories, Documents, Achievements).
* **Filesystem Document Referencing:** Storing local path strings and safely opening attached files via native OS applications with path validation.
* **Cyclic Memory Carousel:** Navigating active memories in an endless loop using a circular linked list.
* **Chronological Lifetime Timeline:** Traversing dated memories and achievements sequentially using a singly linked list.
* **Relational Graph Modeling:** Creating undirected relationships between records and traversing connections using BFS and DFS algorithms.
* **Hierarchical Taxonomy:** Organizing records into category trees and navigating subcategories using an N-ary tree.
* **Dual-Engine Search:** Performing exact numeric ID lookups via a hash table and binary search tree, alongside text-based keyword matching.
* **Priority Triage:** Displaying records in order of importance (priority 5 down to 1) using a binary max-heap.
* **Session Undo History:** Reverting recent supported state-altering actions during the active session using a LIFO stack.
* **Synchronous Task Staging:** Processing queued record operations in strict FIFO sequence using a linked queue.
* **Academic Viva Diagnostics:** Inspecting internal data structure states, node linkages, and operation logs.

### 2.3 User Characteristics
* **Target User:** An individual seeking a structured, local repository for personal digital history.
* **Technical Background:** Standard desktop computer literacy (typing, window management, selecting files through file pickers).
* **Access Level:** Single user. LifeVault relies on host operating system user accounts for filesystem-level access boundaries; no application-level authentication is implemented.

### 2.4 Operating Environment
* **Platform:** Cross-platform desktop operating systems (Microsoft Windows 10/11, macOS 12+, or modern Linux distributions).
* **Python Runtime:** Python 3.10, 3.11, or 3.12.
* **Display Requirement:** Recommended minimum display resolution of $1280 \times 720$ pixels.
* **Storage Footprint:** Standard desktop storage (< 100 MB for Python environment and database file, excluding external user files).

### 2.5 Design and Implementation Constraints
* **Manual Data Structures Implementation:** All ten data structures must be authored manually in standalone Python classes in `data_structures/`. Standard library containers (such as `list`, `dict`, `set`, `heapq`, or `queue.Queue`) must not be used to implement the core algorithms.
* **Persistent Source of Truth:** SQLite (`sqlite3`) is the sole persistent store. All queries must use parameterized placeholders (`?`) to prevent SQL injection, and foreign keys must be explicitly enabled via `PRAGMA foreign_keys = ON;`.
* **Synchronous Execution:** All data structure operations, database queries, and task processing workflows must execute synchronously in the application thread. Asynchronous worker threads, background tasks, and schedulers are excluded to ensure deterministic testing and academic evaluation.
* **Visual Direction:** The interface must adhere to the designated Navy and Lavender design system (`#172B4D` primary navy, `#243B63` secondary navy, `#B9A7E8` lavender accent, `#F4F5FA` canvas, `#FFFFFF` cards).
* **Schema Integrity:** Requirements must strictly conform to the approved database schema (`records` and `record_connections`). No unsupported tables (such as `activity_log` or `categories`) or columns shall be introduced.

### 2.6 Assumptions and Dependencies
* The host environment has a functioning Python 3.10+ interpreter with packages listed in `requirements.txt` installed (specifically `customtkinter` and `pytest`).
* User-referenced local files remain at their specified filesystem paths; if moved or deleted externally, LifeVault will handle the missing path gracefully without raising unhandled exceptions.
* Normal operating system file permissions permit reading and writing the SQLite database file in the application directory.

---

## 3. System Features and Functional Requirements

The system defines exactly 62 uniquely numbered functional requirements (`FR-001` through `FR-062`) partitioned across ten user-facing functional modules and one internal task queue pipeline.

### 3.1 Module 1: Dashboard (Owner: Anushka Samad)
**Description:** Serves as the application landing screen, presenting aggregate record metrics, recent entries, and quick creation shortcuts.  
**Associated Data Structure:** Dynamic Array (`DynamicArray`) — Maintains the in-memory array of active records to compute active summary counts, filter recent items, and support indexed iteration.

* **FR-001:** The system shall display aggregate summary metric cards for: Total Active Records, Active Memories, Active Documents, Active Achievements, and Archived Records.
* **FR-002:** The system shall compute active record metrics (Total Active Records, Active Memories, Active Documents, and Active Achievements) through traversal of the in-memory `DynamicArray`, while the Archived Records count shall be retrieved through an SQLite repository query to preserve the four-layer architecture without storing archived records in the active in-memory array.
* **FR-003:** The system shall render a "Recent Activity" view displaying up to five of the most recently created active records ordered by the existing `created_at` timestamp in descending order, populated from the active in-memory `DynamicArray` without adding unapproved database columns.
* **FR-004:** The system shall provide quick-action buttons on the Dashboard that navigate directly to the creation forms for Memories, Documents, and Achievements.
* **FR-005:** The system shall display an informative placeholder message when zero active records exist in the vault.

*Inputs:* User navigation clicks; internal notifications from the Service Layer when records change; repository queries for archived totals.  
*Outputs:* Formatted metric summary cards, list of recent records, empty state view.  
*Error Handling:* If database queries fail on startup, metrics are presented as zero with an informative status banner.

### 3.2 Module 2: Memory Vault (Owner: Anushka Samad)
**Description:** Dedicated interface for managing personal memories, narrative life reflections, and continuous cyclic browsing.  
**Associated Data Structure:** Circular Linked List (`CircularLinkedList`) — Arranges active memories into an endless cycle where the tail node references the head node, enabling continuous Next/Previous carousel navigation.

* **FR-006:** The system shall allow users to create a Memory record by providing Title, Category, Date (`YYYY-MM-DD`), Description, Priority (1–5), and an optional local media/image file path.
* **FR-007:** The system shall validate that Title and Category contain non-whitespace text and that Date conforms to the ISO `YYYY-MM-DD` format prior to submitting to the Service Layer.
* **FR-008:** The system shall populate a custom `CircularLinkedList` with all active Memory records during view initialization.
* **FR-009:** The system shall provide "Next Memory" and "Previous Memory" controls that traverse the `CircularLinkedList` cyclically without encountering null pointer termination.
* **FR-010:** The system shall allow users to edit existing memory fields, persisting changes to SQLite first and then updating the in-memory `CircularLinkedList`.
* **FR-011:** The system shall allow users to archive a selected memory, removing it from active circular navigation.
* **FR-012:** The system shall allow users to permanently delete a memory record following explicit confirmation in a modal dialog.

*Inputs:* Form field text, date strings, integer priority, local file path strings, carousel navigation clicks.  
*Outputs:* Memory detail card, carousel view, modal edit dialogs, confirmation popups.  
*Error Handling:* Invalid date strings display an inline error message; empty memory collections disable carousel navigation buttons.

### 3.3 Module 3: Life Timeline (Owner: Anushka Samad)
**Description:** Displays dated memories and achievements in chronological sequence across the user's lifetime.  
**Associated Data Structure:** Singly Linked List (`SinglyLinkedList`) — Arranges active dated records into a forward-traversable linked chain ordered chronologically by `record_date`.

* **FR-013:** The system shall collect all active Memory and Achievement records and order them chronologically by `record_date`.
* **FR-014:** The system shall populate a custom `SinglyLinkedList` with the chronologically ordered records.
* **FR-015:** The system shall render the timeline view by traversing the `SinglyLinkedList` from head to tail, displaying dated event cards.
* **FR-016:** The system shall allow users to filter timeline entries by record type (All, Memories Only, Achievements Only).
* **FR-017:** The system shall allow users to filter timeline entries within a user-specified start date and end date range.

*Inputs:* Type filter selections, date range filter bounds.  
*Outputs:* Chronological sequence of event cards.  
*Error Handling:* Specifying a start date that occurs after an end date displays an inline validation message.

### 3.4 Module 4: Memory Connections (Owner: Anushka Samad)
**Description:** Models, creates, and visualizes semantic relationships between arbitrary vault records.  
**Associated Data Structure:** Graph (`Graph`) — Custom adjacency-list graph representation where vertices represent record IDs and edges represent bidirectional relationships.

* **FR-018:** The system shall allow users to establish an undirected relationship between any two active records with an optional relation label.
* **FR-019:** The system shall reject self-referencing connections (linking a record to itself) and duplicate connections between an already linked pair of records.
* **FR-020:** The system shall persist connections in the `record_connections` SQLite table and reconstruct the custom `Graph` adjacency list during initialization.
* **FR-021:** The system shall display the immediate neighbors of a selected record by querying the custom `Graph`'s adjacency list.
* **FR-022:** The system shall execute and display a Breadth-First Search (BFS) traversal starting from a selected record to explore relationship layers.
* **FR-023:** The system shall execute and display a Depth-First Search (DFS) traversal starting from a selected record for deep relationship discovery.
* **FR-024:** The system shall allow users to remove an existing relationship, deleting the corresponding row from `record_connections` and updating the in-memory `Graph`.

*Inputs:* Source record ID, target record ID, optional relation label string, traversal trigger clicks.  
*Outputs:* Relationship list, neighbor record summaries, BFS/DFS traversal sequence displays.  
*Error Handling:* Attempted duplicate connections trigger an informative warning; requesting neighbors for a disconnected or non-existent record displays an empty neighbor state.

### 3.5 Module 5: Category Manager (Owner: Anushka Samad)
**Description:** Manages hierarchical record categorization and nested taxonomy browsing.  
**Associated Data Structure:** General Tree (`CategoryTree`) — An N-ary hierarchical tree where each node represents a category or subcategory segment.

* **FR-025:** The system shall organize categories into a hierarchical tree structure originating from a predefined root node (`LifeVault`).
* **FR-026:** The system shall reconstruct the `CategoryTree` at startup by parsing the hierarchical path strings stored in the `category` column of active records (e.g., `Documents/Academic/Transcripts`).
* **FR-027:** The system shall allow users to add new category paths into the custom `CategoryTree` in memory; such paths created without assigning any record are temporary and will not persist across application restarts unless at least one record is saved with that category path in the existing `records.category` field, without introducing a separate categories table.
* **FR-028:** The system shall display the category taxonomy in an expandable/indented visual hierarchy.
* **FR-029:** The system shall allow users to select a category node in the tree to retrieve and display all active records assigned to that category or its descendant subcategories.
* **FR-030:** The system shall reject the deletion of a category node if active records currently reference that category string.

*Inputs:* Category path strings, tree node selection clicks.  
*Outputs:* Visual hierarchical tree view, list of records filtered by selected category branch.  
*Error Handling:* Malformed or empty category path strings are rejected with feedback.

### 3.6 Module 6: Document Vault (Owner: Ubaid Raza)
**Description:** Catalogs vital personal, educational, legal, and medical documents, referencing external local files.  
**Associated Architecture:** Service/Repository layer with local filesystem path verification and native process launching.

* **FR-031:** The system shall allow users to create a Document record by supplying Title, Category, Document Date (`YYYY-MM-DD`), Description, Priority (1–5), and an optional local file path.
* **FR-032:** The system shall provide an OS file-picker dialog allowing users to browse and attach a local file path (e.g., PDF, DOCX, image) to the document record.
* **FR-033:** The system shall store file paths strictly as text references in the `file_path` column without copying, moving, or uploading the underlying file bytes.
* **FR-034:** The system shall verify the existence of the referenced file on the local filesystem before attempting to open it via the host operating system's default viewer.
* **FR-035:** If a referenced file is missing, moved, or inaccessible, the system shall intercept the error and present an informative warning dialog without terminating or freezing the application.
* **FR-036:** The system shall support editing document metadata, archiving documents, and permanently deleting documents upon explicit confirmation.

*Inputs:* Document form inputs, file-picker dialog selections, "Open File" button clicks.  
*Outputs:* Document table/card view, launch of external native viewer, missing-file alerts.  
*Error Handling:* Missing or inaccessible file paths display an alert: *"The referenced file could not be found at its original path."*

### 3.7 Module 7: Achievement Vault (Owner: Ubaid Raza)
**Description:** Preserves honors, certifications, competitive awards, and life milestones.  
**Associated Architecture:** Service/Repository layer supporting milestone metadata aligned with the approved database schema.

* **FR-037:** The system shall allow users to create an Achievement record by supplying Title, Category, Achievement Date (`YYYY-MM-DD`), Description, Priority (1–5), and an optional certificate file path.
* **FR-038:** The system shall record organizational or issuing body details within the existing documented fields (such as within the `category` hierarchy or `description` text), strictly conforming to the database schema without introducing unapproved columns.
* **FR-039:** The system shall validate that Title, Category, and Date are populated and formatted correctly prior to submission.
* **FR-040:** The system shall display achievements as cards detailing title, category, date, description, priority badge, and attached certificate status.
* **FR-041:** The system shall support filtering achievements by category and date range.
* **FR-042:** The system shall support editing, archiving, and permanently deleting achievement records.

*Inputs:* Achievement form inputs, category and date filter controls.  
*Outputs:* Formatted achievement cards, filtered result lists.  
*Error Handling:* Mandatory field omissions highlight invalid fields with corrective prompts.

### 3.8 Module 8: Smart Search (Owner: Ubaid Raza)
**Description:** Dual-engine search system providing exact numeric ID retrieval and multi-attribute keyword scanning.  
**Associated Data Structures:** 
* Binary Search Tree (`BinarySearchTree`) — Indexes active records by integer record ID for ordered retrieval.
* Hash Table (`HashTable`) — Custom separate-chaining hash table for direct $O(1)$ average exact ID lookup.

* **FR-043:** The system shall populate both the `BinarySearchTree` and `HashTable` with active records during startup and update them upon record creation, update, or archival.
* **FR-044:** The system shall provide an "Exact ID Search" mode that retrieves records matching a specified integer ID by querying the custom `HashTable` or `BinarySearchTree`.
* **FR-045:** The system shall provide a "Keyword Search" mode that performs a case-insensitive linear scan across Title, Category, and Description fields of active records.
* **FR-046:** The system shall allow users to constrain keyword searches by record type (All, Memories, Documents, Achievements).
* **FR-047:** The system shall display an explicit "No Records Found" view when a search produces zero matching records.

*Inputs:* Search query string, search mode toggle ("Exact ID" vs. "Keyword"), record type filter.  
*Outputs:* List of matching record cards, empty search placeholder.  
*Error Handling:* Entering non-numeric text in Exact ID mode displays an advisory message: *"Please enter a valid numeric ID."*

### 3.9 Module 9: Priority Vault (Owner: Ubaid Raza)
**Description:** Triage interface organizing records strictly by importance rating (priority 5 down to 1).  
**Associated Data Structure:** Max-Heap / Priority Queue (`PriorityQueue`) — A custom array-backed complete binary tree satisfying the max-heap invariant, using record ID as a deterministic secondary tie-breaker.

* **FR-048:** The system shall construct an in-memory custom `PriorityQueue` populated with active records ordered by priority (5 = Highest, 1 = Normal).
* **FR-049:** The system shall display records extracted from the priority queue in strictly non-increasing order of priority score.
* **FR-050:** The system shall display visual priority badges on all record cards reflecting their numerical score.
* **FR-051:** When a record's priority is modified, the system shall persist the change to SQLite first and subsequently update or rebuild the in-memory `PriorityQueue`.

*Inputs:* Priority screen navigation, priority filter selections.  
*Outputs:* Priority-ordered record list with color-coded priority badges.  
*Error Handling:* An empty priority queue presents a friendly placeholder.

### 3.10 Module 10: Archive & Undo (Owner: Ubaid Raza)
**Description:** Manages soft-deleted records, restoration workflows, and transient session undo history.  
**Associated Data Structure:** Stack (`Stack`) — A custom LIFO linked structure capturing reversible command mementos executed during the active application session.

* **FR-052:** The system shall implement soft-deletion by setting a record's `archived` column in SQLite to `1`, removing it from active views without destroying data.
* **FR-053:** The system shall provide a dedicated "Archive Vault" screen displaying all records currently having `archived = 1`.
* **FR-054:** The system shall allow users to restore an archived record, setting `archived = 0` in SQLite and re-indexing it into all active in-memory data structures.
* **FR-055:** The system shall allow users to permanently delete an archived record, removing it irreversibly from SQLite after explicit modal confirmation; permanent deletion cannot be undone.
* **FR-056:** The system shall record reversible command mementos on a custom `Stack` during the active session whenever a supported action occurs (Record Creation, Archival, Restoration).
* **FR-057:** The system shall provide an "Undo" action that inspects the most recent command using the custom `Stack.peek()` method, executes the inverse operation through the Service Layer and commits the database transaction, synchronizes in-memory data structures upon commit, and only then removes the command from the stack using `Stack.pop()`; if the persistence operation fails, the command shall remain preserved in the `Stack` and in-memory structures shall remain unmodified.
* **FR-058:** The system shall disable the "Undo" control when the custom `Stack` contains no reversible commands.

*Inputs:* Archive/restore button clicks, Undo button click, permanent deletion confirmation.  
*Outputs:* Archived record table, updated active views, confirmation status alerts.  
*Error Handling:* If the undo stack is empty, the undo control remains disabled; attempting undo on an empty stack produces no operation. If an undo transaction fails, the command is kept on the stack and the failure is reported.

### 3.11 Internal Pipeline: Task Queue Processor (Owner: Ubaid Raza)
**Description:** An internal synchronous FIFO queue processor for staging and executing record operations in strict arrival sequence.  
**Associated Data Structure:** Queue (`Queue`) — A custom linked FIFO queue with distinct head and tail pointers.

* **FR-059:** The system shall maintain an internal synchronous `Queue` instance to stage pending record mutation requests.
* **FR-060:** The system shall enqueue operation tasks with associated payload metadata in the order they are submitted.
* **FR-061:** The system shall dequeue and execute tasks synchronously in FIFO order, committing each operation through the Service Layer.
* **FR-062:** The system shall expose `enqueue`, `dequeue`, `front`/`peek`, `is_empty`, and `size` methods that are verifiable via automated pytest test suites.

*Inputs:* Operation task payloads.  
*Outputs:* Sequential synchronous execution of tasks, queue length telemetry.  
*Error Handling:* Calling dequeue on an empty queue safely returns `None` or raises an explicit empty exception without terminating the program.

---

## 4. External Interface Requirements

### 4.1 User Interface Requirements
* **Framework:** Python `customtkinter` with high-DPI scaling enabled.
* **Layout Structure:**
  * Fixed Left Navigation Sidebar: Houses the LifeVault brand header and navigation buttons for Dashboard, Memory Vault, Document Vault, Achievement Vault, Life Timeline, Connections, Priority Vault, Archive, Search, and Diagnostics Demo.
  * Main Content Canvas: Dynamically displays the active view with header title, descriptive subtitle, primary action buttons, and scrollable content panels.
* **Color System:**
  * Primary Navy: `#172B4D` (Sidebar background, primary headers)
  * Secondary Navy: `#243B63` (Active navigation buttons, sub-headers)
  * Lavender Accent: `#B9A7E8` (Action buttons, highlighted badges, focus outlines)
  * Light Background: `#F4F5FA` (Main content canvas)
  * Surface Cards: `#FFFFFF` (Record cards, form panels)
  * Typography: Clean system sans-serif font, text color `#1E293B`, secondary text `#64748B`.
* **Forms & Dialogs:**
  * All input dialogs must include descriptive labels, placeholder hints, and inline validation text.
  * Destructive actions (permanent deletion) must require explicit user confirmation in a modal popup.

### 4.2 Hardware Interface Requirements
* Standard keyboard and mouse or trackpad.
* Standard display monitor with a recommended resolution of $1280 \times 720$ or higher.
* Local persistent storage drive (HDD or SSD) for storing the application files and SQLite database.

### 4.3 Software Interface Requirements
* **Operating System:** Windows 10/11, macOS Monterey (12.0) or later, Ubuntu 20.04 LTS or equivalent Linux distribution.
* **Python Interpreter:** Python 3.10, 3.11, or 3.12.
* **Dependencies:**
  * `customtkinter >= 5.2.0` (GUI components)
  * `pytest >= 7.0.0` (Test execution via `python -m pytest`)
* **Standard Library:** `sqlite3`, `pathlib`, `os`, `sys`, `subprocess`, `datetime`, `typing`.

### 4.4 Communication Interface Requirements
* **Network Interfaces:** None. LifeVault operates strictly offline. It initiates no network connections, creates no sockets, contacts no remote APIs, and requires no internet access.

---

## 5. Non-Functional Requirements

Requirements are uniquely numbered using the convention `NFR-XXX`. There are exactly 22 non-functional requirements (`NFR-001` through `NFR-022`).

### 5.1 Performance
* **NFR-001 (Startup Rehydration Efficiency):** The application shall reconstruct in-memory runtime indexes from the SQLite database sequentially during startup without unhandled latency under typical personal collection volumes (< 1,000 records).
* **NFR-002 (Algorithmic Retrieval Complexity):** Exact ID search via the custom `HashTable` shall execute in $O(1)$ average time ($O(n)$ worst-case under bucket collisions). Search via the custom manually implemented `BinarySearchTree` shall execute in $O(\log n)$ average time and $O(n)$ worst-case time for degenerate skewed tree topologies, reflecting the expected behavior of an unaugmented binary search tree without self-balancing mechanisms.
* **NFR-003 (Graph Traversal Complexity):** Graph BFS and DFS traversals shall execute with time complexity bounded by $O(V + E)$ where $V$ is the number of records and $E$ is the number of connections.
* **NFR-004 (UI Responsiveness):** View transitions and carousel navigation steps shall execute synchronously and refresh the interface promptly under standard local dataset sizes.

### 5.2 Reliability & Fault Tolerance
* **NFR-005 (Graceful Input Validation):** The system shall intercept malformed user inputs (e.g., invalid date formats, empty required fields) and display descriptive inline feedback without raising unhandled exceptions.
* **NFR-006 (Missing External File Handling):** The system shall verify filesystem path existence prior to opening external files; if a referenced file is missing, it shall display an informative alert dialog without terminating the application.
* **NFR-007 (Safe Connection Termination):** The application shall cleanly close SQLite database connections upon window closure, preventing locked database files or journal corruption.

### 5.3 Usability
* **NFR-008 (Design Uniformity):** All screens shall strictly adhere to the designated Navy and Lavender visual palette and typography guidelines.
* **NFR-009 (Action Confirmation):** The system shall require explicit modal confirmation prior to executing irreversible permanent deletion.
* **NFR-010 (Empty State Guidance):** Every screen shall present a clean empty-state placeholder providing clear guidance when no records are available.

### 5.4 Security and Local Data Protection
* **NFR-011 (SQL Injection Immunity):** All SQL statements executed through repository classes shall use parameterized queries (`?` placeholders). Dynamic string concatenation in SQL commands is strictly prohibited.
* **NFR-012 (Local Data Boundary):** All user records and metadata shall reside exclusively within a local SQLite database file on the host machine. Zero telemetry or personal data shall be transmitted externally.
* **NFR-013 (Input Whitespace Sanitization):** Text inputs shall be stripped of leading and trailing whitespace before persistence.

### 5.5 Maintainability and Code Quality
* **NFR-014 (Architectural Decoupling):** Code shall strictly maintain layer boundaries: Presentation classes shall contain no SQL statements, and Repository classes shall contain no GUI references.
* **NFR-015 (Isolated Data Structure Units):** Each of the ten data structures shall reside in an isolated Python file in `data_structures/`, accompanied by independent test modules in `tests/`.
* **NFR-016 (Prohibition of Algorithmic Shortcuts):** Custom data structure classes shall not import or wrap high-level library algorithms (`heapq`, `queue.Queue`, `collections`) to implement their core operations.

### 5.6 Portability
* **NFR-017 (Cross-Platform Path Resolution):** All filesystem paths shall be manipulated using Python's `pathlib.Path` to maintain compatibility across Windows, macOS, and Linux directory conventions.
* **NFR-018 (Native Document Launcher):** Opening a referenced document shall invoke the host operating system's native launcher (`os.startfile` on Windows, `open` on macOS, `xdg-open` on Linux).

### 5.7 Data Integrity
* **NFR-019 (Foreign Key Integrity):** SQLite connections shall execute `PRAGMA foreign_keys = ON;` upon initialization to enforce referential constraints between records and connections.
* **NFR-020 (Transactional Atomicity):** Multi-step database operations (e.g., deleting a record and removing its associated graph edges) shall execute within atomic database transactions, rolling back completely if any step fails.
* **NFR-021 (Dual-State Consistency):** In-memory data structures shall only be updated after the underlying SQLite transaction has committed successfully.

### 5.8 Offline Operation
* **NFR-022 (Network Independence):** The software shall deliver 100% of its functionality in an air-gapped or disconnected environment with zero external network connectivity.

---

## 6. Data Requirements and Database Schema

### 6.1 Main Data Entities
1. **Record Entity:** Core entity representing a personal legacy entry. Differentiated by `record_type` (`Memory`, `Document`, `Achievement`).
2. **Record Connection Entity:** An undirected semantic link connecting two record entities.

### 6.2 SQLite Database Schema

The approved persistent database schema consists strictly of two relational tables: `records` and `record_connections`. No unsupported tables are defined or utilized.

#### Table: `records`
Stores all primary personal legacy entries across the three record types.

| Column Name | Data Type | Constraints | Description |
|---|---|---|---|
| `id` | `INTEGER` | `PRIMARY KEY AUTOINCREMENT` | Unique integer record identifier |
| `record_type` | `TEXT` | `NOT NULL CHECK (record_type IN ('Memory', 'Document', 'Achievement'))` | Entity discriminator |
| `title` | `TEXT` | `NOT NULL` | Title of the record entry |
| `category` | `TEXT` | `NOT NULL` | Category or hierarchical category path string |
| `record_date` | `TEXT` | `NOT NULL` | ISO formatted date (`YYYY-MM-DD`) |
| `description` | `TEXT` | `DEFAULT ''` | Narrative description or notes |
| `file_path` | `TEXT` | `DEFAULT ''` | Local filesystem path string to referenced file |
| `priority` | `INTEGER` | `NOT NULL DEFAULT 3 CHECK (priority BETWEEN 1 AND 5)` | Importance rating (1 = Normal, 5 = Highest) |
| `archived` | `INTEGER` | `NOT NULL DEFAULT 0 CHECK (archived IN (0, 1))` | Soft-deletion indicator (0 = Active, 1 = Archived) |
| `created_at` | `TEXT` | `NOT NULL` | Record creation timestamp |

#### Table: `record_connections`
Stores undirected relationships between pairs of records.

| Column Name | Data Type | Constraints | Description |
|---|---|---|---|
| `id` | `INTEGER` | `PRIMARY KEY AUTOINCREMENT` | Unique connection identifier |
| `source_id` | `INTEGER` | `NOT NULL, FOREIGN KEY REFERENCES records(id) ON DELETE CASCADE` | Source record ID |
| `target_id` | `INTEGER` | `NOT NULL, FOREIGN KEY REFERENCES records(id) ON DELETE CASCADE` | Target record ID |
| `relation_label` | `TEXT` | `DEFAULT ''` | Optional relationship annotation |

*Normalization and Uniqueness Invariant:*
$$\text{CHECK}(source\_id < target\_id), \quad \text{UNIQUE}(source\_id, target\_id)$$
Each undirected edge is stored exactly once in SQLite. During startup rehydration, the custom `Graph` populates adjacency lists in both directions ($source \rightarrow target$ and $target \rightarrow source$).

### 6.3 Category Tree Reconstruction Model
Because the approved database schema does not include a separate `categories` table, category taxonomy is derived entirely from the existing `records.category` text column. The hierarchical `CategoryTree` is dynamically reconstructed at application startup through the following deterministic algorithm:
1. Initialize `CategoryTree` with a root node labeled `LifeVault`.
2. Query active records from SQLite and extract all distinct `category` path strings stored in `records.category`.
3. Split each path string by delimiter (e.g., `"Documents/Academic/Transcripts"` $\rightarrow$ `["Documents", "Academic", "Transcripts"]`).
4. Traverse or insert corresponding tree nodes branch by branch using `CategoryTree.add_path()`.
5. Map active record references to their corresponding leaf or branch category nodes.

*Temporary Category Rule:* Any category path added by a user in the Category Manager that has no records assigned to it exists purely as a temporary in-memory node in the `CategoryTree`. It will not persist across application restarts. Only when a record is assigned and saved with that category path does the path become persistently reconstructable from `records.category` upon subsequent application startups. No auxiliary categories table is added.

### 6.4 Operational In-Memory Structures (Stack and Queue)
Unlike the persistent runtime indexes, the operational structures are session-bound:
* **Undo Stack (`Stack`):** Initialized empty at startup. It records command mementos for reversible operations executed during the active application session. Undo history is not persisted across application restarts.
* **Task Queue (`Queue`):** Initialized empty at startup. It stages and executes record mutation tasks synchronously in FIFO order during runtime.

### 6.5 Dual-State Synchronization Workflow
All state mutations must follow this strict sequence:
1. **Input Submission:** User submits a form or action via the GUI.
2. **Validation:** Service Layer validates data types, required fields, and constraints.
3. **Persistence:** Repository Layer executes parameterized SQL statements within an SQLite transaction.
4. **Commit:** Transaction commits to SQLite successfully.
5. **Memory Synchronization:** Service Layer updates or rebuilds the affected in-memory data structures.
6. **UI Refresh:** GUI refreshes the displayed view to reflect the updated synchronized state.

*Failure Rule:* If Step 3 or 4 fails, an exception is caught, the transaction rolls back, in-memory structures remain untouched, and the GUI displays an error message.

---

## 7. Use Case Specifications

### UC-01: Create and Manage a Memory
* **Primary Actor:** User
* **Preconditions:** LifeVault is running; Memory Vault or Dashboard is open.
* **Main Flow:**
  1. User clicks "Add Memory".
  2. System displays input form (Title, Category, Date, Description, Priority, optional Media Path).
  3. User enters details and clicks "Save".
  4. Service Layer validates that Title and Category are non-empty and Date conforms to `YYYY-MM-DD`.
  5. Repository executes an `INSERT` statement into `records` with `record_type = 'Memory'`.
  6. Transaction commits successfully.
  7. Service Layer updates `DynamicArray`, `CircularLinkedList`, `HashTable`, and `BinarySearchTree`.
  8. Service Layer pushes a `CREATE` command memento onto the `Stack`.
  9. System closes dialog, displays success notification, and refreshes the memory view.
* **Alternative Flows:**
  * *4a. Validation Failure:* System displays inline error messages; form remains open for correction.
  * *6a. Database Error:* System rolls back transaction, leaves in-memory structures unchanged, and alerts user.
* **Postconditions:** A new memory is saved in SQLite and indexed across in-memory structures.

### UC-02: Add and Manage a Document
* **Primary Actor:** User
* **Preconditions:** Document Vault screen is open.
* **Main Flow:**
  1. User clicks "Add Document".
  2. System presents document creation form.
  3. User inputs Title, Category, Date, Description, Priority, and clicks "Browse File".
  4. System launches native OS file picker; user selects a local file.
  5. System records the absolute file path into the form field.
  6. User clicks "Save". Service Layer validates input and Repository persists record to SQLite.
  7. Upon successful commit, relevant in-memory indexes are updated.
  8. Document row appears in Document Vault table.
* **Alternative Flows:**
  * *User Opens Attached File:* User clicks "Open File" on a document row. System verifies file path existence via `pathlib.Path(file_path).exists()`. If valid, system launches the host OS viewer. If missing, system presents a warning dialog: *"The referenced file could not be found at its original path."*
* **Postconditions:** Document metadata and local path reference are persisted.

### UC-03: Record an Achievement
* **Primary Actor:** User
* **Preconditions:** Achievement Vault screen is open.
* **Main Flow:**
  1. User clicks "Add Achievement".
  2. User enters Title, Category (optionally encoding organization/institution), Date, Description, Priority, and optional certificate file path.
  3. User clicks "Save". Service Layer validates required fields.
  4. Repository executes `INSERT` into `records` with `record_type = 'Achievement'`.
  5. Upon commit, Service Layer updates `DynamicArray`, `SinglyLinkedList` (Timeline), `PriorityQueue`, and search indexes.
  6. Achievement card is displayed on screen.
* **Postconditions:** Achievement milestone is saved and reflected across timeline and priority views.

### UC-04: Search Records
* **Primary Actor:** User
* **Preconditions:** Search screen is open.
* **Main Flow:**
  1. User selects search mode ("Exact ID" or "Keyword").
  2. *Branch 1 (Exact ID):* User enters an integer ID. System queries in-memory `HashTable` or `BinarySearchTree`. Record is returned in $O(1)$ average time.
  3. *Branch 2 (Keyword):* User enters text query and optional type filter. System executes case-insensitive substring scan across Title, Category, and Description of active records.
  4. System renders matching record cards.
* **Alternative Flows:**
  * *2a. Non-Numeric ID in Exact Mode:* System displays alert: *"Please enter a valid numeric ID."*
  * *3a. Zero Matches:* System displays "No Records Found" placeholder.
* **Postconditions:** Search results are presented without modifying system state.

### UC-05: Connect Related Records
* **Primary Actor:** User
* **Preconditions:** At least two active records exist; Connections screen is open.
* **Main Flow:**
  1. User selects Source Record and Target Record from dropdown menus.
  2. User optionally inputs a relationship label.
  3. User clicks "Create Connection".
  4. System verifies that Source ID $\ne$ Target ID and that no edge currently exists between them.
  5. Repository inserts edge into `record_connections` table.
  6. Upon successful commit, Service Layer updates in-memory `Graph` via `Graph.add_edge(source_id, target_id)`.
  7. System displays updated relationship list and neighbor view.
* **Alternative Flows:**
  * *4a. Self-Link Attempted:* System rejects action: *"Cannot link a record to itself."*
  * *4b. Duplicate Link Attempted:* System rejects action: *"These records are already connected."*
* **Postconditions:** An undirected edge is established in SQLite and in-memory Graph.

### UC-06: Browse Timeline
* **Primary Actor:** User
* **Preconditions:** Life Timeline screen is open; dated records exist.
* **Main Flow:**
  1. System traverses in-memory `SinglyLinkedList` containing chronologically ordered records.
  2. System renders sequential event cards from earliest to latest date.
  3. User optionally applies type filter or date range bounds.
  4. System re-filters displayed nodes and refreshes the timeline.
* **Postconditions:** Chronological life narrative is displayed.

### UC-07: Manage Categories
* **Primary Actor:** User
* **Preconditions:** Category Manager screen is open.
* **Main Flow:**
  1. System traverses in-memory `CategoryTree` and renders hierarchical tree view.
  2. User enters a new subcategory path and clicks "Add Category".
  3. System calls `CategoryTree.add_path()` and adds temporary in-memory nodes to the `CategoryTree`.
  4. System informs the user that the category path remains temporary until at least one record is assigned to it.
  5. User assigns a record to the category path, saving it to SQLite in `records.category`.
  6. User clicks any category node in the tree.
  7. System retrieves and displays all active records assigned to that category branch.
* **Alternative Flows:**
  * *Restart Without Assigned Records:* If the application is restarted before any record is assigned to the new category path, the temporary category path is discarded, and the tree is reconstructed strictly from populated `records.category` values.
* **Postconditions:** Category hierarchy is updated and available for record categorization; persistent retention is established once a record references the path in `records.category`.

### UC-08: Set Record Priority
* **Primary Actor:** User
* **Preconditions:** Priority Vault or Record Edit screen is open.
* **Main Flow:**
  1. User assigns priority rating (1 to 5) during creation or editing.
  2. System persists updated priority to SQLite.
  3. Upon commit, Service Layer updates or rebuilds in-memory `PriorityQueue`.
  4. User opens Priority Vault screen.
  5. System extracts records from `PriorityQueue` and renders records from Priority 5 down to Priority 1.
* **Postconditions:** High-priority items are prioritized visually and algorithmically.

### UC-09: Archive and Restore Records
* **Primary Actor:** User
* **Preconditions:** Target record exists in active vault.
* **Main Flow (Archiving):**
  1. User selects record and clicks "Archive".
  2. Repository updates SQLite setting `archived = 1`.
  3. Upon commit, Service Layer removes record from active in-memory data structures.
  4. Service Layer pushes `ARCHIVE` command memento onto the `Stack`.
  5. Record disappears from active views and appears in Archive Vault.
* **Alternative Flow (Restoring):**
  1. User navigates to Archive Vault.
  2. User selects an archived record and clicks "Restore".
  3. Repository updates SQLite setting `archived = 0`.
  4. Upon commit, Service Layer re-indexes record into active in-memory data structures.
  5. Service Layer pushes `RESTORE` command memento onto the `Stack`.
  6. Record returns to active vault screens.
* **Postconditions:** Record archival status is toggled safely without permanent data loss.

### UC-10: Undo Supported Actions
* **Primary Actor:** User
* **Preconditions:** At least one supported action (Create, Archive, Restore) was executed during the active session; `Stack` is not empty.
* **Main Flow:**
  1. User clicks "Undo" in the application interface.
  2. System inspects the top command memento from the custom `Stack` using `peek()`.
  3. Service Layer determines and executes the inverse operation (e.g., reversing creation, archival, or restoration).
  4. Repository commits the state modification to SQLite within a transaction.
  5. Upon successful database commit, Service Layer updates or synchronizes affected in-memory data structures.
  6. System removes the command memento from the stack using `pop()`.
  7. System displays status confirmation and refreshes the active view.
* **Alternative Flows:**
  * *1a. Empty Stack:* Undo button is disabled; clicking produces no action.
  * *4a. Database Persistence Failure:* If the database transaction fails to commit, the transaction is rolled back, the command memento is preserved in the `Stack` (no `pop()` is executed), in-memory data structures remain unchanged, and an error dialog is presented to the user.
* **Postconditions:** System state is reverted to the state preceding the undone command, or preserved untouched upon database failure.

---

## 8. System Constraints and Boundaries

The following explicit constraints define the technical scope and boundaries of LifeVault:
1. **Single-User Architecture:** Designed strictly for a single user per application installation. Multi-user accounts, logins, and permissions are excluded.
2. **Offline Local Execution:** The software operates entirely locally. Cloud synchronization, remote database connections, and web-based API calls are strictly forbidden.
3. **No Machine Learning or AI Functionality:** Tagging, categorization, and graph connection discovery are deterministic. Automated AI suggestions, OCR, or NLP summarization are outside project scope.
4. **No Direct Binary Storage:** Large media files are not stored as BLOBs in SQLite. The database stores validated local filesystem URI strings.
5. **No Legal or Inheritance Claims:** LifeVault is an academic organizational tool. It provides no legal guarantees, will execution mechanisms, or probate workflows.
6. **Form Factor:** The application is developed exclusively for desktop environments. Mobile, browser-based, or web application variants are out of scope.
7. **Synchronous Execution:** All data structure operations and database queries run synchronously in the main thread. Asynchronous worker threads and background schedulers are excluded.
8. **No Separate Categories Table:** Category taxonomy is derived dynamically from category strings in `records.category`. Category paths created in memory without assigning any record are temporary and do not persist across restarts.
9. **Session-Bound Undo History:** The custom undo `Stack` is an in-memory operational structure; undo history is not persisted across application restarts. Permanent deletions are irreversible and cannot be undone.

---

## 9. Acceptance Criteria

The system shall be deemed complete and acceptable for academic evaluation when all of the following measurable criteria are met:

* **AC-01 (CRUD and Persistent Verification):** All three record types (Memory, Document, Achievement) can be created, viewed, edited, soft-deleted (archived), restored, and permanently deleted via the GUI with verified SQLite persistence.
* **AC-02 (Data Structure Manual Implementation):** All ten custom data structures (`DynamicArray`, `SinglyLinkedList`, `CircularLinkedList`, `CategoryTree`, `Graph`, `BinarySearchTree`, `HashTable`, `PriorityQueue`, `Stack`, `Queue`) are implemented in separate Python classes without relying on high-level standard library shortcuts for core algorithms.
* **AC-03 (Automated Unit Test Pass Rate):** All standalone unit test suites authored in `tests/` pass with 100% success when executed via `python -m pytest`.
* **AC-04 (Startup Hydration Integrity):** Closing and reopening the application with an existing database correctly reconstructs all persistent in-memory data structures with zero state loss or corruption.
* **AC-05 (Timeline Chronology):** The Life Timeline displays active Memory and Achievement records strictly in non-decreasing chronological order based on `record_date`.
* **AC-06 (Graph Relationship Integrity):** Creating a connection between two records correctly updates `record_connections`, establishes bidirectional adjacency in the custom `Graph`, and supports cycle-safe BFS and DFS traversals without self-loops or duplicate edges.
* **AC-07 (Priority Queue Invariant):** The Priority Vault surfaces Priority 5 records ahead of lower-priority records, verified through UI inspection and heap property tests.
* **AC-08 (Undo Transaction Reversal):** Executing "Undo" successfully reverts the most recent supported operation (Creation, Archival, Restoration) via the LIFO `Stack` during an active session, preserving the stack command if the underlying database operation fails.
* **AC-09 (Search Correctness):** Exact ID search returns the specific record in $O(1)$ average time, and keyword search correctly identifies substring matches across active titles, categories, and descriptions.
* **AC-10 (Fault Handling & Safe File Launch):** Attempting to open a missing or moved local file displays an informative user alert without throwing unhandled exceptions or crashing the GUI.
* **AC-11 (Dual-State Consistency Enforcement):** In-memory data structures are updated only after database transactions commit successfully; failed database operations leave in-memory state unmodified.

---

## 10. Requirements Traceability Matrix

The following matrix maps all 62 functional requirements (`FR-001` through `FR-062`) to their corresponding module, owner, associated data structure or architecture component, and verifying acceptance criteria:

| Requirement ID | Subsystem / Module | Module Owner | Associated Component / Structure | Primary Acceptance Criteria |
|---|---|---|---|---|
| **FR-001** | Dashboard | Anushka Samad | Dynamic Array | AC-01, AC-04 |
| **FR-002** | Dashboard | Anushka Samad | Dynamic Array & Repository Query | AC-01, AC-02, AC-04 |
| **FR-003** | Dashboard | Anushka Samad | Dynamic Array | AC-01, AC-02 |
| **FR-004** | Dashboard | Anushka Samad | Dynamic Array | AC-01 |
| **FR-005** | Dashboard | Anushka Samad | Dynamic Array | AC-01, AC-10 |
| **FR-006** | Memory Vault | Anushka Samad | Circular Linked List | AC-01, AC-04 |
| **FR-007** | Memory Vault | Anushka Samad | Circular Linked List | AC-01, AC-10 |
| **FR-008** | Memory Vault | Anushka Samad | Circular Linked List | AC-02, AC-04 |
| **FR-009** | Memory Vault | Anushka Samad | Circular Linked List | AC-02, AC-03 |
| **FR-010** | Memory Vault | Anushka Samad | Circular Linked List | AC-01, AC-04, AC-11 |
| **FR-011** | Memory Vault | Anushka Samad | Circular Linked List | AC-01, AC-08, AC-11 |
| **FR-012** | Memory Vault | Anushka Samad | Circular Linked List | AC-01, AC-04, AC-11 |
| **FR-013** | Life Timeline | Anushka Samad | Singly Linked List | AC-01, AC-05 |
| **FR-014** | Life Timeline | Anushka Samad | Singly Linked List | AC-02, AC-05 |
| **FR-015** | Life Timeline | Anushka Samad | Singly Linked List | AC-03, AC-05 |
| **FR-016** | Life Timeline | Anushka Samad | Singly Linked List | AC-05 |
| **FR-017** | Life Timeline | Anushka Samad | Singly Linked List | AC-05 |
| **FR-018** | Memory Connections | Anushka Samad | Graph (Adjacency List) | AC-01, AC-06, AC-11 |
| **FR-019** | Memory Connections | Anushka Samad | Graph (Adjacency List) | AC-06 |
| **FR-020** | Memory Connections | Anushka Samad | Graph (Adjacency List) | AC-04, AC-06 |
| **FR-021** | Memory Connections | Anushka Samad | Graph (Adjacency List) | AC-02, AC-06 |
| **FR-022** | Memory Connections | Anushka Samad | Graph (Adjacency List) | AC-03, AC-06 |
| **FR-023** | Memory Connections | Anushka Samad | Graph (Adjacency List) | AC-03, AC-06 |
| **FR-024** | Memory Connections | Anushka Samad | Graph (Adjacency List) | AC-01, AC-06, AC-11 |
| **FR-025** | Category Manager | Anushka Samad | General Tree | AC-02, AC-04 |
| **FR-026** | Category Manager | Anushka Samad | General Tree | AC-02, AC-04 |
| **FR-027** | Category Manager | Anushka Samad | General Tree | AC-02, AC-03 |
| **FR-028** | Category Manager | Anushka Samad | General Tree | AC-01, AC-02 |
| **FR-029** | Category Manager | Anushka Samad | General Tree | AC-01, AC-09 |
| **FR-030** | Category Manager | Anushka Samad | General Tree | AC-01, AC-10 |
| **FR-031** | Document Vault | Ubaid Raza | (Filesystem / Repository) | AC-01, AC-04, AC-11 |
| **FR-032** | Document Vault | Ubaid Raza | (Filesystem / Repository) | AC-01, AC-10 |
| **FR-033** | Document Vault | Ubaid Raza | (Filesystem / Repository) | AC-01, AC-04 |
| **FR-034** | Document Vault | Ubaid Raza | (Filesystem / Repository) | AC-01, AC-10 |
| **FR-035** | Document Vault | Ubaid Raza | (Filesystem / Repository) | AC-10 |
| **FR-036** | Document Vault | Ubaid Raza | (Filesystem / Repository) | AC-01, AC-04, AC-11 |
| **FR-037** | Achievement Vault | Ubaid Raza | (Filesystem / Repository) | AC-01, AC-04, AC-11 |
| **FR-038** | Achievement Vault | Ubaid Raza | (Filesystem / Repository) | AC-01, AC-04 |
| **FR-039** | Achievement Vault | Ubaid Raza | (Filesystem / Repository) | AC-01, AC-10 |
| **FR-040** | Achievement Vault | Ubaid Raza | (Filesystem / Repository) | AC-01 |
| **FR-041** | Achievement Vault | Ubaid Raza | (Filesystem / Repository) | AC-01, AC-05 |
| **FR-042** | Achievement Vault | Ubaid Raza | (Filesystem / Repository) | AC-01, AC-04, AC-11 |
| **FR-043** | Smart Search | Ubaid Raza | BST & Hash Table | AC-02, AC-04, AC-11 |
| **FR-044** | Smart Search | Ubaid Raza | BST & Hash Table | AC-02, AC-09 |
| **FR-045** | Smart Search | Ubaid Raza | BST & Hash Table | AC-01, AC-09 |
| **FR-046** | Smart Search | Ubaid Raza | BST & Hash Table | AC-09 |
| **FR-047** | Smart Search | Ubaid Raza | BST & Hash Table | AC-09, AC-10 |
| **FR-048** | Priority Vault | Ubaid Raza | Max-Heap / Priority Queue | AC-02, AC-04 |
| **FR-049** | Priority Vault | Ubaid Raza | Max-Heap / Priority Queue | AC-02, AC-07 |
| **FR-050** | Priority Vault | Ubaid Raza | Max-Heap / Priority Queue | AC-07 |
| **FR-051** | Priority Vault | Ubaid Raza | Max-Heap / Priority Queue | AC-01, AC-07, AC-11 |
| **FR-052** | Archive & Undo | Ubaid Raza | Stack | AC-01, AC-04, AC-11 |
| **FR-053** | Archive & Undo | Ubaid Raza | Stack | AC-01 |
| **FR-054** | Archive & Undo | Ubaid Raza | Stack | AC-01, AC-04, AC-11 |
| **FR-055** | Archive & Undo | Ubaid Raza | Stack | AC-01, AC-04, AC-11 |
| **FR-056** | Archive & Undo | Ubaid Raza | Stack | AC-02, AC-08 |
| **FR-057** | Archive & Undo | Ubaid Raza | Stack | AC-02, AC-08, AC-11 |
| **FR-058** | Archive & Undo | Ubaid Raza | Stack | AC-08, AC-10 |
| **FR-059** | Task Queue Pipeline | Ubaid Raza | Queue | AC-02, AC-03 |
| **FR-060** | Task Queue Pipeline | Ubaid Raza | Queue | AC-02, AC-03 |
| **FR-061** | Task Queue Pipeline | Ubaid Raza | Queue | AC-02, AC-03, AC-11 |
| **FR-062** | Task Queue Pipeline | Ubaid Raza | Queue | AC-02, AC-03 |

---

## 11. Assumptions, Dependencies, and Explicit Design Decisions

In accordance with strict academic guidelines, the following specific architectural and technical resolutions are documented:
1. **Course Designation:** The course title is officially verified as *"Data Structures (BSCS)"*. No specific institutional course code (such as CS2001) is asserted.
2. **Achievement Entity Schema Alignment:** The database table `records` contains columns `id`, `record_type`, `title`, `category`, `record_date`, `description`, `file_path`, `priority`, `archived`, and `created_at`. No separate `organization` or `issuer` column exists in the approved schema. Requirements explicitly specify that organizational metadata is recorded within the existing `category` hierarchy or `description` fields.
3. **Category Tree Reconstruction vs. Persistence:** The approved SQLite schema does not contain an independent `categories` table. Category persistence is realized through record assignment: active records store category paths in `records.category`. The `CategoryTree` is dynamically reconstructed from distinct category strings upon startup. Standalone category paths created in memory without attached records are temporary and do not persist across restarts.
4. **Undo Scope and Operational Stack:** The custom `Stack` operates strictly as an in-memory session structure. Reversible operations are limited to Creation, Archival, and Restoration. Permanent deletion is irreversible and cannot be undone. Undo history is not persisted across application restarts.
5. **Queue Role:** The `Queue` structure operates strictly as an internal synchronous FIFO task staging processor, fully meeting the requirement for an independent custom data structure without introducing unsupported asynchronous workers or background schedulers.
6. **Performance Metrics:** Abstract or unverified numerical benchmarks (e.g., millisecond startup claims) are excluded in favor of testable algorithmic complexity bounds (Big-$O$) and observable GUI responsiveness.

---
*End of Software Requirements Specification (SRS) for LifeVault.*
