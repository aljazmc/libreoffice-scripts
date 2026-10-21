from common import drawing, export, load_project

document, output = load_project("build")

export(drawing(document), output + ".otg", "draw8_template")
