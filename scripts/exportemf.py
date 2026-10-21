from common import drawing, export, load_project

document, output = load_project("build")

export(drawing(document), output + ".emf", "draw_emf_Export")
