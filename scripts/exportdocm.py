from common import export, load_project

document, output = load_project("build")

export(document, output + ".docm", "MS Word 2007 XML VBA")
