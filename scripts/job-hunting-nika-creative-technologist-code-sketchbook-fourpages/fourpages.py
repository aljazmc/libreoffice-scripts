"""Code Sketchbook of Nika Zupan, four pages.

The whole sketchbook, including the ones that crashed.
"""
from content import DOCUMENT, PERSONA
from typesetting import typeset

DESIGN = {
    "accent": "#ff6ec7",
    "ink": "#d1fae5",
    "muted": "#f9a8d4",
    "page": "#0b0f0c",
    "font": "DejaVu Sans Mono",
    "header": "frame",
    "name_case": "lower",
    "heading": "slab",
    "heading_case": "lower",
    "bullet": ">>",
    "bullet_width": 18,
    "separator": " @ ",
    "contact_join": "  //  ",
    "body_align": "start",
    "margin": 50,
    "heading_format": "> sketch_{number:02d}: {slug}",
    "footer": "nika@ljubljana:~/sketches$ ls -la",
    "divider": "∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿",
}


def fourpages():
    return typeset(PERSONA, DOCUMENT, DESIGN, 4)
