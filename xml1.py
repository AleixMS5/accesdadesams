import os
import xml.etree.ElementTree as ET
from jinja2 import Environment, FileSystemLoader
environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("plantilla.html")
if False == os.path.exists("pepe.xml"):
    f1 = open("pepe.xml", "w")
    f1.write("<games></games>")
    f1.close()
tree = ET.parse("pepe.xml")
root = tree.getroot()
alfonso = 100
conta = 0
idfalso = -1
while (True):
    print("  Tria una obcio del menu")
    print(
        "\n 1.- Insertar un nou joc.\n 2.- Llistar els jocs (id, name, year, developer)\n 3.- Mostrar totes les dades d’un joc.\n 4.- Modificar un joc (identificant quin joc pel seu id).\n 5.- Eliminar un joc.\n 6.- Sortir.\n")

    alfonso = input()
    if alfonso == "1":
        #insertem les dades
        for game in root.findall('game'):
            idfalso = int(game.get("id"))
            if idfalso > conta:
                conta = idfalso
        conta += 1
        id = str(conta)
        print("digues el que s'et va demanant per introduir el nou videojoc")
        game = ET.SubElement(root, "game")
        game.set("id", id)
        name = ET.SubElement(game, "name")
        print("digues el nom del videojoc:")
        name.text = input()
        dev = ET.SubElement(game, "dev")
        print("digues el desarrolador del videojoc:")
        dev.text = input()
        year = ET.SubElement(game, "year")
        print("digues l'any en que va sortir el videojoc:")
        year.text = input()
        systems = ET.SubElement(game, "systems")
        print("digues els sistemes per als que va sortit el videojoc separats per comes (1,2,3...):")
        systems.text = input()
        genre = ET.SubElement(game, "genre")
        print("digues el genere del videojoc:")
        genre.text = input()
        description = ET.SubElement(game, "description")
        print("digues una descripció per al videojoc:")
        description.text = input()
        imageURL = ET.SubElement(game, "imageURL")
        print("dona la url d'una imatge del videojoc:")
        imageURL.text = input()
        tree.write("pepe.xml")
        continue
    elif alfonso == "2":
        #veure tots els jocs

        for game in root.findall('game'):
            name = game.find('name').text.strip()
            year = game.find('year').text.strip()
            dev = game.find('dev').text.strip()
            id = game.get('id')
            print(id, name, year, dev)
        continue
    elif alfonso == "3":
        #veure un joc a partir de la id
        pepe = input()
        for game in root.findall('game'):
            id = game.get('id')
            name = game.find('name').text.strip()
            year = game.find('year').text.strip()
            dev = game.find('dev').text.strip()
            systems = game.find('systems').text.strip()
            genre = game.find('genre').text.strip()
            description = game.find('description').text.strip()
            imageURL = game.find('imageURL').text.strip()

            if id == pepe:
                print("id", id, "nom", name, "any", year, "dev", dev, "systems", systems, "genre", genre, "description",
                      description, "imageURL", imageURL)

        continue
    elif alfonso == "4":
        #modificar el joc a partir de la id
        print("l'id del videojoc que vols modificar:")
        pepe = input()
        print("avans era aixi")
        for game in root.findall('game'):
            id = game.get('id')
            name = game.find('name').text.strip()
            year = game.find('year').text.strip()
            dev = game.find('dev').text.strip()
            systems = game.find('systems').text.strip()
            genre = game.find('genre').text.strip()
            description = game.find('description').text.strip()
            imageURL = game.find('imageURL').text.strip()

            if id == pepe:
                print("id", id, "nom", name, "any", year, "dev", dev, "systems", systems,"genre",genre,"description",description,"imageURL",imageURL )

        for game in root.findall('game'):
            id = game.get('id')
            if int(id) == int(pepe):
                root.remove(game)

        game = ET.SubElement(root, "game")

        game.set("id", pepe)
        name = ET.SubElement(game, "name")
        print("digues el nom del videojoc:")
        name.text = input()
        dev = ET.SubElement(game, "dev")
        print("digues el desarrolador del videojoc:")
        dev.text = input()
        year = ET.SubElement(game, "year")
        print("digues l'any en que va sortir el videojoc:")
        year.text = input()
        systems = ET.SubElement(game, "systems")
        print("digues els sistemes per als que va sortit el videojoc separats per comes (1,2,3...):")
        systems.text = input()
        genre = ET.SubElement(game, "genre")
        print("digues el genere del videojoc:")
        genre.text = input()
        description = ET.SubElement(game, "description")
        print("digues una descripció per al videojoc:")
        description.text = input()
        imageURL = ET.SubElement(game, "imageURL")
        print("dona la url d'una imatge del videojoc:")
        imageURL.text = input()
        tree.write("pepe.xml")
        continue
    elif alfonso == "5":
        #esborrar jocs a partir de la id
        print("digues la id del joc a borrar")
        pepe = input()
        for game in root.findall('game'):
            id = game.get('id')
            if int(id) == int(pepe):
                root.remove(game)

        tree.write("pepe.xml")
        continue

    elif alfonso == "6":
        #sortir
        break
arrayJocs=[]
for game in root.findall('game'):
    id = game.get('id')
    name = game.find('name').text.strip()
    year = game.find('year').text.strip()
    dev = game.find('dev').text.strip()
    systems = game.find('systems').text.strip()
    genre = game.find('genre').text.strip()
    description = game.find('description').text.strip()
    imageURL = game.find('imageURL').text.strip()
    arrayJocs.append({'id':id,'name':name,'year':year,'dev':dev,'systems':systems,'genre':genre,'description':description,'imageURL':imageURL})
jocs = {"jocs": arrayJocs}
textoFinal = template.render(jocs)
file = open("games.html","w")

file.write(textoFinal)
