"""Curriculum Vitae of Kai Berg, four pages.

The full set of drawings, with the stories in the margins.
"""
from content import DOCUMENT, PERSONA
from typesetting import typeset

DESIGN = {
    "accent": "#7dd3fc",
    "ink": "#e6f0ff",
    "muted": "#9db8e8",
    "page": "#0f2a5f",
    "font": "Liberation Sans",
    "heading_font": "Noto Sans Mono",
    "header": "rule",
    "name_case": "upper",
    "heading": "box",
    "heading_case": "upper",
    "heading_format": "{number:02d} / {title}",
    "bullet": "+",
    "separator": " — ",
    "contact_join": "   |   ",
    "footer": "SHEET A-01 · KAI BERG · CV",
    "density": "spacious",
    "divider": "┼──────────────┼──────────────┼",
}


def fourpages():
    return typeset(PERSONA, DOCUMENT, DESIGN, 4)
