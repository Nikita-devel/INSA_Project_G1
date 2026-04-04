# -*- coding: utf-8 -*-
"""
Fichier : tests.py
Archive de tests pour la validation de grille et la détection d'alignements.
"""
from moteur import trois_alignes, validation_grille, selectionner_les_cases

def test_validation_grille():
    """ Teste si la grille initiale est bien générée sans combinaisons. """
    grille_valide = [
        [1, 2, 3],
        [2, 3, 1],
        [3, 1, 2]
    ]
    assert validation_grille(grille_valide) == True, "Erreur : La grille devrait être valide"

    grille_invalide = [
        [1, 1, 1],
        [2, 3, 2],
        [3, 2, 3]
    ]
    assert validation_grille(grille_invalide) == False, "Erreur : La grille devrait être invalide"
    print("Tous les tests de validation_grille() ont reussi !")

def test_trois_alignes():
    """ Teste la détection globale d'alignements (cas limites inclus). """
    grille_sans = [
        [0, 1, 2, 3],
        [1, 2, 3, 0],
        [2, 3, 0, 1],
        [3, 0, 1, 2]
    ]
    assert trois_alignes(grille_sans) == False, "Erreur TEST 1 (Grille sans alignement)"

    grille_horizontale = [
        [0, 1, 2, 3],
        [1, 1, 1, 0],
        [2, 3, 0, 1],
        [3, 0, 1, 2]
    ]
    assert trois_alignes(grille_horizontale) == True, "Erreur TEST 2 (Alignement horizontal)"

    # Cas limite très important (Ignorer les -1)
    grille_detruite = [
        [-1, -1, -1, 3],
        [1, 2, 3, 0],
        [2, 3, 0, 1],
        [3, 0, 1, 2]
    ]
    assert trois_alignes(grille_detruite) == False, "Erreur TEST 3 (Ignorer cases détruites)"
    print("Tous les tests de trois_alignes() ont reussi !")

def est_identique(liste1, liste2):
    """ Utilitaire FIMI pour comparer deux listes de listes sans 'in' """
    if len(liste1) != len(liste2):
        return False
        
    identique = True
    for i in range(len(liste1)):
        if liste1[i][0] != liste2[i][0] or liste1[i][1] != liste2[i][1]:
            identique = False
            
    return identique

def test_selectionner_les_cases():
    """ Teste si les bonnes coordonnées sont sélectionnées (ex: 4 bonbons). """
    grille_quatre = [
        [1, 1, 1, 1],
        [2, 3, 0, 1],
        [3, 0, 1, 2],
        [0, 2, 3, 0]
    ]
    
    cases_attendues = [[0, 0], [0, 1], [0, 2], [0, 3]]
    resultat = selectionner_les_cases(grille_quatre)
    
    assert est_identique(resultat, cases_attendues) == True, "Erreur TEST 4 (Sélection de 4 bonbons)"
    print("Tous les tests de selectionner_les_cases() ont reussi !")

if __name__ == "__main__":
    print("Debut des tests ...")
    test_validation_grille()
    test_trois_alignes()
    test_selectionner_les_cases()