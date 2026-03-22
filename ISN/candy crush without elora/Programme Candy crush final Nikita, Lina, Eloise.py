import random
from random import randint


#Les fonctions + le programme principal : Nikita, Lina, Eloise 


# FONCTIONS CREATION / VALIDATION DE LA GRILLE
def creer_grille_aleatoire(nb_lignes, nb_colonnes, nb_couleurs):

    grille = []

    for i in range(nb_lignes):

        ligne = []

        for j in range(nb_colonnes):
            ligne.append(randint(0, nb_couleurs-1))

        grille.append(ligne)

    return grille 


def validation_grille(grille):

    if trois_alignes(grille):
        return False
    else:
        return True 

def verif_score_max(score, score_max):

    if score >= score_max:
        print("Score maximum atteint ! Fin du jeu.")
        return True
    else:
        print("Le joueur continue a jouer")
        return False 


#FONCTIONS D'AFFICHAGE 
def afficher_regles():
    print("""Pour le niveau 2 :
Echangez 2 bonbons de place sur la grille pour creer un groupe de 3 bonbons de meme couleur.
Si 3 bonbons de meme couleur sont alignes ils se detruisent.
Si il y a plus de 3 bonbons de la meme couleur alignes, ils se detruisent tous.
""")


def afficher_compteur(compteur):
    print(f"Le score est de {compteur}")


def afficher_fin_jeu():
    print("Bravo vous avez gagne !!!")

def afficher_grille(grille):

    print("Grille actuelle :")

    for ligne in grille:
        print(ligne)

#FONCTIONS UTILITAIRES  

def ajouter_sans_doublon(liste, x, y):
    """
    Ajoute les coordonnées [x,y] à la liste seulement si elles ne sont pas déjà présentes.
    """

    present = False

    for i in range(len(liste)):
        if liste[i][0] == x and liste[i][1] == y:
            present = True

    if present == False:
        liste.append([x, y])

    return liste

def sont_voisins(coo_1, coo_2):
    """
    Vérifie si deux cases sont voisines.
    """

    x1, y1 = coo_1
    x2, y2 = coo_2

    voisins = False

    if x1 == x2 and (y1 == y2 + 1 or y1 == y2 - 1):
        voisins = True

    if y1 == y2 and (x1 == x2 + 1 or x1 == x2 - 1):
        voisins = True

    return voisins


#FONCTIONS DETECTION DES ALIGNEMENTS

def trois_alignes(grille):

    lignes = len(grille)
    colonnes = len(grille[0])

    alignement_trouve = False

    i = 0
    while i < lignes and alignement_trouve == False:
        j = 0
        while j < colonnes - 2 and alignement_trouve == False:

            couleur = grille[i][j]

            if couleur != -1:
                if grille[i][j+1] == couleur and grille[i][j+2] == couleur:
                    alignement_trouve = True

            j += 1
        i += 1

    i = 0
    while i < lignes - 2 and alignement_trouve == False:
        j = 0
        while j < colonnes and alignement_trouve == False:

            couleur = grille[i][j]

            if couleur != -1:
                if grille[i+1][j] == couleur and grille[i+2][j] == couleur:
                    alignement_trouve = True

            j += 1
        i += 1

    return alignement_trouve

def selectionner_les_cases(grille):

    lignes = len(grille)
    colonnes = len(grille[0])

    a_detruire = []

    for i in range(lignes):
        for j in range(colonnes - 2):

            c = grille[i][j]

            if c != -1 and grille[i][j+1] == c and grille[i][j+2] == c:

                a_detruire = ajouter_sans_doublon(a_detruire, i, j)
                a_detruire = ajouter_sans_doublon(a_detruire, i, j+1)
                a_detruire = ajouter_sans_doublon(a_detruire, i, j+2)

    for i in range(lignes - 2):
        for j in range(colonnes):

            c = grille[i][j]

            if c != -1 and grille[i+1][j] == c and grille[i+2][j] == c:

                a_detruire = ajouter_sans_doublon(a_detruire, i, j)
                a_detruire = ajouter_sans_doublon(a_detruire, i+1, j)
                a_detruire = ajouter_sans_doublon(a_detruire, i+2, j)

    return a_detruire


def ya_voisin(grille, cases_alignees):

    lignes = len(grille)
    colonnes = len(grille[0])

    selection_finale = []

    for k in range(len(cases_alignees)):
        selection_finale.append(cases_alignees[k])

    i = 0

    while i < len(selection_finale):

        x, y = selection_finale[i]

        couleur = grille[x][y]

        if x-1 >= 0 and grille[x-1][y] == couleur:
            selection_finale = ajouter_sans_doublon(selection_finale, x-1, y)

        if x+1 < lignes and grille[x+1][y] == couleur:
            selection_finale = ajouter_sans_doublon(selection_finale, x+1, y)

        if y-1 >= 0 and grille[x][y-1] == couleur:
            selection_finale = ajouter_sans_doublon(selection_finale, x, y-1)

        if y+1 < colonnes and grille[x][y+1] == couleur:
            selection_finale = ajouter_sans_doublon(selection_finale, x, y+1)

        i += 1

    return selection_finale


#FONCTIONS ACTIONS SUR LA GRILLE

def detruire_cases(grille, liste):

    for (x, y) in liste:
        grille[x][y] = -1

    return grille

def echange_les_cases(grille, coo_1, coo_2):

    x1, y1 = coo_1
    x2, y2 = coo_2

    temp = grille[x1][y1]
    grille[x1][y1] = grille[x2][y2]
    grille[x2][y2] = temp

    return grille

def generer_cases(grille, nb_couleurs=4):

    lignes = len(grille)
    colonnes = len(grille[0])

    for j in range(colonnes):

        colonne_temp = []

        for i in range(lignes):
            if grille[i][j] != -1:
                colonne_temp.append(grille[i][j])

        trous = lignes - len(colonne_temp)

        nouvelle_col = []

        for k in range(trous):
            nouvelle_col.append(random.randint(0, nb_couleurs-1))

        for k in range(len(colonne_temp)):
            nouvelle_col.append(colonne_temp[k])

        for i in range(lignes):
            grille[i][j] = nouvelle_col[i]

    return grille


#PROGRAMME CANDY CRUSH Lina, Eloise, Nikita 

def candy_crush(nb_lignes=5, nb_colonnes=5, nb_couleurs=4, score_max=50):

    afficher_regles()

    score = 0

    grille = creer_grille_aleatoire(nb_lignes, nb_colonnes, nb_couleurs)

    afficher_grille(grille)

    while not verif_score_max(score, score_max):

        print("\nChoisissez deux cases a echanger")

        x1 = int(input("ligne 1 : "))
        y1 = int(input("colonne 1 : "))

        x2 = int(input("ligne 2 : "))
        y2 = int(input("colonne 2 : "))

        if sont_voisins((x1,y1),(x2,y2)):

            grille = echange_les_cases(grille,(x1,y1),(x2,y2))

            afficher_grille(grille)

            if trois_alignes(grille):

                cases = selectionner_les_cases(grille)

                cases = ya_voisin(grille,cases)

                grille = detruire_cases(grille,cases)

                score += len(cases)

                grille = generer_cases(grille)

                afficher_grille(grille)

                afficher_compteur(score)

            else:

                print("Pas d'alignement -> echange annule")

                grille = echange_les_cases(grille,(x1,y1),(x2,y2))

        else:

            print("Les cases ne sont pas voisines")

    afficher_fin_jeu() 


#On lance le jeu
print(candy_crush())



