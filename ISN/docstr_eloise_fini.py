# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 16:40:31 2026

@author: elois
"""
import csv

from datetime import datetime, timezone

###########
# Fonctions de conversion (Internes)
###########

def di_vers_d(di):
    """Conversion du format list de int vers la date date.datetime."""
    return datetime(di[0], di[1], di[2], di[3], di[4], tzinfo=timezone.utc)

def est_avant(d1, d2):
    """Renvoie True si d1 est avant ou identique à d2."""
    return di_vers_d(d1) <= di_vers_d(d2)

def heure_vers_int(h):
    """Convertit une heure flottante (ex: 8.5) en (8, 30)."""
    heure_int = int(h)
    minutes_int = round((h - heure_int) * 60)
    return heure_int, minutes_int



def extraire_date_event(ev, deb = True):
    """
    Renvoie la date sous forme de liste d'entiers [A, M, J, H, M].
    Prend en entrée une ligne du CSV (liste de chaînes de caractères).
    """
    heure_str = ev[3] if deb else ev[4]
    # virgule au lieu du point
    heure_float = float(heure_str.replace(',', '.'))
    heure_int, minutes_int = heure_vers_int(heure_float)
    
    return [int(ev[0]), int(ev[1]), int(ev[2]), heure_int, minutes_int]

def trier_par_date(liste_cours):
    """
    Trie la liste des cours par ordre chronologique croissant
    en utilisant l'algorithme du tri à bulles.
    """
    n = len(liste_cours)
    for i in range(n):
        for j in range(0, n - i - 1):
            date_actuelle = extraire_date_event(liste_cours[j])
            date_suivante = extraire_date_event(liste_cours[j + 1])
            if not est_avant(date_actuelle, date_suivante):
                liste_cours[j], liste_cours[j + 1] = liste_cours[j + 1], liste_cours[j]
                
    return liste_cours
