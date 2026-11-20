"""Cash Flow Statement of Lumen Analytics, four pages.

The statement, the reconciliation, the quarters and the notes.
"""
from content import BUSINESS, DOCUMENT
from typesetting import typeset

DESIGN = {
    "accent": "#4f46e5",
    "ink": "#111827",
    "muted": "#6b7280",
    "page": "#ffffff",
    "font": "Lato",
    "series": ["#4f46e5", "#06b6d4", "#a855f7", "#f59e0b", "#9ca3af"],
    "good": "#10b981",
    "warn": "#f59e0b",
    "bad": "#ef4444",
    "info": "#06b6d4",
    "radius": 3,
    "header": "rule",
    "heading": "plain",
    "table": "lines",
    "body_align": "start",
    "footer": "Lumen Analytics Inc. · Cash Flow Statement · confidential",
}


def fourpages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 4)
