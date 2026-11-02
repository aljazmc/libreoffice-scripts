"""Stack Plan of Wharf Street HQ Move, two pages.

The stack plan with floors, desks, the sharing ratios and the adjacencies.
"""
from content import DOCUMENT, PROJECT
from typesetting import typeset

DESIGN = {
    "accent": "#b5651d",
    "ink": "#2e2a26",
    "muted": "#6f665d",
    "page": "#fdfcf9",
    "font": "TeX Gyre Termes",
    "heading_font": "Liberation Sans Narrow",
    "chart_font": "Liberation Sans Narrow",
    "header": "bar",
    "heading": "plain",
    "heading_format": "{number}/ {title}",
    "bullet": "—",
    "bullet_width": 16,
    "body_align": "justify",
    "table": "lines",
    "series": ["#b5651d", "#4a6670", "#d9a066", "#8aa29e", "#c8c2b6"],
    "good": "#5c8a4f",
    "warn": "#d9a066",
    "bad": "#b23a2b",
    "info": "#4a6670",
    "radius": 0,
    "footer": "Wharf Street HQ Move · Stack Plan",
}


def twopages():
    return typeset(PROJECT, DOCUMENT, DESIGN, 2)
