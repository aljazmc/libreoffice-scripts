"""Product Roadmap of Pocket Bank App Relaunch, four pages.

The roadmap in full: themes, bets, the release train, dependencies, capacity
and what we said no to.
"""
from content import DOCUMENT, PROJECT
from typesetting import typeset

DESIGN = {
    "accent": "#6d28d9",
    "ink": "#1e1b2e",
    "muted": "#6b6880",
    "page": "#ffffff",
    "font": "Lato",
    "header": "band",
    "heading": "plain",
    "bullet": "●",
    "bullet_width": 12,
    "body_align": "start",
    "table": "zebra",
    "series": ["#6d28d9", "#14b8a6", "#f59e0b", "#ec4899", "#a5a3b8"],
    "good": "#10b981",
    "warn": "#f59e0b",
    "bad": "#ef4444",
    "info": "#3b82f6",
    "radius": 4,
    "footer": "Pocket Bank · Product Roadmap · internal",
}


def fourpages():
    return typeset(PROJECT, DOCUMENT, DESIGN, 4)
