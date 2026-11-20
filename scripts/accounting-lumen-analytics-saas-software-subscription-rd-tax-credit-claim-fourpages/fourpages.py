"""R&D Tax Credit Claim of Lumen Analytics, four pages.

The claim, the technical narrative, the cost workings and the declarations.
"""
from content import BUSINESS, DOCUMENT
from typesetting import typeset

DESIGN = {
    "accent": "#4f46e5",
    "ink": "#111827",
    "muted": "#6b7280",
    "page": "#f9fafb",
    "font": "DejaVu Sans",
    "series": ["#4f46e5", "#06b6d4", "#a855f7", "#f59e0b", "#9ca3af"],
    "good": "#10b981",
    "warn": "#f59e0b",
    "bad": "#ef4444",
    "info": "#06b6d4",
    "radius": 0,
    "heading_font": "DejaVu Sans",
    "header": "rule",
    "heading": "box",
    "heading_case": "upper",
    "table": "grid",
    "density": "compact",
    "body_align": "start",
    "footer": "Lumen Analytics Inc. · R&D Tax Credit Claim · confidential",
}


def fourpages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 4)
