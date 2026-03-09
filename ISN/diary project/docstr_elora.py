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

def pense_bete_IE(calendrier_trie): # je me suis trompee et j'ai fait la partie de Lina
    """ Renvoie la date de la prochaine IE à partir de la date d'aujourd'hui
    Parameters:
    - calendrier trie: cal. Calendrier (déjà trié) de l'utilisateur
    Return
    - None. Affichage pense-bête
   """
    date_debut = aujourdhui()
    date_fin = extraire_date_event(calendrier_trie[-1]) #dernier cours du calendrier
    evenements = liste_evenement(calendrier_trie, date debut, date fin) #mettre tous les evenements en liste
    i = 0
    IE = False
    while i < len(evenements) and not IE :
        if "EV" in evenements[i] :
            IE = True
            date_IE = extraire_date_event(evenements[i])
            matiere_IE = evenements[i][5] #trouver matiere en prenant 6eme colonne excel
            print(f"Nous sommes le {jour_semaine(aujourdhui())} {aujourdhui()}.")
            print(f"La prochaine évaluation sera : {matiere_IE} le {jour_semaine(evenements[i]} {date_IE[2]} de {date_IE[3]}h à {date_IE[4]}h.")
        i += 1
    if not IE :
        print(f"Nous sommes le {jour_semaine(aujourdhui())} {aujourdhui()}.")
        print("PLUS D'IE, YOUPI !!!")