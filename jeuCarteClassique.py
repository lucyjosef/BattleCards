from jeuCartes import jeuCartes
from Carte import Carte

class jeuCarteClassique(jeuCartes):

    def initialiser(self):
        for val in range(2, 15):
            for coul in range(4):
                self.cartes.append(Carte(val, coul))
