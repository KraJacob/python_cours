import glob
dossier = "D:\PERSO\python\cours_tp\dossier_exemple\**"
files = glob.glob(dossier, recursive=True)
for folder in files:
    print(folder)