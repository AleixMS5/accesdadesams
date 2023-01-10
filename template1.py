from jinja2 import Environment, FileSystemLoader
import xml.etree.ElementTree as ET
tree = ET.parse("pepe.xml")
root = tree.getroot()
for game in root.findall('game'):
    id = game.get('id')
    name = game.find('name').text.strip()
    year = game.find('year').text.strip()
    dev = game.find('dev').text.strip()
    systems = game.find('systems').text.strip()
    genre = game.find('genre').text.strip()
    description = game.find('description').text.strip()
    imageURL = game.find('imageURL').text.strip()

enviroment = Environment(loader=FileSystemLoader("templates/"))
template = enviroment.get_template("plantilla.html")
info = {"jocs":[
    {"name":name}]}
contingut = template.render(info)
file = open("web.html", "w")

file.write(contingut)
