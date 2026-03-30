"""
Fichier : main.py
Orchestre la boucle de jeu de Candy Crush.
"""
from moteur import *
from interface import *

def candy_crush(nb_lignes=5, nb_colonnes=5, nb_couleurs=4, score_max=150):
    
    afficher_regles()
    score = 0

    # 1. Création garantie SANS combinaison initiale 
    grille = creer_grille_aleatoire(nb_lignes, nb_colonnes, nb_couleurs)
    while validation_grille(grille) == False:
        grille = creer_grille_aleatoire(nb_lignes, nb_colonnes, nb_couleurs)

    # NOUVEAU : On passe nb_couleurs à la fonction d'affichage
    afficher_grille(grille, nb_couleurs)

    # 2. Boucle principale du jeu
    while verif_score_max(score, score_max) == False:

        print("\n--- CHOISISSEZ DEUX CASES A ECHANGER ---")
        x1 = int(input("Ligne 1 : "))
        y1 = int(input("Colonne 1 : "))
        x2 = int(input("Ligne 2 : "))
        y2 = int(input("Colonne 2 : "))

        coo_1 = [x1, y1]
        coo_2 = [x2, y2]

        if sont_voisins(coo_1, coo_2) == True:
            
            # On simule l'échange
            grille = echange_les_cases(grille, coo_1, coo_2)
            afficher_grille(grille, nb_couleurs)

            if trois_alignes(grille) == True:
                
                # Gestion des réactions en chaîne (Cascades / Niveau 2)
                cascade_en_cours = True
                while cascade_en_cours == True:
                    
                    cases = selectionner_les_cases(grille)
                    cases = ya_voisin(grille, cases)
                    
                    grille = detruire_cases(grille, cases)
                    score += len(cases) * 10 
                    
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
                afficher_grille(grille, nb_couleurs) # On réaffiche la grille après annulation
        else:
            print("\nLes cases ne sont pas voisines !")

    afficher_fin_jeu() 

# Lancement du jeu
if __name__ == "__main__":
    candy_crush()