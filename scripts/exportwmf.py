from common import drawing, export, load_project

document, output = load_project("build")

export(drawing(document), output + ".wmf", "draw_wmf_Export")
