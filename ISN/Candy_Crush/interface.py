"""
Fichier : interface.py
Contient toutes les fonctions d'affichage et d'interaction avec le joueur.
Équipe : Nikita, Lina, Éloïse
"""
import matplotlib.pyplot as plt # Import exigé par le sujet

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
    """
    print(f"Le score est de {compteur}")

def afficher_fin_jeu():
    """
    Affiche le message de fin de jeu en cas de victoire.
    """
    print("\nBravo vous avez gagne !!!")

def afficher_grille_console(grille):
    """
    (Version texte) Affiche la grille de jeu dans la console.
    """
    print("\nGrille actuelle :")
    for ligne in grille:
        print(ligne)

def afficher_grille(grille, nb_type_bonbons):
    """
    Affiche la grille de jeu "grille" contenant au maximum nb_type_bonbons (entier) 
    couleurs de bonbons différentes via une fenêtre graphique Matplotlib.
    Les bonbons sont codés entre 0 et nb_type_bonbons-1.
    """
    plt.imshow(grille, vmin=0, vmax=nb_type_bonbons-1, cmap='jet')
    plt.pause(0.1)
    plt.draw()
    plt.pause(0.1)