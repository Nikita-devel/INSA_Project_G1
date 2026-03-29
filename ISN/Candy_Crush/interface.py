"""
Fichier : interface.py
Contient toutes les fonctions d'affichage et d'interaction avec le joueur.
Équipe : Nikita, Lina, Éloïse
"""

def afficher_regles():
    """
    Affiche les règles du jeu Candy Crush dans la console au lancement.
    """
    print("""Pour le niveau 2 : 
    Echangez 2 bonbons de place sur la grille pour creer un groupe de 3 bonbons de meme couleur.
    Si 3 bonbons de meme couleur sont alignes ils se detruisent.
    Si il y a plus de 3 bonbons de la meme couleur alignes, ils se detruisent tous.
    """)

def afficher_compteur(compteur):
    """
    Affiche le score actuel du joueur.
    
    Paramètres :
        compteur : int (Le score actuel à afficher)
    """
    print(f"Le score est de {compteur}")

def afficher_fin_jeu():
    """
    Affiche le message de fin de jeu en cas de victoire.
    """
    print("Bravo vous avez gagne !!!")

def afficher_grille(grille):
    """
    Affiche la grille de jeu dans la console, ligne par ligne.

    Paramètres:
        grille : list[list[int]] (Liste 2D representant la grille du jeu)
    """
    print("\nGrille actuelle :")
    for ligne in grille:
        print(ligne)