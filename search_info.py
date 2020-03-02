import glob
import json
dossier = "D:\PERSO\python\cours_tp\dossier_exemple\**"
files = glob.glob(dossier, recursive=True)
for f in files:
    if f.endswith('.json'):
        with open(f, 'r') as file:
            contenu = json.load(file)
            if 'Credit Mutuel' in contenu:
                credit_mutuel = contenu["Credit Mutuel"]["Numero de compte"]
    elif f.endswith('.txt'):
        # print(f)
        with open(f, 'r',encoding="utf-8") as fichier:
            contenu = fichier.read()
            # print(contenu)
            if "Numéro de sécurité sociale" in contenu:
                securit_social = contenu.split(':')[-1]
                #print("ok")
print(f'le numéro de crédit mutuel est {credit_mutuel}')
print(f'le numéro de sécurité sociale est {securit_social}')