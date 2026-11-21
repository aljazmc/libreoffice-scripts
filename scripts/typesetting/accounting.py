"""Typeset a document of text, tables and charts as a flat ODT document of
exactly the given number of A4 pages.

A document is the subject (a project or a business: its name and author)
and the DOCUMENT of content.py: a header made of the subject, the title and
the document control strip, and the sections of the document. Sections
are text (paragraphs, bullets, entries, tags, callouts), tables, and
figures: charts drawn as SVG and embedded in the
document, so they stay sharp in every format.

A document fills its pages by choosing what goes in: every paragraph,
entry, table row and figure has a priority, and the most important ones are
kept, in the order of the document, as long as a simulation of the page
breaks says that they fit into the pages. Line heights are fixed, line
wrapping is estimated from the average width of the characters of each
font, figures have a fixed height and tables break between rows, so the
simulation knows the height of everything.

The DESIGN of the document, given by its project script, picks the fonts,
the colors, the page and the look of the header, the headings, the tables
and the charts: see stylesheet() and Theme for what it can say.
"""
import base64
import math
import re
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape

NAMESPACES = {
    "office": "urn:oasis:names:tc:opendocument:xmlns:office:1.0",
    "style": "urn:oasis:names:tc:opendocument:xmlns:style:1.0",
    "text": "urn:oasis:names:tc:opendocument:xmlns:text:1.0",
    "table": "urn:oasis:names:tc:opendocument:xmlns:table:1.0",
    "fo": "urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0",
    "svg": "urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0",
    "dc": "http://purl.org/dc/elements/1.1/",
    "draw": "urn:oasis:names:tc:opendocument:xmlns:drawing:1.0",
}

# the average advance of a character of English prose, spaces included, in
# ems, of the regular and the bold face
FONTS = {
    "Lato": (0.438, 0.443),
    "Liberation Sans": (0.442, 0.478),
    "Liberation Serif": (0.406, 0.431),
    "TeX Gyre Pagella": (0.443, 0.459),
    "TeX Gyre Heros": (0.441, 0.477),
    "TeX Gyre Termes": (0.404, 0.429),
    "DejaVu Sans": (0.504, 0.571),
    "DejaVu Serif": (0.514, 0.568),
    "Quicksand": (0.457, 0.482),
    "TeX Gyre Adventor": (0.476, 0.477),
    "TeX Gyre Bonum": (0.493, 0.529),
    "TeX Gyre Schola": (0.465, 0.522),
    "TeX Gyre Heros Cn": (0.361, 0.391),
    "Liberation Sans Narrow": (0.362, 0.392),
    "DejaVu Sans Mono": (0.602, 0.602),
    "Liberation Mono": (0.600, 0.600),
    "Noto Sans Mono": (0.600, 0.600),
    "C059": (0.469, 0.526),
    "P052": (0.448, 0.461),
    "Tuffy": (0.426, 0.458),
    "Nimbus Sans": (0.447, 0.482),
    "URW Gothic": (0.490, 0.495),
    "URW Bookman": (0.498, 0.532),
}
MONOSPACED = {"DejaVu Sans Mono", "Liberation Mono", "Noto Sans Mono"}
# how much wider capitals are than prose, by font
CAPITALS = {"TeX Gyre Schola": 1.29, "C059": 1.29, "Lato": 1.29,
            "Liberation Sans": 1.25, "Nimbus Sans": 1.25,
            "TeX Gyre Heros": 1.25, "TeX Gyre Heros Cn": 1.25,
            "Liberation Sans Narrow": 1.25, "TeX Gyre Pagella": 1.35,
            "P052": 1.35, "TeX Gyre Termes": 1.4, "Liberation Serif": 1.4,
            "URW Gothic": 1.15, "DejaVu Sans": 1.17, "Quicksand": 1.17,
            "Tuffy": 1.23, "URW Bookman": 1.27, "TeX Gyre Adventor": 1.17}

# A4 in points
A4 = (595.28, 841.89)
MARGIN_X = 50
MARGIN_TOP = 42
MARGIN_BOTTOM = 32
FOOTER_HEIGHT = 12
FOOTER_SPACING = 10

# the estimate of the lines of text is made this much longer for its
# errors, and this much of every page is kept free; figures have exact
# heights
SAFETY = 0.03
RESERVE = 2

MARKUP = re.compile(r"(\*\*.+?\*\*|\*.+?\*)")

for prefix, uri in NAMESPACES.items():
    ET.register_namespace(prefix, uri)


def qualified(name):
    prefix, local = name.split(":")
    return f"{{{NAMESPACES[prefix]}}}{local}"


def element(parent, tag, **attributes):
    """Attribute names use "__" for ":" and "_" for "-", e.g.
    fo__font_size="10pt" sets fo:font-size."""
    return ET.SubElement(parent, qualified(tag),
                         {qualified(key.replace("__", ":").replace("_", "-")):
                          str(value) for key, value in attributes.items()})


def pt(value):
    return f"{value:g}pt"


def mix(start, end, t):
    """The color t of the way from start to end."""
    channels = [round(a + (b - a) * t) for a, b in
                zip(bytes.fromhex(start[1:]), bytes.fromhex(end[1:]))]
    return "#" + bytes(channels).hex()


def luminance(color):
    r, g, b = bytes.fromhex(color[1:])
    return (0.299 * r + 0.587 * g + 0.114 * b) / 255


def page_size(design):
    width, height = A4
    if design.get("orientation") == "landscape":
        width, height = height, width
    return width, height


def text_width(design):
    return page_size(design)[0] - 2 * design.get("margin", MARGIN_X)


def text_height(design):
    return (page_size(design)[1] - MARGIN_TOP - MARGIN_BOTTOM
            - FOOTER_HEIGHT - FOOTER_SPACING)


def advance(text, size, font, bold=False):
    """The estimated width of the text in points."""
    regular, heavy = FONTS[font]
    return len(text) * (heavy if bold else regular) * size


def wrap(text, size, width, font, bold=False):
    """The text broken into lines no wider than the width."""
    result, line = [], ""
    for word in text.split():
        candidate = f"{line} {word}" if line else word
        if line and advance(candidate, size, font, bold) > width:
            result.append(line)
            line = word
        else:
            line = candidate
    return result + [line] if line else result


# charts

class Theme:
    """The colors and fonts of the charts. The design names the accent, ink,
    muted and page colors, the chart_font (else the body font), the series
    colors, the status colors good, warn, bad and info, the grid color and
    the radius of the corners of bars and tiles."""

    def __init__(self, design):
        self.accent = design["accent"]
        self.ink = design.get("ink", "#1f2328")
        self.muted = design.get("muted", "#5b6470")
        self.page = design.get("page", "#ffffff")
        self.font = design.get("chart_font", design["font"])
        self.bold_font = design.get("chart_heading_font", self.font)
        self.grid = design.get("grid", mix(self.muted, self.page, 0.72))
        self.series = design.get("series") or [
            self.accent, mix(self.accent, self.ink, 0.5),
            mix(self.accent, self.page, 0.45), self.muted,
            mix(self.muted, self.page, 0.5)]
        self.status = {"good": design.get("good", "#2e9d5b"),
                       "warn": design.get("warn", "#e3a21a"),
                       "bad": design.get("bad", "#d64545"),
                       "info": design.get("info", "#3a7bd5"),
                       "accent": self.accent, "ink": self.ink,
                       "muted": self.muted, "grid": self.grid,
                       "neutral": mix(self.muted, self.page, 0.55),
                       "page": self.page}
        self.radius = design.get("radius", 2)
        self.title_case = design.get("chart_title_case")

    def color(self, spec, index=0):
        """A color from a series index, a status name or a hex value."""
        if spec is None:
            return self.series[index % len(self.series)]
        if isinstance(spec, int):
            return self.series[spec % len(self.series)]
        if spec.startswith("#"):
            return spec
        return self.status[spec]

    def tint(self, color, t):
        return mix(color, self.page, t)

    def on(self, color):
        """A legible text color on the color."""
        light, dark = ((self.page, self.ink) if luminance(self.page) > 0.5
                       else (self.ink, self.page))
        return dark if luminance(color) > 0.6 else light


class Canvas:
    """SVG elements in points."""

    def __init__(self, theme):
        self.theme = theme
        self.parts = []

    def rect(self, x, y, w, h, fill, stroke=None, width=0.75, radius=0,
             dash=None):
        if w <= 0 or h <= 0:
            return
        attributes = f'fill="{fill or "none"}"'
        if stroke:
            attributes += f' stroke="{stroke}" stroke-width="{width:g}"'
        if dash:
            attributes += f' stroke-dasharray="{dash}"'
        if radius:
            radius = min(radius, w / 2, h / 2)
            attributes += f' rx="{radius:.2f}" ry="{radius:.2f}"'
        self.parts.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" '
                          f'height="{h:.2f}" {attributes}/>')

    def line(self, x1, y1, x2, y2, stroke, width=0.75, dash=None):
        extra = f' stroke-dasharray="{dash}"' if dash else ""
        self.parts.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" '
                          f'y2="{y2:.2f}" stroke="{stroke}" '
                          f'stroke-width="{width:g}"{extra}/>')

    def polyline(self, points, stroke, width=1.25, dash=None):
        extra = f' stroke-dasharray="{dash}"' if dash else ""
        path = " ".join(f"{x:.2f},{y:.2f}" for x, y in points)
        self.parts.append(f'<polyline points="{path}" fill="none" '
                          f'stroke="{stroke}" stroke-width="{width:g}" '
                          f'stroke-linejoin="round"{extra}/>')

    def polygon(self, points, fill, stroke=None, width=0.75):
        path = " ".join(f"{x:.2f},{y:.2f}" for x, y in points)
        extra = (f' stroke="{stroke}" stroke-width="{width:g}"' if stroke
                 else "")
        self.parts.append(f'<polygon points="{path}" fill="{fill}"{extra}/>')

    def path(self, d, fill, stroke=None, width=0.75):
        extra = (f' stroke="{stroke}" stroke-width="{width:g}"' if stroke
                 else "")
        self.parts.append(f'<path d="{d}" fill="{fill}"{extra}/>')

    def circle(self, x, y, r, fill, stroke=None, width=0.75):
        extra = (f' stroke="{stroke}" stroke-width="{width:g}"' if stroke
                 else "")
        self.parts.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}" '
                          f'fill="{fill or "none"}"{extra}/>')

    def text(self, x, y, value, size=7.5, color=None, anchor="start",
             bold=False, italic=False, font=None):
        """Text with its baseline at y."""
        font = font or (self.theme.bold_font if bold else self.theme.font)
        style = ' font-weight="bold"' if bold else ""
        style += ' font-style="italic"' if italic else ""
        self.parts.append(
            f'<text x="{x:.2f}" y="{y:.2f}" font-family="{font}" '
            f'font-size="{size:g}" fill="{color or self.theme.ink}" '
            f'text-anchor="{anchor}"{style}>{escape(str(value))}</text>')

    def lines(self, x, y, value, size, width, color=None, anchor="start",
              bold=False, leading=1.2, limit=None):
        """Wrapped text from the baseline y; returns the number of lines."""
        font = self.theme.bold_font if bold else self.theme.font
        rows = wrap(value, size, width, font, bold)
        if limit and len(rows) > limit:
            rows = rows[:limit]
            rows[-1] = rows[-1].rstrip(".,;") + "…"
        for index, row in enumerate(rows):
            self.text(x, y + index * size * leading, row, size, color,
                      anchor, bold)
        return len(rows)

    def width(self, value, size, bold=False):
        """The estimated width, a little generous: labels are short and
        often in capitals."""
        return 1.08 * advance(str(value), size,
                              self.theme.bold_font if bold
                              else self.theme.font, bold)

    def svg(self, width, height):
        body = "".join(self.parts)
        return (f'<svg xmlns="http://www.w3.org/2000/svg" '
                f'width="{width:.2f}pt" height="{height:.2f}pt" '
                f'viewBox="0 0 {width:.2f} {height:.2f}">{body}</svg>')


def number(value, chart):
    """The value formatted with the format of the chart, e.g. "€{:,.1f}m"."""
    if isinstance(value, str):
        return value
    return chart.get("format", "{:,.0f}" if value == int(value)
                     else "{:,.1f}").format(value)


def nice_ticks(low, high, count=5):
    """Round ticks covering low to high."""
    if high == low:
        high = low + 1
    raw = (high - low) / count
    magnitude = 10 ** math.floor(math.log10(raw))
    step = next(m * magnitude for m in (1, 2, 2.5, 5, 10)
                if m * magnitude >= raw)
    start = math.floor(low / step) * step
    ticks, value = [], start
    while value < high + step * 0.999:
        ticks.append(round(value, 10))
        value += step
    return ticks


def legend(canvas, x, y, entries, size=7, align="start"):
    """Swatches and names in a row starting at x, or ending at x."""
    theme = canvas.theme
    items = [(name, color, canvas.width(name, size) + 18)
             for name, color in entries]
    total = sum(item[2] for item in items)
    if align == "end":
        x -= total
    for name, color, span in items:
        if isinstance(color, tuple):
            color, dash = color
            canvas.line(x, y - 2.5, x + 9, y - 2.5, color, 1.5, dash)
        else:
            canvas.rect(x, y - 6.5, 8, 8, color, radius=theme.radius)
        canvas.text(x + 11, y, name, size, theme.muted)
        x += span
    return total


def chart_title(canvas, chart, x, y, w):
    """The title of a chart at the top of its box; returns its height."""
    if not chart.get("title"):
        return 0
    title = chart["title"]
    if canvas.theme.title_case == "upper":
        title = title.upper()
    canvas.text(x, y + 9, title, 8.5, canvas.theme.ink, bold=True)
    if chart.get("subtitle"):
        canvas.text(x + canvas.width(title, 8.5, True) + 6, y + 9,
                    chart["subtitle"], 7.5, canvas.theme.muted)
    return 16


def series_legend(canvas, chart, x, y, w, entries):
    """The legend at the top right; returns the height it needs when the
    chart has no title to share the line with."""
    if chart.get("legend", len(entries) > 1) and entries:
        legend(canvas, x + w, y + 9, entries, align="end")
        return 14
    return 0


def gantt(canvas, chart, x, y, w, h):
    """Bars of tasks on a time scale. The chart has columns (the labels of
    the periods) or start, end and ticks, tasks with label, start, end,
    group, progress, critical, milestone and section, groups (the names of
    the colors of the legend), deps (pairs of task indices) and today."""
    theme = canvas.theme
    top = chart_title(canvas, chart, x, y, w)
    groups = chart.get("groups", [])
    entries = [(name, theme.color(i)) for i, name in enumerate(groups)]
    top = max(top, series_legend(canvas, chart, x, y, w, entries))
    tasks = chart["tasks"]
    if "columns" in chart:
        start, end = 0, len(chart["columns"])
    else:
        start, end = chart["start"], chart["end"]
    size = chart.get("size", 7.5)
    label_width = min(max(canvas.width(t["label"], size, t.get("section"))
                          for t in tasks) + 10, w * chart.get("labels", 0.34))
    left, right = x + label_width, x + w - 4
    header = 14
    row = (h - top - header - (10 if chart.get("today") is not None else 2)
           ) / len(tasks)

    def at(value):
        return left + (value - start) / (end - start) * (right - left)

    body_top = y + top + header
    if "columns" in chart:
        for index, label in enumerate(chart["columns"]):
            if index % 2:
                canvas.rect(at(index), body_top, at(index + 1) - at(index),
                            row * len(tasks), theme.tint(theme.grid, 0.7))
            canvas.text((at(index) + at(index + 1)) / 2, body_top - 4,
                        label, 6.5, theme.muted, "middle")
    for position, label in chart.get("ticks", []):
        canvas.line(at(position), body_top - 2, at(position),
                    body_top + row * len(tasks), theme.grid, 0.5)
        canvas.text(at(position), body_top - 4, label, 6.5, theme.muted,
                    "middle")
    canvas.line(left, body_top, right, body_top, theme.grid, 0.75)

    centers = []
    for index, task in enumerate(tasks):
        top_y = body_top + index * row
        middle = top_y + row / 2
        centers.append(middle)
        bold = task.get("section", False)
        label = task["label"]
        while canvas.width(label, size, bold) > label_width - 8:
            label = label[:-2] + "…"
        canvas.text(x + (0 if bold else 6 * bool(chart.get("indent"))),
                    middle + size * 0.35, label, size,
                    theme.ink if bold else theme.muted if task.get("muted")
                    else theme.ink, bold=bold)
        if index:
            canvas.line(x, top_y, right, top_y, theme.tint(theme.grid, 0.5),
                        0.4)
        color = (theme.status["bad"] if task.get("critical")
                 else theme.color(task.get("group", 0)))
        if task.get("milestone"):
            cx, r = at(task["start"]), min(row * 0.34, 5)
            canvas.polygon([(cx, middle - r), (cx + r, middle),
                            (cx, middle + r), (cx - r, middle)],
                           theme.ink if task.get("done") else color)
            if task.get("text"):
                canvas.text(cx + r + 3, middle + 2.5, task["text"], 6.5,
                            theme.muted)
            continue
        x1, x2 = at(task["start"]), at(task["end"])
        bar = min(row * (0.4 if bold else 0.62), 11)
        if bold:
            canvas.rect(x1, middle - bar / 2, x2 - x1, bar, theme.ink)
            canvas.polygon([(x1, middle + bar / 2), (x1 + 4, middle + bar / 2),
                            (x1, middle + bar / 2 + 3)], theme.ink)
            canvas.polygon([(x2, middle + bar / 2), (x2 - 4, middle + bar / 2),
                            (x2, middle + bar / 2 + 3)], theme.ink)
            continue
        progress = task.get("progress")
        if progress is not None and progress < 1:
            canvas.rect(x1, middle - bar / 2, x2 - x1, bar,
                        theme.tint(color, 0.6), radius=theme.radius)
            canvas.rect(x1, middle - bar / 2, (x2 - x1) * progress, bar,
                        color, radius=theme.radius)
        else:
            canvas.rect(x1, middle - bar / 2, x2 - x1, bar, color,
                        radius=theme.radius)
        if task.get("text"):
            inside = canvas.width(task["text"], 6.5) * 1.1 < x2 - x1 - 8
            if inside:
                canvas.text(x1 + 3, middle + 2.3, task["text"], 6.5,
                            theme.on(color))
            elif x2 + canvas.width(task["text"], 6.5) + 3 < right:
                canvas.text(x2 + 3, middle + 2.3, task["text"], 6.5,
                            theme.muted)
            else:
                canvas.text(x1 - 3, middle + 2.3, task["text"], 6.5,
                            theme.muted, "end")
    for a, b in chart.get("deps", []):
        ax = at(tasks[a].get("end", tasks[a]["start"]))
        bx = at(tasks[b]["start"])
        ay, by = centers[a], centers[b]
        bend = max(ax + 3, bx - 3) if bx > ax + 6 else ax + 3
        canvas.polyline([(ax, ay), (bend, ay), (bend, by - 4), (bend, by),
                         (bx - 1, by)], theme.muted, 0.6)
        canvas.polygon([(bx - 1, by), (bx - 4, by - 2), (bx - 4, by + 2)],
                       theme.muted)
    if chart.get("today") is not None:
        tx = at(chart["today"])
        canvas.line(tx, body_top - 2, tx, body_top + row * len(tasks),
                    theme.accent, 1, "3,2")
        label = chart.get("today_label", "today")
        canvas.rect(tx - canvas.width(label, 6.5, True) / 2 - 3,
                    body_top + row * len(tasks) - 1,
                    canvas.width(label, 6.5, True) + 6, 9, theme.accent,
                    radius=2)
        canvas.text(tx, body_top + row * len(tasks) + 6, label, 6.5,
                    theme.on(theme.accent), "middle", bold=True)


def axis_frame(canvas, chart, x, y, w, h, low, high, left_pad=None):
    """A value axis with gridlines; returns the plot box and the scale."""
    theme = canvas.theme
    ticks = chart.get("yticks") or nice_ticks(low, high,
                                               chart.get("ticks", 4))
    low, high = min(ticks[0], low), max(ticks[-1], high)
    labels = [number(t, {"format": chart["axis_format"]} if
                     chart.get("axis_format") else chart) for t in ticks]
    pad = left_pad if left_pad is not None else (
        max(canvas.width(label, 6.5) for label in labels) + 6)
    box = (x + pad, y, w - pad, h)

    def scale(value):
        return y + h - (value - low) / (high - low) * h

    for tick, label in zip(ticks, labels):
        ty = scale(tick)
        canvas.line(box[0], ty, x + w, ty,
                    theme.muted if tick == 0 and low < 0 else theme.grid,
                    0.5, None if tick == 0 else "1.5,1.5")
        canvas.text(box[0] - 4, ty + 2.3, label, 6.5, theme.muted, "end")
    return box, scale


def line_chart(canvas, chart, x, y, w, h):
    """Series of values over the labels of x. A series has name, values (None
    for missing), color, dash, area and markers; the chart can have a
    target, a band (low, high, label), marks (index, label) and
    end_labels."""
    theme = canvas.theme
    top = chart_title(canvas, chart, x, y, w)
    series = chart["series"]
    entries = [(s["name"], (theme.color(s.get("color"), i),
                            "3,2" if s.get("dash") else None))
               for i, s in enumerate(series)]
    top = max(top, series_legend(canvas, chart, x, y, w, entries))
    values = [v for s in series for v in s["values"] if v is not None]
    if chart.get("target") is not None:
        values.append(chart["target"])
    low = min(values + [0]) if chart.get("zero", True) else min(values)
    high = max(values)
    if not chart.get("zero", True):
        low -= (high - low) * 0.1
    box, scale = axis_frame(canvas, chart, x, y + top + 4, w,
                            h - top - 18, low, high * 1.04)
    labels = chart["x"]
    count = len(labels)

    def at(index):
        return box[0] + 6 + index * (box[2] - 12) / max(count - 1, 1)

    if chart.get("band"):
        b_low, b_high, b_label = chart["band"]
        canvas.rect(box[0], scale(b_high), box[2], scale(b_low) -
                    scale(b_high), theme.tint(theme.status["good"], 0.85))
        canvas.text(box[0] + box[2] - 2, scale(b_high) + 8, b_label, 6.5,
                    theme.status["good"], "end")
    every = max(1, math.ceil(count * canvas.width(max(labels, key=len), 6.5)
                             / (box[2] * 0.8)))
    for index, label in enumerate(labels):
        if index % every == 0 or index == count - 1 and every == 1:
            canvas.text(at(index), box[1] + box[3] + 10, label, 6.5,
                        theme.muted, "middle")
    for index, label in chart.get("marks", []):
        canvas.line(at(index), box[1], at(index), box[1] + box[3],
                    theme.muted, 0.6, "2,2")
        canvas.text(at(index) + 3, box[1] + 7, label, 6.5, theme.muted)
    if chart.get("target") is not None:
        ty = scale(chart["target"])
        canvas.line(box[0], ty, box[0] + box[2], ty, theme.status["bad"],
                    0.9, "4,2")
        canvas.text(box[0] + box[2] - 2, ty - 3,
                    chart.get("target_label", "target"), 6.5,
                    theme.status["bad"], "end")
    for i, s in enumerate(series):
        color = theme.color(s.get("color"), i)
        points = [(at(j), scale(v)) for j, v in enumerate(s["values"])
                  if v is not None]
        if s.get("area") and len(points) > 1:
            base = scale(max(low, 0))
            canvas.polygon(points + [(points[-1][0], base),
                                     (points[0][0], base)],
                           theme.tint(color, 0.8))
    for i, s in enumerate(series):
        color = theme.color(s.get("color"), i)
        points = [(at(j), scale(v)) for j, v in enumerate(s["values"])
                  if v is not None]
        canvas.polyline(points, color, s.get("width", 1.5),
                        "3,2" if s.get("dash") else None)
        if s.get("markers", chart.get("markers", count <= 14)):
            for px, py in points:
                canvas.circle(px, py, 1.8, theme.page, color, 1)
        if chart.get("end_labels") and points:
            last = [v for v in s["values"] if v is not None][-1]
            canvas.text(points[-1][0] + 4, points[-1][1] + 2.5,
                        number(last, chart), 6.5, color, bold=True)


def bar_chart(canvas, chart, x, y, w, h):
    """Bars of the series over the categories, grouped or stacked,
    vertical or horizontal. A series has name, values and color, or colors
    per bar; the chart can have a target, value labels and inside labels."""
    theme = canvas.theme
    top = chart_title(canvas, chart, x, y, w)
    series = chart["series"]
    categories = chart["categories"]
    stacked = chart.get("stacked", False)
    entries = [(s["name"], theme.color(s.get("color"), i))
               for i, s in enumerate(series)]
    top = max(top, series_legend(canvas, chart, x, y, w, entries))
    if stacked:
        sums = [sum(s["values"][j] for s in series)
                for j in range(len(categories))]
        high, low = max(sums), min([0] + [v for s in series
                                          for v in s["values"]])
    else:
        flat = [v for s in series for v in s["values"] if v is not None]
        high, low = max(flat + [0]), min(flat + [0])
    if chart.get("target") is not None:
        high = max(high, chart["target"])
    show = chart.get("values", True)
    size = chart.get("size", 7)

    def value_color(s, i, j):
        if s.get("colors"):
            return theme.color(s["colors"][j])
        return theme.color(s.get("color"), i)

    if chart.get("horizontal"):
        label_width = min(max(canvas.width(c, size) for c in categories) + 12,
                          w * 0.4)
        value_room = 30 if show else 4
        plot_x, plot_w = x + label_width, w - label_width - value_room
        plot_top = y + top + 2
        rows = len(categories)
        row = (h - top - 14) / rows
        span = high - low

        def at(value):
            return plot_x + (value - low) / span * plot_w

        for tick in nice_ticks(low, high, 4):
            if tick > high * 1.001:
                continue
            canvas.line(at(tick), plot_top, at(tick), plot_top + rows * row,
                        theme.grid, 0.5, "1.5,1.5")
            canvas.text(at(tick), plot_top + rows * row + 9,
                        number(tick, chart), 6.5, theme.muted, "middle")
        thickness = row * chart.get("thickness", 0.66)
        for j, category in enumerate(categories):
            middle = plot_top + j * row + row / 2
            canvas.text(x, middle + size * 0.35, category, size, theme.ink)
            if stacked:
                left = at(max(low, 0))
                for i, s in enumerate(series):
                    value = s["values"][j]
                    color = value_color(s, i, j)
                    width = value / span * plot_w
                    canvas.rect(left, middle - thickness / 2, width,
                                thickness, color)
                    label = (s.get("labels") or [None] * len(categories))[j]
                    if label is None and chart.get("inside") and value:
                        label = number(value, chart)
                    if label and canvas.width(label, 6.5) < width - 4:
                        canvas.text(left + width / 2, middle + 2.3, label,
                                    6.5, theme.on(color), "middle")
                    left += width
                if show:
                    canvas.text(left + 3, middle + 2.3,
                                number(sums[j], chart), 6.5, theme.ink,
                                bold=True)
            else:
                band = thickness / len(series)
                for i, s in enumerate(series):
                    value = s["values"][j]
                    if value is None:
                        continue
                    top_y = middle - thickness / 2 + i * band
                    x0, x1 = sorted((at(max(low, 0)), at(value)))
                    canvas.rect(x0, top_y, x1 - x0, band * 0.9,
                                value_color(s, i, j), radius=theme.radius)
                    if show and value < 0:
                        canvas.text(x0 - 3, top_y + band * 0.45 + 2.3,
                                    number(value, chart), 6.5, theme.ink,
                                    "end")
                    elif show:
                        canvas.text(x1 + 3, top_y + band * 0.45 + 2.3,
                                    number(value, chart), 6.5, theme.ink)
        if chart.get("target") is not None:
            tx = at(chart["target"])
            canvas.line(tx, plot_top - 2, tx, plot_top + rows * row,
                        theme.status["bad"], 1, "3,2")
            canvas.text(tx + 2, plot_top + 5,
                        chart.get("target_label", "target"), 6.5,
                        theme.status["bad"])
        return

    box, scale = axis_frame(canvas, chart, x, y + top + 6, w,
                            h - top - 22, low, high * 1.08)
    count = len(categories)
    slot = box[2] / count
    thickness = slot * chart.get("thickness", 0.62)
    every = max(1, math.ceil(count * canvas.width(max(categories, key=len),
                                                  6.5) / (box[2] * 0.95)))
    for j, category in enumerate(categories):
        center = box[0] + slot * (j + 0.5)
        if j % every == 0:
            canvas.text(center, box[1] + box[3] + 10, category, 6.5,
                        theme.muted, "middle")
        if stacked:
            bottom = scale(0)
            for i, s in enumerate(series):
                value = s["values"][j]
                height = scale(0) - scale(value) if value > 0 else 0
                color = value_color(s, i, j)
                canvas.rect(center - thickness / 2, bottom - height,
                            thickness, height, color)
                if chart.get("inside") and height > 11 and value:
                    canvas.text(center, bottom - height / 2 + 2.3,
                                number(value, chart), 6, theme.on(color),
                                "middle")
                bottom -= height
            if show:
                canvas.text(center, bottom - 3, number(sums[j], chart), 6.5,
                            theme.ink, "middle", bold=True)
        else:
            band = thickness / len(series)
            for i, s in enumerate(series):
                value = s["values"][j]
                if value is None:
                    continue
                left = center - thickness / 2 + i * band
                y0, y1 = sorted((scale(0), scale(value)))
                canvas.rect(left, y0, band * 0.92, y1 - y0,
                            value_color(s, i, j), radius=theme.radius)
                if show:
                    label_y = y0 - 3 if value >= 0 else y1 + 8
                    canvas.text(left + band * 0.46, label_y,
                                number(value, chart), 6.5, theme.ink,
                                "middle")
    if chart.get("target") is not None:
        ty = scale(chart["target"])
        canvas.line(box[0], ty, box[0] + box[2], ty, theme.status["bad"], 1,
                    "3,2")
        canvas.text(box[0] + box[2], ty - 3,
                    chart.get("target_label", "target"), 6.5,
                    theme.status["bad"], "end")


def arc(cx, cy, radius, inner, start, end):
    """The path of a ring segment between the angles, clockwise from the
    top, in radians."""
    end = min(end, start + 2 * math.pi - 1e-4)
    large = 1 if end - start > math.pi else 0

    def point(r, angle):
        return cx + r * math.sin(angle), cy - r * math.cos(angle)

    (x1, y1), (x2, y2) = point(radius, start), point(radius, end)
    (x3, y3), (x4, y4) = point(inner, end), point(inner, start)
    return (f"M{x1:.2f},{y1:.2f} A{radius:.2f},{radius:.2f} 0 {large} 1 "
            f"{x2:.2f},{y2:.2f} L{x3:.2f},{y3:.2f} A{inner:.2f},{inner:.2f} "
            f"0 {large} 0 {x4:.2f},{y4:.2f} Z")


def donut(canvas, chart, x, y, w, h):
    """A ring of segments (label, value, color) with a center (big, small)
    and a legend with values and shares."""
    theme = canvas.theme
    top = chart_title(canvas, chart, x, y, w)
    segments = chart["segments"]
    total = sum(s[1] for s in segments)
    shares = chart.get("shares", "%" not in chart.get("format", ""))
    legend_w = (max(canvas.width(seg[0], 7) for seg in segments)
                + max(canvas.width(number(seg[1], chart), 7, True)
                      for seg in segments) + (30 if shares else 0) + 26)
    beside = (w - legend_w) / 2 - 8
    stacked = beside < 34 and (h - top) > 120
    if stacked:
        # too narrow for a legend beside the ring: the legend goes below
        row = 10
        radius = min(w / 2 - 4, (h - top - 8 - row * len(segments)) / 2)
        cx, cy = x + w / 2, y + top + radius + 2
    else:
        radius = max(min((h - top) / 2 - 2, w * 0.22, beside),
                     min(22, (h - top) / 2 - 2))
        cx, cy = x + radius + 2, y + top + (h - top) / 2
    hole = radius * chart.get("hole", 0.6)
    angle = 0
    for index, segment in enumerate(segments):
        color = theme.color(segment[2] if len(segment) > 2 else None, index)
        sweep = segment[1] / total * 2 * math.pi
        canvas.path(arc(cx, cy, radius, hole, angle, angle + sweep), color,
                    theme.page, 1)
        angle += sweep
    if chart.get("center"):
        big, small = chart["center"]
        size = min(15, radius * 0.42)
        while size > 6 and canvas.width(big, size, True) > hole * 1.7:
            size -= 0.5
        canvas.text(cx, cy + 2, big, size, theme.ink, "middle", bold=True)
        if hole > 18:
            canvas.text(cx, cy + 11, small, 6.5, theme.muted, "middle")
    if stacked:
        lx, ly = x + 2, cy + radius + 12
    else:
        lx = cx + radius + 14
        row = min(14, (h - top) / len(segments))
        ly = cy - row * len(segments) / 2 + row * 0.7
    value_x = x + w
    values_width = max(canvas.width(number(s[1], chart), 7, True)
                       for s in segments)
    for index, segment in enumerate(segments):
        color = theme.color(segment[2] if len(segment) > 2 else None, index)
        canvas.rect(lx, ly - 6.5, 8, 8, color, radius=theme.radius)
        label = segment[0]
        while len(label) > 2 and canvas.width(label, 7) > (
                value_x - lx - values_width - (42 if shares else 16)):
            label = label[:-2] + "…"
        canvas.text(lx + 12, ly, label, 7, theme.ink)
        canvas.text(value_x - (26 if shares else 0), ly,
                    number(segment[1], chart), 7, theme.ink, "end",
                    bold=True)
        if shares:
            canvas.text(value_x, ly, f"{segment[1] / total:.0%}", 7,
                        theme.muted, "end")
        ly += row


def risk_matrix(canvas, chart, x, y, w, h):
    """A five by five matrix of likelihood and impact with the risks (id,
    likelihood, impact) placed in their cells, and their residual position
    (id, likelihood, impact) as rings; with a list of the risks next to it
    when the risks have a fourth element, their description."""
    theme = canvas.theme
    top = chart_title(canvas, chart, x, y, w)
    levels = chart.get("levels", 5)
    axis = 14
    side = min(h - top - axis - 12, (w - axis) * (0.55 if any(
        len(r) > 3 for r in chart["risks"]) else 1))
    cell = side / levels
    mx, my = x + axis + 10, y + top
    for row in range(levels):
        impact = levels - row
        for col in range(levels):
            likelihood = col + 1
            score = impact * likelihood
            if score >= 15:
                color = theme.status["bad"]
            elif score >= 10:
                color = theme.tint(theme.status["bad"], 0.45)
            elif score >= 5:
                color = theme.tint(theme.status["warn"], 0.35)
            else:
                color = theme.tint(theme.status["good"], 0.45)
            canvas.rect(mx + col * cell, my + row * cell, cell, cell, color,
                        theme.page, 1.5)
    canvas.parts.append(
        f'<text x="{x + 6:.2f}" y="{my + side / 2:.2f}" '
        f'font-family="{theme.font}" font-size="6.5" fill="{theme.muted}" '
        f'text-anchor="middle" transform="rotate(-90 {x + 6:.2f} '
        f'{my + side / 2:.2f})">impact</text>')
    for index in range(levels):
        canvas.text(mx - 4, my + index * cell + cell / 2 + 2.3,
                    str(levels - index), 6.5, theme.muted, "end")
        canvas.text(mx + index * cell + cell / 2, my + side + 9,
                    str(index + 1), 6.5, theme.muted, "middle")
    canvas.text(mx + side / 2, my + side + 18, "likelihood", 6.5,
                theme.muted, "middle")
    occupied = {}
    pill = min(cell * 0.42, 15)

    def place(likelihood, impact):
        key = (likelihood, impact)
        index = occupied.get(key, 0)
        occupied[key] = index + 1
        per_row = max(1, int(cell // (pill + 2)))
        px = (mx + (likelihood - 1) * cell + 3 + pill / 2
              + (index % per_row) * (pill + 2))
        py = (my + (levels - impact) * cell + 3 + pill / 2
              + (index // per_row) * (pill + 2))
        return px, py

    for residual in chart.get("residual", []):
        px, py = place(residual[1], residual[2])
        canvas.circle(px, py, pill / 2, theme.page, theme.ink, 1)
        canvas.text(px, py + 2.2, residual[0], min(6, pill * 0.45),
                    theme.ink, "middle")
    for risk in chart["risks"]:
        px, py = place(risk[1], risk[2])
        canvas.circle(px, py, pill / 2, theme.ink)
        canvas.text(px, py + 2.2, risk[0], min(6, pill * 0.45), theme.page,
                    "middle", bold=True)
    described = [r for r in chart["risks"] if len(r) > 3]
    if described:
        lx = mx + side + 18
        ly = my + 8
        for risk in described:
            canvas.text(lx, ly, risk[0], 7, theme.accent, bold=True)
            used = canvas.lines(lx + 20, ly, risk[3], 7, x + w - lx - 20,
                                theme.ink, limit=2)
            ly += used * 8.4 + 4
            if ly > y + h - 4:
                break
        if chart.get("residual"):
            canvas.circle(lx + 3, y + h - 6, 3, theme.page, theme.ink, 1)
            canvas.text(lx + 10, y + h - 4, "after treatment", 6.5,
                        theme.muted)


def heatmap(canvas, chart, x, y, w, h):
    """A table of rows and cols with colored cells. Values are numbers,
    colored from low to high (or by thresholds, (value, color) from the
    lowest), or texts colored by the badges of the chart, {text: color}."""
    theme = canvas.theme
    top = chart_title(canvas, chart, x, y, w)
    rows, cols, values = chart["rows"], chart["cols"], chart["values"]
    size = chart.get("size", 7)
    label_width = min(max(canvas.width(r, size) for r in rows) + 8,
                      w * chart.get("labels", 0.3))
    header = chart.get("header", 16)
    cell_w = (w - label_width) / len(cols)
    cell_h = (h - top - header) / len(rows)
    numeric = [v for row in values for v in row
               if isinstance(v, (int, float))]
    low, high = (min(numeric), max(numeric)) if numeric else (0, 1)
    base = theme.color(chart.get("color", "accent"))
    for index, col in enumerate(cols):
        canvas.lines(x + label_width + cell_w * (index + 0.5),
                     y + top + header - 4 - (6.5 * 1.15 if canvas.width(
                         col, 6.5) > cell_w - 2 else 0),
                     col, 6.5, cell_w - 2, theme.muted, "middle",
                     leading=1.15, limit=2)
    for r, row in enumerate(rows):
        cy = y + top + header + r * cell_h
        canvas.text(x, cy + cell_h / 2 + size * 0.35, row, size, theme.ink)
        for c, value in enumerate(values[r]):
            cx = x + label_width + c * cell_w
            if isinstance(value, (int, float)):
                if chart.get("thresholds"):
                    color = theme.color(chart["thresholds"][0][1])
                    for limit, name in chart["thresholds"]:
                        if value >= limit:
                            color = theme.color(name)
                else:
                    t = (value - low) / ((high - low) or 1)
                    color = mix(theme.tint(base, 0.9), base, t)
                label = number(value, chart)
            elif value in (None, ""):
                color, label = theme.tint(theme.grid, 0.6), ""
            else:
                color = theme.color(chart.get("badges", {}).get(value,
                                                                "neutral"))
                label = value
            canvas.rect(cx + 1, cy + 1, cell_w - 2, cell_h - 2, color,
                        radius=theme.radius)
            if chart.get("show", True) and label:
                canvas.text(cx + cell_w / 2, cy + cell_h / 2 + 2.4, label,
                            min(7, cell_h * 0.5), theme.on(color), "middle",
                            bold=chart.get("bold", False))


def kpis(canvas, chart, x, y, w, h):
    """A row of tiles with label, value, note, status, delta and spark (a
    list of numbers drawn as a small line)."""
    theme = canvas.theme
    top = chart_title(canvas, chart, x, y, w)
    tiles = chart["tiles"]
    gap = 6
    tile_w = (w - gap * (len(tiles) - 1)) / len(tiles)
    tile_h = h - top
    style = chart.get("style", "card")
    for index, tile in enumerate(tiles):
        tx = x + index * (tile_w + gap)
        ty = y + top
        status = theme.color(tile.get("status", "accent"))
        if style == "card":
            canvas.rect(tx, ty, tile_w, tile_h, theme.tint(status, 0.88),
                        radius=theme.radius + 1)
            canvas.rect(tx, ty, 3, tile_h, status)
        elif style == "outline":
            canvas.rect(tx, ty, tile_w, tile_h, None, status, 1,
                        radius=theme.radius + 1)
        else:
            canvas.line(tx, ty, tx + tile_w, ty, status, 2)
        pad = 8
        canvas.text(tx + pad, ty + 11, tile["label"].upper(), 6.2,
                    theme.muted, bold=True)
        size = min(chart.get("size", 17), (tile_h - 22) * 0.75)
        value = str(tile["value"])
        while canvas.width(value, size, True) > tile_w - 2 * pad and size > 8:
            size -= 1
        canvas.text(tx + pad, ty + 14 + size, value, size, theme.ink,
                    bold=True)
        if tile.get("delta"):
            delta = tile["delta"]
            good = tile.get("delta_status", "good" if delta.startswith(
                ("+", "▲")) else "bad")
            canvas.text(tx + pad + canvas.width(value, size, True) + 5,
                        ty + 14 + size, delta, 7, theme.color(good),
                        bold=True)
        if tile.get("note"):
            canvas.text(tx + pad, ty + tile_h - 6, tile["note"], 6.5,
                        theme.muted)
        if tile.get("spark"):
            spark = tile["spark"]
            sw, sh = tile_w * 0.32, (tile_h - 22) * 0.5
            sx, sy = tx + tile_w - sw - pad, ty + 16
            low, high = min(spark), max(spark)
            points = [(sx + i * sw / (len(spark) - 1),
                       sy + sh - (v - low) / ((high - low) or 1) * sh)
                      for i, v in enumerate(spark)]
            canvas.polyline(points, status, 1.2)
            canvas.circle(*points[-1], 1.8, status)


def timeline(canvas, chart, x, y, w, h):
    """Events (at, label, sub, status: done, now or planned) along a line
    from start to end, with phases (start, end, label) as bands under it
    and ticks (at, label)."""
    theme = canvas.theme
    top = chart_title(canvas, chart, x, y, w)
    start, end = chart["start"], chart["end"]
    left, right = x + 6, x + w - 6

    def at(value):
        return left + (value - start) / (end - start) * (right - left)

    phases = chart.get("phases", [])
    line_y = y + top + (h - top) * chart.get("line", 0.5)
    band = 12
    for index, (p_start, p_end, label) in enumerate(phases):
        color = theme.color(None, index)
        canvas.rect(at(p_start) + 0.5, line_y - band / 2,
                    at(p_end) - at(p_start) - 1, band, color)
        if canvas.width(label, 6.5, True) < at(p_end) - at(p_start) - 4:
            canvas.text((at(p_start) + at(p_end)) / 2, line_y + 2.3, label,
                        6.5, theme.on(color), "middle", bold=True)
    if not phases:
        canvas.line(left, line_y, right, line_y, theme.ink, 1.5)
    for position, label in chart.get("ticks", []):
        canvas.line(at(position), line_y + band / 2, at(position),
                    line_y + band / 2 + 3, theme.muted, 0.6)
        anchor = ("start" if at(position) < left + 12 else "end"
                  if at(position) > right - 12 else "middle")
        canvas.text(at(position), line_y + band / 2 + 11, label, 6.5,
                    theme.muted, anchor)
    events = sorted(chart["events"], key=lambda e: e["at"])
    room = (h - top) * 0.5 - band / 2 - 4
    for index, event in enumerate(events):
        ex = at(event["at"])
        up = event.get("side", "up" if index % 2 == 0 else "down") == "up"
        stem = room - event.get("lift", 0) - 24
        if not up and chart.get("ticks"):
            stem -= 10
        stem = max(stem * event.get("length", 1), 10)
        status = event.get("status", "planned")
        color = (theme.ink if status == "done" else theme.accent
                 if status == "now" else theme.muted)
        y1 = line_y - band / 2 if up else line_y + band / 2
        y2 = y1 - stem if up else y1 + stem
        canvas.line(ex, y1, ex, y2, color, 0.6)
        if status == "done":
            canvas.circle(ex, line_y, 3.5, theme.ink, theme.page, 1)
        elif status == "now":
            canvas.circle(ex, line_y, 4.5, theme.page, theme.accent, 2)
        else:
            canvas.circle(ex, line_y, 3.5, theme.page, theme.muted, 1)
        anchor = ("start" if ex < left + 40 else "end" if ex > right - 40
                  else "middle")
        width = chart.get("label_width", 90)
        if up:
            sub_y = y2 - 3
            lines_count = len(wrap(event["label"], 7, width, theme.bold_font,
                                   True))
            if event.get("sub"):
                canvas.text(ex, sub_y, event["sub"], 6.5, theme.muted, anchor)
                sub_y -= 8.5
            canvas.lines(ex, sub_y - (lines_count - 1) * 8.2, event["label"],
                         7, width, color if status != "planned" else
                         theme.ink, anchor, True, 1.17)
        else:
            used = canvas.lines(ex, y2 + 8, event["label"], 7, width,
                                color if status != "planned" else theme.ink,
                                anchor, True, 1.17)
            if event.get("sub"):
                canvas.text(ex, y2 + 8 + used * 8.2, event["sub"], 6.5,
                            theme.muted, anchor)


def waterfall(canvas, chart, x, y, w, h):
    """Steps (label, value) from a first total, with "total" steps
    (label, None) showing the running total; increases are bad and
    decreases good when invert is set, e.g. for costs."""
    theme = canvas.theme
    top = chart_title(canvas, chart, x, y, w)
    steps = chart["steps"]
    running, bars = 0, []
    for index, (label, value) in enumerate(steps):
        if value is None:
            bars.append((label, 0, running, "total"))
        elif index == 0:
            running = value
            bars.append((label, 0, value, "total"))
        else:
            bars.append((label, running, running + value,
                         "up" if value >= 0 else "down"))
            running += value
    low = min(min(b[1], b[2]) for b in bars)
    high = max(max(b[1], b[2]) for b in bars)
    box, scale = axis_frame(canvas, chart, x, y + top + 6, w, h - top - 30,
                            min(low, 0), high * 1.08)
    slot = box[2] / len(bars)
    thickness = slot * 0.62
    invert = chart.get("invert", False)
    previous = None
    for index, (label, a, b, kind) in enumerate(bars):
        center = box[0] + slot * (index + 0.5)
        if kind == "total":
            color = theme.color(chart.get("total_color", "ink"))
        elif (kind == "up") != invert:
            color = theme.status["good"]
        else:
            color = theme.status["bad"]
        y0, y1 = sorted((scale(a), scale(b)))
        canvas.rect(center - thickness / 2, y0, thickness, max(y1 - y0, 1),
                    color, radius=theme.radius / 2)
        value = b if kind == "total" else b - a
        text = number(abs(value) if kind != "total" else value, chart)
        if kind != "total":
            text = ("+" if value >= 0 else "−") + text
        canvas.text(center, y0 - 3, text, 6.5, theme.ink, "middle",
                    bold=kind == "total")
        if previous is not None:
            canvas.line(previous, scale(a if kind != "total" else b),
                        center - thickness / 2,
                        scale(a if kind != "total" else b), theme.muted,
                        0.5, "1.5,1.5")
        previous = center + thickness / 2
        canvas.lines(center, box[1] + box[3] + 9, label, 6.5, slot - 2,
                     theme.muted, "middle", leading=1.15, limit=2)


def quadrant(canvas, chart, x, y, w, h):
    """Points (label, x, y, color) on two axes from 0 to 10, with the names
    of the quadrants (top left, top right, bottom left, bottom right) and
    the names of the axes, x and y."""
    theme = canvas.theme
    top = chart_title(canvas, chart, x, y, w)
    groups = chart.get("groups", [])
    entries = [(name, theme.color(i)) for i, name in enumerate(groups)]
    top = max(top, series_legend(canvas, chart, x, y, w, entries))
    px, py = x + 14, y + top + 2
    pw, ph = w - 14, h - top - 16
    names = chart.get("quadrants", ["", "", "", ""])
    tints = [0.9, 0.8, 0.95, 0.9]
    for index in range(4):
        qx = px + (index % 2) * pw / 2
        qy = py + (index // 2) * ph / 2
        canvas.rect(qx + 1, qy + 1, pw / 2 - 2, ph / 2 - 2,
                    theme.tint(theme.accent, tints[index]),
                    radius=theme.radius)
        canvas.text(qx + (6 if index % 2 == 0 else pw / 2 - 6),
                    qy + (11 if index < 2 else ph / 2 - 6),
                    names[index].upper(), 6.2, theme.muted,
                    "start" if index % 2 == 0 else "end", bold=True)
    canvas.text(px + pw / 2, py + ph + 11, chart.get("x", "") + " →", 6.5,
                theme.muted, "middle")
    canvas.parts.append(
        f'<text x="{x + 8:.2f}" y="{py + ph / 2:.2f}" '
        f'font-family="{theme.font}" font-size="6.5" fill="{theme.muted}" '
        f'text-anchor="middle" transform="rotate(-90 {x + 8:.2f} '
        f'{py + ph / 2:.2f})">{escape(chart.get("y", ""))} →</text>')
    for point in chart["points"]:
        label, vx, vy = point[:3]
        color = theme.color(point[3] if len(point) > 3 else "ink")
        cx = px + 6 + vx / 10 * (pw - 12)
        cy = py + ph - 6 - vy / 10 * (ph - 12)
        radius = point[4] if len(point) > 4 else 3.5
        canvas.circle(cx, cy, radius, color, theme.page, 0.75)
        right = cx + canvas.width(label, 6.5) + 8 < px + pw
        canvas.text(cx + (radius + 2) * (1 if right else -1), cy + 2.3,
                    label, 6.5, theme.ink, "start" if right else "end")


def progress(canvas, chart, x, y, w, h):
    """Rows of label, value, target, status and note as bars on a track
    from 0 to max."""
    theme = canvas.theme
    top = chart_title(canvas, chart, x, y, w)
    items = chart["items"]
    size = chart.get("size", 7.5)
    label_width = min(max(canvas.width(i["label"], size) for i in items) + 10,
                      w * chart.get("labels", 0.4))
    value_width = max(canvas.width(number(i.get("display", i["value"]),
                                          chart), 7, True)
                      for i in items) + 8
    track_x, track_w = x + label_width, w - label_width - value_width
    row = (h - top) / len(items)
    maximum = chart.get("max", 100)
    for index, item in enumerate(items):
        ry = y + top + index * row
        middle = ry + row / 2 - (3 if item.get("note") else 0)
        canvas.text(x, middle + size * 0.35, item["label"], size, theme.ink)
        if item.get("note"):
            canvas.text(x, middle + size * 0.35 + 9, item["note"], 6.3,
                        theme.muted)
        thickness = min(row * 0.38, 8)
        color = theme.color(item.get("status", chart.get("color", "accent")))
        canvas.rect(track_x, middle - thickness / 2, track_w, thickness,
                    theme.tint(theme.grid, 0.4), radius=thickness / 2)
        share = max(0, min(item["value"] / maximum, 1))
        canvas.rect(track_x, middle - thickness / 2, track_w * share,
                    thickness, color, radius=thickness / 2)
        if item.get("target") is not None:
            tx = track_x + track_w * min(item["target"] / maximum, 1)
            canvas.line(tx, middle - thickness, tx, middle + thickness,
                        theme.ink, 1.2)
        canvas.text(x + w, middle + 2.5,
                    number(item.get("display", item["value"]), chart), 7,
                    theme.ink, "end", bold=True)


def board(canvas, chart, x, y, w, h):
    """Columns with title, tone and cards (text or (text, meta))."""
    theme = canvas.theme
    top = chart_title(canvas, chart, x, y, w)
    columns = chart["columns"]
    gap = 6
    col_w = (w - gap * (len(columns) - 1)) / len(columns)
    size = chart.get("size", 7)
    for index, column in enumerate(columns):
        cx = x + index * (col_w + gap)
        cy = y + top
        tone = theme.color(column.get("tone"), index)
        canvas.rect(cx, cy, col_w, h - top, theme.tint(tone, 0.92),
                    radius=theme.radius + 1)
        canvas.rect(cx, cy, col_w, 16, tone, radius=theme.radius + 1)
        canvas.rect(cx, cy + 10, col_w, 6, tone)
        title = column["title"]
        canvas.text(cx + 6, cy + 11, title.upper(), 6.8, theme.on(tone),
                    bold=True)
        if column.get("count", True):
            canvas.text(cx + col_w - 6, cy + 11, str(len(column["cards"])),
                        6.8, theme.on(tone), "end", bold=True)
        card_y = cy + 21
        for card in column["cards"]:
            text, meta = (card, None) if isinstance(card, str) else card
            rows = wrap(text, size, col_w - 18, theme.font)
            card_h = len(rows) * size * 1.2 + 7 + (9 if meta else 0)
            if card_y + card_h > y + h - 3:
                break
            canvas.rect(cx + 4, card_y, col_w - 8, card_h, theme.page,
                        theme.tint(tone, 0.6), 0.6, theme.radius)
            canvas.rect(cx + 4, card_y, 2, card_h, tone)
            canvas.lines(cx + 10, card_y + size + 2, text, size,
                         col_w - 18, theme.ink)
            if meta:
                canvas.text(cx + 10, card_y + card_h - 4, meta, 6.2,
                            theme.muted)
            card_y += card_h + 4


def card_height(chart, w):
    """The height a board needs for its fullest column."""
    columns = chart["columns"]
    col_w = (w - 6 * (len(columns) - 1)) / len(columns)
    size = chart.get("size", 7)
    font = chart["_font"]
    tallest = 0
    for column in columns:
        total = 21
        for card in column["cards"]:
            text, meta = (card, None) if isinstance(card, str) else card
            total += (len(wrap(text, size, col_w - 18, font)) * size * 1.2
                      + 11 + (9 if meta else 0))
        tallest = max(tallest, total)
    return tallest + 2 + (16 if chart.get("title") else 0)


def tree(canvas, chart, x, y, w, h):
    """A breakdown: the root (label, code, children) over a row of its
    children, each over a column of its own children. Nodes can have a
    status color and a note."""
    theme = canvas.theme
    top = chart_title(canvas, chart, x, y, w)
    root = chart["root"]
    children = root["children"]
    gap = 6
    col_w = (w - gap * (len(children) - 1)) / len(children)
    size = chart.get("size", 6.8)

    def node(nx, ny, nw, item, level):
        label = (f"{item['code']}  " if item.get("code") else "") + \
            item["label"]
        rows = wrap(label, size, nw - 10, theme.bold_font if level < 2
                    else theme.font, level < 2)
        nh = len(rows) * size * 1.2 + 7 + (8 if item.get("note") else 0)
        status = theme.color(item.get("status", "accent" if level == 0
                                      else 0 if level == 1 else "grid"))
        if level == 0:
            fill, ink = theme.ink, theme.page
        elif level == 1:
            fill, ink = status, theme.on(status)
        else:
            fill, ink = theme.page, theme.ink
        canvas.rect(nx, ny, nw, nh, fill,
                    theme.tint(status, 0.3) if level > 1 else None, 0.75,
                    theme.radius)
        if level > 1 and item.get("status"):
            canvas.rect(nx, ny, 2.5, nh, status)
        canvas.lines(nx + nw / 2 if level < 2 else nx + 6, ny + size + 2,
                     label, size, nw - 10, ink,
                     "middle" if level < 2 else "start", level < 2)
        if item.get("note"):
            canvas.text(nx + (nw / 2 if level < 2 else 6), ny + nh - 3,
                        item["note"], 6, theme.muted if level > 1 else ink,
                        "middle" if level < 2 else "start")
        return nh

    root_w = min(w * 0.4, 200)
    root_h = node(x + (w - root_w) / 2, y + top, root_w, root, 0)
    bus = y + top + root_h + 8
    canvas.line(x + w / 2, y + top + root_h, x + w / 2, bus, theme.muted, 0.75)
    first = x + col_w / 2
    last = x + (len(children) - 1) * (col_w + gap) + col_w / 2
    canvas.line(first, bus, last, bus, theme.muted, 0.75)
    for index, child in enumerate(children):
        cx = x + index * (col_w + gap)
        canvas.line(cx + col_w / 2, bus, cx + col_w / 2, bus + 7,
                    theme.muted, 0.75)
        ch = node(cx, bus + 7, col_w, child, 1)
        cy = bus + 7 + ch + 5
        spine = cx + 4
        for grandchild in child.get("children", []):
            gh = node(cx + 9, cy, col_w - 9, grandchild, 2)
            canvas.line(spine, cy + gh / 2, cx + 9, cy + gh / 2,
                        theme.muted, 0.6)
            last_mid = cy + gh / 2
            cy += gh + 4
        if child.get("children"):
            canvas.line(spine, bus + 7 + ch, spine, last_mid, theme.muted,
                        0.6)


def tree_height(chart, w):
    root = chart["root"]
    children = root["children"]
    col_w = (w - 6 * (len(children) - 1)) / len(children)
    size = chart.get("size", 6.8)
    bold, font = chart["_bold_font"], chart["_font"]

    def nh(item, nw, level):
        label = (f"{item['code']}  " if item.get("code") else "") + \
            item["label"]
        return (len(wrap(label, size, nw - 10, bold if level < 2 else font,
                         level < 2)) * size * 1.2 + 7
                + (8 if item.get("note") else 0))

    tallest = max(nh(child, col_w, 1) + 5 + sum(
        nh(g, col_w - 9, 2) + 4 for g in child.get("children", []))
        for child in children)
    return ((16 if chart.get("title") else 0) + nh(root, min(w * 0.4, 200), 0)
            + 15 + tallest + 2)


def funnel(canvas, chart, x, y, w, h):
    """Stages (label, value) as centered bars from the widest, with the
    share kept from the previous stage; a pyramid grows downwards."""
    theme = canvas.theme
    top = chart_title(canvas, chart, x, y, w)
    stages = chart["stages"]
    label_width = max(canvas.width(s[0], 7) for s in stages) + 10
    value_width = 70
    bx, bw = x + label_width, w - label_width - value_width
    row = (h - top) / len(stages)
    widest = max(s[1] for s in stages)
    base = theme.color(chart.get("color", "accent"))
    for index, stage in enumerate(stages):
        label, value = stage[:2]
        ry = y + top + index * row
        width = max(bw * (value / widest) ** chart.get("power", 1), 4)
        color = theme.color(stage[2]) if len(stage) > 2 else mix(
            base, theme.page, index / len(stages) * 0.55)
        canvas.rect(bx + (bw - width) / 2, ry + 1.5, width, row - 3, color,
                    radius=theme.radius)
        canvas.text(x, ry + row / 2 + 2.5, label, 7, theme.ink)
        canvas.text(x + w - value_width + 6, ry + row / 2 + 2.5,
                    number(value, chart), 7.5, theme.ink, bold=True)
        if index and chart.get("shares", True):
            share = value / stages[index - 1][1]
            canvas.text(x + w, ry + row / 2 + 2.5, f"{share:.0%}", 6.5,
                        theme.muted, "end")


def chevrons(canvas, chart, x, y, w, h):
    """Steps (label, sub, status: done, now or planned) as arrows in a row,
    with a note under each."""
    theme = canvas.theme
    top = chart_title(canvas, chart, x, y, w)
    steps = chart["steps"]
    tip = 9
    step_w = (w + tip * (len(steps) - 1) * 0.0) / len(steps)
    arrow_h = min(chart.get("arrow", 34), h - top)
    for index, step in enumerate(steps):
        sx = x + index * step_w
        status = step.get("status", "planned")
        if status == "done":
            fill = theme.ink
        elif status == "now":
            fill = theme.accent
        else:
            fill = theme.tint(theme.muted, 0.75)
        if step.get("color"):
            fill = theme.color(step["color"])
        sy = y + top
        notch = tip if index else 0
        points = [(sx, sy), (sx + step_w - 2, sy),
                  (sx + step_w - 2 + tip, sy + arrow_h / 2),
                  (sx + step_w - 2, sy + arrow_h), (sx, sy + arrow_h),
                  (sx + notch, sy + arrow_h / 2)]
        if index == len(steps) - 1:
            points[2] = (sx + step_w - 2, sy + arrow_h / 2)
        canvas.polygon(points, fill)
        ink = theme.on(fill)
        rows = wrap(step["label"], 7, step_w - tip - 10, theme.bold_font,
                    True)[:2]
        first = sy + arrow_h / 2 + 2.5 - (len(rows) - 1) * 4.2
        for line_index, row in enumerate(rows):
            canvas.text(sx + notch + 5, first + line_index * 8.4, row, 7,
                        ink, bold=True)
        if step.get("sub"):
            canvas.lines(sx + 2, sy + arrow_h + 10, step["sub"], 6.5,
                         step_w - 6, theme.muted, limit=chart.get(
                             "sub_lines", 4))


def sankey(canvas, chart, x, y, w, h):
    """Flows between nodes in columns. Nodes have id, label, col and color;
    links are (source id, target id, value). A node is as tall as the
    larger of what flows in and what flows out."""
    theme = canvas.theme
    top = chart_title(canvas, chart, x, y, w)
    nodes = {node["id"]: dict(node) for node in chart["nodes"]}
    order = [node["id"] for node in chart["nodes"]]
    for node in nodes.values():
        node["in"] = sum(link[2] for link in chart["links"] if link[1] == node["id"])
        node["out"] = sum(link[2] for link in chart["links"]
                          if link[0] == node["id"])
        node["value"] = node.get("value", max(node["in"], node["out"]))
    columns = max(node["col"] for node in nodes.values()) + 1
    size = chart.get("size", 7)
    node_w, gap = 8, chart.get("gap", 8)

    def label_width(col):
        return max([canvas.width(n["label"], size, True) for n in
                    nodes.values() if n["col"] == col] + [0]) + 8

    left_room = label_width(0)
    right_room = max(label_width(columns - 1),
                     canvas.width("000,000", size) + 8)
    span = w - left_room - right_room - node_w
    height = h - top - 4
    scale = min(
        (height - gap * (sum(1 for n in nodes.values() if n["col"] == c)
                         - 1))
        / sum(n["value"] for n in nodes.values() if n["col"] == c)
        for c in range(columns))
    for col in range(columns):
        members = [nodes[i] for i in order if nodes[i]["col"] == col]
        total = (sum(n["value"] for n in members) * scale
                 + gap * (len(members) - 1))
        cursor = y + top + 2 + (height - total) / 2
        for node in members:
            node["x"] = x + left_room + span * col / max(columns - 1, 1)
            node["y"] = cursor
            node["h"] = max(node["value"] * scale, 1)
            node["in_at"] = node["out_at"] = cursor
            cursor += node["h"] + gap
    for index, (source, target, value, *rest) in enumerate(chart["links"]):
        a, b = nodes[source], nodes[target]
        color = theme.color(rest[0] if rest else b.get("color", index))
        thick = value * scale
        x1, x2 = a["x"] + node_w, b["x"]
        y1, y2 = a["out_at"], b["in_at"]
        a["out_at"] += thick
        b["in_at"] += thick
        middle = (x1 + x2) / 2
        canvas.path(f"M{x1:.2f},{y1:.2f} C{middle:.2f},{y1:.2f} "
                    f"{middle:.2f},{y2:.2f} {x2:.2f},{y2:.2f} "
                    f"L{x2:.2f},{y2 + thick:.2f} C{middle:.2f},"
                    f"{y2 + thick:.2f} {middle:.2f},{y1 + thick:.2f} "
                    f"{x1:.2f},{y1 + thick:.2f} Z",
                    theme.tint(color, chart.get("tint", 0.62)))
    for index, key in enumerate(order):
        node = nodes[key]
        color = theme.color(node.get("color", index))
        canvas.rect(node["x"], node["y"], node_w, node["h"], color)
        middle = node["y"] + node["h"] / 2
        value = number(node["value"], chart)
        if node["col"] == 0:
            canvas.text(node["x"] - 4, middle - 1, node["label"], size,
                        theme.ink, "end", bold=True)
            canvas.text(node["x"] - 4, middle + 7, value, size - 0.5,
                        theme.muted, "end")
            continue
        label_x = node["x"] + node_w + 4
        if node["col"] != columns - 1:
            box = max(canvas.width(node["label"], size, True),
                      canvas.width(value, size - 0.5)) + 6
            canvas.rect(label_x - 2, middle - 9, box, 19, theme.page,
                        radius=2)
        canvas.text(label_x, middle - 1, node["label"], size, theme.ink,
                    bold=True)
        canvas.text(label_x, middle + 7, value, size - 0.5, theme.muted)


def gauges(canvas, chart, x, y, w, h):
    """Half-circle dials in a row, each with label, value from min to max,
    display, status, target and note."""
    theme = canvas.theme
    top = chart_title(canvas, chart, x, y, w)
    items = chart["items"]
    cell = w / len(items)
    radius = min(cell / 2 - 10, h - top - 34)
    for index, item in enumerate(items):
        cx = x + cell * (index + 0.5)
        cy = y + top + 4 + radius
        low, high = item.get("min", 0), item.get("max", 100)
        share = max(0, min((item["value"] - low) / (high - low), 1))
        color = theme.color(item.get("status", "accent"))
        inner = radius * 0.74
        canvas.path(arc(cx, cy, radius, inner, -math.pi / 2, math.pi / 2),
                    theme.tint(theme.grid, 0.45))
        if share > 0:
            canvas.path(arc(cx, cy, radius, inner, -math.pi / 2,
                            -math.pi / 2 + math.pi * share), color)
        if item.get("target") is not None:
            angle = (-math.pi / 2 + math.pi * (item["target"] - low)
                     / (high - low))
            canvas.line(cx + (inner - 3) * math.sin(angle),
                        cy - (inner - 3) * math.cos(angle),
                        cx + (radius + 3) * math.sin(angle),
                        cy - (radius + 3) * math.cos(angle), theme.ink,
                        1.5)
        display = item.get("display", number(item["value"], chart))
        canvas.text(cx, cy - 2, display, min(15, radius * 0.42), theme.ink,
                    "middle", bold=True)
        canvas.text(cx - (radius + inner) / 2, cy + 8,
                    number(low, chart), 6, theme.muted, "middle")
        canvas.text(cx + (radius + inner) / 2, cy + 8,
                    number(high, chart), 6, theme.muted, "middle")
        canvas.text(cx, cy + 18, item["label"], 7.5, theme.ink, "middle",
                    bold=True)
        if item.get("note"):
            canvas.text(cx, cy + 27, item["note"], 6.5, theme.muted,
                        "middle")


CHARTS = {
    "gantt": gantt, "line": line_chart, "bars": bar_chart, "donut": donut,
    "risk": risk_matrix, "heatmap": heatmap, "kpis": kpis,
    "timeline": timeline, "waterfall": waterfall, "quadrant": quadrant,
    "progress": progress, "board": board, "tree": tree, "funnel": funnel,
    "chevrons": chevrons, "sankey": sankey, "gauges": gauges,
}


def auto_height(chart, width, theme):
    """The height of a chart that has none."""
    title = 16 if chart.get("title") else 0
    kind = chart["type"]
    chart = {**chart, "_font": theme.font, "_bold_font": theme.bold_font}
    if kind == "gantt":
        if not title and len(chart.get("groups", [])) > 1:
            title = 14
        return title + 16 + len(chart["tasks"]) * chart.get("row", 13) + (
            10 if chart.get("today") is not None else 2)
    if kind == "board":
        return card_height(chart, width)
    if kind == "tree":
        return tree_height(chart, width)
    if kind == "kpis":
        return title + 54
    if kind == "gauges":
        return title + 100
    if kind == "sankey":
        return title + 180
    if kind == "progress":
        return title + len(chart["items"]) * (
            24 if any(i.get("note") for i in chart["items"]) else 16)
    if kind == "heatmap":
        return title + 16 + len(chart["rows"]) * chart.get("row", 15)
    if kind == "funnel":
        return title + len(chart["stages"]) * 16
    if kind == "bars" and chart.get("horizontal"):
        return title + 16 + len(chart["categories"]) * chart.get("row", 16)
    if kind == "chevrons":
        return title + 34 + (40 if any(s.get("sub") for s in
                                       chart["steps"]) else 4)
    return title + 140


def figure_svg(charts, widths, height, width, theme, gap=16):
    """One SVG of the charts side by side."""
    canvas = Canvas(theme)
    total = sum(widths)
    x = 0
    usable = width - gap * (len(charts) - 1)
    for chart, share in zip(charts, widths):
        chart_w = usable * share / total
        CHARTS[chart["type"]](canvas, chart, x, 0, chart_w, height)
        x += chart_w + gap
    return canvas.svg(width, height)


# styles

def stylesheet(design):
    """The paragraph styles of a document, by role. Sizes, line heights,
    spacing and paddings are in points; paddings are (top, bottom, left,
    right).

    The design names the accent, ink (text), muted and page (background)
    colors, the body font and heading_font, the density, the side margin,
    the orientation, the header ("rule", "band", "bar", "centered" or
    "frame"), the heading ("rule", "bar", "tint", "box", "slab", "center"
    or "plain", in heading_case "upper" or "lower"), the body_align and
    the table style ("lines", "grid", "zebra" or "slab").
    """
    accent = design["accent"]
    muted = design.get("muted", "#5b6470")
    ink = design.get("ink", "#1f2328")
    page = design.get("page", "#ffffff")
    body = design["font"]
    heading_font = design.get("heading_font", body)
    header = design.get("header", "rule")
    heading = design.get("heading", "rule")
    width = text_width(design)
    scale = {"compact": 0.95, "regular": 1, "airy": 1.05,
             "spacious": 1.1}[design.get("density", "regular")]
    size, line = round(10 * scale * 2) / 2, round(14 * scale * 2) / 2
    align = "center" if header in ("centered", "frame") else "start"

    sheet = {}

    def add(role, **spec):
        sheet[role] = {"font": body, "size": size, "line": line,
                       "before": 0, "after": 0, "color": ink,
                       "width": width, **spec}

    title_size = design.get("title_size", 24) * scale
    eyebrow = dict(font=heading_font, size=size - 1.5, line=line - 2,
                   bold=True, color=accent, caps=True, align=align)
    title = dict(font=heading_font, size=title_size, line=title_size * 1.18,
                 before=2, bold=True, color=ink if header != "band"
                 else page, align=align, case=design.get("title_case"))
    subtitle = dict(font=heading_font, size=size + 1.5, line=line + 3,
                    after=8, italic=design.get("subtitle_italic", True),
                    color=muted, align=align)
    if header == "band":
        eyebrow.update(color=mix(accent, "#ffffff", 0.75), background=accent,
                       pad=(12, 0, 14, 14))
        title.update(background=accent, pad=(2, 2, 14, 14), before=0)
        subtitle.update(color=mix(accent, "#ffffff", 0.82),
                        background=accent, pad=(0, 12, 14, 14))
    elif header == "bar":
        bar = (5, accent)
        eyebrow.update(border_left=bar, pad=(0, 0, 12, 0))
        title.update(border_left=bar, pad=(0, 0, 12, 0), before=0)
        subtitle.update(border_left=bar, pad=(0, 2, 12, 0))
    elif header == "frame":
        title.update(box=(2, accent), pad=(8, 8, 10, 10), before=6, after=6)
    else:
        subtitle.update(border=accent, pad=(0, 8, 0, 0))
    add("eyebrow", **eyebrow)
    add("title", **title)
    add("subtitle", **subtitle)

    common = dict(font=heading_font, size=size + 2.5, line=line + 4,
                  before=14, after=6, bold=True, color=accent, keep=True,
                  case=design.get("heading_case"))
    if heading == "box":
        add("heading", **common, box=(1.25, accent), pad=(2, 2, 6, 6))
    elif heading == "slab":
        add("heading", **{**common, "color": page}, background=accent,
            pad=(3, 3, 6, 6))
    elif heading == "center":
        add("heading", **common, caps=True, align="center")
    elif heading == "rule":
        add("heading", **common, caps=True, border=accent, pad=(0, 2, 0, 0))
    elif heading == "bar":
        add("heading", **common, border_left=(3.5, accent),
            pad=(1, 1, 7, 0))
    elif heading == "tint":
        add("heading", **common, caps=True,
            background=mix(accent, page, 0.86), pad=(3, 3, 6, 6))
    else:
        add("heading", **{**common, "size": size + 3.5, "line": line + 6})

    add("entry", size=size + 0.5, line=line + 0.5, before=8, bold=True,
        keep=True, tab=True)
    add("meta", size=size - 0.5, line=line - 0.5, after=2, italic=True,
        color=muted, keep=True)
    add("body", after=5, align=design.get("body_align", "justify"))
    hang = design.get("bullet_width", 14)
    add("bullet", after=2, left=hang + 2, first=-hang, hang=True)
    add("tag", after=3)
    add("field", after=3, align=design.get("body_align", "justify"))
    add("motto", font=heading_font, size=size + 1.5, line=line + 4,
        before=4, after=8, italic=True, color=accent,
        background=mix(accent, page, 0.92), pad=(7, 7, 12, 12),
        align="center")
    for tone in ("accent", "good", "warn", "bad", "info"):
        color = design.get(tone, {"accent": accent, "good": "#2e9d5b",
                                  "warn": "#e3a21a", "bad": "#d64545",
                                  "info": "#3a7bd5"}[tone])
        add("callout-" + tone, before=4, after=8,
            background=mix(color, page, 0.88), border_left=(3.5, color),
            pad=(6, 6, 10, 10), align="start")
    add("figure", size=2, before=6, after=8, line=None)
    # Writer does not move a heading kept with the next paragraph to the
    # next page when it follows a table, so every table ends with this
    add("spacer", size=1, line=1)
    add("caption", size=size - 1.5, line=line - 3, after=8, italic=True,
        color=muted, before=-4)
    add("cell", size=size - 1, line=line - 2.5, align="start")
    add("cell-head", size=size - 1.5, line=line - 3, bold=True, color=page
        if design.get("table") == "slab" else accent, caps=True,
        align="start")
    add("cell-head-plain", **{**sheet["cell-head"], "caps": False,
                              "case": None})
    add("cell-bold", size=size - 1, line=line - 2.5, bold=True,
        align="start")
    add("cell-muted", size=size - 1, line=line - 2.5, italic=True,
        color=muted, align="start")
    add("cell-indent", size=size - 1, line=line - 2.5, left=10,
        align="start")
    add("cell-indent2", size=size - 1, line=line - 2.5, left=20,
        align="start")
    add("meta-label", size=size - 2.5, line=line - 5, bold=True,
        color=muted, caps=True, align=align if align == "center" else
        "start")
    add("meta-value", size=size - 0.5, line=line - 1.5, bold=True,
        align=align if align == "center" else "start")
    add("footer", size=7.5, line=FOOTER_HEIGHT, color=muted, align="center")
    add("entry-end", **{**sheet["entry"], "keep": False})
    add("meta-end", **{**sheet["meta"], "keep": False})
    return sheet


def paragraph_style(parent, name, spec):
    style = element(parent, "style:style", style__name=name,
                    style__family="paragraph")
    paragraph = {"fo__margin_top": pt(max(spec["before"], 0)),
                 "fo__margin_bottom": pt(spec["after"]),
                 "fo__margin_left": pt(spec.get("left", 0)),
                 "fo__text_indent": pt(spec.get("first", 0)),
                 "fo__text_align": spec.get("align", "start"),
                 "fo__widows": 2, "fo__orphans": 2}
    if spec["line"]:
        paragraph["fo__line_height"] = pt(spec["line"])
    if spec.get("keep"):
        paragraph["fo__keep_with_next"] = "always"
    if spec.get("border"):
        paragraph["fo__border_bottom"] = f"0.75pt solid {spec['border']}"
    if spec.get("border_left"):
        width, color = spec["border_left"]
        paragraph["fo__border_left"] = f"{pt(width)} solid {color}"
    if spec.get("box"):
        width, color = spec["box"]
        paragraph["fo__border"] = f"{pt(width)} solid {color}"
    if spec.get("background"):
        paragraph["fo__background_color"] = spec["background"]
    if spec.get("pad"):
        top, bottom, left, right = spec["pad"]
        paragraph.update(fo__padding_top=pt(top),
                         fo__padding_bottom=pt(bottom),
                         fo__padding_left=pt(left),
                         fo__padding_right=pt(right))
    properties = element(style, "style:paragraph-properties", **paragraph)
    if spec.get("tab"):
        element(element(properties, "style:tab-stops"), "style:tab-stop",
                style__type="right",
                style__position=pt(spec["width"] - spec.get("left", 0)))
    elif spec.get("hang"):
        element(element(properties, "style:tab-stops"), "style:tab-stop",
                style__type="left", style__position="0pt")

    text = {"style__font_name": spec["font"],
            "fo__font_size": pt(spec["size"]),
            "fo__font_weight": "bold" if spec.get("bold") else "normal",
            "fo__font_style": "italic" if spec.get("italic") else "normal",
            "fo__color": spec["color"]}
    if spec.get("caps"):
        text.update(fo__text_transform="uppercase",
                    fo__letter_spacing="0.6pt")
    if spec.get("case"):
        text["fo__text_transform"] = {"upper": "uppercase",
                                      "lower": "lowercase"}[spec["case"]]
    element(style, "style:text-properties", **text)


def text_styles(parent, design):
    for name, properties in (
            ("strong", {"fo__font_weight": "bold"}),
            ("emphasis", {"fo__font_style": "italic"}),
            ("accent", {"fo__color": design["accent"],
                        "fo__font_weight": "bold"}),
            ("muted", {"fo__color": design.get("muted", "#5b6470"),
                       "fo__font_weight": "normal"})):
        style = element(parent, "style:style", style__name=name,
                        style__family="text")
        element(style, "style:text-properties", **properties)


# a paragraph is a role and runs of text: (text, style), where the style is
# None, a text style, "tab" for a tab to the right tab stop or "indent" for
# the tab that ends a bullet

def runs(text, style=None):
    """**bold** in the text becomes strong and *italic* emphasis."""
    content = []
    for part in MARKUP.split(text):
        if part.startswith("**") and part.endswith("**"):
            content.append((part[2:-2], "strong"))
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            content.append((part[1:-1], "emphasis"))
        elif part:
            content.append((part, style))
    return content


def lines(spec, content, width=None):
    """Wrap the words of the runs into the width of the paragraph."""
    regular, bold = FONTS[spec["font"]]
    top, bottom, left, right = spec.get("pad") or (0, 0, 0, 0)
    border = spec["border_left"][0] if spec.get("border_left") else 0
    if spec.get("box"):
        border = 2 * spec["box"][0]
    width = ((width or spec["width"]) - spec.get("left", 0) - left - right
             - border)
    upper = spec.get("caps") or spec.get("case") == "upper"
    scale = (CAPITALS.get(spec["font"], 1.3)
             if upper and spec["font"] not in MONOSPACED else 1)
    if spec.get("caps"):
        scale += 0.6 / spec["size"] / regular
    count, x = 1, 0.0
    for text, style in content:
        if style in ("tab", "indent"):
            x += 24 if style == "tab" else 0
            continue
        bolder = spec.get("bold") or style in ("strong", "accent")
        em = (bold if bolder else regular) * spec["size"] * scale
        for index, word in enumerate(text.split(" ")):
            advance_ = (index > 0) * em + len(word) * em
            if x and x + advance_ > width:
                count, x = count + 1, len(word) * em
            else:
                x += advance_
    return count


# blocks: what the simulation of the pages and the writer both understand

class Paragraph:
    def __init__(self, role, content):
        self.role, self.content = role, content

    def measure(self, sheet):
        spec = sheet[self.role]
        self.keep = spec.get("keep", False)
        self.count = lines(spec, self.content)
        top, bottom, *_ = spec.get("pad") or (0, 0)
        border = 0.75 if spec.get("border") else 0
        if spec.get("box"):
            border = 2 * spec["box"][0]
        self.head = max(spec["before"], 0) + top + border / 2
        self.tail = spec["after"] + bottom + border / 2
        self.line = spec["line"] * (1 + SAFETY)
        self.height = self.head + self.tail + self.count * self.line
        # paragraphs in a box or a band are not split
        self.split = (self.count >= 4 and not spec.get("background")
                      and not spec.get("box"))

    def minimum(self):
        return (self.head + 2 * self.line) if self.split else self.height


class Figure:
    def __init__(self, svg, width, height):
        self.svg, self.width, self.height = svg, width, height
        self.keep = False

    def measure(self, sheet):
        spec = sheet["figure"]
        self.total = spec["before"] + spec["after"] + self.height + 1

    def minimum(self):
        return self.total


# the rows of financial statements: the paragraph style of their cells, the
# indent of the first cell and the extra height of their rules
ROW_STYLES = {
    None: ("cell", 0, 0), "indent": ("cell", 10, 0),
    "indent2": ("cell", 20, 0), "muted": ("cell-muted", 0, 0),
    "section": ("cell-bold", 0, 0), "subtotal": ("cell-bold", 0, 0.5),
    "total": ("cell-bold", 0, 3), "highlight": ("cell-bold", 0, 0),
}


def row_cells(row):
    """The cells and the style of a row: a list of cells, or a dict of
    cells and a style from ROW_STYLES."""
    if isinstance(row, dict):
        return row["cells"], row.get("style")
    return row, None


def head_role(sheet, cells, widths):
    """The style of the header cells: in capitals, unless a word of one of
    them would not fit its column in capitals and break in the middle."""
    spec = sheet["cell-head"]
    font = spec["font"]
    scale = CAPITALS.get(font, 1.3) if font not in MONOSPACED else 1
    em = (FONTS[font][1] * spec["size"] * scale + 0.6) * 1.1
    for text, width in zip(cells, widths):
        longest = max(text.split() or [""], key=len)
        if len(longest) * em > width - 8:
            return "cell-head-plain"
    return "cell-head"


class Table:
    def __init__(self, columns, header, rows, badges, section):
        self.columns, self.header, self.rows = columns, header, rows
        self.badges, self.section = badges, section
        self.keep = False
        self.meta = False
        self.headless = bool(section) and section.get("header") is False

    def row_height(self, sheet, row, head=False):
        cells, style = row_cells(row)
        indent, extra = 0, 0
        if self.meta:
            spec = sheet["meta-label" if head else "meta-value"]
            pad = 2
        elif head:
            spec, pad = None, 3.5
        else:
            role, indent, extra = ROW_STYLES[style]
            spec, pad = sheet[role], 3
        tallest = max(lines(spec or sheet[head_role(sheet, cells,
                                                    self.widths)],
                            runs(cell),
                            width - 2 * 4 - (indent if i == 0 else 0))
                      for i, (cell, width) in
                      enumerate(zip(cells, self.widths)))
        spec = spec or sheet["cell-head"]
        return (tallest * spec["line"] * (1 + SAFETY) + 2 * pad + 0.75
                + extra)

    def measure(self, sheet):
        total = sheet["cell"]["width"]
        fractions = [c[1] for c in self.columns]
        self.widths = [total * f / sum(fractions) for f in fractions]
        self.head = (0 if self.headless else
                     self.row_height(sheet, self.header, True))
        self.heights = [self.row_height(sheet, row) for row in self.rows]
        self.after = (10 if self.meta else 8) + 1

    def minimum(self):
        return self.head + (self.heights[0] if self.heights else 0)


def paginate(blocks, sheet, room):
    """The number of pages the blocks fill, each page room points high,
    and the height used on the last page."""
    pages, used = 1, 0.0

    def need(index):
        """The height that must go on the page with block index: the block,
        and the start of the next if it keeps with it."""
        total, i = 0.0, index
        while i < len(blocks):
            block = blocks[i]
            if block.keep and i + 1 < len(blocks):
                total += block.height if isinstance(block, Paragraph) else \
                    block.minimum()
                i += 1
            else:
                return total + block.minimum()
        return total

    for index, block in enumerate(blocks):
        if used and used + need(index) > room:
            pages, used = pages + 1, 0.0
        if isinstance(block, Paragraph):
            if used + block.height <= room:
                used += block.height
                continue
            if not block.split:
                if used:
                    pages, used = pages + 1, 0.0
                used += block.height
                while used > room:
                    pages, used = pages + 1, used - room
                continue
            remaining, head = block.count, block.head
            while used + head + remaining * block.line + block.tail > room:
                fit = int((room - used - head) // block.line)
                if remaining - fit == 1:
                    fit -= 1
                if fit < 2:
                    fit = 0 if used else max(fit, 1)
                if fit:
                    remaining, head = remaining - fit, 0
                pages, used = pages + 1, 0.0
            used += head + remaining * block.line + block.tail
        elif isinstance(block, Figure):
            if used and used + block.total > room:
                pages, used = pages + 1, 0.0
            used += block.total
        else:
            if used and used + block.minimum() > room:
                pages, used = pages + 1, 0.0
            used += block.head
            for height in block.heights:
                if used + height > room:
                    pages, used = pages + 1, block.head
                used += height
            used += block.after
    return pages, used


# content

class Item:
    """Blocks that go in together, after their parent. Items without a
    priority go in only with their children."""

    def __init__(self, blocks, priority=None, parent=None):
        self.blocks = blocks
        self.priority = priority
        self.parent = parent
        self.children = []
        if parent:
            parent.children.append(self)

    def walk(self):
        yield self
        for child in self.children:
            yield from child.walk()

    def chain(self):
        item = self
        while item:
            yield item
            item = item.parent


def roman(number):
    numerals = [(10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    result = ""
    for value, numeral in numerals:
        while number >= value:
            result, number = result + numeral, number - value
    return result


def bullet(text, design):
    return Paragraph("bullet", [(design.get("bullet", "•"), "accent"),
                                ("", "indent")] + runs(text))


def entry_blocks(entry, design):
    title = runs(entry["title"])
    if entry.get("org"):
        title += ([(design.get("separator", " · "), "muted")]
                  + runs(entry["org"], "muted"))
    if entry.get("dates"):
        title += [("", "tab")] + runs(entry["dates"], "muted")
    blocks = [Paragraph("entry", title)]
    if entry.get("meta"):
        blocks.append(Paragraph("meta", runs(entry["meta"])))
    return blocks


def at_pages(value, pages):
    """A value, or the value for the number of pages of a {pages: value}
    dictionary, e.g. the height of a figure."""
    if isinstance(value, dict):
        return value.get(pages, value[max(k for k in value if k <= pages)]
                         if any(k <= pages for k in value) else
                         value[min(value)])
    return value


def figure(section, design, theme, pages):
    width = text_width(design)
    charts = section["charts"]
    widths = section.get("widths", [1] * len(charts))
    gap = 16
    usable = width - gap * (len(charts) - 1)
    height = at_pages(section.get("height"), pages)
    if height is None:
        height = max(auto_height(chart, usable * share / sum(widths), theme)
                     for chart, share in zip(charts, widths))
    svg = figure_svg(charts, widths, height, width, theme, gap)
    return Figure(svg, width, height)


def section_items(section, number, design, theme, pages):
    """The section as a tree of items. Its weight is the priority of its
    first paragraph, entry, row or figure, its step is how much less
    important each next one is, and inner is how much less important each
    next line of an entry is. The stories of entries start at the priority
    story."""
    weight = section.get("weight", 1)
    step = section.get("step", 1)
    blocks = []
    if section.get("heading"):
        title = section["heading"]
        if design.get("numbered"):
            title = f"{number:02d} · {title}"
        if design.get("heading_format"):
            slug = re.sub(r"[^a-z0-9]+", "-", section["heading"].lower())
            title = design["heading_format"].format(
                title=section["heading"], number=number, slug=slug.strip("-"),
                roman=roman(number))
        blocks = [Paragraph("heading", runs(title))]
    root = Item(blocks)

    kind = section["kind"]
    if kind == "text":
        for index, paragraph in enumerate(section["paragraphs"]):
            Item([Paragraph("body", runs(paragraph))], weight + index * step,
                 root)
    elif kind == "motto":
        Item([Paragraph("motto", runs(section["text"]))], weight, root)
    elif kind == "callout":
        content = runs(section["text"])
        if section.get("label"):
            content = [(section["label"] + "  ", "accent")] + content
        Item([Paragraph("callout-" + section.get("tone", "accent"),
                        content)], weight, root)
    elif kind == "bullets":
        for index, text in enumerate(section["items"]):
            Item([bullet(text, design)], weight + index * step, root)
    elif kind == "tags":
        for index, (label, value) in enumerate(section["items"]):
            Item([Paragraph("tag", [(label + ": ", "accent")] + runs(value))],
                 weight + index * step, root)
    elif kind == "entries":
        inner = section.get("inner", 1)
        for index, entry in enumerate(section["entries"]):
            base = weight + index * step
            parent = Item(entry_blocks(entry, design), base - inner / 2,
                          root)
            children = ([Paragraph("body", runs(text))
                         for text in entry.get("text", [])]
                        + [Paragraph("field", [(label + ": ", "accent")]
                                     + runs(value))
                           for label, value in entry.get("fields", [])]
                        + [bullet(text, design)
                           for text in entry.get("items", [])])
            for line, block in enumerate(children):
                Item([block], base + line * inner, parent)
            for line, text in enumerate(entry.get("story", [])):
                Item([Paragraph("body", runs(text))],
                     section.get("story", weight + 6) + index * step + line,
                     parent)
    elif kind == "figure":
        Item([figure(section, design, theme, pages)], weight, root)
        if section.get("caption"):
            Item([Paragraph("caption", runs(section["caption"]))],
                 weight + section.get("caption_step", 2), root.children[-1])
    elif kind == "table":
        # every row is an item of its own, or, for a whole table such as a
        # balance sheet, all rows are one item: the table is put together
        # from the rows that go in when the document is written. Rows that
        # are dicts can have min_pages and max_pages of their own.
        rows = [row for row in section["rows"] if not isinstance(row, dict)
                or row.get("min_pages", 1) <= pages
                <= row.get("max_pages", 4)]
        if section.get("whole"):
            Item([("row", section, row) for row in rows], weight, root)
        else:
            for index, row in enumerate(rows):
                Item([("row", section, row)], weight + index * step, root)
        root.table = section
    else:
        raise ValueError(f"unknown section kind: {kind}")
    return root


def header_blocks(project, document, design):
    blocks = [Paragraph("eyebrow", runs(document.get("eyebrow",
                                                     project["name"]))),
              Paragraph("title", runs(document["title"]))]
    if document.get("subtitle"):
        blocks.append(Paragraph("subtitle", runs(document["subtitle"])))
    if document.get("meta"):
        meta = document["meta"]
        blocks.append(Table([(label, 1, "start") for label, _ in meta],
                            [label for label, _ in meta],
                            [[value for _, value in meta]], {}, None))
        blocks[-1].meta = True
    return blocks


def assemble(roots, chosen):
    """The blocks of the chosen items, with the rows of a table joined into
    one table."""
    blocks = []
    for root in roots:
        rows = []
        for item in root.walk():
            if item not in chosen:
                continue
            for block in item.blocks:
                if isinstance(block, tuple) and block[0] == "row":
                    rows.append(block[2])
                else:
                    blocks.append(block)
        if getattr(root, "table", None) and rows:
            section = root.table
            blocks.append(Table(section["columns"],
                                [c[0] for c in section["columns"]], rows,
                                section.get("badges", {}), section))
    for index, block in enumerate(blocks):
        if isinstance(block, Paragraph) and block.role in (
                "entry", "meta", "entry-end", "meta-end"):
            following = blocks[index + 1] if index + 1 < len(blocks) else None
            base = block.role.replace("-end", "")
            if not (isinstance(following, Paragraph) and following.role in (
                    "meta", "body", "field", "bullet")):
                block.role = base + "-end"
            else:
                block.role = base
    return blocks


def compose(project, document, design, pages):
    """The styles and the blocks of the document, and how full its last
    page is."""
    sheet = stylesheet(design)
    theme = Theme(design)
    room = text_height(design) - RESERVE
    top = header_blocks(project, document, design)

    sections = [section for section in document["sections"]
                if section.get("min_pages", 1) <= pages
                <= section.get("max_pages", 4)]
    roots, number = [], 0
    for section in sections:
        number += bool(section.get("heading"))
        roots.append(section_items(section, number, design, theme, pages))

    items = [item for root in roots for item in root.walk()]

    def layout(chosen):
        blocks = top + assemble(roots, chosen)
        for block in blocks:
            block.measure(sheet)
        return blocks, paginate(blocks, sheet, room)

    chosen = set()
    for item in sorted((item for item in items if item.priority is not None),
                       key=lambda item: item.priority):
        missing = [link for link in item.chain() if link not in chosen]
        trial = chosen | set(missing)
        _, (count, _) = layout(trial)
        if count <= pages:
            chosen = trial
    blocks, (count, used) = layout(chosen)
    return sheet, theme, blocks, count, used / room


def table_styles(automatic, design, sheet, name, table, meta=False):
    """The automatic styles of a table: its width, its columns and its
    cells, plain, in the colors of its badges and in the styles of its
    rows. A section can choose its own look, e.g. "plain" for an address
    block."""
    accent = design["accent"]
    page = design.get("page", "#ffffff")
    muted = design.get("muted", "#5b6470")
    ink = design.get("ink", "#1f2328")
    look = "meta" if meta else (table.section or {}).get(
        "look", design.get("table", "lines"))
    width = sheet["cell"]["width"]
    style = element(automatic, "style:style", style__name=name,
                    style__family="table")
    element(style, "style:table-properties", style__width=pt(width),
            table__align="margins", fo__margin_top="0pt",
            fo__margin_bottom=pt(8 if not meta else 10),
            style__may_break_between_rows="true")
    for index, w in enumerate(table.widths):
        column = element(automatic, "style:style",
                         style__name=f"{name}.c{index}",
                         style__family="table-column")
        element(column, "style:table-column-properties",
                style__column_width=pt(w))
    rule = f"0.75pt solid {mix(muted, page, 0.55)}"
    strong = f"1pt solid {accent}"

    def cell(style_name, background=None, head=False, stripe=False,
             row=None):
        cell_style = element(automatic, "style:style", style__name=style_name,
                             style__family="table-cell")
        properties = {"fo__padding_top": pt(3.5 if head else 3),
                      "fo__padding_bottom": pt(3.5 if head else 3),
                      "fo__padding_left": "4pt", "fo__padding_right": "4pt"}
        if look == "plain":
            properties["fo__border"] = "none"
            properties["fo__padding_left"] = "0pt"
        elif look == "grid":
            properties["fo__border"] = rule
        elif look == "meta":
            properties["fo__border_top"] = (f"0.75pt solid {accent}"
                                            if head else "none")
            properties["fo__border_bottom"] = ("none" if head else
                                               f"0.75pt solid {accent}")
            properties["fo__padding_top"] = "4pt" if head else "0pt"
            properties["fo__padding_bottom"] = "0pt" if head else "4pt"
            properties["fo__padding_left"] = "0pt"
        else:
            properties["fo__border_bottom"] = strong if head else rule
        if look == "slab" and head:
            background = accent
        if look == "zebra" and stripe and not background:
            background = mix(accent, page, 0.93)
        if row in ("section", "highlight"):
            background = mix(accent, page, 0.88 if row == "section"
                             else 0.8)
        if row == "subtotal":
            properties["fo__border_top"] = f"0.75pt solid {ink}"
        if row == "total":
            properties["fo__border_top"] = f"1pt solid {ink}"
            properties["fo__border_bottom"] = f"2.5pt double {ink}"
        if background:
            properties["fo__background_color"] = background
        if look == "grid" and "fo__border_top" in properties:
            properties.pop("fo__border")
            properties.setdefault("fo__border_bottom", rule)
            properties.update(fo__border_left=rule, fo__border_right=rule)
        element(cell_style, "style:table-cell-properties",
                style__vertical_align="middle", **properties)

    cell(f"{name}.h", head=True)
    cell(f"{name}.d")
    cell(f"{name}.s", stripe=True)
    for style in ("section", "subtotal", "total", "highlight"):
        cell(f"{name}.{style}", row=style)
    theme = Theme(design)
    for index, (text, tone) in enumerate(table.badges.items()):
        color = theme.color(tone)
        cell(f"{name}.b{index}", mix(color, page, 0.7))


def write_table(body, automatic, design, sheet, name, table):
    meta = getattr(table, "meta", False)
    table_styles(automatic, design, sheet, name, table, meta)
    node = element(body, "table:table", table__name=name,
                   table__style_name=name)
    for index in range(len(table.widths)):
        element(node, "table:table-column",
                table__style_name=f"{name}.c{index}")
    aligns = [c[2] if len(c) > 2 else "start" for c in table.columns]
    badges = list(table.badges)

    def row(parent, cells, head, stripe=False, kind=None):
        tr = element(parent, "table:table-row")
        role, indent, _ = ROW_STYLES[kind]
        for index, text in enumerate(cells):
            if head:
                style = f"{name}.h"
            elif text in badges:
                style = f"{name}.b{badges.index(text)}"
            elif kind in ("section", "subtotal", "total", "highlight"):
                style = f"{name}.{kind}"
            else:
                style = f"{name}.s" if stripe else f"{name}.d"
            td = element(tr, "table:table-cell", table__style_name=style,
                         office__value_type="string")
            align = aligns[index]
            if meta:
                p_style = "meta-label" if head else "meta-value"
            elif head:
                p_style = head_role(sheet, cells, table.widths)
            elif index == 0 and indent:
                p_style = {10: "cell-indent", 20: "cell-indent2"}[indent]
            else:
                p_style = role
            if align != "start" and not p_style.startswith(
                    ("meta", "cell-indent")):
                p_style = f"{p_style}-{align}"
            write_paragraph(td, p_style, runs(text))

    if not table.headless:
        header = element(node, "table:table-header-rows")
        row(header, table.header, True)
    for index, entry in enumerate(table.rows):
        cells, kind = row_cells(entry)
        row(node, cells, False, index % 2 == 1, kind)


def write_paragraph(parent, role, content):
    paragraph = element(parent, "text:p", text__style_name=role)
    last = None
    for part, style in content:
        if style in ("tab", "indent"):
            last = element(paragraph, "text:tab")
        elif style:
            last = element(paragraph, "text:span", text__style_name=style)
            last.text = part
        elif last is None:
            paragraph.text = (paragraph.text or "") + part
        else:
            last.tail = (last.tail or "") + part
    return paragraph


def typeset(project, document, design, pages):
    """The flat ODT document of the pages."""
    sheet, theme, blocks, _, _ = compose(project, document, design, pages)
    title = document["title"]

    root = ET.Element(qualified("office:document"))
    root.set(qualified("office:version"), "1.3")
    root.set(qualified("office:mimetype"),
             "application/vnd.oasis.opendocument.text")
    meta = element(root, "office:meta")
    element(meta, "dc:title").text = f"{project['name']} – {title}"
    element(meta, "dc:creator").text = project.get("author", project["name"])

    faces = element(root, "office:font-face-decls")
    for font in sorted({spec["font"] for spec in sheet.values()}):
        element(faces, "style:font-face", style__name=font,
                svg__font_family=f"'{font}'")

    styles = element(root, "office:styles")
    default = element(styles, "style:default-style",
                      style__family="paragraph")
    element(default, "style:text-properties", style__font_name=design["font"],
            fo__language="en", fo__country="GB", fo__hyphenate="false")
    for role, spec in sheet.items():
        paragraph_style(styles, role, spec)
        if role in ("cell", "cell-head", "cell-head-plain", "cell-bold",
                    "cell-muted"):
            for align in ("center", "end"):
                paragraph_style(styles, f"{role}-{align}",
                                {**spec, "align": align})
    text_styles(styles, design)
    graphic = element(styles, "style:style", style__name="chart",
                      style__family="graphic")
    element(graphic, "style:graphic-properties", style__vertical_pos="top",
            style__vertical_rel="baseline", fo__border="none",
            fo__padding="0pt", style__wrap="none")

    automatic = element(root, "office:automatic-styles")
    layout = element(automatic, "style:page-layout", style__name="page")
    margin = design.get("margin", MARGIN_X)
    width, height = page_size(design)
    page = ({"fo__background_color": design["page"], "draw__fill": "solid",
             "draw__fill_color": design["page"]} if design.get("page") else {})
    element(layout, "style:page-layout-properties",
            fo__page_width=pt(width), fo__page_height=pt(height),
            fo__margin_top=pt(MARGIN_TOP), fo__margin_bottom=pt(MARGIN_BOTTOM),
            fo__margin_left=pt(margin), fo__margin_right=pt(margin),
            style__print_orientation=design.get("orientation", "portrait"),
            **page)
    element(element(layout, "style:footer-style"),
            "style:header-footer-properties",
            fo__min_height=pt(FOOTER_HEIGHT),
            fo__margin_top=pt(FOOTER_SPACING))

    master = element(element(root, "office:master-styles"),
                     "style:master-page", style__name="Standard",
                     style__page_layout_name="page")
    footer = element(element(master, "style:footer"), "text:p",
                     text__style_name="footer")
    footer.text = design.get("footer", f"{project['name']} · {title}")
    if pages > 1:
        footer.text += " · "
        number = element(footer, "text:page-number",
                         text__select_page="current")
        number.text = "1"
        number.tail = " / "
        element(footer, "text:page-count").text = str(pages)

    body = element(element(root, "office:body"), "office:text")
    tables = figures = 0
    for block in blocks:
        if isinstance(block, Paragraph):
            write_paragraph(body, block.role, block.content)
        elif isinstance(block, Figure):
            figures += 1
            paragraph = element(body, "text:p", text__style_name="figure")
            frame = element(paragraph, "draw:frame", draw__style_name="chart",
                            draw__name=f"Figure {figures}",
                            text__anchor_type="as-char",
                            svg__width=pt(block.width),
                            svg__height=pt(block.height), draw__z_index=0)
            image = element(frame, "draw:image",
                            draw__mime_type="image/svg+xml")
            element(image, "office:binary-data").text = base64.b64encode(
                block.svg.encode()).decode()
        else:
            tables += 1
            write_table(body, automatic, design, sheet, f"Table{tables}",
                        block)
            element(body, "text:p", text__style_name="spacer")
    return ET.tostring(root, encoding="unicode", xml_declaration=True)


def fill(project, document, design, pages):
    """The number of pages the simulation fills, and how full the last
    one is."""
    *_, count, used = compose(project, document, design, pages)
    return count, used
