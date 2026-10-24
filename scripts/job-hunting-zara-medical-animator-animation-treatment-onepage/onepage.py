"""A Valve, Replaced of Zara Haddad, one page.

A one-page pitch for a medical animation, typed like a screenplay.
"""
from content import DOCUMENT, PERSONA
from typesetting import typeset

DESIGN = {
    "accent": "#111111",
    "ink": "#111111",
    "muted": "#444444",
    "page": "#fffef8",
    "font": "Noto Sans Mono",
    "header": "centered",
    "heading": "plain",
    "heading_case": "upper",
    "heading_format": "{number}. INT. {title} — CONTINUOUS",
    "bullet": "—",
    "bullet_width": 18,
    "body_align": "start",
    "margin": 72,
    "footer": "“A Valve, Replaced” · treatment draft 3 · Zara Haddad",
}


def onepage():
    return typeset(PERSONA, DOCUMENT, DESIGN, 1)
