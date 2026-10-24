"""Curriculum Vitae of Maks Kovač, four pages.

The complete build log of a career, crashes included.
"""
from content import DOCUMENT, PERSONA
from typesetting import typeset

DESIGN = {
    "accent": "#ff2fd0",
    "ink": "#e9d5ff",
    "muted": "#22d3ee",
    "page": "#14002b",
    "font": "TeX Gyre Adventor",
    "header": "frame",
    "name_case": "upper",
    "heading": "box",
    "heading_case": "upper",
    "heading_format": "◢ {title} ◣",
    "bullet": "◆",
    "bullet_width": 14,
    "separator": " // ",
    "contact_join": "  //  ",
    "body_align": "start",
    "footer": "MAKS KOVAČ // CV // RENDERED AT 90 FPS",
    "density": "spacious",
    "divider": "▲ ▼ ▲ ▼ ▲ ▼ ▲",
}


def fourpages():
    return typeset(PERSONA, DOCUMENT, DESIGN, 4)
