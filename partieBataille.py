from Joueur import Joueur
from jeuCarteClassique import jeuCarteClassique


class partieBataille:

    def __init__(self, nom1, prenom1, nom2, prenom2):
        self.nom1 = nom1
        self.prenom1 = prenom1
        self.nom2 = nom2
        self.prenom2 = prenom2


        self.__joueur1 = Joueur(nom1, prenom1)
        self.__joueur2 = Joueur(nom2, prenom2)

        self.__jeuDeCarte = jeuCarteClassique()

    def distribuer(self):
        while True:
            self.__joueur1.ajouter(self.__jeuDeCarte.tirerCarte())
            self.__joueur2.ajouter(self.__jeuDeCarte.tirerCarte())

    tableauArchive = []
    def bataille(self):

        if len(self.__joueur1.paquet.cartes) > 1:
            self.tableauArchive.append(self.__joueur1.tirer())
            cJoueur1 = self.__joueur1.tirer()
        else:
            self.finPartie()

        if len(self.__joueur2.paquet.cartes) > 1:
            self.tableauArchive.append(self.__joueur2.tirer())
            cJoueur2 = self.__joueur2.tirer()
        else:
            self.finPartie()

        print(cJoueur1, 'CONTRE\r\n', cJoueur2)
        if cJoueur1.valeur < cJoueur2.valeur:
            self.tableauArchive.append(cJoueur1)
            self.tableauArchive.append(cJoueur2)
            self.__joueur2.victoires += 1
            self.__joueur1.defaites += 1
            print(self.__joueur2.prenom, ' gagne et récupère les cartes dans son paquet !')
            for i in range(len(self.tableauArchive)):
                self.__joueur2.ajouter(self.tableauArchive.pop(0))
            self.main()
        elif cJoueur1.valeur > cJoueur2.valeur:
            self.tableauArchive.append(cJoueur1)
            self.tableauArchive.append(cJoueur2)
            self.__joueur1.victoires += 1
            self.__joueur2.defaites += 1
            print(self.__joueur1.prenom, ' gagne et récupère les cartes dans son paquet !')
            for i in range(len(self.tableauArchive)):
                self.__joueur1.ajouter(self.tableauArchive.pop(0))
            self.main()
        else:
            print("BATAAAAAAAAAILLE !!!")
            self.bataille()


    def melanger(self):
        jeuCarteClassique.melange(self.__jeuDeCarte)

    def demarrerPartie(self):
        try:
            self.melanger()
            self.distribuer()
        except IndexError as err:
            while True:
                self.main()

    def finPartie(self):
        if self.__joueur1.defaites < self.__joueur2.defaites:
            print(self.__joueur1.prenom, 'a gagné cette partie!')
        elif self.__joueur2.defaites < self.__joueur1.defaites:
            print(self.__joueur2.prenom, 'a gagné cette partie!')
        else:
            print("Egalité, chose rare dans la bataille.")
        exit(1)
        restart = input("Tape 1 pour rejouer ! Sinon tape n'importe quelle touche !")
        if restart == 1:
            self.demarrerPartie()
        else:
            exit(1)

    def main(self):
        while len(self.__joueur1.paquet.cartes) != 0 or len(self.__joueur2.paquet.cartes) != 0:
            if len(self.__joueur1.paquet.cartes) != 0:
                cJoueur1 = self.__joueur1.tirer()
            else:
                self.finPartie()

            if len(self.__joueur2.paquet.cartes) != 0:
                cJoueur2 = self.__joueur2.tirer()
            else:
                self.finPartie()

            print(cJoueur1, '\r CONTRE\n\r', cJoueur2, '\r ')
            if cJoueur1.valeur < cJoueur2.valeur:
                self.__joueur2.ajouter(cJoueur1)
                self.__joueur2.ajouter(cJoueur2)
                self.__joueur2.victoires += 1
                self.__joueur1.defaites += 1
                print(self.__joueur2.prenom, 'gagne et récupère les cartes dans son paquet !')
                print(len(self.__joueur1.paquet.cartes))
                print(len(self.__joueur2.paquet.cartes))
            elif cJoueur1.valeur > cJoueur2.valeur:
                self.__joueur1.ajouter(cJoueur1)
                self.__joueur1.ajouter(cJoueur2)
                self.__joueur1.victoires += 1
                self.__joueur2.defaites += 1
                print(self.__joueur1.prenom, 'gagne et récupère les cartes dans son paquet !')
                print(len(self.__joueur1.paquet.cartes))
                print(len(self.__joueur2.paquet.cartes))
            else:
                print("BATAAAAAAAAAILLE !!!")
                self.bataille()
            nextRound = input("")
            if nextRound == "1":
                self.finPartie()
            else:
                if self.__joueur1.paquet.cartes == 0 or self.__joueur2.paquet.cartes == 0:
                  exit(1)
        print("gyjugjvfgh")
        self.finPartie()

    # GETSETTEUR SPACE ! Yoloooo
    def __getJoueur1(self):
        return self.__joueur1
    def __setJoueur1(self, joueur1):
        self.__joueur1 = joueur1
    joueur1 = property(__getJoueur1, __setJoueur1)

    def __getJoueur2(self):
        return self.__joueur2
    def __setJoueur2(self, joueur2):
        self.__joueur2 = joueur2
    joueur2 = property(__getJoueur2, __setJoueur2)

    def __getJeuDeCarte(self):
        return self.__jeuDeCarte
    def __setJeuDeCarte(self, jeuDeCarte):
        self.__jeuDeCarte = jeuDeCarte
    jeuDeCarte = property(__getJeuDeCarte, __setJeuDeCarte)
