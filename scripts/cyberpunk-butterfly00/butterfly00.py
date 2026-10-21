import math
import re
import xml.etree.ElementTree as ET

NAMESPACES = {
    "office": "urn:oasis:names:tc:opendocument:xmlns:office:1.0",
    "style": "urn:oasis:names:tc:opendocument:xmlns:style:1.0",
    "text": "urn:oasis:names:tc:opendocument:xmlns:text:1.0",
    "draw": "urn:oasis:names:tc:opendocument:xmlns:drawing:1.0",
    "fo": "urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0",
    "svg": "urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0",
    "dc": "http://purl.org/dc/elements/1.1/",
    "loext": "urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0",
}

TITLE = "Cyberpunk Butterfly 00"
DPI = 96
WIDTH = 1920
HEIGHT = 1080
HORIZON = 680
CENTER_X = WIDTH // 2
CENTER_Y = 430
RADIAL_STEPS = 48

POINT = re.compile(r"(-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?)")

for prefix, uri in NAMESPACES.items():
    ET.register_namespace(prefix, uri)


def qualified(name):
    prefix, local = name.split(":")
    return f"{{{NAMESPACES[prefix]}}}{local}"


def element(parent, tag, **attributes):
    """Attribute names use "__" for ":" and "_" for "-", e.g.
    svg__stroke_width="2px" sets svg:stroke-width."""
    return ET.SubElement(parent, qualified(tag),
                         {qualified(key.replace("__", ":").replace("_", "-")):
                          str(value) for key, value in attributes.items()})


def inch(pixels):
    return f"{pixels / DPI:.4f}in"


def new_document(width, height):
    """A text document with one page of the given size and no margins."""
    document = ET.Element(qualified("office:document"))
    document.set(qualified("office:version"), "1.3")
    document.set(qualified("office:mimetype"),
                 "application/vnd.oasis.opendocument.text")
    element(element(document, "office:meta"), "dc:title").text = TITLE
    element(document, "office:styles")

    layout = element(element(document, "office:automatic-styles"),
                     "style:page-layout", style__name="page")
    element(layout, "style:page-layout-properties",
            fo__page_width=inch(width), fo__page_height=inch(height),
            fo__margin_top="0in", fo__margin_bottom="0in",
            fo__margin_left="0in", fo__margin_right="0in",
            style__print_orientation="landscape")
    element(element(document, "office:master-styles"), "style:master-page",
            style__name="Standard", style__page_layout_name="page")
    element(element(document, "office:body"), "office:text")
    return document


def section(document, name):
    return document.find(qualified(name))


def text(document):
    return section(document, "office:body").find(qualified("office:text"))


def graphic_style(document, name, **properties):
    """Shapes run through the text in the background, without fill or
    stroke unless the properties say otherwise."""
    style = element(section(document, "office:automatic-styles"),
                    "style:style", style__name=name, style__family="graphic")
    element(style, "style:graphic-properties",
            **{"draw__stroke": "none", "draw__fill": "none",
               "style__wrap": "run-through",
               "style__run_through": "background", **properties})
    return name


def gradient(document, name, kind, start, end, border="0%", **attributes):
    element(section(document, "office:styles"), "draw:gradient",
            draw__name=name, draw__style=kind, draw__start_color=start,
            draw__end_color=end, draw__start_intensity="100%",
            draw__end_intensity="100%", draw__border=border, **attributes)
    return {"draw__fill": "gradient", "draw__fill_gradient_name": name}


def linear_gradient(document, name, stops):
    """Top to bottom across the bounds of each filled shape."""
    return gradient(document, name, "linear", stops[0], stops[-1],
                    draw__angle="0deg")


def radial_gradient(document, name, stops, center=("50%", "50%"),
                    border="0%"):
    """From the center to the edge of the bounds of each filled shape.
    ODF starts radial gradients on the edge, so the stops are swapped.

    The SVG export draws radial gradients as rings, and the seams between
    many thin rings let the background show through, so there are fewer.
    """
    return {**gradient(document, name, "radial", stops[-1], stops[0],
                       border, draw__cx=center[0], draw__cy=center[1]),
            "draw__gradient_step_count": RADIAL_STEPS}


def glow(color, radius, transparency=40):
    """LibreOffice's own shape glow, a blurred halo around the shape."""
    return {"loext__glow_radius": inch(radius), "loext__glow_color": color,
            "loext__glow_transparency": f"{transparency}%"}


def stroke(color, width, **attributes):
    return {"draw__stroke": "solid", "svg__stroke_color": color,
            "svg__stroke_width": inch(width), **attributes}


def shape(document, tag, name, style, **attributes):
    """Anchor the shape to the first page, above the shapes before it."""
    body = text(document)
    z_index = sum(child.tag.startswith(f"{{{NAMESPACES['draw']}}}")
                  for child in body)
    return element(body, tag, draw__name=name, draw__style_name=style,
                   draw__z_index=z_index, text__anchor_type="page",
                   text__anchor_page_number=1, **attributes)


def rect(document, name, style, x, y, width, height):
    return shape(document, "draw:rect", name, style, svg__x=inch(x),
                 svg__y=inch(y), svg__width=inch(width),
                 svg__height=inch(height))


def custom_shape(document, name, style, left, top, width, height, path,
                 view_box, **geometry):
    """LibreOffice draws glow only around rectangles and custom shapes, so
    the other shapes are custom shapes with the given enhanced path."""
    custom = shape(document, "draw:custom-shape", name, style,
                   svg__x=inch(left), svg__y=inch(top),
                   svg__width=inch(width), svg__height=inch(height))
    element(custom, "draw:enhanced-geometry", svg__viewBox=view_box,
            draw__enhanced_path=path, **geometry)
    return custom


def ellipse(document, name, style, cx, cy, rx, ry):
    return custom_shape(document, name, style, cx - rx, cy - ry, 2 * rx,
                        2 * ry, "U 10800 10800 10800 10800 0 360 Z N",
                        "0 0 21600 21600", draw__type="ellipse")


def bounds(d):
    """The left, top, width and height of the points of the path data."""
    points = [(float(x), float(y)) for x, y in POINT.findall(d)]
    xs, ys = zip(*points)
    left, top = min(xs), min(ys)
    return left, top, max(max(xs) - left, 1), max(max(ys) - top, 1)


def path(document, name, style, d):
    """Place the SVG path data, given in page pixels, by its bounds, as
    gradients are laid over the bounds of the shape. Each subpath of an
    enhanced path ends with N and its coordinates are space separated."""
    left, top, width, height = bounds(d)
    local = POINT.sub(lambda match: "%.2f %.2f" % (float(match[1]) - left,
                                                    float(match[2]) - top), d)
    enhanced = " ".join(f"M{subpath.rstrip()} N"
                        for subpath in local.split("M") if subpath.strip())
    return custom_shape(document, name, style, left, top, width, height,
                        enhanced, f"0 0 {width:.2f} {height:.2f}")


def path_data(strokes, closed=True):
    """Each stroke is a start point followed by cubic segments given as
    (control1, control2, end) point triples."""
    commands = []
    for start, *segments in strokes:
        commands.append("M %g,%g" % start)
        for segment in segments:
            commands.append("C " + " ".join("%g,%g" % point
                                            for point in segment))
        if closed:
            commands.append("Z")
    return " ".join(commands)


def polygon_data(polygons):
    return " ".join("M " + " L ".join("%.2f,%.2f" % point
                                      for point in polygon) + " Z"
                    for polygon in polygons)


def mirror(points):
    return [(2 * CENTER_X - x, y) for x, y in points]


def mirror_stroke(stroke):
    start, *segments = stroke
    return [mirror([start])[0]] + [tuple(mirror(segment)) for segment in segments]


def mix(start, end, t):
    """The color t of the way from start to end, past end when t > 1."""
    channels = [min(max(round(a + (b - a) * t), 0), 255) for a, b in
                zip(bytes.fromhex(start[1:]), bytes.fromhex(end[1:]))]
    return "#" + bytes(channels).hex()


def add_sky(document):
    # LibreOffice Draw skips a gradient rectangle as wide as the page from
    # the top down to the horizon, but not one covering the whole page, so
    # the sky gradient goes on behind the ground to reach its end color on
    # the horizon
    rect(document, "Sky",
         graphic_style(document, "sky",
                       **linear_gradient(document, "sky-gradient",
                                         ["#05010f",
                                          mix("#05010f", "#3b0a5c",
                                              HEIGHT / HORIZON)])),
         0, 0, WIDTH, HEIGHT)
    rect(document, "Ground",
         graphic_style(document, "ground",
                       **linear_gradient(document, "ground-gradient",
                                         ["#12002a", "#020008"])),
         0, HORIZON, WIDTH, HEIGHT - HORIZON)


def add_sun(document):
    radius = 300
    center_y = HORIZON - 60

    # ODF has no clip paths, so the bands between the stripes cut out of
    # the lower half are drawn as slices of the circle above the horizon
    bands = []
    top = center_y - radius
    for gap_top, gap in sorted((HORIZON - 40 - i * 34, 4 + 3 * i)
                               for i in range(7)):
        bands.append((top, gap_top))
        top = gap_top + gap
    bands.append((top, HORIZON))

    def half_width(y):
        return math.sqrt(max(radius ** 2 - (y - center_y) ** 2, 0))

    slices = []
    for band_top, band_bottom in bands:
        steps = max(int(band_bottom - band_top) // 2, 1)
        ys = [band_top + (band_bottom - band_top) * i / steps
              for i in range(steps + 1)]
        slices.append([(CENTER_X + half_width(y), y) for y in ys]
                      + [(CENTER_X - half_width(y), y) for y in reversed(ys)])

    # the SVG export lays a gradient over each subpath, so each band is a
    # shape of its own with its part of the gradient over the whole sun
    gradient_top = HORIZON - 2 * radius
    for index, (band, polygon) in enumerate(zip(bands, slices)):
        colors = [mix("#ffd319", "#ff2975", (y - gradient_top) / (2 * radius))
                  for y in band]
        path(document, "Sun",
             graphic_style(document, f"sun-{index}",
                           **linear_gradient(document, f"sun-gradient-{index}",
                                             colors),
                           **glow("#ff2975", 40)),
             polygon_data([polygon]))


def add_grid(document):
    lines = []
    for i in range(-14, 15):
        start, end = CENTER_X + i * 40, CENTER_X + i * 260
        bottom = HEIGHT
        # end the lines on the page edges instead of clipping them
        if not 0 <= end <= WIDTH:
            edge = 0 if end < 0 else WIDTH
            bottom = HORIZON + (HEIGHT - HORIZON) * (edge - start) / (end - start)
            end = edge
        lines.append(f"M {start},{HORIZON} L {end:.2f},{bottom:.2f}")
    depth = 6.0
    while depth < HEIGHT - HORIZON:
        y = HORIZON + depth
        lines.append(f"M 0,{y:.2f} L {WIDTH},{y:.2f}")
        depth *= 1.45

    path(document, "Grid",
         graphic_style(document, "grid", **stroke("#ff00ff", 2),
                       **glow("#ff00ff", 6)),
         " ".join(lines))


def wing_outlines():
    upper = [(CENTER_X - 12, CENTER_Y - 20),
             ((CENTER_X - 120, CENTER_Y - 260), (CENTER_X - 420, CENTER_Y - 330),
              (CENTER_X - 470, CENTER_Y - 230)),
             ((CENTER_X - 520, CENTER_Y - 120), (CENTER_X - 330, CENTER_Y + 20),
              (CENTER_X - 12, CENTER_Y + 10))]
    lower = [(CENTER_X - 12, CENTER_Y + 20),
             ((CENTER_X - 260, CENTER_Y + 30), (CENTER_X - 400, CENTER_Y + 170),
              (CENTER_X - 330, CENTER_Y + 260)),
             ((CENTER_X - 260, CENTER_Y + 340), (CENTER_X - 90, CENTER_Y + 230),
              (CENTER_X - 12, CENTER_Y + 60))]
    return [upper, lower]


def add_wings(document):
    opacity = {"draw__opacity": "92%"}
    left = wing_outlines()
    outline = path_data(left + [mirror_stroke(stroke) for stroke in left])

    # one shape for each wing, as the SVG export lays a gradient over each
    # subpath, with the gradient centered on the body as far as it can be
    for index, wing in enumerate(left + [mirror_stroke(stroke)
                                         for stroke in left]):
        wing_data = path_data([wing])
        x, y, width, height = bounds(wing_data)
        center = [f"{min(max(offset, 0), 1):.0%}"
                  for offset in ((CENTER_X - x) / width,
                                 (CENTER_Y - y) / height)]
        path(document, "Wing",
             graphic_style(document, f"wing-{index}",
                           **radial_gradient(document, f"wing-gradient-{index}",
                                             ["#00f0ff", "#7a00ff"], center),
                           **glow("#00f0ff", 25), **opacity),
             wing_data)

    spot = graphic_style(document, "spot",
                         **radial_gradient(document, "spot-gradient",
                                           ["#ff2975", "#ffd319"]),
                         **opacity)
    for x, y, size in ((-330, -190, 90), (-200, -90, 60), (-250, 170, 70)):
        for cx in (CENTER_X + x, CENTER_X - x):
            ellipse(document, "Wing spot", spot, cx, CENTER_Y + y,
                    size / 2, size / 2)

    path(document, "Wing outline",
         graphic_style(document, "wing-outline",
                       **stroke("#e0ffff", 5, draw__stroke_linejoin="round"),
                       **opacity),
         outline)
    veins = [(start, (start, tip, tip)) for start, (_, _, tip), _ in left]
    veins = veins + [mirror_stroke(vein) for vein in veins]
    path(document, "Wing veins",
         graphic_style(document, "wing-veins", **stroke("#e0ffff", 2),
                       **opacity),
         path_data(veins, closed=False))


def add_body(document):
    body_glow = glow("#ff2975", 12)
    ellipse(document, "Body",
            graphic_style(document, "body",
                          **linear_gradient(document, "body-gradient",
                                            ["#ffffff", "#ff2975"]),
                          **body_glow),
            CENTER_X, CENTER_Y + 40, 16, 130)
    ellipse(document, "Head",
            graphic_style(document, "head",
                          **radial_gradient(document, "head-gradient",
                                            ["#ffffff", "#ff2975"],
                                            center=("50%", "40%")),
                          **body_glow),
            CENTER_X, CENTER_Y - 106, 24, 24)

    antenna = [(CENTER_X - 8, CENTER_Y - 125),
               ((CENTER_X - 30, CENTER_Y - 200), (CENTER_X - 90, CENTER_Y - 250),
                (CENTER_X - 130, CENTER_Y - 250))]
    path(document, "Antennae",
         graphic_style(document, "antennae",
                       **stroke("#ff2975", 4, svg__stroke_linecap="round"),
                       **body_glow),
         path_data([antenna, mirror_stroke(antenna)], closed=False))


def butterfly00():
    document = new_document(WIDTH, HEIGHT)
    add_sky(document)
    add_sun(document)
    add_grid(document)
    add_wings(document)
    add_body(document)
    element(text(document), "text:p")
    return ET.tostring(document, encoding="unicode", xml_declaration=True)
