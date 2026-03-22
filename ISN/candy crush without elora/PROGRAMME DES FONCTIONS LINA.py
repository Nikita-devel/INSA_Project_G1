##FONCTIONS LINA 

from random import randint 


def afficher_grille(grille):
    """
    Affiche la grille de jeu dans la console.

    Parametres:
        grille : list[list[int]]
            Liste 2D representant la grille du jeu.

    Sortie:
        Affichage de la grille dans la console.
    """

    print("Grille actuelle :")
    for ligne in grille:
        print(ligne)



def validation_grille(grille):
    """
    Verifie si la grille est valide (pas de 3 bonbons alignes).

    Parametres:
        grille : list[list[int]]

    Sortie:
        booleen : True si la grille est valide, False sinon.
    """

    if trois_alignes(grille):
        return False
    else:
        return True


def creer_grille_nulle(nb_lignes, nb_colonnes):
    """
    Cree une grille remplie de 0.

    Parametres:
        nb_lignes : int
        nb_colonnes : int

    Sortie:
        list[list[int]] : grille de taille nb_lignes x nb_colonnes.
    """

    grille = []

    for i in range(nb_lignes):
        ligne = []
        for j in range(nb_colonnes):
            ligne.append(0)
        grille.append(ligne)

    return grille


def creer_grille_aleatoire(nb_lignes, nb_colonnes, nb_couleurs):
    """
    Cree une grille aleatoire.

    Parametres:
        nb_lignes : int
        nb_colonnes : int
        nb_couleurs : int
            Nombre de types de bonbons.

    Sortie:
        list[list[int]] : grille remplie de valeurs aleatoires.
    """

    grille = creer_grille_nulle(nb_lignes, nb_colonnes)

    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            grille[i][j] = randint(0, nb_couleurs - 1)

    return grille


def verif_score_max(score, score_max):
    """
    Verifie si le score actuel depasse le score maximum.

    Parametres:
        score : int
            Score actuel du joueur
        score_max : int
            Score maximum enregistre

    Sortie:
        int : score maximum mis a jour
    """

    if score > score_max:
        return score
    else:
        return score_max

def verif_score_max(score, score_max):
    """
    Verifie si le score maximum est atteint.

    Parametres:
        score : int
            Score actuel du joueur
        score_max : int
            Score maximum a atteindre

    Sortie:
        booleen : True si le score maximum est atteint (fin du jeu),
        False sinon (le joueur continue a jouer).
    """

    if score >= score_max:
        print("Score maximum atteint ! Fin du jeu.")
        return True
    else:
        print("Le joueur continue a jouer")
        return False

