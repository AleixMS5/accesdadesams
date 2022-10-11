from jinja2 import Environment, FileSystemLoader

enviroment = Environment(loader=FileSystemLoader("templates/"))
template = enviroment.get_template("html1.html")
info = {"titol": "la meva vida"}
file = open("web.html", "w")
contingut = template.render(info)
file.write(contingut)
