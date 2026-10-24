"""Cover Letter of Kai Berg, two pages.

Why a games artist wants to light real rooms.
"""
from content import DOCUMENT, PERSONA
from typesetting import typeset

DESIGN = {
    "accent": "#7dd3fc",
    "ink": "#e6f0ff",
    "muted": "#9db8e8",
    "page": "#0f2a5f",
    "font": "Liberation Sans",
    "heading_font": "Noto Sans Mono",
    "header": "rule",
    "name_case": "upper",
    "heading": "plain",
    "heading_case": "upper",
    "heading_format": "— {title}",
    "bullet": "+",
    "separator": " — ",
    "contact_join": "   |   ",
    "footer": "SHEET L-01 · KAI BERG · LETTER",
}


def twopages():
    return typeset(PERSONA, DOCUMENT, DESIGN, 2)
