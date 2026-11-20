"""Capitalisation Table of Lumen Analytics, four pages.

Landscape. Every holder, every round, the pool, the waterfall at exit and
the notes.
"""
from content import BUSINESS, DOCUMENT
from typesetting import typeset

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


def fourpages():
    return typeset(BUSINESS, DOCUMENT, DESIGN, 4)
