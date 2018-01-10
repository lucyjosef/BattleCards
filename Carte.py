class Carte:

    couleurs = ('Coeur', 'Carreau', 'Trefle', 'Pique')
    valeurs = (None, None, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Valet', 'Dame', 'Roi', 'As')

    def __init__(self, val, coul):
        try:
            Carte.validation(val, coul)
        except Exception as err:
            print(err)
            exit(1)
        self.__valeur = val
        self.__couleur = coul

    @staticmethod
    def validation(val, coul):
        if val < 2 or val > 14:
            raise Exception("La valeur d'une carte est comprise entre 2 et 14")
        if coul < 0 or coul > 3:
            raise Exception("Le code couleur d'une carte est compris ente 0 et 3")

    def affiche(self):
        print(Carte.valeurs[self.__valeur], 'de', Carte.couleurs[self.__couleur])

    # Affiche carte avec table ASCII

    def affiche_ascii(self):
        nom = str(Carte.valeurs[self.__valeur]) + " de " + Carte.couleurs[self.__couleur]
        taille = len(nom) + 2
        print("/", "-" * taille, "\\", sep="")
        print("|", " " * taille, "|", sep="")
        print("|", " " * taille, "|", sep="")
        print("|", " " * taille, "|", sep="")
        print("|", " " * taille, "|", sep="")
        print("|", nom, "|")
        print("|", " " * taille, "|", sep="")
        print("|", " " * taille, "|", sep="")
        print("|", " " * taille, "|", sep="")
        print("|", " " * taille, "|", sep="")
        print("\\", "-" * taille, "/", sep="")

    def __str__(self):
        # return str(Carte.valeurs[self.__valeur]) + ' de ' + Carte.couleurs[self.__couleur]
        return str(self.affiche_ascii())

    # Get et Setteur de Valeur

    def __getValeur(self):
        return self.__valeur

    def __setValeur(self, val):
        print("OH ! C'est tricher ça !")
        self.__valeur = val

    valeur = property(__getValeur, __setValeur)

    # Get et Setteur de couleur

    def __getCouleur(self):
        return self.__couleur

    def __setCouleur(self, coul):
        print("Ca sert à rien de changer la couleur tout le monde s'en fout...")
        self.__couleur = coul

    couleur = property(__getCouleur, __setCouleur)
