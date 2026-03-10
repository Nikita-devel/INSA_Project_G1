# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

afficher_regles = print("""Pour le niveau 2 : 
Echangez 2 bonbons de place sur la grille pour créer un groupe de 3 bonbons de même couleur, si 3 bobnons de même couleur sont alignés ils se détruisent. 
Si il y a plus de 3 bonbons de la même couleur alignés, ils se détruisent tous.""")


afficher_compteur = print(f'Le score est de {compteur}')

afficher_fin_jeu = print('Bravo vous avez gagné !!!')

def détruire_cases(grille, liste):
    """
    détruit les cases de la liste

    Parameters
    ----------
    grille : liste 2D
        grille de jeu
    liste : liste
        liste des coordonnées des bonbons à supprimer

    Returns
    -------
    grille : liste 2D
        grille de jeu sans les combinaisons supprimées

    """
    couleur=[]
    for (x, y) in liste:
        if grille[x][y] not in couleur:
            couleur.append(grille[x][y])
        grille[x][y] = -1
        maj_score(liste)
        return grille
    
def echange_les_cases(grille, coo_1, coo_2):
    x_1, y_1 = coo_1
    x_2, y_2 = coo_2
    grille[x_1][y_1] = temp
    grille[x_1][y_1] = grille[x_2][y_2]
    grille[x_2][y_2] = temp
    return grille
            