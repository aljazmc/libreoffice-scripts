"""Cover Letter of Nika Zupan, four pages.

The long version, including what Nika would build in the first year.
"""
from content import DOCUMENT, PERSONA
from typesetting import typeset

DESIGN = {
    "accent": "#39ff14",
    "ink": "#d1fae5",
    "muted": "#6ee7b7",
    "page": "#0b0f0c",
    "font": "DejaVu Sans Mono",
    "header": "rule",
    "name_case": "lower",
    "heading": "plain",
    "heading_case": "lower",
    "bullet": "[x]",
    "bullet_width": 24,
    "separator": " @ ",
    "contact_join": "  //  ",
    "body_align": "start",
    "margin": 50,
    "heading_format": "// {title}",
    "footer": "nika@ljubljana:~$ cat letter.txt",
    "density": "airy",
}


def fourpages():
    return typeset(PERSONA, DOCUMENT, DESIGN, 4)
