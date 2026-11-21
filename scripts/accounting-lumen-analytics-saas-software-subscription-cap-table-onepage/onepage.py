"""Capitalisation Table of Lumen Analytics, one page.

Landscape. Who owns Lumen after the Series A, fully diluted.
"""
from content import BUSINESS, DOCUMENT
from typesetting.accounting import typeset

DESIGN = {
    "accent": "#4f46e5",
    "ink": "#111827",
    "muted": "#6b7280",
    "page": "#ffffff",
    "font": "Liberation Sans Narrow",
    "series": ["#4f46e5", "#06b6d4", "#a855f7", "#f59e0b", "#9ca3af"],
    "good": "#10b981",
    "warn": "#f59e0b",
    "bad": "#ef4444",
    "info": "#06b6d4",
    "radius": 3,
    "orientation": "landscape",
    "heading_font": "Lato",
    "header": "band",
    "heading": "tint",
    "table": "zebra",
    "body_align": "start",
    "footer": "Lumen Analytics Inc. · Capitalisation Table · confidential",
}


def onepage():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 1)
