import gzip
import os
import shutil
import tempfile

from common import drawing, export, load_project

document, output = load_project("build")

# draw_svgz_Export fails to write shapes with both a gradient and
# transparency, so this compresses the output of draw_svg_Export instead
with tempfile.TemporaryDirectory() as tmp:
    svg = os.path.join(tmp, "drawing.svg")
    export(drawing(document), svg, "draw_svg_Export")
    with open(svg, "rb") as source, gzip.open(output + ".svgz", "wb") as target:
        shutil.copyfileobj(source, target)
