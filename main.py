import os
import shutil
import urllib.request
from getpass import getuser

try:
    directori = "/home/" + (getuser()) + "/URLDownloaderMontero"
    i = 1
    os.mkdir(directori)
except FileExistsError:
    print(" ")

while (i != 0):
    initial_count = 0
    print("\n")
    print("0:sotir del programa")
    print("1:descarregar url")
    print("2:actualitzar url")
    print("\n")
    i = int(input("digues l'obcio del menu"))


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------CREAR--FITXERS-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if i == 1:
        print("dona la url")
        urlint = input()
        agafardomini = urlint.split("/")
        try:
            directori = "/home/" + (getuser()) + "/URLDownloaderMontero/" + agafardomini[2]
            os.mkdir(directori)
        except FileExistsError:
            print(" ")
        if False == os.path.exists(
                "/home/" + (getuser()) + "/URLDownloaderMontero/" + agafardomini[2] + "/" + agafardomini[
                    len(agafardomini) - 1] + ".html"):
            f1 = open(
                "/home/" + (getuser()) + "/URLDownloaderMontero/" + agafardomini[2] + "/" + agafardomini[
                    len(agafardomini) - 1] + ".html",
                "w")

            connexio = urllib.request.urlopen(urlint)
            contingut = connexio.read().decode('UTF-8')
            f1.write(contingut)
            f1.close()

        else:
            # comptem els fitxers
            pepe = True
            while pepe != False:

                try:
                    open("/home/" + (getuser()) + "/URLDownloaderMontero/" + agafardomini[2] + "/" + agafardomini[
                        len(agafardomini) - 1] + ".html", "x")

                except FileExistsError:
                    initial_count += 1
                    while os.path.exists(
                            "/home/" + (getuser()) + "/URLDownloaderMontero/" + agafardomini[2] + "/" + agafardomini[
                                len(agafardomini) - 1] + "-" + str(initial_count) + "-.html"):
                        try:

                            open("/home/" + (getuser()) + "/URLDownloaderMontero/" + agafardomini[2] + "/" +
                                 agafardomini[
                                     len(agafardomini) - 1] + ".html", "x")
                        except FileExistsError:
                            break;
                    else:
                        break;

            shutil.copy(
                "/home/" + (getuser()) + "/URLDownloaderMontero/" + agafardomini[2] + "/" + agafardomini[
                    len(agafardomini) - 1] + ".html",
                "/home/" + (getuser()) + "/URLDownloaderMontero/" + agafardomini[2] + "/" + agafardomini[
                    len(agafardomini) - 1] + "-" + str(initial_count) + "-.html")

            os.remove("/home/" + (getuser()) + "/URLDownloaderMontero/" + agafardomini[2] + "/" + agafardomini[
                len(agafardomini) - 1] + ".html")
            f1 = open(
                "/home/" + (getuser()) + "/URLDownloaderMontero/" + agafardomini[2] + "/" + agafardomini[
                    len(agafardomini) - 1] + ".html",
                "w")

            connexio = urllib.request.urlopen(urlint)
            contingut = connexio.read().decode('UTF-8')
            f1.write(contingut)
            f1.close()

        print("fitxer creat")
        continue
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------MODIFICAR--FITXERS-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if i == 2:
        print("dona la url a actalitzar")
        urlact = input()
        agafardomini = urlact.split("/")
        if False == os.path.exists(
                "/home/" + (getuser()) + "/URLDownloaderMontero/" + agafardomini[2] + "/" + agafardomini[
                    len(agafardomini) - 1] + ".html"):
            print("aquesta url no ha estat introduïda per favor introdueixla abans per poder-la actualitzar")
            continue
        else:

            pepe = True
            while pepe != False:

                try:
                    os.remove("/home/" + (getuser()) + "/URLDownloaderMontero/" + agafardomini[2] + "/" + agafardomini[
                        len(agafardomini) - 1] + ".html")

                except FileNotFoundError:
                    initial_count += 1
                    while os.path.exists("/home/" + (getuser()) + "/URLDownloaderMontero/" + agafardomini[2] + "/" + agafardomini[
                                len(agafardomini) - 1] + "-" + str(initial_count) + "-.html"):

                        try:
                            os.remove("/home/" + (getuser()) + "/URLDownloaderMontero/" + agafardomini[2] + "/" + agafardomini[
                    len(agafardomini) - 1] + "-" + str(initial_count) + "-.html")
                            initial_count += 1

                        except FileNotFoundError:
                            break
                    else:
                        break
        f1 = open(
            "/home/" + (getuser()) + "/URLDownloaderMontero/" + agafardomini[2] + "/" + agafardomini[
                len(agafardomini) - 1] + ".html",
            "w")

        connexio = urllib.request.urlopen(urlact)
        contingut = connexio.read().decode('UTF-8')
        f1.write(contingut)
        f1.close()
        continue
