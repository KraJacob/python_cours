import os

chemin = "D:\PERSO\python\cours_tp\dossier_test"
d={
    "Films":["Le seigneur des anneaux","Harry Potter","Moon","Forrest Gump"],
    "Employes":["Paul","Pierre","Marie"],
    "Exercices":["les_variables","les_fichiers","les_boucles"]
}

# for k,v in d.items():
#     dossier = os.path.join(chemin,k)
#     if os.path.exists(dossier):
#         pass
#     else:
#         os.mkdir(dossier)
#         for el in v:
#             sous_dossier = os.path.join(dossier,el)
#             os.mkdir(sous_dossier)
for k,v in d.items():
    for dossier in v:
        docs = os.path.join(chemin,k,dossier)
        os.makedirs(docs, exist_ok=True)