import random
nombre_mystere = random.randrange(50)
for i in range(5):
    val_saisie = input("Veuillez saisir un nombre : ")
    if val_saisie.isdigit():
        val_saisie = int(val_saisie)
        if val_saisie == nombre_mystere:
            print("Bravo ! vous avez trouvé le nombre mystère ")
            break
        elif val_saisie > nombre_mystere:
            print("Le nombre saisi est supérieur au nombre mtystère")
        elif val_saisie < nombre_mystere:
            print("Le nombre saisi est plus petit que le nombre mystère")
    else:
        print("Veuillez entrer un nombre !")
    if i == 4:
        print(f"Vous avez perdu, le mystère était {nombre_mystere}")