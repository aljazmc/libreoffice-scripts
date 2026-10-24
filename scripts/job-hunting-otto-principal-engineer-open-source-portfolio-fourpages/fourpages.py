"""Open Source Portfolio of Otto Lindgren, four pages.

Everything, including the project Otto handed over and why.
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
    "density": "airy",
    "divider": "* * *",
}


def fourpages():
    return typeset(PERSONA, DOCUMENT, DESIGN, 4)
