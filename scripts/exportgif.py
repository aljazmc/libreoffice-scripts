from common import drawing, export, load_project

document, output = load_project("build")

export(drawing(document), output + ".gif", "draw_gif_Export",
       PixelWidth=1920,
       PixelHeight=1080)
