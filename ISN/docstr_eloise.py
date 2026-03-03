# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 14:26:41 2026

@author: elois
"""






def trie_liste(liste, colonne):
   """
    Trie une liste de données par date (année puis jour) et par heure croissante.

    Paramètres
    ----------
    liste : list
        Liste contenant les éléments à trier du tableau excel. Chaque élément de la liste
        est lui-même une liste contenant:
        - une date (année et jour)
        - une heure
        - éventuellement d'autres informations.

    colonne : int
        Indice correspondant à la position de la date dans chaque sous-liste.
        avec l'heure en indice (liste+1)

    """
    
    
    
    
def generer_cle_ascii(ligne):
    """
    Concatène Année, Mois, Jour et Heure en une chaîne ASCII
    Format: YYYYMMDDHH (avec padding de zéros)
    """
    annee = str(int(ligne[0]))
    mois = str(int(ligne[1])).zfill(2)
    jour = str(int(ligne[2])).zfill(2)
    
    heure_val = float(ligne[3])
    heure_str = f"{heure_val:04.1f}".replace('.', '') 
    
    return annee + mois + jour + heure_str

def trier_par_date(liste_cours):
    """Trie la liste des cours par ordre croissant selon la clé ASCII"""
    n = len(liste_cours)
    for i in range(n):
        for j in range(0, n - i - 1):
            if generer_cle_ascii(liste_cours[j]) > generer_cle_ascii(liste_cours[j + 1]):
                temp = liste_cours[j]
                liste_cours[j] = liste_cours[j + 1]
                liste_cours[j + 1] = temp
    return liste_cours