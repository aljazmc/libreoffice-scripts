"""Artist Statement of Ruth Okonkwo-Lane, four pages.

The full statement, including the year the machines came.
"""
from content import DOCUMENT, PERSONA
from typesetting import typeset

DESIGN = {
    "accent": "#2a9d8f",
    "ink": "#1b1b1b",
    "muted": "#264653",
    "page": "#fff4d6",
    "font": "Liberation Serif",
    "heading_font": "Liberation Sans Narrow",
    "header": "bar",
    "name_case": "lower",
    "display": 1,
    "heading": "center",
    "bullet": "✶",
    "bullet_width": 14,
    "separator": " ~ ",
    "contact_join": "  ✶  ",
    "body_align": "start",
    "divider": "✶   ✶   ✶",
    "footer": "artist statement · ruth okonkwo-lane",
    "density": "spacious",
}


def fourpages():
    return typeset(PERSONA, DOCUMENT, DESIGN, 4)
