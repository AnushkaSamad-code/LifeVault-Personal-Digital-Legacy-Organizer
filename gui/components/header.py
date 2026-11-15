"""Page Header Component.

Owner: Anushka Samad
Purpose: Consistent top header showing screen title, subtitle, and optional action badges.
"""

import customtkinter as ctk
from gui import theme


class PageHeader(ctk.CTkFrame):
    """Reusable header frame for LifeVault screens."""

    def __init__(self, master, title: str, subtitle: str, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.title_label = ctk.CTkLabel(
            self,
            text=title,
            font=theme.FONT_TITLE,
            text_color=theme.COLOR_TEXT_PRIMARY,
            anchor="w",
        )
        self.title_label.pack(fill="x", padx=0, pady=(0, 2))

        self.subtitle_label = ctk.CTkLabel(
            self,
            text=subtitle,
            font=theme.FONT_SUBTITLE,
            text_color=theme.COLOR_TEXT_SECONDARY,
            anchor="w",
        )
        self.subtitle_label.pack(fill="x", padx=0, pady=(0, 15))
