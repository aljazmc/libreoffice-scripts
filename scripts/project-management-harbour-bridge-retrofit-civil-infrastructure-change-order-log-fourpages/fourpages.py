"""Change Order Log of Harbour Bridge Retrofit, four pages.

The change orders in full, the trend by month, the causes and the lessons
for the contract.
"""
from content import DOCUMENT, PROJECT
from typesetting import typeset

DESIGN = {
    "accent": "#e8590c",
    "ink": "#0d2a4a",
    "muted": "#5c6f82",
    "page": "#ffffff",
    "font": "TeX Gyre Heros",
    "heading_font": "TeX Gyre Heros Cn",
    "chart_font": "TeX Gyre Heros Cn",
    "header": "rule",
    "title_case": "upper",
    "heading": "slab",
    "heading_case": "upper",
    "heading_format": "{number:02d}  {title}",
    "bullet": "▪",
    "body_align": "start",
    "table": "grid",
    "series": ["#0d2a4a", "#e8590c", "#6f8fae", "#f2a65a", "#b9c7d4"],
    "radius": 0,
    "chart_title_case": "upper",
    "density": "compact",
    "footer": "HBR-24 · Change Order Log · Port Aldwick City Works",
}


def fourpages():
    return typeset(PROJECT, DOCUMENT, DESIGN, 4)
