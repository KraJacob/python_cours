import glob
import json
dossier = "D:\PERSO\python\cours_tp\dossier_exemple\**"
files = glob.glob(dossier,recursive=True)
crediMutuel = 0
numSecuriteSocial = 0
for file in files:
    if file.endswith('.json'):
        with open(file,'r') as f:
            contenu = json.load(f)
            if 'Credit Mutuel' in contenu:
               crediMutuel = contenu['Credit Mutuel']['Numero de compte']
    if file.endswith('.txt'):
        with open(file,'r',encoding='utf_8') as f:
            contenu = f.read()
            if 'Numéro de sécurité sociale' in contenu:
                numSecuriteSocial = contenu.split(':')[1]
print(f'le numéro de crédit mutuel est : {crediMutuel}')
print(f'Le numéro de sécurité social est : {numSecuriteSocial}')