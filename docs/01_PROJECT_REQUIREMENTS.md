# Project Requirements — LifeVault

## 1. Overview
LifeVault is a Python desktop application that helps a user organize personal digital memories, documents, achievements, and related records in one local archive.

The project demonstrates practical use of ten Data Structures through a usable GUI. It is an educational project, not a legal inheritance platform or a secure cloud vault.

## 2. Problem statement
Personal records are often scattered across folders, galleries, notes and devices. Finding, categorizing and connecting these records can become inconvenient. LifeVault provides one local desktop interface for organizing and retrieving these records.

## 3. Objectives
- Create, view, update, archive, restore and delete records.
- Organize records by type and category.
- Search records by ID, title, category and description.
- Display memories and achievements chronologically.
- Connect related records.
- Demonstrate all ten Data Structures through actual operations.
- Store records locally using SQLite.
- Provide a clean, accessible navy/lavender desktop GUI.

## 4. Users
Version 1 is a single-user local desktop application. No multi-user accounts or online services are required.

## 5. Record types
### Memory
Fields: ID, title, category, date, description, optional image/file path, importance, created timestamp, archived status.

### Document
Fields: ID, title, category, document date, description, optional local file path, importance, created timestamp, archived status.

### Achievement
Fields: ID, title, category, date, description, optional certificate file path, importance, created timestamp, archived status.

## 6. Functional requirements
- FR-01: Display dashboard counts and recent active records.
- FR-02: Add a Memory record.
- FR-03: Add a Document record and optionally select a local file.
- FR-04: Add an Achievement record.
- FR-05: View all active records with type filters.
- FR-06: View record details.
- FR-07: Edit an existing record.
- FR-08: Archive a record.
- FR-09: View archived records.
- FR-10: Restore an archived record.
- FR-11: Permanently delete a record after confirmation.
- FR-12: Search by numeric ID or text fields.
- FR-13: Filter records by type, category and date range.
- FR-14: Display timeline ordered by date.
- FR-15: Connect two records and show their relationship.
- FR-16: Show related records for a selected record.
- FR-17: Browse memories using circular navigation.
- FR-18: Show high-priority records using a custom priority queue.
- FR-19: Undo supported recent actions using a custom stack.
- FR-20: Persist data in SQLite and reload it after restart.

## 7. Non-functional requirements
- NFR-01: Local-first; no internet connection required for normal use.
- NFR-02: GUI must be consistent and easy to navigate.
- NFR-03: Use parameterized SQL.
- NFR-04: Handle invalid input and unavailable file paths gracefully.
- NFR-05: Keep modules separated and code maintainable.
- NFR-06: Core Data Structures must be custom implementations.
- NFR-07: Application must not crash on empty database or no search results.
- NFR-08: Include unit tests for all ten structures and tests for core services.

## 8. Out of scope
- Cloud synchronization or online backup.
- AI-based tagging or recommendations.
- Legal will, inheritance or account-transfer functions.
- Sharing private vaults with other users.
- Mobile app or web app.
- Encryption claims unless separately designed, implemented and tested.

## 9. Acceptance criteria
The project is considered ready for demonstration when:
1. All three record types can be added, viewed, edited, archived and restored.
2. Search and filters return correct results.
3. Records persist after closing and reopening the app.
4. Timeline orders records by date.
5. Graph connections can be created and viewed.
6. Stack undo works for the explicitly supported actions.
7. Priority queue returns higher-priority records first.
8. Each of the ten custom Data Structures has independent unit tests.
9. The GUI has no blocking errors in the agreed demo workflow.
10. The team can explain the purpose, operations and complexity of each structure.
