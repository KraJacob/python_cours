source_depart = r"D:\PERSO\python\cours_tp\trie_noms\prenom.txt"
source_final = r"D:\PERSO\python\cours_tp\trie_noms\prenoms_tries.txt"
with open(source_depart,'r',encoding="utf-8") as prenom:
    prenoms = []
    prenom_tries = []
    contenu = prenom.read().splitlines()
    for el in contenu:
        el_trie = el.split()
        prenoms.extend(el_trie)
    for prenom in prenoms:
        prenom_tries.append(prenom.strip(',. '))
    prenom_tries.sort()
    with open(source_final,'w',encoding='utf-8') as file:
        for prenom in prenom_tries:
            file.write(prenom+'\n')
