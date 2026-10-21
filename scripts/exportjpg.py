from common import drawing, export, load_project

document, output = load_project("build")

export(drawing(document), output + ".jpg", "draw_jpg_Export",
       PixelWidth=1920,
       PixelHeight=1080,
       Quality=90)
