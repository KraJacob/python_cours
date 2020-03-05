class Livre():
    def __init__(self,nom,nombre_de_page,prix):
        self.nom = nom
        self.nombre_de_page = nombre_de_page
        self.prix = prix


livre_HP = Livre("Harry Potter",300,10.99)
livre_LOTR = Livre("Le Seigneur des Anneaux",400,13.99)
print(livre_HP.nombre_de_page)
print(livre_LOTR.nombre_de_page)