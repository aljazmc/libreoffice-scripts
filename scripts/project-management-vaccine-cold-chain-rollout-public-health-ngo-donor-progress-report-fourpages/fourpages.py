"""Donor Progress Report of Cold Chain for Every Child, four pages.

Year 2 in full: results, spending, stories, challenges, risks and the plan
for year 3.
"""
from content import DOCUMENT, PROJECT
from typesetting.project_management import typeset

DESIGN = {
    "accent": "#0072bc",
    "ink": "#1a1a1a",
    "muted": "#5a6670",
    "page": "#ffffff",
    "font": "DejaVu Sans",
    "header": "band",
    "heading": "box",
    "heading_case": "upper",
    "bullet": "■",
    "body_align": "start",
    "table": "grid",
    "density": "compact",
    "series": ["#0072bc", "#f7941d", "#00a1de", "#8dc63f", "#a0a8ae"],
    "good": "#4f9a2f",
    "warn": "#f7941d",
    "bad": "#e2231a",
    "info": "#00a1de",
    "radius": 1,
    "footer": "Cold Chain for Every Child · Donor Progress Report · not for "
        "publication",
}


def fourpages():
    return typeset(PROJECT, DOCUMENT, DESIGN, 4)
