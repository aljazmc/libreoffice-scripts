"""Move Schedule of Wharf Street HQ Move, two pages.

Landscape. The waves with teams, crates, IT and the checkpoints.
"""
from content import DOCUMENT, PROJECT
from typesetting.project_management import typeset

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
    "orientation": "landscape",
    "footer": "Wharf Street HQ Move · Move Schedule · Fictional example",
}


def twopages():
    return typeset(PROJECT, DOCUMENT, DESIGN, 2)
