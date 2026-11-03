"""Three-Week Lookahead of Harbour Bridge Retrofit, one page.

Landscape. The next three weeks of the works on one bar chart, with the
night possessions and the critical path.
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
    "orientation": "landscape",
    "footer": "HBR-24 · Three-Week Lookahead · Port Aldwick City Works",
}


def onepage():
    return typeset(PROJECT, DOCUMENT, DESIGN, 1)
