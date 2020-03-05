source = input("Entrer le chemin du fichier : ")
try:
    with open(source,'r') as file:
        print(file.read())
except FileNotFoundError:
    print("Fichier introuvable")
except UnicodeDecodeError:
    print("Impossible de lire ce fichier")