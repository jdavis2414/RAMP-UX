"""
mui_circular_spinner.py
───────────────────────
Material UI CircularProgress — primary colour, indeterminate only.

Two layout variants
───────────────────
  MuiCircularSpinner          — standalone ring (centred)
  MuiCircularSpinnerInline    — ring + label on a single row

Usage
─────
    from mui_circular_spinner import MuiCircularSpinner, MuiCircularSpinnerInline

    # Standalone
    spinner = MuiCircularSpinner(size="medium")
    page.add(spinner.build())
    spinner.show()

    # Inline
    inline = MuiCircularSpinnerInline(label="Saving changes…")
    page.add(inline.build())
    inline.set_label("Upload complete")
    inline.hide()

Run this file for a live demo:
    python mui_circular_spinner.py
"""

from __future__ import annotations
import flet as ft

# ── MUI default primary token ─────────────────────────────────────────────────
_PRIMARY       = "#1976d2"
_PRIMARY_TRACK = "#c8e0f7"

# ── Size presets (diameter px, stroke width px) ───────────────────────────────
_SIZES: dict[str, tuple[int, float]] = {
    "small":  (20, 2.5),
    "medium": (40, 3.6),
    "large":  (56, 4.5),
}


# ─────────────────────────────────────────────────────────────────────────────
# Standalone spinner
# ─────────────────────────────────────────────────────────────────────────────

class MuiCircularSpinner:
    """
    Primary-colour indeterminate circular spinner.

    Parameters
    ----------
    size : "small" | "medium" | "large"  (default "medium")
    """

    def __init__(self, size: str = "medium"):
        diameter, stroke = _SIZES.get(size, _SIZES["medium"])
        self._ring = ft.ProgressRing(
            value=None,
            width=diameter,
            height=diameter,
            color=_PRIMARY,
            bgcolor=_PRIMARY_TRACK,
            stroke_width=stroke,
            visible=False,
        )

    def build(self) -> ft.Control:
        return self._ring

    def show(self) -> None:
        self._ring.visible = True
        self._ring.update()

    def hide(self) -> None:
        self._ring.visible = False
        self._ring.update()


# ─────────────────────────────────────────────────────────────────────────────
# Inline spinner (ring + label on one row)
# ─────────────────────────────────────────────────────────────────────────────

class MuiCircularSpinnerInline:
    """
    Primary-colour indeterminate spinner with a text label on the same row.

    Parameters
    ----------
    label    : str   — text shown to the right of the ring
    size     : "small" | "medium" | "large"  (default "small" — suits inline use)
    spacing  : int   — gap between ring and label in px  (default 10)
    """

    def __init__(
        self,
        label: str = "Loading…",
        size: str = "small",
        spacing: int = 10,
    ):
        diameter, stroke = _SIZES.get(size, _SIZES["small"])

        self._ring = ft.ProgressRing(
            value=None,
            width=diameter,
            height=diameter,
            color=_PRIMARY,
            bgcolor=_PRIMARY_TRACK,
            stroke_width=stroke,
        )

        # font-size scales with the ring so they feel balanced
        font_size = {20: 13, 40: 14, 56: 16}.get(diameter, 13)

        self._label = ft.Text(
            value=label,
            size=font_size,
            color="#00000099",       # MUI text.secondary
            weight=ft.FontWeight.W_400,
        )

        self._row = ft.Row(
            controls=[self._ring, self._label],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=spacing,
            visible=False,
        )

    def build(self) -> ft.Control:
        return self._row

    def show(self) -> None:
        self._row.visible = True
        self._row.update()

    def hide(self) -> None:
        self._row.visible = False
        self._row.update()

    def set_label(self, text: str) -> None:
        self._label.value = text
        self._label.update()


# ─────────────────────────────────────────────────────────────────────────────
# Demo
# ─────────────────────────────────────────────────────────────────────────────

import asyncio

def main(page: ft.Page):
    page.title   = "MUI Circular Spinner — demo"
    page.bgcolor = "#ffffff"
    page.padding = 40
    page.theme   = ft.Theme(font_family="Inter")

    def label(text: str) -> ft.Text:
        return ft.Text(text, size=11, color="#00000060",
                       weight=ft.FontWeight.W_600)

    # ── standalone ────────────────────────────────────────────────────────────
    sm  = MuiCircularSpinner(size="small")
    md  = MuiCircularSpinner(size="medium")
    lg  = MuiCircularSpinner(size="large")

    standalone_row = ft.Row(
        controls=[
            ft.Column([sm.build(), label("small")],
                      horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=6),
            ft.Column([md.build(), label("medium")],
                      horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=6),
            ft.Column([lg.build(), label("large")],
                      horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=6),
        ],
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=32,
    )

    # ── inline ────────────────────────────────────────────────────────────────
    inline_sm  = MuiCircularSpinnerInline(label="Validating…",      size="small")
    inline_md  = MuiCircularSpinnerInline(label="Uploading file…",  size="medium")
    inline_lg  = MuiCircularSpinnerInline(label="Processing data…", size="large")

    inline_col = ft.Column(
        controls=[inline_sm.build(), inline_md.build(), inline_lg.build()],
        spacing=20,
    )

    page.add(
        ft.Text("Standalone", size=13, weight=ft.FontWeight.W_500, color="#000000de"),
        ft.Container(content=standalone_row, padding=ft.padding.symmetric(vertical=12)),
        ft.Divider(height=1, color="#e0e0e0"),
        ft.Container(height=8),
        ft.Text("Inline", size=13, weight=ft.FontWeight.W_500, color="#000000de"),
        ft.Container(content=inline_col, padding=ft.padding.symmetric(vertical=12)),
    )

    # reveal all after a short delay so the animation is visibly spinning on load
    async def reveal():
        await asyncio.sleep(0.1)
        for s in [sm, md, lg, inline_sm, inline_md, inline_lg]:
            s.show()

    page.run_task(reveal)


if __name__ == "__main__":
    ft.app(target=main)
