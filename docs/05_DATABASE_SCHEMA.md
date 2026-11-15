# Database Design — SQLite

## Design principle
SQLite stores permanent records. The custom Data Structures are rebuilt from persisted data when the application starts.

## Table: records
| Column | Type | Rule |
|---|---|---|
| id | INTEGER | Primary key, autoincrement |
| record_type | TEXT | NOT NULL; Memory/Document/Achievement |
| title | TEXT | NOT NULL |
| category | TEXT | NOT NULL |
| record_date | TEXT | ISO date YYYY-MM-DD |
| description | TEXT | Optional, default empty |
| file_path | TEXT | Optional local path |
| priority | INTEGER | 1–5, default 3 |
| archived | INTEGER | 0 or 1, default 0 |
| created_at | TEXT | Timestamp |

## Table: record_connections
| Column | Type | Rule |
|---|---|---|
| id | INTEGER | Primary key |
| source_id | INTEGER | Foreign key to records.id |
| target_id | INTEGER | Foreign key to records.id |
| relation_label | TEXT | Optional description |

Add a uniqueness rule for each normalized pair so duplicate links cannot be inserted. Store each undirected edge once in the database; the Graph class should add both adjacency directions in memory.

## Optional table: activity_log
Use only if needed for recent activity and undo audit:
- id
- action_type
- record_id
- action_summary
- created_at

## Database rules
- Enable foreign keys using `PRAGMA foreign_keys = ON`.
- Use parameterized queries.
- Validate record type and priority in application code and, where suitable, SQL CHECK constraints.
- Use transactions for multi-step operations.
- Do not store binary files in SQLite for this medium project; store file paths and explain that moving a file can make its path unavailable.
- Define what happens to connections when a record is permanently deleted (cascade delete or explicit cleanup).
