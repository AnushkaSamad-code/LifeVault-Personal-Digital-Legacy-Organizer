# Data Structures Specification

All structures must be implemented manually in separate Python modules. Each class must have a docstring, clear operations, edge-case handling and independent unit tests.

## 1. Dynamic Array
File: `data_structures/dynamic_array.py`
Use: Maintain an indexed in-memory collection of loaded records for iteration and dashboard calculations.
Required operations: append, get(index), set(index, value), remove_at(index), length, iteration, resize.
Explain: access O(1), append amortized O(1), remove_at O(n).

## 2. Singly Linked List
File: `data_structures/singly_linked_list.py`
Use: Maintain a memory activity/history chain in insertion order.
Required operations: append, prepend (optional), find, delete, traverse/to_list, length.
Explain: append O(1) if tail maintained; search O(n).

## 3. Stack
File: `data_structures/stack.py`
Use: Undo history.
Required operations: push, pop, peek, is_empty, size.
Use a custom backing structure or clearly explain the internal representation. Do not use a third-party stack.
Explain: push/pop O(1).

## 4. Queue
File: `data_structures/queue.py`
Use: FIFO queue for pending record-processing tasks or UI-independent task simulation. It must have a real demonstrated workflow, not just exist unused.
Required operations: enqueue, dequeue, front/peek, is_empty, size.
Prefer a linked-node implementation to achieve O(1) enqueue/dequeue.

## 5. Circular Linked List
File: `data_structures/circular_linked_list.py`
Use: Cycle through active memories (next/previous if doubly circular is chosen; otherwise next only).
Required operations: append, next_item, reset/current, traverse safely with a size bound.
Explain how last node points to first node.

## 6. Binary Search Tree
File: `data_structures/binary_search_tree.py`
Use: Search records by integer record ID.
Required operations: insert, search, delete, inorder traversal.
Handle duplicate keys by updating the value or rejecting duplicates consistently.
Explain average O(log n), worst O(n).

## 7. General Tree
File: `data_structures/category_tree.py`
Use: Category hierarchy, e.g. LifeVault → Documents → Academic → Certificates.
Required operations: add_path, find, children, traversal.
Avoid relying on database category order as a substitute for tree traversal.

## 8. Graph
File: `data_structures/graph.py`
Use: Connect related record IDs.
Required operations: add_vertex, add_edge, remove_edge, neighbors, BFS, DFS.
Use adjacency list. Prevent duplicate edges and self-edges.
Persist edges in SQLite and rebuild the graph at startup.
Explain BFS/DFS complexity O(V + E).

## 9. Heap / Priority Queue
File: `data_structures/priority_queue.py`
Use: Show important records with priority 5 before 4 ... before 1.
Required operations: push, peek, pop, is_empty, size, heapify or rebuild.
Implement a binary max-heap manually; do not use `heapq`.
Use a stable tie-breaker such as insertion sequence or record ID so equal priorities are predictable.
Explain push/pop O(log n), peek O(1).

## 10. Hash Table
File: `data_structures/hash_table.py`
Use: Fast exact lookup by record ID.
Required operations: set, get, delete, contains, collision handling, resizing (recommended).
Use separate chaining or open addressing and document the chosen method.
Explain average O(1), worst O(n).

## Integration rules
- SQLite remains persistent source of truth.
- On startup: load active and archived records as appropriate, then build Array, BST, Hash Table, category Tree, Priority Queue, memory Linked List/Circular Linked List and Graph.
- After add/edit/archive/restore/delete: update or rebuild affected structures to avoid stale indexes.
- Queue must be exercised by a real app workflow (e.g. enqueue add/update/archive requests and process them in FIFO order) or a clearly documented task-processing demonstration.
- Never claim a structure is used by a feature if the feature actually bypasses it.
- Provide a Data Structure demo screen or developer diagnostics view showing operations and sample outputs for viva.
