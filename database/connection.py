"""Database Connection Management.

Owner: Ubaid Raza
Purpose: Provides thread-safe connection handling and schema initialization
         for the SQLite persistent store.
"""

from pathlib import Path
import sqlite3
from typing import Optional

DEFAULT_DB_PATH = Path(__file__).resolve().parent.parent / "lifevault.db"
SCHEMA_PATH = Path(__file__).resolve().parent / "schema.sql"


class DatabaseConnection:
    """Manages SQLite database connections and schema setup."""

    def __init__(self, db_path: Optional[Path] = None):
        self.db_path = db_path or DEFAULT_DB_PATH

    def get_connection(self) -> sqlite3.Connection:
        """Create and return a configured sqlite3 connection."""
        conn = sqlite3.connect(str(self.db_path))
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn

    def initialize_schema(self) -> None:
        """Execute schema.sql to ensure all required tables exist."""
        if not SCHEMA_PATH.exists():
            raise FileNotFoundError(f"Schema file missing at: {SCHEMA_PATH}")

        with open(SCHEMA_PATH, "r", encoding="utf-8") as schema_file:
            script = schema_file.read()

        with self.get_connection() as conn:
            conn.executescript(script)
            conn.commit()
