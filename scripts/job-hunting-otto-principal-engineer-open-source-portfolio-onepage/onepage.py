"""Open Source Portfolio of Otto Lindgren, one page.

One project, its users and its maintainer, on one page.
"""
from content import DOCUMENT, PERSONA
from typesetting import typeset

DESIGN = {
    "accent": "#859900",
    "ink": "#4a5a60",
    "muted": "#a3a38b",
    "page": "#fdf6e3",
    "font": "Liberation Mono",
    "header": "rule",
    "name_format": "# {name}",
    "heading": "plain",
    "heading_format": "### {title}",
    "bullet": "*",
    "bullet_width": 14,
    "separator": " | ",
    "contact_join": " | ",
    "body_align": "start",
    "margin": 52,
    "footer": "PORTFOLIO.md · MIT licensed",
}


def onepage():
    return typeset(PERSONA, DOCUMENT, DESIGN, 1)
