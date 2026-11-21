"""Typeset a job hunting document as a flat ODT document of exactly the
given number of A4 pages.

A document is the PERSONA and the DOCUMENT of content.py: a header made
of who the persona is, the sections of the document and, for letters, the
sign-off. A document fills its pages by choosing what goes in: every
paragraph, entry and line of a section has a priority, and the most
important ones that fit into the estimated height of the pages are kept,
in the order of the document. Line heights are fixed, so the height of a
paragraph is its number of lines, estimated from the average width of the
characters of its font, times its line height.

The DESIGN of the document, given by its project script, picks the fonts,
the colors and the look of the page, the header, the headings and the
bullets: see stylesheet() for what it can say.
"""
import re
import xml.etree.ElementTree as ET

NAMESPACES = {
    "office": "urn:oasis:names:tc:opendocument:xmlns:office:1.0",
    "style": "urn:oasis:names:tc:opendocument:xmlns:style:1.0",
    "text": "urn:oasis:names:tc:opendocument:xmlns:text:1.0",
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
}
MONOSPACED = {"DejaVu Sans Mono", "Liberation Mono", "Noto Sans Mono"}

# A4 in points
PAGE_WIDTH = 595.28
PAGE_HEIGHT = 841.89
MARGIN_X = 56.7
MARGIN_TOP = 48
MARGIN_BOTTOM = 36
FOOTER_HEIGHT = 12
FOOTER_SPACING = 12
TEXT_HEIGHT = (PAGE_HEIGHT - MARGIN_TOP - MARGIN_BOTTOM - FOOTER_HEIGHT
               - FOOTER_SPACING)

# the height lost on each page break to paragraphs kept together, and the
# share of the pages kept free for the errors of the estimate
BREAK_LOSS = 40
SAFETY = 0.04

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


# styles

def text_width(design):
    return PAGE_WIDTH - 2 * design.get("margin", MARGIN_X)


def stylesheet(kind, design):
    """The paragraph styles of a document of the kind ("cv", "letter" or
    "doc"), by role. Sizes, line heights, spacing and paddings are in
    points; paddings are (top, bottom, left, right).

    The design names the accent, ink (text), muted and page (background)
    colors, the body font and heading_font, the density, the side margin,
    the header ("rule", "band", "bar", "centered" or "frame", with the name
    display times larger and in name_case "upper" or "lower"), the heading
    ("rule", "bar", "tint", "box", "slab", "center" or "plain", in
    heading_case "upper" or "lower"), and the body_align.
    """
    accent = design["accent"]
    muted = design.get("muted", "#4b5563")
    ink = design.get("ink", "#1f2328")
    page = design.get("page", "#ffffff")
    body = design["font"]
    heading_font = design.get("heading_font", body)
    header = design.get("header", "rule")
    heading = design.get("heading", "rule")
    width = text_width(design)
    scale = {"compact": 0.95, "regular": 1, "airy": 1.05,
             "spacious": 1.1}[design.get("density", "regular")]
    size, line = {"cv": (10, 13.5), "letter": (11, 16),
                  "doc": (10.5, 14.5)}[kind]
    size, line = round(size * scale * 2) / 2, round(line * scale * 2) / 2
    align = "center" if header in ("centered", "frame") else "start"

    sheet = {}

    def add(role, **spec):
        sheet[role] = {"font": body, "size": size, "line": line,
                       "before": 0, "after": 0, "color": ink,
                       "width": width, **spec}

    name_size = {"cv": 26, "letter": 21, "doc": 13}[kind] * scale
    if kind != "doc":
        name_size *= design.get("display", 1)
    name = dict(font=heading_font, size=name_size, line=name_size * 1.2,
                bold=True, color=accent, align=align,
                case=design.get("name_case"))
    headline = dict(font=heading_font, size=size + 2, line=line + 3,
                    color=muted, align=align)
    contact = dict(size=size - 0.5, line=line, before=4, after=8,
                   color=muted, align=align)
    if header == "band":
        name.update(color="#ffffff", background=accent, pad=(14, 0, 14, 14))
        headline.update(color=mix(accent, "#ffffff", 0.8),
                        background=accent, pad=(2, 12, 14, 14))
        contact.update(before=8)
    elif header == "bar":
        bar = (4, accent)
        name.update(border_left=bar, pad=(2, 0, 12, 0))
        headline.update(border_left=bar, pad=(0, 0, 12, 0))
        contact.update(border_left=bar, pad=(0, 2, 12, 0), before=0,
                       after=10)
    elif header == "frame":
        name.update(box=(2, accent), pad=(8, 8, 10, 10), after=6)
        contact.update(border=accent, pad=(0, 6, 0, 0))
    else:
        contact.update(border=accent, pad=(0, 6, 0, 0))
    add("name", **name)
    add("headline", **headline)
    add("contact", **contact)

    common = dict(font=heading_font, size=size + 1.5, line=line + 2,
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
            background=mix(accent, "#ffffff", 0.86), pad=(3, 3, 6, 6))
    else:
        add("heading", **{**common, "size": size + 3, "line": line + 5})

    add("entry", size=size + 0.5, line=line + 0.5, before=8, bold=True,
        keep=True, tab=True)
    add("meta", size=size - 0.5, line=line - 0.5, after=2, italic=True,
        color=muted, keep=True)
    add("body", after=4, align=design.get("body_align", "justify"))
    hang = design.get("bullet_width", 14)
    add("bullet", after=2, left=hang + 2, first=-hang, hang=True)
    add("divider", font=heading_font, before=10, after=0, color=accent,
        align="center", keep=True)
    add("tag", after=3)
    add("field", after=3, align="justify")
    add("motto", font=heading_font, size=size + 1, line=line + 3,
        before=4, after=6, italic=True, color=accent,
        background=mix(accent, "#ffffff", 0.92), pad=(6, 6, 10, 10),
        align="center")

    if kind == "letter":
        sheet["body"].update(after=9)
        sheet["heading"].update(caps=False, before=10, after=5)
        add("date", before=14, after=10, align="end")
        add("address", line=line - 1.5)
        add("subject", before=16, after=12, bold=True, color=accent)
        add("salutation", after=9)
        add("signoff", before=6)
        add("signature", font=heading_font, before=30, bold=True,
            color=accent)
    elif kind == "doc":
        add("title", font=heading_font, size=24 * scale, line=30 * scale,
            before=4, bold=True, color=accent, align=align)
        add("subtitle", font=heading_font, size=size + 2, line=line + 4,
            after=6, italic=True, color=muted, align=align)
        sheet["heading"].update(size=sheet["heading"]["size"] + 1.5,
                                line=sheet["heading"]["line"] + 3, before=18)
        sheet["entry"].update(size=size + 1, line=line + 1, before=10)

    add("footer", size=7.5, line=FOOTER_HEIGHT, color=muted, align="center")
    if design.get("body_align"):
        sheet["field"]["align"] = design["body_align"]

    # entries without lines of their own end without keeping with the next
    for role in ("entry", "meta"):
        sheet[role + "-end"] = {**sheet[role], "keep": False}
    return sheet


def paragraph_style(parent, name, spec):
    style = element(parent, "style:style", style__name=name,
                    style__family="paragraph")
    paragraph = {"fo__line_height": pt(spec["line"]),
                 "fo__margin_top": pt(spec["before"]),
                 "fo__margin_bottom": pt(spec["after"]),
                 "fo__margin_left": pt(spec.get("left", 0)),
                 "fo__text_indent": pt(spec.get("first", 0)),
                 "fo__text_align": spec.get("align", "start"),
                 "fo__widows": 2, "fo__orphans": 2}
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
    # a right tab for dates, or a tab at the indent that ends a bullet,
    # however wide the bullet is
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
                    fo__letter_spacing="0.8pt")
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
            ("muted", {"fo__color": design.get("muted", "#4b5563"),
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


def lines(spec, content):
    """Wrap the words of the runs into the width of the paragraph."""
    regular, bold = FONTS[spec["font"]]
    top, bottom, left, right = spec.get("pad") or (0, 0, 0, 0)
    border = spec["border_left"][0] if spec.get("border_left") else 0
    if spec.get("box"):
        border = 2 * spec["box"][0]
    width = spec["width"] - spec.get("left", 0) - left - right - border
    upper = spec.get("caps") or spec.get("case") == "upper"
    scale = 1.22 if upper and spec["font"] not in MONOSPACED else 1
    if spec.get("caps"):
        scale += 0.8 / spec["size"] / regular
    count, x = 1, 0.0
    for text, style in content:
        if style in ("tab", "indent"):
            x += 24 if style == "tab" else 0
            continue
        bolder = spec.get("bold") or style in ("strong", "accent")
        em = (bold if bolder else regular) * spec["size"] * scale
        for index, word in enumerate(text.split(" ")):
            advance = (index > 0) * em + len(word) * em
            if x and x + advance > width:
                count, x = count + 1, len(word) * em
            else:
                x += advance
    return count


def height(spec, content):
    top, bottom, *_ = spec.get("pad") or (0, 0)
    border = 0.75 if spec.get("border") else 0
    if spec.get("box"):
        border = 2 * spec["box"][0]
    return (spec["before"] + spec["after"] + top + bottom + border
            + lines(spec, content) * spec["line"])


# content

class Item:
    """Paragraphs that go in together, after their parent. Items without a
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
    return ("bullet", [(design.get("bullet", "•"), "accent"), ("", "indent")]
            + runs(text))


def entry_blocks(entry, design):
    title = runs(entry["title"])
    if entry.get("org"):
        title += ([(design.get("separator", " · "), "muted")]
                  + runs(entry["org"], "muted"))
    meta = entry.get("meta")
    # narrow pages have no room for dates on the right of the title
    if entry.get("dates") and design.get("dates_below"):
        meta = entry["dates"] + (f" · {meta}" if meta else "")
    elif entry.get("dates"):
        title += [("", "tab")] + runs(entry["dates"], "muted")
    blocks = [("entry", title)]
    if meta:
        blocks.append(("meta", runs(meta)))
    return blocks


def section_items(section, number, design, headings):
    """The section as a tree of items. Its weight is the priority of its
    first paragraph, entry or line, its step is how much less important
    each next one is, and inner is how much less important each next line
    of an entry is. The stories of entries start at the priority story."""
    weight = section.get("weight", 1)
    step = section.get("step", 1)
    blocks = []
    if section.get("heading") and headings:
        title = section["heading"]
        if design.get("numbered"):
            title = f"{number:02d} · {title}"
        if design.get("mark"):
            title = f"{design['mark']} {title}"
        # e.g. "$ cat ~/{slug}.txt", "[{number}] {title}" or "{roman}."
        if design.get("heading_format"):
            slug = re.sub(r"[^a-z0-9]+", "-", section["heading"].lower())
            title = design["heading_format"].format(
                title=section["heading"], number=number, slug=slug.strip("-"),
                roman=roman(number))
        blocks = [("heading", runs(title))]
        if design.get("divider"):
            blocks.insert(0, ("divider", runs(design["divider"])))
    root = Item(blocks)

    if section["kind"] == "text":
        for index, paragraph in enumerate(section["paragraphs"]):
            Item([("body", runs(paragraph))], weight + index * step, root)
    elif section["kind"] == "motto":
        Item([("motto", runs(section["text"]))], weight, root)
    elif section["kind"] == "bullets":
        for index, text in enumerate(section["items"]):
            Item([bullet(text, design)], weight + index * step, root)
    elif section["kind"] == "tags":
        for index, (label, value) in enumerate(section["items"]):
            Item([("tag", [(label + ": ", "accent")] + runs(value))],
                 weight + index * step, root)
    elif section["kind"] == "entries":
        inner = section.get("inner", 1)
        for index, entry in enumerate(section["entries"]):
            base = weight + index * step
            parent = Item(entry_blocks(entry, design), base - inner / 2,
                          root)
            children = ([("body", runs(text)) for text in entry.get("text", [])]
                        + [("field", [(label + ": ", "accent")] + runs(value))
                           for label, value in entry.get("fields", [])]
                        + [bullet(text, design)
                           for text in entry.get("items", [])])
            for line, block in enumerate(children):
                Item([block], base + line * inner, parent)
            # the story of an entry is told only once everything else fits
            for line, text in enumerate(entry.get("story", [])):
                Item([("body", runs(text))],
                     section.get("story", weight + 6) + index * step + line,
                     parent)
    else:
        raise ValueError(f"unknown section kind: {section['kind']}")
    return root


def kind_of(document):
    return ("letter" if "recipient" in document
            else "cv" if document.get("cv") else "doc")


def header_blocks(persona, document, kind, design):
    contact = design.get("contact_join", " · ").join(persona["contact"])
    if kind == "doc":
        return [("title", runs(document["title"])),
                ("subtitle", runs(document["subtitle"])),
                ("contact", [(persona["name"], "strong"), (" · ", None)]
                 + runs(persona["headline"] + " · " + contact))]
    name = design.get("name_format", "{name}").format(name=persona["name"])
    blocks = [("name", runs(name)),
              ("headline", runs(persona["headline"])),
              ("contact", runs(contact))]
    if kind == "letter":
        blocks += [("date", runs(document["date"]))]
        blocks += [("address", runs(line)) for line in document["recipient"]]
        blocks += [("subject", runs(document["subject"])),
                   ("salutation", runs(document["salutation"]))]
    return blocks


def footer_blocks(persona, document, kind):
    if kind != "letter":
        return []
    return [("signoff", runs(document.get("signoff", "Kind regards,"))),
            ("signature", runs(persona["name"]))]


def budget(pages):
    return pages * TEXT_HEIGHT * (1 - SAFETY) - (pages - 1) * BREAK_LOSS


def compose(persona, document, design, pages):
    """The styles and the paragraphs of the document, and its estimated
    height. Letters get their headings from headings_from pages on."""
    kind = kind_of(document)
    sheet = stylesheet(kind, design)
    headings = kind != "letter" or pages >= document.get("headings_from", 2)

    def cost(blocks):
        return sum(height(sheet[role], content) for role, content in blocks)

    top = header_blocks(persona, document, kind, design)
    bottom = footer_blocks(persona, document, kind)
    used = cost(top) + cost(bottom)

    sections = [section for section in document["sections"]
                if section.get("min_pages", 1) <= pages
                <= section.get("max_pages", 4)]
    roots, number = [], 0
    for section in sections:
        number += bool(section.get("heading"))
        roots.append(section_items(section, number, design, headings))

    items = [item for root in roots for item in root.walk()]
    chosen = set()
    for item in sorted((item for item in items if item.priority is not None),
                       key=lambda item: item.priority):
        missing = [link for link in item.chain() if link not in chosen]
        extra = cost([block for link in missing for block in link.blocks])
        if used + extra <= budget(pages):
            chosen.update(missing)
            used += extra

    blocks = top + [block for item in items if item in chosen
                    for block in item.blocks] + bottom
    for index, (role, content) in enumerate(blocks):
        following = blocks[index + 1][0] if index + 1 < len(blocks) else None
        if role in ("entry", "meta") and following not in (
                "meta", "body", "field", "bullet"):
            blocks[index] = (role + "-end", content)
    return sheet, blocks, used


def typeset(persona, document, design, pages):
    """The flat ODT document of the pages."""
    sheet, blocks, _ = compose(persona, document, design, pages)
    title = document["title"]

    root = ET.Element(qualified("office:document"))
    root.set(qualified("office:version"), "1.3")
    root.set(qualified("office:mimetype"),
             "application/vnd.oasis.opendocument.text")
    meta = element(root, "office:meta")
    element(meta, "dc:title").text = f"{persona['name']} – {title}"
    element(meta, "dc:creator").text = persona["name"]

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
    text_styles(styles, design)

    automatic = element(root, "office:automatic-styles")
    layout = element(automatic, "style:page-layout", style__name="page")
    margin = design.get("margin", MARGIN_X)
    # LibreOffice paints the page from its fill, the background is for others
    page = ({"fo__background_color": design["page"], "draw__fill": "solid",
             "draw__fill_color": design["page"]} if design.get("page") else {})
    element(layout, "style:page-layout-properties",
            fo__page_width=pt(PAGE_WIDTH), fo__page_height=pt(PAGE_HEIGHT),
            fo__margin_top=pt(MARGIN_TOP), fo__margin_bottom=pt(MARGIN_BOTTOM),
            fo__margin_left=pt(margin), fo__margin_right=pt(margin),
            style__print_orientation="portrait", **page)
    element(element(layout, "style:footer-style"),
            "style:header-footer-properties",
            fo__min_height=pt(FOOTER_HEIGHT), fo__margin_top=pt(FOOTER_SPACING))

    master = element(element(root, "office:master-styles"),
                     "style:master-page", style__name="Standard",
                     style__page_layout_name="page")
    footer = element(element(master, "style:footer"), "text:p",
                     text__style_name="footer")
    footer.text = design.get("footer", f"{persona['name']} · {title}")
    if pages > 1:
        footer.text += " · "
        number = element(footer, "text:page-number",
                         text__select_page="current")
        number.text = "1"
        number.tail = " / "
        element(footer, "text:page-count").text = str(pages)

    body = element(element(root, "office:body"), "office:text")
    for role, content in blocks:
        paragraph = element(body, "text:p", text__style_name=role)
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
    return ET.tostring(root, encoding="unicode", xml_declaration=True)


def fill(persona, document, design, pages):
    """The estimated share of the pages the document fills."""
    *_, used = compose(persona, document, design, pages)
    return used / (pages * TEXT_HEIGHT)
