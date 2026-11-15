"""Phase 1 Verification Tests.

Verifies:
1. Database schema initialization and table creation.
2. CustomTkinter application shell instantiation.
3. Sidebar registration of all 10 core functional modules + optional about screen.
4. Screen switching across all registered screens without exception.
"""

import sys
from pathlib import Path
import sqlite3

# Ensure project root is in path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from database.connection import DatabaseConnection
from gui.app import LifeVaultApp
from gui.components.sidebar import CORE_NAV_ITEMS


def test_database_initialization(tmp_path: Path):
    """Verify schema initialization creates expected tables and PRAGMA settings."""
    test_db = tmp_path / "test_lifevault.db"
    db_mgr = DatabaseConnection(db_path=test_db)
    db_mgr.initialize_schema()

    assert test_db.exists(), "Database file was not created"

    conn = db_mgr.get_connection()
    cursor = conn.cursor()

    # Query sqlite_master to verify tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = {row["name"] for row in cursor.fetchall()}

    assert "records" in tables, "Table 'records' missing"
    assert "record_connections" in tables, "Table 'record_connections' missing"
    assert "activity_log" in tables, "Table 'activity_log' missing"

    # Verify foreign keys are enabled
    cursor.execute("PRAGMA foreign_keys;")
    fk_status = cursor.fetchone()[0]
    assert fk_status == 1, "Foreign keys PRAGMA not enabled"

    conn.close()
    print("[PASS] Database schema initialization verified.")


def test_app_shell_and_navigation():
    """Verify GUI shell creation and switching across all 10 core screens + about."""
    app = LifeVaultApp()

    # Verify all 10 core items are in CORE_NAV_ITEMS
    assert len(CORE_NAV_ITEMS) == 10, f"Expected 10 core modules, found {len(CORE_NAV_ITEMS)}"

    expected_keys = [
        "dashboard",
        "memory_vault",
        "document_vault",
        "achievement_vault",
        "timeline",
        "connections",
        "category_manager",
        "priority_vault",
        "archive",
        "search",
    ]

    for key, label, owner in CORE_NAV_ITEMS:
        assert key in expected_keys, f"Unexpected key {key} in core items"
        assert key in app.screen_classes, f"Screen {key} not registered in LifeVaultApp"

    # Verify Category Manager is present in core items and Settings/About is optional
    core_keys = [item[0] for item in CORE_NAV_ITEMS]
    assert "category_manager" in core_keys, "Category Manager must be in 10 core modules"
    assert "about" not in core_keys, "About/Settings must be outside the 10 core modules"

    # Test cycling through all screens
    all_keys = core_keys + ["about"]
    for key in all_keys:
        app.show_screen(key)
        app.update()
        assert app.current_screen_key == key, f"Failed to switch to {key}"
        assert key in app.screens, f"Screen instance for {key} was not created"

    # Cleanly destroy app instance
    app.destroy()
    print("[PASS] Application shell, 10 core modules, and navigation verified.")


if __name__ == "__main__":
    import tempfile
    import shutil

    temp_dir = Path(tempfile.mkdtemp())
    try:
        test_database_initialization(temp_dir)
        test_app_shell_and_navigation()
        print("\nAll Phase 1 verification tests passed successfully!")
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)
