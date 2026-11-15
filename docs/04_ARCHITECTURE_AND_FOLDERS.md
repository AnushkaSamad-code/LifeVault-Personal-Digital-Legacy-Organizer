# Architecture and Folder Structure

## Layered architecture
1. Presentation layer: CustomTkinter screens and reusable widgets.
2. Service layer: validation, workflows and coordination.
3. Data Structures layer: custom classes and algorithms.
4. Repository/database layer: SQLite persistence.

GUI must not execute SQL directly. GUI calls service methods. Services call repositories and custom Data Structures.

## Proposed folder structure
```text
LifeVault/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── docs/
│   ├── 00_START_HERE.md
│   ├── 01_PROJECT_REQUIREMENTS.md
│   ├── 02_MODULE_BREAKDOWN.md
│   ├── 03_DATA_STRUCTURES_SPEC.md
│   ├── 04_ARCHITECTURE_AND_FOLDERS.md
│   ├── 05_DATABASE_SCHEMA.md
│   ├── 06_UI_DESIGN_GUIDE.md
│   ├── 07_DEVELOPMENT_TASKS.md
│   └── 08_TESTING_AND_VIVA.md
├── data_structures/
│   ├── __init__.py
│   ├── dynamic_array.py
│   ├── singly_linked_list.py
│   ├── stack.py
│   ├── queue.py
│   ├── circular_linked_list.py
│   ├── binary_search_tree.py
│   ├── category_tree.py
│   ├── graph.py
│   ├── priority_queue.py
│   └── hash_table.py
├── database/
│   ├── __init__.py
│   ├── connection.py
│   ├── schema.sql
│   └── repositories/
│       ├── record_repository.py
│       └── connection_repository.py
├── services/
│   ├── record_service.py
│   ├── search_service.py
│   ├── timeline_service.py
│   ├── relationship_service.py
│   ├── archive_service.py
│   └── undo_service.py
├── gui/
│   ├── app.py
│   ├── theme.py
│   ├── components/
│   └── screens/
│       ├── dashboard.py
│       ├── memory_vault.py
│       ├── document_vault.py
│       ├── achievement_vault.py
│       ├── timeline.py
│       ├── connections.py
│       ├── priority_vault.py
│       ├── archive.py
│       ├── search.py
│       └── data_structure_demo.py
├── tests/
│   ├── test_dynamic_array.py
│   ├── test_singly_linked_list.py
│   ├── test_stack.py
│   ├── test_queue.py
│   ├── test_circular_linked_list.py
│   ├── test_bst.py
│   ├── test_category_tree.py
│   ├── test_graph.py
│   ├── test_priority_queue.py
│   ├── test_hash_table.py
│   └── test_services.py
└── assets/
    ├── icons/
    └── images/
```

## Coding conventions
- Use descriptive snake_case names.
- Use one class per main Data Structure module.
- Add type hints to public methods where practical.
- Keep functions focused and short.
- Use `pathlib.Path` for paths.
- Use `sqlite3` with parameterized queries.
- Do not store database files, virtual environments, cache files or personal user data in Git.
- Keep a `README.md` with installation and run instructions.
