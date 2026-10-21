from common import export, load_project

document, output = load_project("odf")

export(document, output + ".odt", "writer8")
