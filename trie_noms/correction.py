source_depart = r"D:\PERSO\python\cours_tp\trie_noms\prenom.txt"
source_final = r"D:\PERSO\python\cours_tp\trie_noms\prenoms_tries.txt"
with open(source_depart, "r") as f:
    lines = f.read().splitlines()

prenoms = []
for line in lines:
    prenoms.extend(line.split())

prenoms_final = [prenom.strip(",. ") for prenom in prenoms]

with open(source_final, "w") as f:
    f.write("\n".join(sorted(prenoms_final)))