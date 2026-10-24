"""Cover Letter of Ruth Okonkwo-Lane, four pages.

The long letter, with what Ruth would change in the first list.
"""
from content import DOCUMENT, PERSONA
from typesetting import typeset

DESIGN = {
    "accent": "#e63946",
    "ink": "#1b1b1b",
    "muted": "#6b4f3a",
    "page": "#fff4d6",
    "font": "Liberation Serif",
    "heading_font": "Liberation Sans Narrow",
    "header": "rule",
    "name_case": "lower",
    "display": 1.2,
    "heading": "plain",
    "heading_case": "lower",
    "bullet": "✶",
    "bullet_width": 14,
    "separator": " ~ ",
    "contact_join": "  ✶  ",
    "body_align": "justify",
    "footer": "ruth okonkwo-lane · a letter",
    "density": "spacious",
    "divider": "✶   ✶   ✶",
}


def fourpages():
    return typeset(PERSONA, DOCUMENT, DESIGN, 4)
