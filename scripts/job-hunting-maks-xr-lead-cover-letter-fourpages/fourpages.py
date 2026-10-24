"""Cover Letter of Maks Kovač, four pages.

The long letter with a first prototype idea.
"""
from content import DOCUMENT, PERSONA
from typesetting import typeset

DESIGN = {
    "accent": "#ff2fd0",
    "ink": "#e9d5ff",
    "muted": "#22d3ee",
    "page": "#14002b",
    "font": "TeX Gyre Adventor",
    "header": "rule",
    "name_case": "upper",
    "heading": "plain",
    "heading_case": "upper",
    "heading_format": "▸ {title}",
    "bullet": "◆",
    "bullet_width": 14,
    "separator": " // ",
    "contact_join": "  //  ",
    "body_align": "start",
    "footer": "MAKS KOVAČ // LETTER",
    "density": "spacious",
}


def fourpages():
    return typeset(PERSONA, DOCUMENT, DESIGN, 4)
