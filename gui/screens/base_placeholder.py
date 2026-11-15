"""Base Placeholder Screen Component.

Owner: Anushka Samad
Purpose: Standardized card container for Phase 1 module placeholders,
         displaying module info, ownership, assigned data structure, and phase status.
"""

import customtkinter as ctk
from gui import theme
from gui.components.header import PageHeader


class BasePlaceholderScreen(ctk.CTkFrame):
    """Reusable placeholder frame for unintegrated module screens."""

    def __init__(
        self,
        master,
        title: str,
        subtitle: str,
        owner: str,
        data_structure: str,
        module_summary: str,
        **kwargs,
    ):
        super().__init__(master, fg_color=theme.COLOR_BACKGROUND, **kwargs)

        self.pack_propagate(True)

        # Header
        self.header = PageHeader(self, title=title, subtitle=subtitle)
        self.header.pack(fill="x", padx=28, pady=(24, 10))

        # Main Info Card
        card = ctk.CTkFrame(
            self,
            fg_color=theme.COLOR_SURFACE,
            corner_radius=theme.CORNER_RADIUS_CARD,
            border_width=1,
            border_color=theme.COLOR_SURFACE_ALT,
        )
        card.pack(fill="both", expand=True, padx=28, pady=(0, 24))

        # Status badge frame
        badge_frame = ctk.CTkFrame(card, fg_color="transparent")
        badge_frame.pack(fill="x", padx=theme.PADDING_CARD, pady=(theme.PADDING_CARD, 8))

        status_badge = ctk.CTkLabel(
            badge_frame,
            text=" PHASE 1: SHELL READY ",
            font=theme.FONT_BADGE,
            text_color=theme.COLOR_NAVY_PRIMARY,
            fg_color=theme.COLOR_LAVENDER_ACCENT,
            corner_radius=6,
        )
        status_badge.pack(side="left")

        owner_badge = ctk.CTkLabel(
            badge_frame,
            text=f" Owner: {owner} ",
            font=theme.FONT_BADGE,
            text_color=theme.COLOR_TEXT_LIGHT,
            fg_color=theme.COLOR_NAVY_PRIMARY,
            corner_radius=6,
        )
        owner_badge.pack(side="left", padx=(10, 0))

        # Content details
        content_frame = ctk.CTkFrame(card, fg_color="transparent")
        content_frame.pack(fill="both", expand=True, padx=theme.PADDING_CARD, pady=12)

        ds_title = ctk.CTkLabel(
            content_frame,
            text="Assigned Data Structure / Role",
            font=theme.FONT_BODY_BOLD,
            text_color=theme.COLOR_NAVY_PRIMARY,
            anchor="w",
        )
        ds_title.pack(fill="x", pady=(8, 2))

        ds_value = ctk.CTkLabel(
            content_frame,
            text=data_structure,
            font=theme.FONT_BODY,
            text_color=theme.COLOR_TEXT_SECONDARY,
            anchor="w",
        )
        ds_value.pack(fill="x", pady=(0, 12))

        summary_title = ctk.CTkLabel(
            content_frame,
            text="Module Scope & Overview",
            font=theme.FONT_BODY_BOLD,
            text_color=theme.COLOR_NAVY_PRIMARY,
            anchor="w",
        )
        summary_title.pack(fill="x", pady=(8, 2))

        summary_value = ctk.CTkLabel(
            content_frame,
            text=module_summary,
            font=theme.FONT_BODY,
            text_color=theme.COLOR_TEXT_SECONDARY,
            anchor="w",
            justify="left",
            wraplength=700,
        )
        summary_value.pack(fill="x", pady=(0, 16))

        # Ready state notice
        footer_notice = ctk.CTkLabel(
            content_frame,
            text="Ready for subsequent phase implementation. Core navigation and frame controllers are operational.",
            font=theme.FONT_CAPTION,
            text_color=theme.COLOR_TEXT_SECONDARY,
            anchor="w",
        )
        footer_notice.pack(fill="x", side="bottom", pady=(12, 0))
