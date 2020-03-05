class Voiture:
    essence = 100

    def afficher_reservoir(self):
        print(f"La voiture contient {self.essence} litres d’essence")

    def roule(self,km):
        if self.essence <= 0:
            return print("Vous n'avez plus d'essence, faites le plein !")
        elif self.essence < 10:
            print("Vous n'avez bientôt plus d'essence !")
            self.essence = self.essence - ((km*5)/100)
            print(self.afficher_reservoir())
        else:
            self.essence = self.essence - ((km*5)/100)
            self.afficher_reservoir()

    def faire_le_plein(self):
        self.essence += 100
