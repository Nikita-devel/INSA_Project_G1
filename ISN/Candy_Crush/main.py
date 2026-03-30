# -*- coding: utf-8 -*-
"""
Fichier : main.py
Orchestre la boucle de jeu de Candy Crush.
"""
from moteur import *
from interface import *

def candy_crush(nb_lignes=5, nb_colonnes=5, nb_couleurs=4, score_max=3000):
    
    afficher_regles()
    score = 0

    # 1. Création garantie SANS combinaison initiale 
    grille = creer_grille_aleatoire(nb_lignes, nb_colonnes, nb_couleurs)
    while validation_grille(grille) == False:
        grille = creer_grille_aleatoire(nb_lignes, nb_colonnes, nb_couleurs)

    afficher_grille(grille, nb_couleurs)

    # 2. Boucle principale du jeu
    while verif_score_max(score, score_max) == False:

        print("\n--- CHOISISSEZ DEUX CASES A ECHANGER ---")
        
        # Vérification des limites de la grille (Sécurité)
        coordonnees_valides = False
        while coordonnees_valides == False:
            x1 = int(input(f"Ligne 1 (0 à {nb_lignes-1}) : "))
            y1 = int(input(f"Colonne 1 (0 à {nb_colonnes-1}) : "))
            x2 = int(input(f"Ligne 2 (0 à {nb_lignes-1}) : "))
            y2 = int(input(f"Colonne 2 (0 à {nb_colonnes-1}) : "))
            
            # On vérifie que le joueur ne tape pas -1 ou 10 si la grille fait 5x5
            if (x1 >= 0 and x1 < nb_lignes) and (y1 >= 0 and y1 < nb_colonnes) and \
               (x2 >= 0 and x2 < nb_lignes) and (y2 >= 0 and y2 < nb_colonnes):
                coordonnees_valides = True
            else:
                print("Erreur : Coordonnées hors limites. Veuillez réessayer.")

        coo_1 = [x1, y1]
        coo_2 = [x2, y2]

        if sont_voisins(coo_1, coo_2) == True:
            
            # On simule l'échange
            grille = echange_les_cases(grille, coo_1, coo_2)
            afficher_grille(grille, nb_couleurs)

            if trois_alignes(grille) == True:
                
                # Gestion des réactions en chaîne (Cascades)
                cascade_en_cours = True
                while cascade_en_cours == True:
                    
                    cases = selectionner_les_cases(grille)
                    cases = ya_voisin(grille, cases)
                    
                    grille = detruire_cases(grille, cases)
                    score = score + (len(cases) * 10) 
                    
                    print("\nBOOM ! Bonbons détruits.")
                    afficher_grille(grille, nb_couleurs)
                    
                    grille = generer_cases(grille, nb_couleurs)
                    print("\nNouveaux bonbons (Gravité).")
                    afficher_grille(grille, nb_couleurs)
                    afficher_compteur(score)
                    
                    # Arrêt de la réaction en chaîne s'il n'y a plus de combinaison
                    if trois_alignes(grille) == False:
                        cascade_en_cours = False
            else:
                print("\nPas d'alignement -> échange annulé")
                grille = echange_les_cases(grille, coo_1, coo_2)
                afficher_grille(grille, nb_couleurs) 
        else:
            print("\nLes cases ne sont pas voisines !")

    afficher_fin_jeu() 

# Lancement du jeu
if __name__ == "__main__":
    candy_crush()