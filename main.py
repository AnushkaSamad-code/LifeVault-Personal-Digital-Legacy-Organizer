"""LifeVault Application Entry Point.

Team:
- Anushka Samad (CSC-25F-083)
- Ubaid Raza (CSC-25F-013)

Course: Data Structures
Description: Desktop application for organizing personal digital legacies,
             powered by 10 custom in-memory data structures and SQLite persistence.
"""

import sys
from pathlib import Path

# Ensure project root is available on sys.path
PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from database.connection import DatabaseConnection
from gui.app import LifeVaultApp


def main() -> None:
    """Initialize database and launch the CustomTkinter GUI shell."""
    try:
        # Phase 1 scaffolding: initialize database schema if not present
        db_manager = DatabaseConnection()
        db_manager.initialize_schema()

        # Launch UI Shell
        app = LifeVaultApp()
        app.mainloop()
    except Exception as exc:
        print(f"Error launching LifeVault: {exc}", file=sys.stderr)
        raise exc


if __name__ == "__main__":
    main()
