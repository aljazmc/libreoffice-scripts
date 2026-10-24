"""Sound Portfolio of Yuki Mori, four pages.

The full album, including the sounds that were cut.
"""
from content import DOCUMENT, PERSONA
from typesetting import typeset

DESIGN = {
    "accent": "#1e3a8a",
    "ink": "#2b2118",
    "muted": "#64748b",
    "page": "#fbf7ee",
    "font": "TeX Gyre Schola",
    "header": "centered",
    "heading": "center",
    "heading_format": "Track {number:02d} · {title}",
    "divider": "𝄞",
    "bullet": "♪",
    "bullet_width": 14,
    "separator": " · ",
    "contact_join": "  ·  ",
    "margin": 62,
    "footer": "Yuki Mori · sound portfolio · please listen with headphones",
    "density": "spacious",
}


def fourpages():
    return typeset(PERSONA, DOCUMENT, DESIGN, 4)
