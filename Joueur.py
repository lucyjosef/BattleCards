from paquet import paquet


class Joueur:

    def __init__(self, nom, prenom):
        self.__nom = nom
        self.__prenom = prenom
        self.__victoires = 0
        self.__defaites = 0
        self.__paquet = paquet()


    def tirer(self):
        try:
            return self.__paquet.tirerCarte()
        except IndexError:
            print("STOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOP - Joueur.py > def tirer")

    def ajouter(self, carte):
        self.__paquet.ajouter(carte)

    def __add__(self, carte):
        self.ajouter(carte)


    def __getNom(self):
        return self.__nom
    def __setNom(self, nom):
        self.__nom = nom
    nom = property(__getNom, __setNom)

    def __getPrenom(self):
        return self.__prenom
    def __setPrenom(self, prenom):
        self.__prenom = prenom
    prenom = property(__getPrenom, __setPrenom)

    def __getVictoires(self):
        return self.__victoires
    def __setVictoires(self, victoires):
        self.__victoires = victoires
    victoires = property(__getVictoires, __setVictoires)

    def __getDefaites(self):
        return self.__defaites
    def __setDefaites(self, defaites):
        self.__defaites = defaites
    defaites = property(__getDefaites, __setDefaites)

    def __getPaquet(self):
        return self.__paquet
    def __setPaquet(self, paquet):
        self.__paquet = paquet
    paquet = property(__getPaquet, __setPaquet)
