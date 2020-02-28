import json

chemin = r"D:\PERSO\python\fiche.json"

with open(chemin, 'w') as f:
    # écriture dans le fichier json
    json.dump(list(range(5)), f, indent=2)
with open(chemin, 'r') as f:
    # lecture du fichier json
     contenu = json.load(f)
     print(contenu)