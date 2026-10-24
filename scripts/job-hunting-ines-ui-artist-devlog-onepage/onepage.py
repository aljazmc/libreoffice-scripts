"""Saudade Station · Devlog of Inês Duarte, one page.

The day the first build ran, on one page.
"""
from content import DOCUMENT, PERSONA
from typesetting import typeset

DESIGN = {
    "accent": "#4ade80",
    "ink": "#f5f3ff",
    "muted": "#86efac",
    "page": "#1a1033",
    "font": "DejaVu Sans Mono",
    "header": "frame",
    "name_case": "upper",
    "display": 1.2,
    "heading": "box",
    "heading_case": "upper",
    "bullet": "▸",
    "bullet_width": 16,
    "separator": " ✦ ",
    "contact_join": "  ✦  ",
    "body_align": "start",
    "margin": 50,
    "heading_format": "◆ {title}",
    "footer": "SAUDADE STATION · DEVLOG",
}


def onepage():
    return typeset(PERSONA, DOCUMENT, DESIGN, 1)
