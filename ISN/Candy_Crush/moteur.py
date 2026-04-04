# -*- coding: utf-8 -*-
"""
Fichier : moteur.py
Contient la logique interne du jeu, la physique et la génération de la grille.
Équipe : Nikita, Lina, Éloïse
"""
import random
from random import randint

# CREATION ET VALIDATION DE LA GRILLE

def creer_grille_aleatoire(nb_lignes, nb_colonnes, nb_couleurs):
    """
    Cree une grille aleatoire.

    Paramètres:
        nb_lignes : int
        nb_colonnes : int
        nb_couleurs : int
            Nombre de types de bonbons.

    Sortie:
        list[list[int]] : grille remplie de valeurs aleatoires.
    """
    grille = []
    for i in range(nb_lignes):
        ligne = []
        for j in range(nb_colonnes):
            ligne.append(randint(0, nb_couleurs-1))
        grille.append(ligne)
    return grille 

def creer_grille_csv(nom_fichier):
    """
    Cree une grille de jeu a partir d'un fichier texte/CSV.
    Lit le fichier caractere par caractere.
    
    Paramètres:
        nom_fichier : str (Nom du fichier a lire)
        
    Sortie:
        list[list[int]] : La grille 2D prete pour le jeu.
    """
    grille = []
    fichier = open(nom_fichier, "r")
    lignes = fichier.readlines()
    fichier.close() 
    
    for i in range(len(lignes)):
        ligne_texte = lignes[i]
        ligne_entiers = []
        nombre_actuel = ""
        
        # Parcours de chaque caractere de la ligne
        for j in range(len(ligne_texte)):
            caractere = ligne_texte[j]
            
            # Si le caractere n'est ni un espace, ni un saut de ligne
            if caractere != ' ' and caractere != '\n' and caractere != '\r':
                nombre_actuel = nombre_actuel + caractere
            else:
                # Si on a fini de lire un nombre, on l'ajoute a la liste
                if nombre_actuel != "":
                    ligne_entiers.append(int(nombre_actuel))
                    nombre_actuel = ""
                    
        # Pour le dernier nombre de la ligne (s'il n'y a pas d'espace a la fin)
        if nombre_actuel != "":
            ligne_entiers.append(int(nombre_actuel))
            
        # Si la ligne n'etait pas vide, on l'ajoute a la grille
        if len(ligne_entiers) > 0:
            grille.append(ligne_entiers)
            
    return grille

def validation_grille(grille):
    """
    Verifie si la grille de jeu est valide (ne contient pas de combinaison initiale).

    Paramètres:
        grille : list[list[int]]

    Sortie:
        booleen : True si la grille est valide, False sinon.
    """
    if trois_alignes(grille):
        return False
    else:
        return True 

def verif_score_max(score, score_max):
    """
    Verifie si le score maximum est atteint.

    Paramètres:
        score : int
            Score actuel du joueur
        score_max : int
            Score maximum a atteindre

    Sortie:
        booleen : True si le score maximum est atteint (fin du jeu),
        False sinon (le joueur continue a jouer).
    """
    if score >= score_max:
        return True
    else:
        return False 

# UTILITAIRES ET DÉTECTION

def ajouter_sans_doublon(liste, x, y):
    """
    Fonction utilitaire : Ajoute les coordonnées [x, y] à la liste 
    uniquement si elles n'y sont pas déjà, sans utiliser l'opérateur 'in'.
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
    Vérifie si deux cases sont strictement voisines (haut, bas, gauche, droite).
    Empêche le joueur d'échanger des bonbons en diagonale ou éloignés.
    
    Paramètres:
        coo_1 : tuple/list -> Coordonnées de la première case (x1, y1)
        coo_2 : tuple/list -> Coordonnées de la deuxième case (x2, y2)
        
    Sortie:
        bool : True si les cases sont voisines, False sinon.
    """
    x1 = coo_1[0]
    y1 = coo_1[1]
    x2 = coo_2[0]
    y2 = coo_2[1]
    voisins = False

    if x1 == x2 and (y1 == y2 + 1 or y1 == y2 - 1):
        voisins = True
    if y1 == y2 and (x1 == x2 + 1 or x1 == x2 - 1):
        voisins = True

    return voisins

def trois_alignes(grille):
    """
    Parcourt l'intégralité de la grille pour détecter s'il existe au moins un 
    alignement de 3 bonbons (ou plus) de la même couleur, horizontalement ou verticalement.
    
    Paramètres:
        grille : list[list[int]]
            La grille de jeu actuelle.
            
    Sortie:
        bool : True si une combinaison est détectée, False sinon.
    """
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
    """
    Identifie et récupère les coordonnées de tous les bonbons qui font partie 
    d'un alignement de 3 ou plus pour les préparer à la destruction.
    
    Paramètres:
        grille : list[list[int]]
            La grille de jeu contenant potentiellement des combinaisons.
            
    Sortie:
        list[list] : Une liste contenant les coordonnées [x, y] des cases à détruire.
    """
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
    """
    (Mécanique de Niveau 2) : Vérifie les bonbons directement adjacents aux 
    bonbons d'une combinaison. S'ils ont la même couleur que la combinaison, 
    ils sont ajoutés à la liste des cases à détruire.
    
    Paramètres:
        grille : list[list[int]]
            La grille de jeu.
        cases_alignees : list[list]
            La liste des coordonnées des bonbons formant la combinaison de base.
            
    Sortie:
        list[list] : La liste étendue incluant les voisins de même couleur.
    """
    lignes = len(grille)
    colonnes = len(grille[0])
    selection_finale = []

    for k in range(len(cases_alignees)):
        selection_finale.append(cases_alignees[k])

    i = 0
    while i < len(selection_finale):
        x = selection_finale[i][0]
        y = selection_finale[i][1]
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

def echange_possible(grille):
    """
    Vérifie s'il reste au moins un échange valide sur la grille.
    Permet d'arrêter le jeu si le joueur est bloqué.
    """
    lignes = len(grille)
    colonnes = len(grille[0])
    possible = False
    
    i = 0
    while i < lignes and possible == False:
        j = 0
        while j < colonnes and possible == False:
            if j + 1 < colonnes:
                grille = echange_les_cases(grille, [i, j], [i, j+1])
                if trois_alignes(grille) == True:
                    possible = True
                grille = echange_les_cases(grille, [i, j], [i, j+1]) 
            
            if i + 1 < lignes and possible == False:
                grille = echange_les_cases(grille, [i, j], [i+1, j])
                if trois_alignes(grille) == True:
                    possible = True
                grille = echange_les_cases(grille, [i, j], [i+1, j]) 
            j += 1
        i += 1
        
    return possible

# ACTIONS SUR LA GRILLE

def detruire_cases(grille, liste):
    """
    Détruit les cases ciblées en remplaçant leur valeur par -1.

    Paramètres:
        grille : list[list[int]]
            grille de jeu
        liste : list[list]
            liste des coordonnées [x, y] des bonbons à supprimer

    Sortie:
        list[list[int]] : grille de jeu avec les cases supprimées (-1)
    """
    for i in range(len(liste)):
        x = liste[i][0]
        y = liste[i][1]
        grille[x][y] = -1
    return grille

def echange_les_cases(grille, coo_1, coo_2):
    """
    Échange la position de deux bonbons dans la grille.
    
    Paramètres :
        grille : list[list[int]]
            La grille de jeu.
        coo_1, coo_2 : tuple/list
            Les coordonnées [x, y] des deux cases à échanger.
            
    Sortie :
        list[list[int]] : La grille mise à jour.
    """
    x1 = coo_1[0]
    y1 = coo_1[1]
    x2 = coo_2[0]
    y2 = coo_2[1]

    temp = grille[x1][y1]
    grille[x1][y1] = grille[x2][y2]
    grille[x2][y2] = temp

    return grille

def generer_cases(grille, nb_couleurs=4):
    """
    Gère la gravité : fait "tomber" les bonbons situés au-dessus des cases 
    détruites (valeur -1) pour combler les trous, puis génère de nouveaux 
    bonbons aléatoires dans les cases vides laissées en haut de la grille.
    
    Paramètres:
        grille : list[list[int]]
            La grille de jeu avec des trous (cases à -1).
        nb_couleurs : int
            Le nombre de couleurs pour générer les nouveaux bonbons.
            
    Sortie:
        list[list[int]] : La nouvelle grille sans aucun trou.
    """
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