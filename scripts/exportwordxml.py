from common import export, load_project

document, output = load_project("build")

export(document, output + ".wordxml.xml", "MS Word 2003 XML")
