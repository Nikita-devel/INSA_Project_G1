# -*- coding: utf-8 -*-
"""
Fichier : interface.py
Contient toutes les fonctions d'affichage et d'interaction avec le joueur.
Mise à jour graphique : Affichage de cercles colorés.
Équipe : Nikita, Lina, Éloïse
"""
import matplotlib.pyplot as plt
from matplotlib.patches import Circle # Import spécifique pour dessiner des cercles

# AMÉLIORATION : Mode interactif pour des animations fluides
plt.ion() 

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
    Les bonbons sont dessinés sous forme de cercles colorés.
    """
    plt.clf() # Nettoie l'image précédente
    plt.title("Candy Crush ISN ", fontsize=16)
    
    lignes = len(grille)
    colonnes = len(grille[0])
    
    # Palette de couleurs vives (Rouge, Vert, Bleu, Jaune, Orange, Violet)
    palette = ['#FF3B30', '#4CD964', '#007AFF', '#FFCC00', '#FF9500', '#AF52DE']
    
    # Fond du plateau de jeu 
    plt.gca().set_facecolor('#2C3E50')
    
    # Dessiner la grille de fond
    for i in range(lignes + 1):
        plt.axhline(i - 0.5, color='#34495E', linewidth=1)
    for j in range(colonnes + 1):
        plt.axvline(j - 0.5, color='#34495E', linewidth=1)
        
    # Dessiner les bonbons sous forme de cercles
    for i in range(lignes):
        for j in range(colonnes):
            valeur = grille[i][j]
            
            # Si la case n'est pas détruite (-1)
            if valeur != -1:
                # Calcul des coordonnées (j est X, et y doit être inversé pour que la ligne 0 soit en haut)
                x = j
                y = lignes - 1 - i 
                
                # Récupération de la couleur
                couleur_bonbon = palette[valeur % len(palette)]
                
                # Création d'un cercle avec une fine bordure blanche
                # radius=0.4 pour un bon compromis entre taille et espace
                cercle = Circle((x, y), radius=0.4, color=couleur_bonbon, ec='white', lw=1.5)
                plt.gca().add_patch(cercle)
                
    # Paramètres d'affichage
    plt.xlim(-0.5, colonnes - 0.5)
    plt.ylim(-0.5, lignes - 0.5)
    plt.axis('equal') # Important pour que les cercles soient ronds
    plt.axis('off') # Cache les axes X et Y
    
    # Mise à jour de l'affichage
    plt.draw()
    plt.pause(0.3) # Temps de pause pour voir l'animation des combos