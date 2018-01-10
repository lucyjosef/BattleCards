from partieBataille import partieBataille
from Joueur import Joueur

if __name__ == "__main__":

    print("\r\n--------------- REGLES DU JEU ---------------\r\n\r\n"
          "- Le joueur 1 renseigne son nom et prénom\r\n"
          "- Le joueur 2 fait pareil juste après\r\n"
          "- La partie se lance avec un premier tour\r\n"
          "- ENTRER pour poursuivre la partie\r\n"
          "- Le programme se charge de distribuer et tirer les cartes\r\n"
          "- Touche 1 = ENTRER pour interrompre la partie\r\n")

    nom1 = input("JOUEUR 1 -- Ton nom :")
    prenom1 = input("JOUEUR 1 -- Ton prénom :")
    nom2 = input("JOUEUR 2 -- Ton nom :")
    prenom2 = input("JOUEUR 2 -- Ton prénom :")

    partieBataille.demarrerPartie(partieBataille(nom1, prenom1, nom2, prenom2))
