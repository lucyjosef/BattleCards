from jeuCartes import jeuCartes


class paquet(jeuCartes):

    def __init__(self):
        super().__init__(True)  # equivalent a jeuCartes.__init__(True)

    def ajouter(self, carte):
        self.cartes.append(carte)
