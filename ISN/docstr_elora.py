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

def trouver_IE(calendrier_trie): # je me suis trompee et j'ai fait la partie de Lina
    """ Renvoie la date de la prochaine IE à partir de la date d'aujourd'hui
    Parameters:
    - calendrier: cal. Calendrier trie de l'utilisateur
    Return
    - date_IE: date. Date de la plus proche IE. Renvoie None si c'est la fin de l'année. 
   """
    date_debut = aujourdhui()
    date_fin = extraire_date_event(calendrier_trie[-1]) #derniere heure de cours du calendrier
    evenements = liste_evenement(calendrier_trie, date debut, date fin) #mettre tous les evenements en liste
    i = 0
    IE = False
    while i < len(evenements) and not IE :
        if "EV" in evenements[i] :
            IE = True
            date_IE = extraire_date_event(evenements[i])
            matiere_IE = evenements[i][5] #trouver matiere en prenant 6eme colonne excel
            print(f"Nous sommes le {aujourdhui}.")
            print(f"La prochaine évaluation sera : {matiere_IE} le {date_IE[2]} {jour_semaine(evenements[i]} de {date_IE[3]}h à {extraire_date_event(evenements[i], False}h.")
        i += 1
    if not IE :
        print("PLUS D'IE AHAHAHAH")