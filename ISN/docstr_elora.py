def quitter(quit): 
    """ Arrête le programme si quit est True. """
    q = False
    if quit == True:
        q = True
    return q 

#jeu de test quitter():
quit = True
print(quitter(quit))
quit2 = False
print(quitter(quit2))

def trouver_IE(calendrier):
    """ Renvoie la date de la prochaine IE à partir de la date d'aujourd'hui
    Parameters:
    - calendrier: cal. Calendrier de l'utilisateur
    Return
    - date_IE: date. Date de la plus proche IE. Renvoie None si c'est la fin de l'année. 
   """
    date debut = aujourdhui()
    date fin = #dernier evenement du calendrier
    evenements = liste_evenement(calendrier, date debut, date fin)
    i = 0
    IE = False
    date_IE = 0
    while i < len(evenements) and not IE :
        if "IE" in evenements[i] :
            IE = True
            date_IE = extraire_date_event(evenement[i])
        i += 1
        
    
    

