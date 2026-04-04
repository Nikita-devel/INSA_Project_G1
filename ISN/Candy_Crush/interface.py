# -*- coding: utf-8 -*-
"""
Fichier : interface.py
Contient toutes les fonctions d'affichage et d'interaction avec le joueur.
Mise à jour graphique : Affichage de cercles colorés.
Équipe : Nikita, Lina, Éloïse
"""
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Mode interactif pour des animations fluides
plt.ion() 

def afficher_regles():
    """
    Affiche les règles du jeu Candy Crush dans la console au lancement.
    """
    print("""
BIENVENUE DANS CANDY CRUSH

Règles :
1. Échangez 2 bonbons voisins pour aligner 3 bonbons de même couleur.
2. NIVEAU 2 : Tous les bonbons voisins de la même couleur explosent aussi !
3. La gravité fait tomber de nouveaux bonbons, créant des combos (Cascades).
""")

def afficher_compteur(compteur):
    """
    Affiche le score actuel du joueur.
    """
    print(f"Score actuel : {compteur}")

def afficher_fin_jeu():
    """
    Affiche le message de fin de jeu en cas de victoire.
    """
    print("\nBravo ! Vous avez gagne ! Score maximum atteint !")

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
    plt.clf()
    plt.title("Candy Crush ISN", fontsize=16)
    
    lignes = len(grille)
    colonnes = len(grille[0])
    
    palette = ['#FF3B30', '#4CD964', '#007AFF', '#FFCC00', '#FF9500', '#AF52DE', '#34C759']
    
    plt.gca().set_facecolor('#2C3E50')
    
    for i in range(lignes + 1):
        plt.axhline(i - 0.5, color='#34495E', linewidth=1)
    for j in range(colonnes + 1):
        plt.axvline(j - 0.5, color='#34495E', linewidth=1)
        
    for i in range(lignes):
        for j in range(colonnes):
            valeur = grille[i][j]
            
            if valeur != -1:
                x = j
                y = lignes - 1 - i 
                
                couleur_bonbon = palette[valeur % len(palette)]
                
                cercle = Circle((x, y), radius=0.4, color=couleur_bonbon, ec='white', lw=1.5)
                plt.gca().add_patch(cercle)
                
    plt.xlim(-0.5, colonnes - 0.5)
    plt.ylim(-0.5, lignes - 0.5)
    plt.axis('equal') 
    plt.axis('off') 
    
    plt.draw()
    plt.pause(0.5)