"""Sprint Review of Pocket Bank App Relaunch, one page.

Sprint 14 in one page: the goal, the burndown and what was done.
"""
from content import DOCUMENT, PROJECT
from typesetting.project_management import typeset

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
    "footer": "Pocket Bank · Sprint Review · internal",
}


def onepage():
    return typeset(PROJECT, DOCUMENT, DESIGN, 1)
