from common import export, load_project

document, output = load_project("build")

export(document, output + ".docbook.xml", "DocBook File")
