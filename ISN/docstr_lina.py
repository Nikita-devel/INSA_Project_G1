#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 12:53:22 2026

@author: lbachar
"""


def affichage_calendrier(calendrier, date_demandéee, année, mois): #Lina
    """
    Affiche les évènements du calendrier selon le filtre choisi

    Paramètres :
        - calendrier (liste) : calendrier csv 
        - date_demandée (liste d'entriers int) : date au format [année, mois, jour, heure, minute] qui va permettre l'affichage de la semaine demandee
        - annéee (int) : l'année pour afficher par annee 
        - mois (int) : le mois pour un affichage mensuel 
            
    Sortie :
        - le calendrier 

    """

###Rôle :
#Si une date_demandée est fournie :
##il faut déterminer le lundi de la semain
##il faut parcourir les jours de la semaine
##puis il faut afficher les cours jour par jour

#Si annee et mois sont fournis :
##il faut filtrer les évènements correspondant au mois
## puis afficher les cours de ce mois

   
#fonctions a utiliser 

###POUR AFFICHER LE CALENDRIER + FILTRER 

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

##Trouver le point de depart( qui est le lundi )
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

##Pour ajouter les jours de la semaine 

def ajouter_jours(di, jours):
    """Étant donnée une date di en entrée, renvoie la date correspondant à celle-ci + le nombre de jours passé en paramètre.
    Entrée :
        - di (list de int) : format [année, mois, jour, heure, minute]
        - jours (int) : nombre de jours à ajouter
    Sortie : 
        - (list de int) : format [année, mois, jour, heure, minute]
    """
    return d_vers_di(di_vers_d(di) + timedelta(days = jours))


##pour filtrer les evenements du jour == garder ce qu'on veut selon deux dates (entre deux dates)
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


##pour bien ecrire les heures 
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

##afficher correctement le jour de la semaine (Lundi....)
def ajouter_jours(di, jours):
    """Étant donnée une date di en entrée, renvoie la date correspondant à celle-ci + le nombre de jours passé en paramètre.
    Entrée :
        - di (list de int) : format [année, mois, jour, heure, minute]
        - jours (int) : nombre de jours à ajouter
    Sortie : 
        - (list de int) : format [année, mois, jour, heure, minute]
    """
    return d_vers_di(di_vers_d(di) + timedelta(days = jours))

#Fcomparer les deates entr eelles pour etre sur de ne as se trmper ?
def est_avant(d1, d2):
    """Renvoie True si d1 est avant ou identique à d2.
    Entrée :
        - d1 (list de int) : format [année, mois, jour, heure, minute]
        - d2 (list de int) : format [année, mois, jour, heure, minute]
    """
    return di_vers_d(d1) <= di_vers_d(d2)






#FONCTION: AFFICHAGE DU PENSE-BETE 

def affichage_pense_bete(calendrier):
    """
    Affiche la date actuelle ainsi que la prochaine évaluation à venir.

    Paramètres :
        - calendrier (liste) : calendrier csv 

    Sortie :
        - affichage du calendrier

    """

######AFFICHAGE PENSE BETE 
##SOUS-FONCTIONS A UTILISER 

#Il faut determiner on est dans quelle date pour savoir quelle est l'evaluation 
def aujourdhui():
    """Renvoie la date du jour.
    Sortie : 
        - (list de int) : format [année, mois, jour, heure, minute]
    """
    return d_vers_di(datetime.utcnow()) 

##il faut comparer date de today avec l'eval 
def est_avant(d1, d2):
    """Renvoie True si d1 est avant ou identique à d2.
    Entrée :
        - d1 (list de int) : format [année, mois, jour, heure, minute]
        - d2 (list de int) : format [année, mois, jour, heure, minute]
    """
    return di_vers_d(d1) <= di_vers_d(d2)

##il faut trouver la date de l'examen 
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

##pour afficher le jour de l'eval 
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




#FONCTION DEMANDER RETOUR
def demander_retour():
    """
    Met le programme en pause jusqu’a ce que l’utilisateur appuie sur une touche du clavier
    
    """
















