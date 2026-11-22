"""Change Impact Assessment of Wharf Street HQ Move, four pages.

The assessment in full: impacts, the survey, readiness, resistance and the
change plan.
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
    "footer": "Wharf Street HQ Move · Change Impact Assessment · Fictional example",
}


def fourpages():
    return typeset(PROJECT, DOCUMENT, DESIGN, 4)
