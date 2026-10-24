"""Cover Letter of Maks Kovač, two pages.

Why a failed founder wants to build simulators for surgeons.
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


def twopages():
    return typeset(PERSONA, DOCUMENT, DESIGN, 2)
