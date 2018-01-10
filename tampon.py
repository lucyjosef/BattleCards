# partieBataille
    #@staticmethod
    def demarrerPartie(self):
        try:
            jeuCartes.melange(partieBataille.__jeuDeCarte)
            partieBataille.distribuer(partieBataille.__jeuDeCarte)
        except IndexError as err:
            print(err)
            partieBataille.main(partieBataille.__jeuDeCarte)

# partieBataille > bataille
def bataille(self):
    cJoueur1 = self.__joueur1.tirer()
    cJoueur2 = self.__joueur2.tirer()
    # c2Joueur1 = self.__joueur1.tirer()
    # c2Joueur2 = self.__joueur2.tirer()
    print(cJoueur1, 'CONTRE\r\n', cJoueur2)
    if cJoueur1.valeur < cJoueur2.valeur:
        self.__joueur2.ajouter(cJoueur1)
        self.__joueur2.ajouter(cJoueur2)
        # self.__joueur2.ajouter(c2Joueur1)
        # self.__joueur2.ajouter(c2Joueur2)

        self.__joueur2.victoires += 1
        self.__joueur1.defaites += 1
        print(self.__joueur2.prenom, ' gagne et récupère les cartes dans son paquet !')
        self.main()
    elif cJoueur1.valeur > cJoueur2.valeur:
        self.__joueur1.ajouter(cJoueur1)
        self.__joueur1.ajouter(cJoueur2)
        # self.__joueur1.ajouter(c2Joueur1)
        # self.__joueur1.ajouter(c2Joueur2)

        self.__joueur1.victoires += 1
        self.__joueur2.defaites += 1
        print(self.__joueur1.prenom, ' gagne et récupère les cartes dans son paquet !')
        self.main()
    else:
        print("BATAAAAAAAAAILLE !!!")
        self.bataille()