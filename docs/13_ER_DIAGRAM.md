# LifeVault — Entity Relationship Diagram

## 1. Purpose

This document describes the persistent relational data model for LifeVault, a single-user offline personal digital legacy organizer. It accompanies `13_ER_DIAGRAM.puml` and its rendered `13_ER_DIAGRAM.png`.

## 2. Database overview

SQLite is the persistent source of truth. The approved SRS schema contains exactly two tables: `records` and `record_connections`. Record categories are text paths in `records.category`; there is no persistent category table. The Graph, Stack, Queue, trees, lists, arrays, and indexes are in-memory data structures and are not database entities. Local files remain outside SQLite; only their path strings are stored.

## 3. Entities and attributes

### `records`

Stores Memory, Document, and Achievement entries, distinguished by `record_type`.

| Attribute | Type | Key / constraint | Meaning |
|---|---|---|---|
| `id` | INTEGER | PK, AUTOINCREMENT | Unique record identifier. |
| `record_type` | TEXT | NOT NULL; CHECK in Memory, Document, Achievement | Record type discriminator. |
| `title` | TEXT | NOT NULL | Record title. |
| `category` | TEXT | NOT NULL | Category or hierarchical category path. |
| `record_date` | TEXT | NOT NULL in SRS; ISO date YYYY-MM-DD | Date associated with the entry. |
| `description` | TEXT | DEFAULT '' | Narrative or notes. |
| `file_path` | TEXT | DEFAULT '' | Optional local path to an externally stored file. |
| `priority` | INTEGER | NOT NULL; DEFAULT 3; CHECK 1–5 | Importance rating. |
| `archived` | INTEGER | NOT NULL; DEFAULT 0; CHECK 0 or 1 | Soft-archive status. |
| `created_at` | TEXT | NOT NULL | Creation timestamp. |

### `record_connections`

Associative entity storing an undirected relationship between two records as a single normalized row.

| Attribute | Type | Key / constraint | Meaning |
|---|---|---|---|
| `id` | INTEGER | PK, AUTOINCREMENT | Unique connection row identifier. |
| `source_id` | INTEGER | FK to `records.id`; NOT NULL; ON DELETE CASCADE | Lower identifier in the normalized pair. |
| `target_id` | INTEGER | FK to `records.id`; NOT NULL; ON DELETE CASCADE | Higher identifier in the normalized pair. |
| `relation_label` | TEXT | DEFAULT '' | Optional relationship annotation. |

## 4. Primary and foreign keys

Each table has its own integer autoincrement primary key (`records.id` and `record_connections.id`). `record_connections.source_id` and `record_connections.target_id` are separate foreign keys to `records.id`. SQLite foreign-key enforcement is enabled by the application (`PRAGMA foreign_keys = ON`). Deleting a referenced record cascades to its connection rows as specified by the SRS.

## 5. Relationships and cardinality

- A record may be referenced by zero or many connection rows in the **source** role. Each connection row has exactly one source record.
- A record may be referenced by zero or many connection rows in the **target** role. Each connection row has exactly one target record.
- Taken together, the two role relationships model an undirected record-to-record network. The connection table is the associative entity between records; the same record pair is stored once. It is not modeled as two persisted directed edges.
- A self-link is excluded by `source_id < target_id`.

## 6. Constraints and assumptions

The SRS specifies `UNIQUE(source_id, target_id)` together with `CHECK(source_id < target_id)`. The ordering constraint canonicalizes each undirected pair, so the uniqueness constraint also prevents duplicate and reversed copies. Both endpoint columns are NOT NULL foreign keys with cascading deletion. The diagram marks defaults and checks specified by the SRS. No unsupported subtype tables, category table, activity log, or in-memory structure is included.

### Unresolved documentation discrepancy

`docs/05_DATABASE_SCHEMA.md` describes `record_date` as optional and does not list an SQL `NOT NULL` constraint. The approved SRS §6.2 specifies `record_date TEXT NOT NULL`, and its record workflows require a date. Following the SRS authority rule, the diagram uses `NOT NULL`; the implementation should be checked against that baseline if the exact deployed DDL is needed. The SRS describes ISO date format but does not explicitly define a SQL `CHECK` for the format, so no such database check is asserted here. Some defaults in the database overview are also not labeled `NOT NULL`; the diagram does not infer non-nullability from a default.

## 7. Schema confirmation

The diagram represents the two persistent SQLite tables and the columns, keys, references, relationship roles, and explicit constraints documented in the approved SRS and database schema documentation. It reflects LifeVault's single-user offline architecture and excludes runtime-only data structures. Aside from the documented `record_date` discrepancy, no additional schema element is introduced.
