from common import drawing, export, load_project

document, output = load_project("build")

export(drawing(document), output + ".tif", "draw_tif_Export",
       PixelWidth=1920,
       PixelHeight=1080)
