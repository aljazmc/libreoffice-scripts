"""Cover Letter of Inês Duarte, two pages.

Why a self-taught pixel artist wants to make menus.
"""
from content import DOCUMENT, PERSONA
from typesetting import typeset

DESIGN = {
    "accent": "#ffcc00",
    "ink": "#f5f3ff",
    "muted": "#c4b5fd",
    "page": "#1a1033",
    "font": "DejaVu Sans Mono",
    "header": "rule",
    "name_case": "upper",
    "display": 1.2,
    "heading": "plain",
    "heading_case": "upper",
    "bullet": "■",
    "bullet_width": 16,
    "separator": " ✦ ",
    "contact_join": "  ✦  ",
    "body_align": "start",
    "margin": 50,
    "heading_format": "▶ {title}",
    "footer": "PRESS START · LETTER TO MOONFISH GAMES",
}


def twopages():
    return typeset(PERSONA, DOCUMENT, DESIGN, 2)
