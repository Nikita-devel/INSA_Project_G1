import csv
from datetime import datetime, timezone, timedelta

###########
# Fonctions externes/publiques
###########

def extraire_date_event(ev, deb = True):
    """ Renvoie la date de début (par défaut) ou de fin (si deb = False) associée à l’évènement ev.
    Entrée : 
        - ev (list de str) : un évènement tel qu’issu de la lecture du fichier csv
        - deb (boolean) : True si date début, False si date fin
    Sortie : 
        - (list de int) : format [année, mois, jour, heure, minute]
            (arrondi à l’entier le plus proche si nécessaire pour les minutes)
    """
    if deb:
        heure = ev[3]
    else:
        heure = ev[4]
    heure_int, minutes_int = heure_vers_int(float(heure.replace(',', '.')))
    return [int(ev[0]), int(ev[1]), int(ev[2]), heure_int, minutes_int]

def aujourdhui():
    """Renvoie la date du jour.
    Sortie : 
        - (list de int) : format [année, mois, jour, heure, minute]
    """
    return d_vers_di(datetime.utcnow())

def jour_semaine(di):
    """Renvoie le jour de la semaine.
    Entrée :
        - di (list de int) : format [année, mois, jour, heure, minute]
    Sortie : 
        - (str)
    """
    jours = [
        "Lundi", "Mardi", "Mercredi",
        "Jeudi", "Vendredi", "Samedi", "Dimanche"
    ]
    return jours[di_vers_d(di).weekday()]

def lundi_de_la_semaine(di):
    """Renvoie la date du lundi à 0h de la semaine de la date donnée en paramètre.
    Entrée :
        - di (list de int) : format [année, mois, jour, heure, minute]
    Sortie : 
        - (list de int) : format [année, mois, jour, heure, minute]
    """
    di[3] = 0
    di[4] = 0
    d = di_vers_d(di)
    return d_vers_di(d - timedelta(days = d.weekday()))

def ajouter_jours(di, jours):
    """Étant donnée une date di en entrée, renvoie la date correspondant à celle-ci + le nombre de jours passé en paramètre.
    Entrée :
        - di (list de int) : format [année, mois, jour, heure, minute]
        - jours (int) : nombre de jours à ajouter
    Sortie : 
        - (list de int) : format [année, mois, jour, heure, minute]
    """
    return d_vers_di(di_vers_d(di) + timedelta(days = jours))

def est_avant(d1, d2):
    """Renvoie True si d1 est avant ou identique à d2.
    Entrée :
        - d1 (list de int) : format [année, mois, jour, heure, minute]
        - d2 (list de int) : format [année, mois, jour, heure, minute]
    """
    return di_vers_d(d1) <= di_vers_d(d2)

def creer_calendrier(nom_fich):
    """Lecture ligne par ligne du fichier csv contenant les informations du calendrier.
    Entrée :
        - nom_fich (str) : nom du fichier (avec son extension) au format Année;Mois;Jour;H_deb;H_fin;Matiere;Type;Intervenant;Salle, et dont la première ligne correspond aux titres des colonnes. Les évènements n’apparaissent pas nécessairement de manière triés dans le fichier.
    Sortie :
        - (list de list de str) : calendrier sous la forme de liste d’évènements (list de str).
    """
    c = []
    with open(nom_fich, newline="") as f:
        reader = csv.reader(f, delimiter = ";")
        next(reader) # passer la première ligne qui contient les titres des colonnes
        for row in reader: 
            c.append(row)
    return c

def liste_evenements(c, date_debut, date_fin):
    """Etant donné un calendrier (c), une date de début (incluse) et une date de fin (exclue), renvoie la liste des évènements compris entre ces deux dates.
    Entrée :
        - c (list de list de str) : calendrier complet
    Sortie :
        - (list de list de str) : liste d’évènements (list de str)
    """
    ev = []
    for i in range(len(c)):
        date_deb_ev = extraire_date_event(c[i])
        if est_avant(date_debut, date_deb_ev) and not est_avant(date_fin, date_deb_ev):
            ev.append(c[i])
    return ev

###########
# Fonctions internes/privées
###########

def d_vers_di(d):
    """Conversion du format date.datetime vers list of int.    
    Entrée :
        - (date.datetime)
    Sortie :
        - (list de int) : format [année, mois, jour, heure, minute]
    """
    return [d.year, d.month, d.day, d.hour, d.minute]

def di_vers_d(di):
    """Conversion du format list de int vers la date date.datetime.
    Entrée :
        - (list de int) : format [année, mois, jour, heure, minute]
    Sortie :
        - (date.datetime)
    """
    return datetime(di[0], di[1], di[2], di[3], di[4], tzinfo=timezone.utc)

def heure_vers_int(h):
    """ Convertit une heure donnée sous forme de flottant en un couple d’entiers (heure, minute).
        Ex : Pour h = 8.5, renvoie (8, 30) correspondant à 8h30.
    Entrée : 
        - h (float) heure
    Sortie : 
        - (list de int) : format [hour, minute]
            (arrondi à l’entier le plus proche si nécessaire pour les minutes)
    """
    heure_int = int(h)
    minutes_int = round((h - heure_int)*60)
    return heure_int, minutes_int
