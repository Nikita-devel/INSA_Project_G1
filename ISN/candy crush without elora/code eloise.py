# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

afficher_regles = print("""Pour le niveau 2 : 
Echangez 2 bonbons de place sur la grille pour créer un groupe de 3 bonbons de même couleur, si 3 bobnons de même couleur sont alignés ils se détruisent. 
Si il y a plus de 3 bonbons de la même couleur alignés, ils se détruisent tous.""")

compteur = 0
afficher_compteur = print(f'Le score est de {compteur}')

afficher_fin_jeu = print('Bravo vous avez gagné !!!')

def detruire_cases(grille, liste):
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
        #maj_score(liste)
        return grille
    
def echange_les_cases(grille, coo_1, coo_2):
    x_1, y_1 = coo_1
    x_2, y_2 = coo_2
    temp = grille[x_1][y_1] 
    grille[x_1][y_1] = grille[x_2][y_2]
    grille[x_2][y_2] = temp
    return grille

#jeu de test
#pour une liste vide
print(detruire_cases([[1,3],[1,2]], []))
#pur une liste de 2 identiques
print(detruire_cases([[1,3],[1,2]], [(1,1),(2,1)]))

#echanger 2 fois la meme case
print(echange_les_cases([[1,6],[1,6]],(1,1),(1,1)))
#echanger 2 cases differentes
print(echange_les_cases([[1,6],[1,6]],(1,1),(0,1)))




