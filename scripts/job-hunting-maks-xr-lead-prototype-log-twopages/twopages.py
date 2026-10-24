"""Prototype Log of Maks Kovač, two pages.

Seven prototypes, each with what it proved or killed.
"""
from content import DOCUMENT, PERSONA
from typesetting import typeset

DESIGN = {
    "accent": "#22d3ee",
    "ink": "#e9d5ff",
    "muted": "#ff2fd0",
    "page": "#14002b",
    "font": "TeX Gyre Adventor",
    "header": "frame",
    "name_case": "upper",
    "heading": "box",
    "heading_case": "upper",
    "heading_format": "PROTO-{number:03d} · {title}",
    "bullet": "◆",
    "bullet_width": 14,
    "separator": " // ",
    "contact_join": "  //  ",
    "body_align": "start",
    "footer": "PROTOTYPE LOG // MAKS KOVAČ",
}


def twopages():
    return typeset(PERSONA, DOCUMENT, DESIGN, 2)
