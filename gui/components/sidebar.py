"""Sidebar Navigation Component.

Owner: Anushka Samad
Purpose: Persistent left sidebar containing the 10 core functional modules,
         clean active-tab highlights, and an optional bottom About view.
"""

from typing import Callable, Dict
import customtkinter as ctk
from gui import theme

# The 10 Core Functional Modules in requested order
CORE_NAV_ITEMS = [
    ("dashboard", "Dashboard", "Anushka"),
    ("memory_vault", "Memory Vault", "Anushka"),
    ("document_vault", "Document Vault", "Ubaid"),
    ("achievement_vault", "Achievement Vault", "Ubaid"),
    ("timeline", "Life Timeline", "Anushka"),
    ("connections", "Memory Connections", "Anushka"),
    ("category_manager", "Category Manager", "Anushka"),
    ("priority_vault", "Priority Vault", "Ubaid"),
    ("archive", "Archive & Undo", "Ubaid"),
    ("search", "Smart Search", "Ubaid"),
]


class Sidebar(ctk.CTkFrame):
    """Persistent sidebar navigation for LifeVault."""

    def __init__(self, master, on_navigate: Callable[[str], None], **kwargs):
        super().__init__(
            master,
            width=theme.SIDEBAR_WIDTH,
            fg_color=theme.COLOR_NAVY_PRIMARY,
            corner_radius=0,
            **kwargs,
        )
        self.on_navigate = on_navigate
        self.nav_buttons: Dict[str, ctk.CTkButton] = {}
        self.active_key: str = "dashboard"

        # Prevent frame from shrinking below specified width
        self.grid_propagate(False)

        self._build_header()
        self._build_nav_links()
        self._build_footer()

    def _build_header(self) -> None:
        """Render the branding header with title and subtitle."""
        header_frame = ctk.CTkFrame(self, fg_color="transparent")
        header_frame.pack(fill="x", padx=16, pady=(20, 15))

        title = ctk.CTkLabel(
            header_frame,
            text="LifeVault",
            font=(theme.FONT_FAMILY, 20, "bold"),
            text_color=theme.COLOR_TEXT_LIGHT,
            anchor="w",
        )
        title.pack(fill="x")

        subtitle = ctk.CTkLabel(
            header_frame,
            text="Personal Legacy Organizer",
            font=theme.FONT_CAPTION,
            text_color=theme.COLOR_LAVENDER_ACCENT,
            anchor="w",
        )
        subtitle.pack(fill="x", pady=(2, 0))

        # Thin divider
        divider = ctk.CTkFrame(
            self,
            height=1,
            fg_color=theme.COLOR_NAVY_SECONDARY,
        )
        divider.pack(fill="x", padx=14, pady=(0, 10))

    def _build_nav_links(self) -> None:
        """Render navigation buttons for all 10 core functional modules."""
        scroll_frame = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent",
            scrollbar_button_color=theme.COLOR_NAVY_SECONDARY,
            scrollbar_button_hover_color=theme.COLOR_LAVENDER_ACCENT,
        )
        scroll_frame.pack(fill="both", expand=True, padx=8, pady=0)

        for key, label, owner in CORE_NAV_ITEMS:
            btn = ctk.CTkButton(
                scroll_frame,
                text=label,
                font=theme.FONT_BODY,
                anchor="w",
                height=34,
                corner_radius=theme.CORNER_RADIUS_BUTTON,
                fg_color="transparent",
                text_color=theme.COLOR_TEXT_LIGHT,
                hover_color=theme.COLOR_NAVY_SECONDARY,
                command=lambda k=key: self._handle_click(k),
            )
            btn.pack(fill="x", padx=4, pady=2)
            self.nav_buttons[key] = btn

    def _build_footer(self) -> None:
        """Render the optional 'About' button and project info footer outside the 10 core modules."""
        footer_frame = ctk.CTkFrame(self, fg_color="transparent")
        footer_frame.pack(fill="x", side="bottom", padx=8, pady=(8, 14))

        divider = ctk.CTkFrame(
            footer_frame,
            height=1,
            fg_color=theme.COLOR_NAVY_SECONDARY,
        )
        divider.pack(fill="x", padx=6, pady=(0, 8))

        # Optional About / Settings button
        about_btn = ctk.CTkButton(
            footer_frame,
            text="About LifeVault",
            font=theme.FONT_CAPTION,
            anchor="w",
            height=28,
            corner_radius=theme.CORNER_RADIUS_BUTTON,
            fg_color="transparent",
            text_color=theme.COLOR_LAVENDER_ACCENT,
            hover_color=theme.COLOR_NAVY_SECONDARY,
            command=lambda: self._handle_click("about"),
        )
        about_btn.pack(fill="x", padx=4, pady=(0, 4))
        self.nav_buttons["about"] = about_btn

    def _handle_click(self, key: str) -> None:
        """Handle button click and highlight the active item."""
        self.set_active(key)
        self.on_navigate(key)

    def set_active(self, key: str) -> None:
        """Update button styles to indicate the active screen."""
        self.active_key = key
        for k, btn in self.nav_buttons.items():
            if k == key:
                btn.configure(
                    fg_color=theme.COLOR_NAVY_SECONDARY,
                    text_color=theme.COLOR_LAVENDER_ACCENT,
                    font=theme.FONT_BODY_BOLD,
                )
            else:
                btn.configure(
                    fg_color="transparent",
                    text_color=theme.COLOR_TEXT_LIGHT if k != "about" else theme.COLOR_LAVENDER_ACCENT,
                    font=theme.FONT_BODY if k != "about" else theme.FONT_CAPTION,
                )
