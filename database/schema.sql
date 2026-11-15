-- LifeVault SQLite Database Schema
-- Persistent source of truth for all records and relationships

PRAGMA foreign_keys = ON;

-- Core records table
CREATE TABLE IF NOT EXISTS records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    record_type TEXT NOT NULL CHECK(record_type IN ('Memory', 'Document', 'Achievement')),
    title TEXT NOT NULL,
    category TEXT NOT NULL,
    record_date TEXT NOT NULL, -- Format: YYYY-MM-DD
    description TEXT DEFAULT '',
    file_path TEXT DEFAULT '',
    priority INTEGER NOT NULL DEFAULT 3 CHECK(priority BETWEEN 1 AND 5),
    archived INTEGER NOT NULL DEFAULT 0 CHECK(archived IN (0, 1)),
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

-- Undirected record connections table
-- Unique constraint prevents duplicate links regardless of direction
CREATE TABLE IF NOT EXISTS record_connections (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_id INTEGER NOT NULL,
    target_id INTEGER NOT NULL,
    relation_label TEXT DEFAULT '',
    FOREIGN KEY(source_id) REFERENCES records(id) ON DELETE CASCADE,
    FOREIGN KEY(target_id) REFERENCES records(id) ON DELETE CASCADE,
    CHECK(source_id <> target_id)
);

CREATE UNIQUE INDEX IF NOT EXISTS idx_connections_normalized
ON record_connections(
    MIN(source_id, target_id),
    MAX(source_id, target_id)
);

-- Optional activity log table
CREATE TABLE IF NOT EXISTS activity_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    action_type TEXT NOT NULL,
    record_id INTEGER,
    action_summary TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);
