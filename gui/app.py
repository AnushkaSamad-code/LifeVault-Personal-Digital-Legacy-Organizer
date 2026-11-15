"""Application Shell and Navigation Controller.

Owner: Anushka Samad
Purpose: Main application window implementing responsive layout,
         Navy & Lavender theme styling, sidebar navigation, and screen switching.
"""

from typing import Dict, Type
import customtkinter as ctk

from gui import theme
from gui.components.sidebar import Sidebar
from gui.screens.dashboard import DashboardScreen
from gui.screens.memory_vault import MemoryVaultScreen
from gui.screens.document_vault import DocumentVaultScreen
from gui.screens.achievement_vault import AchievementVaultScreen
from gui.screens.timeline import TimelineScreen
from gui.screens.connections import ConnectionsScreen
from gui.screens.category_manager import CategoryManagerScreen
from gui.screens.priority_vault import PriorityVaultScreen
from gui.screens.archive import ArchiveScreen
from gui.screens.search import SearchScreen
from gui.screens.about import AboutScreen


class LifeVaultApp(ctk.CTk):
    """Main LifeVault desktop application shell."""

    def __init__(self):
        super().__init__()

        # Appearance configuration
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        # Window setup
        self.title("LifeVault — Personal Digital Legacy Organizer")
        self.geometry(f"{theme.WINDOW_MIN_WIDTH}x{theme.WINDOW_MIN_HEIGHT}")
        self.minsize(theme.WINDOW_MIN_WIDTH, theme.WINDOW_MIN_HEIGHT)
        self.configure(fg_color=theme.COLOR_BACKGROUND)

        # Configure root grid weights: column 0 is fixed sidebar, column 1 expands
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        # Active screens registry
        self.screens: Dict[str, ctk.CTkFrame] = {}
        self.current_screen_key: str = "dashboard"

        # Screen class mapping for the 10 core modules + optional about
        self.screen_classes: Dict[str, Type[ctk.CTkFrame]] = {
            "dashboard": DashboardScreen,
            "memory_vault": MemoryVaultScreen,
            "document_vault": DocumentVaultScreen,
            "achievement_vault": AchievementVaultScreen,
            "timeline": TimelineScreen,
            "connections": ConnectionsScreen,
            "category_manager": CategoryManagerScreen,
            "priority_vault": PriorityVaultScreen,
            "archive": ArchiveScreen,
            "search": SearchScreen,
            "about": AboutScreen,
        }

        # Setup Layout
        self._build_sidebar()
        self._build_content_area()

        # Show initial screen (Dashboard)
        self.show_screen("dashboard")

    def _build_sidebar(self) -> None:
        """Create and place the persistent navigation sidebar."""
        self.sidebar = Sidebar(self, on_navigate=self.show_screen)
        self.sidebar.grid(row=0, column=0, sticky="nsew")

    def _build_content_area(self) -> None:
        """Create the central dynamic content frame."""
        self.content_container = ctk.CTkFrame(
            self,
            fg_color=theme.COLOR_BACKGROUND,
            corner_radius=0,
        )
        self.content_container.grid(row=0, column=1, sticky="nsew")
        self.content_container.grid_rowconfigure(0, weight=1)
        self.content_container.grid_columnconfigure(0, weight=1)

    def show_screen(self, screen_key: str) -> None:
        """Switch current view to the requested screen key."""
        if screen_key not in self.screen_classes:
            return

        # Lazy instantiation of screens
        if screen_key not in self.screens:
            screen_class = self.screen_classes[screen_key]
            instance = screen_class(self.content_container)
            self.screens[screen_key] = instance
            instance.grid(row=0, column=0, sticky="nsew")

        # Raise the selected screen to the front
        target_screen = self.screens[screen_key]
        target_screen.tkraise()
        self.current_screen_key = screen_key
        self.sidebar.set_active(screen_key)
