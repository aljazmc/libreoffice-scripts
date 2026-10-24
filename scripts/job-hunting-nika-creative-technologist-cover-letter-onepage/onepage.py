"""Cover Letter of Nika Zupan, one page.

A letter to a science museum, typed into a terminal at night.
"""
from content import DOCUMENT, PERSONA
from typesetting import typeset

DESIGN = {
    "accent": "#39ff14",
    "ink": "#d1fae5",
    "muted": "#6ee7b7",
    "page": "#0b0f0c",
    "font": "DejaVu Sans Mono",
    "header": "rule",
    "name_case": "lower",
    "heading": "plain",
    "heading_case": "lower",
    "bullet": "[x]",
    "bullet_width": 24,
    "separator": " @ ",
    "contact_join": "  //  ",
    "body_align": "start",
    "margin": 50,
    "heading_format": "// {title}",
    "footer": "nika@ljubljana:~$ cat letter.txt",
}


def onepage():
    return typeset(PERSONA, DOCUMENT, DESIGN, 1)
