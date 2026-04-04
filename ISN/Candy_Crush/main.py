# -*- coding: utf-8 -*-
"""
Fichier : main.py
Orchestre la boucle de jeu de Candy Crush.
"""
from moteur import *
from interface import *
import matplotlib.pyplot as plt

def candy_crush(score_max=3000):
    
    afficher_regles()
    score = 0
    
    # 1. Menu de lancement : Choix du type de grille
    print("\nMenu de lancement :")
    print("1. Charger une grille depuis un fichier CSV")
    print("2. Generer une grille aleatoire")
    
    choix = ""
    while choix != "1" and choix != "2":
        choix = input("Votre choix (tapez 1 ou 2) : ")
        
    if choix == "1":
        nom_fichier = input("Entrez le nom du fichier (ex: exemple_grille.csv) : ")
        grille = creer_grille_csv(nom_fichier)
        print(f"\nSucces : Grille chargee depuis '{nom_fichier}'.")
        
        # Calcul du nombre de couleurs max manuellement
        valeur_max = 0
        for i in range(len(grille)):
            for j in range(len(grille[0])):
                if grille[i][j] > valeur_max:
                    valeur_max = grille[i][j]
        nb_couleurs = valeur_max + 1
        
        nb_lignes = len(grille)
        nb_colonnes = len(grille[0])
        
    else:
        nb_lignes, nb_colonnes, nb_couleurs = 5, 5, 4
        grille = creer_grille_aleatoire(nb_lignes, nb_colonnes, nb_couleurs)
        while validation_grille(grille) == False:
            grille = creer_grille_aleatoire(nb_lignes, nb_colonnes, nb_couleurs)

    afficher_grille(grille, nb_couleurs)

    # 2. Boucle principale du jeu
    en_cours = True
    while en_cours == True:
        
        if verif_score_max(score, score_max) == True:
            en_cours = False
            afficher_fin_jeu()
            
        elif echange_possible(grille) == False:
            en_cours = False
            print("\nDommage ! Il n'y a plus aucun echange possible sur la grille. Fin de la partie.")
            
        else:
            print("\nChoisissez deux cases a echanger :")
            
            coordonnees_valides = False
            while coordonnees_valides == False:
                x1 = int(input(f"Ligne 1 (0 a {nb_lignes-1}) : "))
                y1 = int(input(f"Colonne 1 (0 a {nb_colonnes-1}) : "))
                x2 = int(input(f"Ligne 2 (0 a {nb_lignes-1}) : "))
                y2 = int(input(f"Colonne 2 (0 a {nb_colonnes-1}) : "))
                
                if (x1 >= 0 and x1 < nb_lignes) and (y1 >= 0 and y1 < nb_colonnes) and \
                   (x2 >= 0 and x2 < nb_lignes) and (y2 >= 0 and y2 < nb_colonnes):
                    coordonnees_valides = True
                else:
                    print("Erreur : Coordonnees hors limites. Veuillez reessayer.")

            coo_1 = [x1, y1]
            coo_2 = [x2, y2]

            if sont_voisins(coo_1, coo_2) == True:
                
                grille = echange_les_cases(grille, coo_1, coo_2)
                afficher_grille(grille, nb_couleurs)

                if trois_alignes(grille) == True:
                    
                    cascade_en_cours = True
                    while cascade_en_cours == True:
                        cases = selectionner_les_cases(grille)
                        cases = ya_voisin(grille, cases)
                        
                        grille = detruire_cases(grille, cases)
                        score = score + (len(cases) * 10) 
                        
                        print("\nBOOM ! Bonbons detruits.")
                        afficher_grille(grille, nb_couleurs)
                        
                        grille = generer_cases(grille, nb_couleurs)
                        print("\nNouveaux bonbons (Gravite).")
                        afficher_grille(grille, nb_couleurs)
                        afficher_compteur(score)
                        
                        if trois_alignes(grille) == False:
                            cascade_en_cours = False
                else:
                    print("\nPas d'alignement -> echange annule")
                    grille = echange_les_cases(grille, coo_1, coo_2)
                    afficher_grille(grille, nb_couleurs) 
            else:
                print("\nLes cases ne sont pas voisines !")

    # Garde la fenetre graphique ouverte a la fin de la partie
    plt.ioff()
    plt.show()

if __name__ == "__main__":
    candy_crush()