# LifeVault — Personal Digital Legacy Organizer

LifeVault is an educational Python desktop application designed to organize personal digital memories, documents, achievements, and connected records in a single local archive.

Built with **CustomTkinter** and **SQLite**, LifeVault demonstrates the practical, manual implementation of **ten core Data Structures** through a modern Navy & Lavender desktop graphical interface.

---

## Team & Responsibilities

- **Anushka Samad (CSC-25F-083)**
  - **Modules:** Dashboard, Memory Vault, Life Timeline, Memory Connections, Category Manager.
  - **Data Structures (5):** Dynamic Array, Singly Linked List, Circular Linked List, Graph (Adjacency List, BFS/DFS), General Tree.
  - **Foundation Responsibility:** GUI theme, navigation shell, sidebar, and placeholder screens.

- **Ubaid Raza (CSC-25F-013)**
  - **Modules:** Document Vault, Achievement Vault, Smart Search, Priority Vault, Archive & Undo, Internal FIFO Queue Processor.
  - **Data Structures (5):** Binary Search Tree, Hash Table, Max Heap / Priority Queue, Stack, Queue.
  - **Foundation Responsibility:** Python environment, requirements, gitignore, and database foundation scaffolding.

---

## Setup & Running the Application

### 1. Prerequisites
- Python 3.10+ (Python 3.13 supported)

### 2. Create and Activate Virtual Environment
```bash
# Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Windows (Command Prompt)
python -m venv .venv
.\.venv\Scripts\activate.bat
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run LifeVault
```bash
python main.py
```

---

## 10 Core Functional Modules

1. **Dashboard:** Overview metrics, count cards, and recent records.
2. **Memory Vault:** Personal memories with sequential & circular browsing.
3. **Document Vault:** Local document metadata and file path handling.
4. **Achievement Vault:** Awards, certificates, and milestones.
5. **Life Timeline:** Chronological ordering of milestones and memories.
6. **Memory Connections:** Relational graph showing connections between records.
7. **Category Manager:** Hierarchical taxonomy tree for record organization.
8. **Priority Vault:** Max Heap prioritization (levels 1 to 5).
9. **Archive & Undo:** Safe archiving, restoration, and stack-based undo.
10. **Smart Search:** Exact ID lookup via BST/Hash Table and keyword search.

*(Optional "About" screen is accessible outside the core 10 modules at the bottom of the sidebar).*
