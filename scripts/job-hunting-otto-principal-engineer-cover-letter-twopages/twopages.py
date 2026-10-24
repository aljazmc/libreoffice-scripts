"""Cover Letter of Otto Lindgren, two pages.

Context, motivation and the gaps, as a reviewer would want them.
"""
from content import DOCUMENT, PERSONA
from typesetting import typeset

DESIGN = {
    "accent": "#268bd2",
    "ink": "#4a5a60",
    "muted": "#93a1a1",
    "page": "#fdf6e3",
    "font": "Liberation Mono",
    "header": "rule",
    "name_format": "# {name}",
    "heading": "plain",
    "heading_format": "> {title}",
    "bullet": "-",
    "bullet_width": 14,
    "separator": " | ",
    "contact_join": " | ",
    "body_align": "start",
    "margin": 52,
    "footer": "letter.md",
}


def twopages():
    return typeset(PERSONA, DOCUMENT, DESIGN, 2)
