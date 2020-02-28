chemin = r"D:\PERSO\python\fichier.txt"
# Ecrire dans fichier 'w' écrase le contenu du fichier alors que 'a' ajoute à la suite du contenu
with open(chemin, 'w', encoding='utf-8') as f:
    f.write("Je viens de créer cette nouvelle ligne dans mon fichier. C'est super avec python.")
# Lecture du contenu du ficher
with open(chemin, 'r', encoding='utf-8') as f:
    contenu = f.read().splitlines()
    print(contenu)