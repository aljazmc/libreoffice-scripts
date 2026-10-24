"""Curriculum Vitae of Nika Zupan, one page.

A CV printed straight from the shell, one screen deep.
"""
from content import DOCUMENT, PERSONA
from typesetting import typeset

DESIGN = {
    "accent": "#39ff14",
    "ink": "#d1fae5",
    "muted": "#6ee7b7",
    "page": "#0b0f0c",
    "font": "DejaVu Sans Mono",
    "header": "frame",
    "name_case": "lower",
    "heading": "slab",
    "heading_case": "lower",
    "bullet": "[x]",
    "bullet_width": 24,
    "separator": " @ ",
    "contact_join": "  //  ",
    "body_align": "start",
    "margin": 50,
    "heading_format": "$ cat ~/{slug}.txt",
    "footer": "nika@ljubljana:~$ less cv.txt",
    "density": "compact",
}


def onepage():
    return typeset(PERSONA, DOCUMENT, DESIGN, 1)
