"""Curriculum Vitae of Otto Lindgren, four pages.

The full history, including the start-up that did not work.
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
    "heading_format": "## {title}",
    "bullet": "-",
    "bullet_width": 14,
    "separator": " | ",
    "contact_join": " | ",
    "body_align": "start",
    "margin": 52,
    "footer": "cv.md · rendered with LibreOffice, of all things",
    "density": "airy",
    "divider": "---",
}


def fourpages():
    return typeset(PERSONA, DOCUMENT, DESIGN, 4)
