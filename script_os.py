import os
chemin = "D:\PERSO\python\cours_tp"
dossier = os.path.join(chemin, "dossier","Test")
# os.makedirs(dossier, exist_ok=True) creation du dossier
if os.path.exists(dossier):
    os.removedirs(dossier)