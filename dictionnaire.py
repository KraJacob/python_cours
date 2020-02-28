employes = {
            "id01": {"prenom": "Paul", "nom": "Dupont", "age": 32},
            "id02": {"prenom": "Julie", "nom": "Dupuit", "age": 25},
            "id03": {"prenom": "Patrick", "nom": "Ferrand", "age": 36}
            }
del employes["id03"]

age = employes["id02"]["age"]

employes["id02"]["age"] = age + 1

age_paul = employes["id01"]["age"]

print(f"liste des employes {employes}")

print(f"l'age de Paul est : {age_paul}")
