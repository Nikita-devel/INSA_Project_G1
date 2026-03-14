"""
Projet Candy Crush - Séance 1 (Découpage Fonctionnel et Docstrings)
Équipe : Nikita, Éloïse, Lina
"""


# PARTIE ÉLOÏSE : Interface, affichage texte et actions directes


def afficher_regles():
    """
    Affiche les règles du jeu Candy Crush dans la console au lancement.
    """
    print("""Pour le niveau 2 : 
Echangez 2 bonbons de place sur la grille pour créer un groupe de 3 bonbons de même couleur, si 3 bobnons de même couleur sont alignés ils se détruisent. 
Si il y a plus de 3 bonbons de la même couleur alignés, ils se détruisent tous.""")

def afficher_compteur(compteur):
    """
    Affiche le score actuel du joueur.
    
    Paramètres :
        compteur : int
            Le score actuel à afficher.
    """
    print(f'Le score est de {compteur}')

def afficher_fin_jeu():
    """
    Affiche le message de fin de jeu en cas de victoire.
    """
    print('Bravo vous avez gagné !!!')

def detruire_cases(grille, liste):
    """
    Détruit les cases ciblées en remplaçant leur valeur par -1.

    Parameters
    ----------
    grille : list[list[int]]
        grille de jeu
    liste : list[tuple]
        liste des coordonnées (x, y) des bonbons à supprimer

    Returns
    -------
    grille : list[list[int]]
        grille de jeu sans les combinaisons supprimées
    """
    couleur = []
    for (x, y) in liste:
        if grille[x][y] not in couleur:
            couleur.append(grille[x][y])
        grille[x][y] = -1
    # maj_score(liste) # À implémenter plus tard
    return grille
    
def echange_les_cases(grille, coo_1, coo_2):
    """
    Échange la position de deux bonbons dans la grille.
    
    Paramètres :
        grille : list[list[int]]
            La grille de jeu.
        coo_1, coo_2 : tuple
            Les coordonnées (x, y) des deux cases à échanger.
            
    Returns :
        list[list[int]] : La grille mise à jour.
    """
    x_1, y_1 = coo_1
    x_2, y_2 = coo_2
    
    temp = grille[x_1][y_1] 
    grille[x_1][y_1] = grille[x_2][y_2]
    grille[x_2][y_2] = temp
    
    return grille
            

# PARTIE LINA : Initialisation, validation et affichage visuel


def afficher_grille(grille):
    """
    Affiche la grille de jeu dans la console.

    Paramètres:
        grille : list[list[int]]
            Liste 2D representant la grille du jeu.

    Sortie:
        Affichage de la grille dans la console
    """
    pass

def validation_grille(grille):
    """
    Verifie si la grille de jeu est valide (ne contient pas de combinaison initiale).

    Paramètres:
        grille : list[list[int]]

    Sortie:
        booleen : True si la grille est valide, False sinon.
    """
    pass

def creer_grille(nom_fichier_csv):
    """
    Cree une grille de jeu a partir d'un fichier CSV.

    Paramètres:
        nom_fichier_csv : str 
            Nom du fichier csv contenant la grille

    Sortie:
        list[list[int]] : Une liste 2D d'entiers correspondant a la grille du jeu.
    """
    pass

def verif_score_max(score, score_max):
    """
    Verifie si le score actuel depasse le score maximum.

    Paramètres:
        score : int
            Score actuel du joueur
        score_max : int
            Score maximum enregistre

    Sortie:
        int : Le score maximum mis a jour. Si le score actuel est superieur, il devient le nouveau score maximum.
    """
    pass


# PARTIE NIKITA : Moteur logique, détection et physique (Niveau 2)


def sont_voisins(coo_1, coo_2):
    """
    Vérifie si deux cases sont strictement voisines (haut, bas, gauche, droite).
    Empêche le joueur d'échanger des bonbons en diagonale ou éloignés.
    
    Paramètres:
        coo_1 : tuple (int, int) -> Coordonnées de la première case (x1, y1)
        coo_2 : tuple (int, int) -> Coordonnées de la deuxième case (x2, y2)
        
    Sortie:
        bool : True si les cases sont voisines, False sinon.
    """
    pass

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
    pass

def selectionner_les_cases(grille):
    """
    Identifie et récupère les coordonnées de tous les bonbons qui font partie 
    d'un alignement de 3 ou plus pour les préparer à la destruction.
    
    Paramètres:
        grille : list[list[int]]
            La grille de jeu contenant potentiellement des combinaisons.
            
    Sortie:
        list[tuple] : Une liste contenant les coordonnées (x, y) des cases à détruire.
    """
    pass

def ya_voisin(grille, cases_alignees):
    """
    (Mécanique de Niveau 2) : Vérifie les bonbons directement adjacents aux 
    bonbons d'une combinaison. S'ils ont la même couleur que la combinaison, 
    ils sont ajoutés à la liste des cases à détruire.
    
    Paramètres:
        grille : list[list[int]]
            La grille de jeu.
        cases_alignees : list[tuple]
            La liste des coordonnées des bonbons formant la combinaison de base.
            
    Sortie:
        list[tuple] : La liste étendue incluant les voisins de même couleur.
    """
    pass

def generer_cases(grille):
    """
    Gère la gravité : fait "tomber" les bonbons situés au-dessus des cases 
    détruites (valeur -1) pour combler les trous, puis génère de nouveaux 
    bonbons aléatoires dans les cases vides laissées en haut de la grille.
    
    Paramètres:
        grille : list[list[int]]
            La grille de jeu avec des trous (cases à -1).
            
    Sortie:
        list[list[int]] : La nouvelle grille sans aucun trou.
    """
    pass