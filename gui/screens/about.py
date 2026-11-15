"""About & Project Identity Screen.

Status: Optional screen outside the 10 core functional modules.
"""

import customtkinter as ctk
from gui import theme
from gui.components.header import PageHeader


class AboutScreen(ctk.CTkFrame):
    """Information view displaying project identity, developers, and architecture."""

    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color=theme.COLOR_BACKGROUND, **kwargs)

        self.header = PageHeader(
            self,
            title="About LifeVault",
            subtitle="Personal Digital Legacy Organizer — Data Structures Course Project",
        )
        self.header.pack(fill="x", padx=28, pady=(24, 10))

        card = ctk.CTkFrame(
            self,
            fg_color=theme.COLOR_SURFACE,
            corner_radius=theme.CORNER_RADIUS_CARD,
            border_width=1,
            border_color=theme.COLOR_SURFACE_ALT,
        )
        card.pack(fill="both", expand=True, padx=28, pady=(0, 24))

        inner = ctk.CTkFrame(card, fg_color="transparent")
        inner.pack(fill="both", expand=True, padx=theme.PADDING_CARD, pady=theme.PADDING_CARD)

        team_title = ctk.CTkLabel(
            inner,
            text="Development Team & Ownership",
            font=theme.FONT_SECTION,
            text_color=theme.COLOR_NAVY_PRIMARY,
            anchor="w",
        )
        team_title.pack(fill="x", pady=(0, 10))

        anushka_info = (
            "• Anushka Samad (CSC-25F-083):\n"
            "   Modules: Dashboard, Memory Vault, Life Timeline, Memory Connections, Category Manager\n"
            "   Data Structures: Dynamic Array, Singly Linked List, Circular Linked List, Graph, General Tree\n"
            "   Foundation: UI Theme, Navigation Shell, Sidebar, and Screen Scaffolding"
        )
        ctk.CTkLabel(
            inner,
            text=anushka_info,
            font=theme.FONT_BODY,
            text_color=theme.COLOR_TEXT_PRIMARY,
            anchor="w",
            justify="left",
        ).pack(fill="x", pady=(0, 12))

        ubaid_info = (
            "• Ubaid Raza (CSC-25F-013):\n"
            "   Modules: Document Vault, Achievement Vault, Smart Search, Priority Vault, Archive & Undo\n"
            "   Data Structures: Binary Search Tree, Hash Table, Max Heap / Priority Queue, Stack, Queue (FIFO Processor)\n"
            "   Foundation: Environment, Dependencies, .gitignore, and Database Connection Scaffolding"
        )
        ctk.CTkLabel(
            inner,
            text=ubaid_info,
            font=theme.FONT_BODY,
            text_color=theme.COLOR_TEXT_PRIMARY,
            anchor="w",
            justify="left",
        ).pack(fill="x", pady=(0, 16))

        arch_title = ctk.CTkLabel(
            inner,
            text="Architecture Principles",
            font=theme.FONT_SECTION,
            text_color=theme.COLOR_NAVY_PRIMARY,
            anchor="w",
        )
        arch_title.pack(fill="x", pady=(8, 4))

        arch_info = (
            "1. Presentation Layer (CustomTkinter) communicates solely via the Service Layer.\n"
            "2. Service Layer coordinates both Repositories (SQLite persistence) and Custom Data Structures (in-memory indexing).\n"
            "3. SQLite is the permanent source of truth; in-memory data structures are populated and rebuilt on startup.\n"
            "4. All ten custom data structures are manually implemented in Python without built-in shortcut libraries."
        )
        ctk.CTkLabel(
            inner,
            text=arch_info,
            font=theme.FONT_BODY,
            text_color=theme.COLOR_TEXT_SECONDARY,
            anchor="w",
            justify="left",
        ).pack(fill="x", pady=(0, 8))
