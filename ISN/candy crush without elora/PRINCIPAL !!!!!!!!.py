#Enesmbles de fonctions + PROGRAMME
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

def est_identique(liste1, liste2):
    """ Fonction utilitaire pour comparer deux listes de coordonnées sans 'in' ni '==' global """
    if len(liste1) != len(liste2):
        return False
        
    identique = True
    for i in range(len(liste1)):
        # On vérifie si chaque élément de liste1 a une correspondance exacte à la même position dans liste2
        if liste1[i][0] != liste2[i][0] or liste1[i][1] != liste2[i][1]:
            identique = False
            
    return identique

if __name__ == "__main__":
    print("Début des tests de détection...")
    test_trois_alignes()
    test_selectionner_les_cases()





#FONCTIONS DETECTION DES ALIGNEMENTS

def trois_alignes(grille):
    """
    Parcourt la grille pour détecter s'il existe au moins un alignement de 3.
    """
    lignes = len(grille)
    colonnes = len(grille[0])
    alignement_trouve = False
    
    # Vérification horizontale avec boucle while (Single Exit)
    i = 0
    while i < lignes and alignement_trouve == False:
        j = 0
        while j < colonnes - 2 and alignement_trouve == False:
            couleur = grille[i][j]
            if couleur != -1:
                if grille[i][j+1] == couleur and grille[i][j+2] == couleur:
                    alignement_trouve = True
            j = j + 1
        i = i + 1
                    
    # Vérification verticale
    i = 0
    while i < lignes - 2 and alignement_trouve == False:
        j = 0
        while j < colonnes and alignement_trouve == False:
            couleur = grille[i][j]
            if couleur != -1:
                if grille[i+1][j] == couleur and grille[i+2][j] == couleur:
                    alignement_trouve = True
            j = j + 1
        i = i + 1
                    
    return alignement_trouve

def selectionner_les_cases(grille):
    """
    Identifie toutes les coordonnées des bonbons alignés par 3 ou plus.
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
    NIVEAU 2 : Trouve tous les voisins de même couleur en cascade.
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
        
        # Haut
        if x - 1 >= 0:
            if grille[x-1][y] == couleur:
                selection_finale = ajouter_sans_doublon(selection_finale, x-1, y)
        # Bas
        if x + 1 < lignes:
            if grille[x+1][y] == couleur:
                selection_finale = ajouter_sans_doublon(selection_finale, x+1, y)
        # Gauche
        if y - 1 >= 0:
            if grille[x][y-1] == couleur:
                selection_finale = ajouter_sans_doublon(selection_finale, x, y-1)
        # Droite
        if y + 1 < colonnes:
            if grille[x][y+1] == couleur:
                selection_finale = ajouter_sans_doublon(selection_finale, x, y+1)
                
        i = i + 1
        
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
    """
    Gravité : Fait tomber les bonbons au-dessus des cases à -1 et génère de nouveaux bonbons.
    """
    lignes = len(grille)
    colonnes = len(grille[0])
    
    for j in range(colonnes):
        colonne_temporaire = []
        
        for i in range(lignes):
            if grille[i][j] != -1:
                colonne_temporaire.append(grille[i][j])
                
        trous = lignes - len(colonne_temporaire)
        
        # On recrée la colonne : d'abord les nouveaux (en haut), puis les anciens
        nouvelle_col = []
        for k in range(trous):
            nouvelle_col.append(random.randint(0, nb_couleurs - 1))
            
        for k in range(len(colonne_temporaire)):
            nouvelle_col.append(colonne_temporaire[k])
            
        # On remplace dans la grille
        for i in range(lignes):
            grille[i][j] = nouvelle_col[i]
            
    return grille










#PROGRAMME PRINCIPAL 
from logique import *
from interface import *

def main():
    points_max = 1000
    score = 0
    en_cours = True
    
    # Affichage des règles au lancement
    afficher_regles()
    
    # Génération et validation de la grille initiale
    nom_fichier = "exemple_grille.csv"
    grille = creer_grille(nom_fichier)
    
    # On s'assure qu'il n'y a pas de combinaison dès le départ (Exigence du barème)
    grille = validation_grille(grille) 
    
    # 3. Boucle principale du jeu
    while en_cours == True:
        afficher_grille(grille)
        afficher_compteur(score)
        
        # Saisie des coordonnées par le joueur (Simplifié FIMI)
        print("\n--- À VOTRE TOUR ---")
        print("Entrez les coordonnées de la première case :")
        x1 = int(input("Ligne 1 : "))
        y1 = int(input("Colonne 1 : "))
        
        print("Entrez les coordonnées de la deuxième case :")
        x2 = int(input("Ligne 2 : "))
        y2 = int(input("Colonne 2 : "))
        
        coo_1 = [x1, y1]
        coo_2 = [x2, y2]
        
        # Étape 1 : Vérifier si les cases sont bien côte à côte
        if sont_voisins(coo_1, coo_2) == True:
            
            # Étape 2 : On simule l'échange
            grille = echange_les_cases(grille, coo_1, coo_2)
            
            # Étape 3 : On vérifie si l'échange a créé un alignement
            if trois_alignes(grille) == True:
                
                # DÉBUT DES CASCADES (Réactions en chaîne)
                cascade_en_cours = True
                while cascade_en_cours == True:
                    
                    # a. Trouver les bonbons alignés
                    cases_alignees = selectionner_les_cases(grille)
                    
                    # b. Ajouter les voisins de même couleur
                    cases_a_detruire = ya_voisin(grille, cases_alignees)
                    
                    # c. Calcul et ajout des points (ex: 10 pts par bonbon)
                    points_gagnes = len(cases_a_detruire) * 10
                    score = score + points_gagnes
                    
                    # d. Détruire les cases (mettre la valeur à -1)
                    grille = detruire_cases(grille, cases_a_detruire)
                    print("\nBOOM ! Destruction des bonbons :")
                    afficher_grille(grille)
                    
                    # e. Faire tomber les bonbons et générer les nouveaux
                    grille = generer_cases(grille)
                    print("\nChute de nouveaux bonbons :")
                    afficher_grille(grille)
                    
                    # f. Vérifier si la chute a créé une nouvelle combinaison
                    if trois_alignes(grille) == False:
                        cascade_en_cours = False # Arrêt de la réaction en chaîne
                
            else:
                # Si l'échange n'a rien donné, on annule (on ré-échange)
                print("\nÉchange invalide (aucune combinaison formée). On annule.")
                grille = echange_les_cases(grille, coo_1, coo_2)
                
        else:
            print("\nErreur : Les cases ne sont pas voisines. Réessayez.")
            
        # 4. Vérification de la condition de victoire
        if score >= points_max:
            en_cours = False
            afficher_fin_jeu()
            
        # (Bonus à faire plus tard : Vérifier s'il reste des échanges possibles pour afficher "Dommage")

if __name__ == "__main__":
    main()












#Les tests de fonctions

def test_trois_alignes():
    # TEST 1 : Cas limite - Grille sans alignement
    grille_sans = [
        [0, 1, 2, 3],
        [1, 2, 3, 0],
        [2, 3, 0, 1],
        [3, 0, 1, 2]
    ]
    assert trois_alignes(grille_sans) == False, "Erreur TEST 1"

    # TEST 2 : Test général - Alignement horizontal
    grille_horizontale = [
        [0, 1, 2, 3],
        [1, 1, 1, 0],
        [2, 3, 0, 1],
        [3, 0, 1, 2]
    ]
    assert trois_alignes(grille_horizontale) == True, "Erreur TEST 2"

    # TEST 3 : Cas limite - Ignorer les cases détruites (-1)
    grille_detruite = [
        [-1, -1, -1, 3],
        [1, 2, 3, 0],
        [2, 3, 0, 1],
        [3, 0, 1, 2]
    ]
    assert trois_alignes(grille_detruite) == False, "Erreur TEST 3"

    print(" Tous les tests de trois_alignes() ont réussi !")

def test_selectionner_les_cases():


    # TEST 4 : Cas limite - Alignement de 4 bonbons
    grille_quatre = [
        [1, 1, 1, 1],
        [2, 3, 0, 1],
        [3, 0, 1, 2],
        [0, 2, 3, 0]
    ]
    
    # Résultat attendu : Les 4 cases de la première ligne
    cases_attendues = [[0, 0], [0, 1], [0, 2], [0, 3]]
    resultat = selectionner_les_cases(grille_quatre)
    
    assert est_identique(resultat, cases_attendues) == True, "Erreur TEST 4"
        
    print(" Tous les tests de selectionner_les_cases() ont réussi !")

def test_validation_grille():
    res = True

    #grille sans alignement
    grille_valide = [
        [1,2,3],
        [2,3,1],
        [3,1,2]    ]
    
    if validation_grille(grille_valide) != True:
        print("Test faux : validation_grille(grille_valide) devrait etre True")
        res = False

    #grille avec 3 alignes
    grille_invalide = [
        [1,1,1],
        [2,3,2],
        [3,2,3] ]
    
    if validation_grille(grille_invalide) != False:
        print("Test faux : validation_grille(grille_invalide) devrait etre False")
        res = False

    return res

def test_creer_grille_aleatoire():


    res = True
    grille = creer_grille_aleatoire(3, 4, 5)

    #test le nombre de lignes
    if len(grille) != 3:
        print("Test faux : nombre de lignes incorrect")
        res = False

    #test le nombre de colonnes
    if len(grille[0]) != 4:
        print("Test faux : nombre de colonnes incorrect")
        res = False

    #test si les valeurs sont dans l'intervalle
    for ligne in grille:
        for val in ligne:
            if val < 0 or val >= 5:
                print("Test faux : valeur hors limites")
                res = False
    return res

#pour une liste vide
print(detruire_cases([[1,3],[1,2]], []))
#pur une liste de 2 identiques
print(detruire_cases([[1,3],[1,2]], [(1,1),(2,1)]))

#echanger 2 fois la meme case
print(echange_les_cases([[1,6],[1,6]],(1,1),(1,1)))
#echanger 2 cases differentes
print(echange_les_cases([[1,6],[1,6]],(1,1),(0,1)))

