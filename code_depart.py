import os
import json

dossier_courant = os.path.dirname(__file__)
chemin_liste = os.path.join(dossier_courant, "list.json")

if os.path.exists(chemin_liste):
    with open(chemin_liste, "r") as f:
        liste_de_courses = json.load(f)
else:
    liste_de_courses = []

affichage = """
Choisissez une option:
\t1: Ajouter un élément
\t2: Enlever un élément
\t3: Afficher la liste
\t4: Vider la liste
\t5: Terminer
"""
response = ''
while response != '5':
    response = input(affichage)
    if response == '1':
        article = input("renseigner le nom de l'article svp : ")
        liste_de_courses.append(article)
    elif response == '2':
        article = input("Le nom de l'article à enlever svp : ")
        if article in liste_de_courses:
            liste_de_courses.remove(article)
        else:
            print("Cet article n'existe pas dans la liste de course")
    elif response == '3':
        if liste_de_courses:
            print("\n".join(liste_de_courses))
            # for elt in liste_de_courses:
                #p rint(elt)
        else:
            print('La liste est vide')
    elif response == '4':
        liste_de_courses.clear()
with open(chemin_liste,'w') as f:
    json.dump(liste_de_courses, f, ensure_ascii=False)