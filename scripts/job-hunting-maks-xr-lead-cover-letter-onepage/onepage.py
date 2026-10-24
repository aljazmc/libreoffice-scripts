"""Cover Letter of Maks Kovač, one page.

A neon letter to a surgical training company.
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
}


def onepage():
    return typeset(PERSONA, DOCUMENT, DESIGN, 1)
