from common import export, load_project

document, output = load_project("build")

export(document, output + ".dotx", "MS Word 2007 XML Template")
