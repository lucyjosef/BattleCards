from Carte import Carte
import random

class jeuCartes:

    def __init__(self, vide=False):
        if self.__class__ is jeuCartes:
            raise Exception("Construction directe interdite !")
        else:
            self.__cartes = []
            if not vide:
                self.initialiser()

    def initialiser(self):
        pass

    def __str__(self):
        jeu = ""
        for i in range(len(self.__cartes)):
            if jeu == "":
                jeu = str(self.__cartes[i])
            else:
                jeu = str(self.__cartes[i]) + ", " + jeu
        return jeu

    def melange(self):
        random.shuffle(self.__cartes)

    def tirerCarte(self):
        try:
            return self.__cartes.pop(0)
        except IndexError:
            print("Toutes les cartes sont jouées ! est passé par jeuCartes.py > tirerCarte")
            raise IndexError
            # return None

    def __getCartes(self):
        return self.__cartes

    def __setCartes(self, carte):
        if len(self.__cartes) > 52:
            raise Exception("Jeu complet")
        self.__cartes.append(carte)
    cartes = property(__getCartes, __setCartes)

    def __add__(self, carte):
        self.ajouter(carte)

    def __len__(self):
        return len(self.__cartes)
