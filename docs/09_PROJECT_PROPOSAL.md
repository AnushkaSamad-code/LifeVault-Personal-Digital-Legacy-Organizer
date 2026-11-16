# Project Proposal: LifeVault – Personal Digital Legacy Organizer

**Course:** Data Structures (BSCS)  
**Academic Level:** Undergraduate / University Level  
**Project Complexity:** Medium  
**Application Type:** Standalone Local Desktop Application  

---

### Project Team & Authors
* **Anushka Samad** (Student ID: `CSC-25F-083`) — Core Modules & Linear/Non-linear Graph Structures
* **Ubaid Raza** (Student ID: `CSC-25F-013`) — Core Modules & Hierarchical/Access/Search Structures

---

## 1. Executive Summary & Project Title

### Project Title
**LifeVault – Personal Digital Legacy Organizer**

LifeVault is a proposed local-first, offline desktop application designed in Python to serve as a unified personal repository for preserving, organizing, indexing, and interlinking personal digital memories, documents, and milestone achievements.

Beyond its utility as an intuitive desktop organizer, LifeVault is architected specifically as a comprehensive course project demonstration for an undergraduate Data Structures course. The proposed application pairs a persistent SQLite database layer with ten manually implemented in-memory data structures, providing concrete, practical instantiations for fundamental computer science algorithms and abstract data types (ADTs).

---

## 2. Introduction & Background

In the contemporary digital era, personal histories and milestones are heavily fragmented across diverse operating systems, local file directories, mobile galleries, cloud services, and ephemeral messaging platforms. Physical documents are digitized into isolated PDF files, photographs remain buried in disconnected folders, and awards or certificates are misplaced over time. When an individual seeks to reconstruct their life narrative, locate important records, or understand the chronological and contextual connections between significant life events, the lack of a centralized, relationship-aware system poses significant friction.

Furthermore, within academic computer science education, data structures such as balanced trees, circular lists, priority queues, and graphs are frequently taught as theoretical abstractions or isolated algorithmic exercises. Students rarely experience how these diverse structures cooperate within a multi-layered software architecture to power end-to-end functionality.

LifeVault addresses both challenges simultaneously:
1. **Practical Domain:** It proposes an offline, desktop-based personal legacy organizer that catalogs life records into three explicit categories: *Memories*, *Documents*, and *Achievements*.
2. **Pedagogical Domain:** It demonstrates the deliberate, purpose-driven application of ten distinct custom data structures built from fundamental principles without reliance on high-level standard library algorithmic shortcuts for core algorithmic operations.

---

## 3. Problem Statement

Existing digital organization systems present three critical limitations:

1. **Fragmentation and Context Loss:** Filesystems categorize records purely hierarchically by directory paths or chronologically by OS timestamps. They fail to represent associative connections (e.g., linking a university degree document to a graduation memory and an academic award achievement).
2. **Privacy Concerns and Unnecessary Overhead:** Mainstream personal management tools increasingly mandate persistent cloud connectivity, user tracking, complex authentication, and subscription overhead. Users seeking a private, offline, self-contained desktop system have few lightweight alternatives.
3. **The Academic Gap in Software Engineering:** In academic curricula, foundational data structures are often demonstrated through basic terminal scripts. There is a need for a unified, visually responsive desktop application that integrates multiple custom data structures—such as graphs for associative networks, circular lists for slideshow traversals, stacks for transaction rollback, and max-heaps for priority scheduling—into a cohesive, decoupled architecture.

---

## 4. Project Objectives

### 4.1 Pedagogical & Algorithmic Objectives
* **Manual Data Structure Construction:** Implement ten foundational data structures from scratch in dedicated Python classes, adhering to academic integrity by avoiding built-in algorithmic shortcuts (such as `heapq`, `queue.Queue`, or standard dictionary indexing for core algorithms).
* **Algorithmic Rigor & Complexity Analysis:** Validate theoretical time and space complexities (Big-$O$) through dedicated test suites and runtime performance analysis.
* **Dual-State System Coordination:** Reconcile persistent relational storage (SQLite) with volatile in-memory custom data structures by hydrating and indexing in-memory structures upon application startup and maintaining synchronization during runtime operations.

### 4.2 Functional & Architectural Objectives
* **Comprehensive Record Management:** Provide robust Create, Read, Update, Archive, Restore, and Delete (CRUD) operations across three distinct record entities: Memories, Documents, and Achievements.
* **Associative Graph Networking:** Enable arbitrary cross-linking between related records to form an undirected knowledge graph navigable via Breadth-First Search (BFS) and Depth-First Search (DFS).
* **Multi-Modal Retrieval:** Support multi-tier searching, including exact numerical ID matching via a Binary Search Tree and Hash Table, alongside text-based searching and category-tree filtering.
* **Transaction Rollback:** Support an explicit undo mechanism powered by a custom LIFO Stack for supported state-altering actions.
* **Clean Layered Architecture:** Enforce strict separation of concerns across a 4-tier model (Presentation, Service, Data Structures, and Persistence/Repository).

---

## 5. Proposed Solution

LifeVault is planned as a medium-complexity, local desktop software application developed using **Python**, **CustomTkinter**, and **SQLite**.

### 5.1 System Architecture
The application will adhere to a decoupled 4-layer architecture:

```
+--------------------------------------------------------------------------+
|                     1. PRESENTATION LAYER (GUI)                          |
|  CustomTkinter UI: Navigation Sidebar, Form Dialogs, Dashboard, Views    |
+--------------------------------------------------------------------------+
                                    |
                                    v
+--------------------------------------------------------------------------+
|                       2. SERVICE LAYER (LOGIC)                           |
|  RecordService, SearchService, RelationshipService, UndoService, etc.    |
|  - Input Validation, Workflow Coordination, Dual-State Sync              |
+--------------------------------------------------------------------------+
                   /                                      \
                  v                                        v
+-----------------------------------+    +---------------------------------+
| 3. DATA STRUCTURES LAYER (MEMORY) |    | 4. PERSISTENCE LAYER (STORAGE)  |
| 10 Manual Python Data Structures  |    | SQLite Database & Repositories  |
| - Fast in-memory indexing         |    | - Source of persistent truth    |
| - Algorithmic traversal & search  |    | - Parameterized relational SQL  |
+-----------------------------------+    +---------------------------------+
```

1. **Presentation Layer:** Built with CustomTkinter, rendering a modern desktop interface styled in an intentional **Navy and Lavender** palette (`#172B4D` primary navy, `#243B63` secondary navy, `#B9A7E8` lavender accent, `#F4F5FA` light background). It will contain no direct SQL queries and will delegate user actions to the service layer.
2. **Service Layer:** Will house application business logic, input sanitization, transaction coordination, and state synchronization between the database and memory.
3. **Data Structures Layer:** Ten custom-built classes residing in memory. On startup, services will read persistent records from SQLite and hydrate these structures to power runtime navigation, indexing, sorting, and graph operations.
4. **Persistence Layer:** Will utilize Python's native `sqlite3` module to manage relational tables (`records`, `record_connections`, and optional `activity_log`) with foreign key enforcement and parameterized queries.

---

## 6. Main Features and Modules

The system is partitioned into modular subsystems with clearly demarcated team ownership:

```
                                  LIFEVAULT SYSTEM
                                         |
     +-----------------------------------+-----------------------------------+
     |                                                                       |
[ANUSHKA SAMAD]                                                         [UBAID RAZA]
- Dashboard (Dynamic Array)                                             - Document Vault (Local File Handling)
- Memory Vault (Circular Linked List)                                   - Achievement Vault (Milestones & Awards)
- Life Timeline (Singly Linked List)                                    - Smart Search (BST & Hash Table)
- Memory Connections (Graph)                                            - Priority Vault (Max-Heap / PQ)
- Category Manager (General Tree)                                       - Archive & Undo (Stack)
                                                                        - Task Processing Pipeline (Queue)
```

### 6.1 Modules Owned by Anushka Samad

1. **Dashboard Module (Dynamic Array):**
   * Computes dynamic summary metrics (total records, active memories, documents, achievements, archived count).
   * Displays recent records and activity feeds via contiguous dynamic array traversal.
   * Houses quick-action shortcuts for rapid record creation.
2. **Memory Vault Module (Circular Linked List):**
   * Dedicated interface for managing personal memories (dates, narratives, emotional significance, and optional media paths).
   * Implements cyclical, continuous "Next / Previous" memory browsing without hard boundaries, creating an interactive memory carousel.
3. **Life Timeline Module (Singly Linked List):**
   * Chronological sequential view aggregating memories and achievements across an individual's lifetime.
   * Leverages a linked list to maintain chronological node sequences, enabling forward historical traversal and timeline filtering.
4. **Memory Connections Module (Graph):**
   * Manages semantic relationships between arbitrary records (e.g., linking a milestone to supporting documents and memories).
   * Provides graph inspection, displaying immediate neighbors, detecting cycles, and executing Breadth-First (BFS) and Depth-First (DFS) traversals.
5. **Category Manager (General Tree):**
   * Structures records into an N-ary hierarchical tree taxonomy (e.g., `Root` $\rightarrow$ `Documents` $\rightarrow$ `Academic` $\rightarrow$ `Transcripts`).
   * Supports branch addition, path searches, and hierarchical traversal.

### 6.2 Modules Owned by Ubaid Raza

1. **Document Vault Module:**
   * Catalogs vital personal, educational, legal, and medical documents.
   * Stores metadata and references to local filesystem paths with safe file-launching routines and missing-file exception handling.
2. **Achievement Vault Module:**
   * Dedicated registry for honors, completed certifications, degrees, and competitive milestones.
   * Formats milestone cards with organizational metadata, completion dates, and credential file links.
3. **Smart Search Module (Binary Search Tree & Hash Table):**
   * Dual-engine search system:
     * *Exact ID Retrieval:* Fast $O(1)$ average lookup via a custom Hash Table and ordered $O(\log n)$ average retrieval via a Binary Search Tree.
     * *Text/Attribute Scan:* Substring filtering across title, description, and category.
4. **Priority Vault Module (Max-Heap / Priority Queue):**
   * Manages importance triage (scale 1 to 5).
   * Surfaces the highest-priority records first via a custom binary Max-Heap, providing visual indicators of record criticality.
5. **Archive & Undo Module (Stack):**
   * Implements soft-deletion (archival flag) to prevent accidental data loss, accompanied by complete restoration workflows.
   * Manages a LIFO undo stack to revert destructive or state-changing operations (such as record edits, deletions, or status transitions).
6. **Internal Queue Task Processing Pipeline (Queue):**
   * A basic FIFO (First In, First Out) pending-task processor that queues and processes record operations in order.
   * Demonstrates essential Queue operations (`enqueue`, `dequeue`, `front`/`peek`, `is_empty`, `size`) in a direct, synchronous record-handling workflow.

### 6.3 Shared Integration Responsibilities (Both Members)
* Joint specification and agreement on database schemas, repository interfaces, and service contracts prior to integration.
* Comprehensive testing of integrated workflows, cross-module data flow validation, and UI consistency verification.
* Compilation of final technical documentation, viva defense preparation, and demonstration datasets.

---

## 7. Implementation of All 10 Data Structures

The project mandates the ground-up implementation of ten distinct data structures in separate modules. Each structure fulfills a real functional role in LifeVault:

| # | Data Structure | Source File | Assigned Member | Practical Role in LifeVault | Core Operations | Target Time Complexity |
|---|---|---|---|---|---|---|
| **1** | **Dynamic Array** | `data_structures/dynamic_array.py` | Anushka Samad | In-memory record collection, random indexing, and dashboard aggregations. | `append`, `get`, `set`, `remove_at`, `resize`, `length`, `iteration` | Access: $O(1)$<br>Append: Amortized $O(1)$<br>Remove: $O(n)$ |
| **2** | **Singly Linked List** | `data_structures/singly_linked_list.py` | Anushka Samad | Chronological timeline chain and sequential event traversal. | `append`, `prepend`, `delete`, `find`, `traverse`, `to_list`, `length` | Prepend: $O(1)$<br>Append: $O(1)$ (with tail)<br>Search/Delete: $O(n)$ |
| **3** | **Circular Linked List** | `data_structures/circular_linked_list.py` | Anushka Samad | Continuous, cyclic memory browsing and carousel navigation. | `append`, `next_item`, `reset`, `current`, `traverse_bounded` | Next: $O(1)$<br>Append: $O(1)$<br>Search: $O(n)$ |
| **4** | **General Tree (N-ary)** | `data_structures/category_tree.py` | Anushka Samad | Hierarchical category taxonomy and nested classification. | `add_path`, `find_node`, `get_children`, `traverse_preorder` | Search: $O(n)$<br>Insert: $O(d)$ ($d = \text{depth}$) |
| **5** | **Graph (Adjacency List)** | `data_structures/graph.py` | Anushka Samad | Inter-record relationship networks, cross-referencing, and graph traversals. | `add_vertex`, `add_edge`, `remove_edge`, `get_neighbors`, `bfs`, `dfs` | Traversals (BFS/DFS): $O(V + E)$<br>Edge Ops: $O(V)$ / $O(\text{deg}(v))$ |
| **6** | **Binary Search Tree** | `data_structures/binary_search_tree.py` | Ubaid Raza | Exact numeric record ID search and ordered in-order indexing. | `insert`, `search`, `delete`, `inorder_traversal` | Search/Insert: Avg $O(\log n)$, Worst $O(n)$ |
| **7** | **Hash Table** | `data_structures/hash_table.py` | Ubaid Raza | Direct record lookup by unique primary record ID. | `set`, `get`, `delete`, `contains`, `rehash` (chaining collision handling) | Lookup/Insert/Delete:<br>Avg $O(1)$, Worst $O(n)$ |
| **8** | **Max-Heap / Priority Queue** | `data_structures/priority_queue.py` | Ubaid Raza | Importance-based record retrieval (priority levels 5 down to 1). | `push`, `pop`, `peek`, `heapify`, `is_empty`, `size` | Peek: $O(1)$<br>Push/Pop: $O(\log n)$<br>Heapify: $O(n)$ |
| **9** | **Stack** | `data_structures/stack.py` | Ubaid Raza | Action history and state reversal (Undo functionality). | `push`, `pop`, `peek`, `is_empty`, `size` | Push/Pop/Peek: $O(1)$ |
| **10**| **Queue** | `data_structures/queue.py` | Ubaid Raza | FIFO pending-task processor for sequential record operations. | `enqueue`, `dequeue`, `front`, `is_empty`, `size` | Enqueue/Dequeue: $O(1)$ |

### Detailed Structural Specifications

1. **Dynamic Array (`DynamicArray`):** Implements a geometric resizing array (allocating double capacity upon saturation) to hold active record pointers, demonstrating manual memory tracking, indexing, and amortized constant-time additions.
2. **Singly Linked List (`SinglyLinkedList`):** Built with discrete `Node` objects maintaining reference pointers to subsequent nodes. Used to maintain sequential event logs and chronological historical chains without requiring contiguous memory blocks.
3. **Circular Linked List (`CircularLinkedList`):** A specialized linked structure wherein the tail node's `next` pointer references the head node. Enables continuous circular browsing of memories in the GUI without encountering null-pointer termination.
4. **General Tree (`CategoryTree`):** A hierarchical structure where each `TreeNode` maintains a collection of child pointers. Mirrors directory-like organization for categories (e.g., `Personal`, `Financial`, `Medical`), enabling recursive path traversal and subtree querying.
5. **Graph (`Graph`):** Implements a custom adjacency-list graph representation to model relationships between record IDs. In strict adherence to the project's custom Data Structures implementation requirements, the graph's internal adjacency representation and core operations (`add_vertex`, `add_edge`, `remove_edge`, `get_neighbors`, `bfs`, and `dfs`) are custom-implemented without substituting Python built-in dictionaries or sets as replacements for the custom Graph implementation. It prevents duplicate edges and self-loops, identifies neighbor connections, and supports path exploration via Breadth-First Search (BFS) and Depth-First Search (DFS).
6. **Binary Search Tree (`BinarySearchTree`):** Maintains binary sorting invariants ($Left.ID < Node.ID < Right.ID$). Powers ordered lookups by record identifier and produces sorted key sequences via in-order depth-first traversal.
7. **Hash Table (`HashTable`):** Implements a dedicated hash function with separate chaining to resolve hash collisions. Supports fast record retrieval and dynamic rehashing when load factor thresholds are exceeded.
8. **Max-Heap Priority Queue (`PriorityQueue`):** An array-backed complete binary tree satisfying the max-heap property ($Parent \ge Children$). Guarantees that records tagged with priority 5 are dequeued before lower-priority records, utilizing a deterministic secondary tie-breaker (e.g., record ID) for stability.
9. **Stack (`Stack`):** A strict LIFO structure backed by linked nodes. Captures historical reversible commands, allowing users to undo unintended edits, deletions, or status modifications.
10. **Queue (`Queue`):** A strict FIFO structure implemented via linked nodes with distinct `head` and `tail` pointers. Manages pending record-handling tasks in the exact sequence they were submitted.

---

## 8. Technology Stack & Technical Decisions

The chosen technology stack reflects the confirmed decisions established for this project:

* **Programming Language:** **Python 3.10+**
  * Selected for its clean syntax, cross-platform stability, typing support (`typing` annotations), and suitability for object-oriented data structure design.
* **Graphical User Interface (GUI):** **CustomTkinter**
  * A modern extension of Python's standard `tkinter` library providing styled, high-DPI scaled UI components.
  * Configured with a dedicated visual theme:
    * Primary Navy: `#172B4D`
    * Secondary Navy: `#243B63`
    * Lavender Accent: `#B9A7E8`
    * Light Background: `#F4F5FA`
    * Pure White Surface Cards: `#FFFFFF`
    * Dark Slate Typography: `#1E293B`
* **Persistent Storage:** **SQLite (`sqlite3`)**
  * Serverless, zero-configuration, ACID-compliant relational database engine.
  * Operates as the persistent source of truth across sessions, utilizing parameterized queries (`?`) to prevent SQL injection and enforcing foreign key constraints (`PRAGMA foreign_keys = ON`).
* **Testing Framework:** **pytest**
  * Pytest will be used as the project's testing framework to develop and execute automated unit tests for all custom data structures and integration tests for service workflows using `python -m pytest`. Pytest is installed in the local environment and was verified by executing initial foundation tests; comprehensive automated test suites will be developed across subsequent phases as custom data structures and services are constructed.
* **Application Paradigm:** **Standalone Local Desktop Application**
  * Operates locally with zero external network or cloud prerequisites, ensuring data remains on the user's local machine and delivering predictable offline execution.
* **Complexity Classification:** **Medium Complexity**
  * Calibrated specifically for university data structures curriculum requirements, balancing algorithmic rigor with clean software architecture.

---

## 9. Project Scope & Boundary Analysis

To ensure feasibility, academic rigor, and system stability, the project boundaries are explicitly defined:

### 9.1 In-Scope Capabilities
* Manual implementation and standalone unit testing of all 10 specified data structures.
* Complete local lifecycle management (Create, Read, Update, Archive, Restore, Delete) for Memory, Document, and Achievement entities.
* Local filesystem document referencing with path validation and missing-file safeguards.
* Bidirectional graph connection creation and neighbor visualization.
* Chronological timeline sequencing and category tree navigation.
* Multi-criteria search (exact ID via BST/Hash Table; substring scanning across text attributes).
* Priority management via Max-Heap.
* Action undo operations via Stack.
* Synchronous FIFO task processing via Queue.
* Startup state rehydration from SQLite into in-memory data structures.
* Dedicated "Data Structure Demo / Diagnostics" screen for academic viva examinations.

### 9.2 Out-of-Scope (Explicit Non-Goals)
* **Cloud Synchronization & Remote Hosting:** No cloud databases, remote backups, or third-party web APIs.
* **Multi-User Collaboration & Authentication:** No user login screens, role-based access control, or shared vaults.
* **Artificial Intelligence & Machine Learning:** No automated OCR, image recognition, or natural language categorization.
* **Legal Inheritance & Will Execution:** No automated legal claims, estate management, or probate legal guarantees.
* **Heavy Binary Blob Storage:** The database will not embed large binary files; it stores validated local filesystem URI strings.
* **Mobile / Web Implementations:** The system is exclusively focused on the desktop form factor.

---

## 10. Expected Outcomes & Deliverables

Upon completion, the LifeVault project is planned to produce the following academic and software engineering deliverables:

1. **Functional Desktop Application:** A responsive and stable Python desktop application operating under the custom navy and lavender theme.
2. **Modular Custom Data Structure Library:** Ten verified, well-documented Python modules in the `data_structures/` package, implemented without reliance on standard library container shortcuts for core algorithms.
3. **Automated Test Suite:** Test coverage implemented in `tests/` and run with `pytest`, validating boundary conditions, empty states, resizing behavior, collision resolution, and traversal accuracies.
4. **Normalized Relational Database Architecture:** Complete SQLite schema scripts (`schema.sql`) and associated repository classes with foreign key constraints and transaction integrity.
5. **Comprehensive Technical Documentation:**
   * Software Requirements Specification (SRS).
   * High-Level and Low-Level Architecture Documents.
   * Data Structures Specification and Complexity Matrices.
   * User Guide and Installation Manual.
   * Viva Voce Defense Question & Answer Guide.
6. **Academic Viva Diagnostics Mode:** An interactive view within the GUI allowing instructors to inspect the internal states, node arrangements, and operations of the underlying data structures during evaluation.

---

## 11. Planned Phased Development Methodology

The project is structured according to a planned 10-phase incremental engineering lifecycle:

* **Phase 0: Documentation Review & Requirements Alignment** — Detailed requirements analysis, project proposal authoring, and SRS specification.
* **Phase 1: Project Foundation & Shell** — Environment setup, package directory layout, and initial CustomTkinter application shell with the navy and lavender theme.
* **Phase 2: Independent Data Structures Development** — Manual implementation and isolated unit testing of all 10 data structures using pytest.
* **Phase 3: Database & Persistence Layer** — SQLite schema definition, repository implementation, and transaction management.
* **Phase 4: Service Layer & Dual-State Integration** — Synchronization logic between SQLite records and in-memory data structures, including the FIFO queue workflow.
* **Phase 5: Reusable UI Components & Dashboard** — Navigation sidebar, summary metric cards, and responsive layout foundations.
* **Phase 6: Core Record Vault Modules** — Complete UI forms and CRUD workflows for Memory, Document, and Achievement vaults.
* **Phase 7: Advanced Data Structure UI Views** — Search screen, Category tree viewer, Timeline, Memory carousel, Graph connections view, Priority vault, and Undo stack integration.
* **Phase 8: Comprehensive QA & System Integration** — End-to-end user journey validation, edge case handling, and restart persistence verification.
* **Phase 9: Final Academic Deliverables & Viva Prep** — Finalized project documentation, application screenshots, demo datasets, and viva presentation materials.

---

## 12. Conclusion

LifeVault bridges the critical gap between abstract theoretical computer science and practical desktop software development. By coupling an offline, local-first personal legacy organizer with ten manually implemented data structures, the proposed project provides a rigorous, university-caliber platform demonstrating the tangible utility of arrays, linked lists, trees, graphs, heaps, hash tables, stacks, and queues.

Designed with a decoupled 4-layer architecture, styled with an intentional navy and lavender interface, and grounded by SQLite persistence, LifeVault represents a well-structured, feasible, and educationally meaningful academic endeavor for both team members.
