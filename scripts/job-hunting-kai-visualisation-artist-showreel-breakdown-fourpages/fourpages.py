"""Showreel Breakdown of Kai Berg, four pages.

Every shot, every tool and the work cut from the reel.
"""
from content import DOCUMENT, PERSONA
from typesetting import typeset

DESIGN = {
    "accent": "#fde68a",
    "ink": "#e6f0ff",
    "muted": "#fcd34d",
    "page": "#0f2a5f",
    "font": "Liberation Sans",
    "heading_font": "Noto Sans Mono",
    "header": "rule",
    "name_case": "upper",
    "heading": "box",
    "heading_case": "upper",
    "heading_format": "TC {number:02d}:00 · {title}",
    "bullet": "+",
    "separator": " — ",
    "contact_join": "   |   ",
    "footer": "SHEET R-01 · SHOWREEL BREAKDOWN",
    "density": "spacious",
    "divider": "▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸",
}


def fourpages():
    return typeset(PERSONA, DOCUMENT, DESIGN, 4)
