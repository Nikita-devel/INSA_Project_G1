from calendrier import *

def trier_par_date(liste_cours):
    """
    Trie le calendrier par ordre chronologique (année, mois, jour, puis heure), 
    car le fichier CSV n'est pas ordonné. Utilise l'algorithme du tri à bulles.

    Paramètres :
        - liste_cours (list) : Liste d'événements brute extraite du fichier csv.

    Return :
        - (list) : La liste triée prête pour un affichage séquentiel.
    """
    n = len(liste_cours)
    
    # Parcours de l'ensemble de la liste pour le tri à bulles
    for i in range(n):
        # Comparaison des éléments adjacents pour faire remonter le plus tardif
        for j in range(0, n - i - 1):
            date_actuelle = extraire_date_event(liste_cours[j])
            date_suivante = extraire_date_event(liste_cours[j + 1])
            
            # Échange des éléments si le premier est postérieur au second
            if not est_avant(date_actuelle, date_suivante):
                temp = liste_cours[j]
                liste_cours[j] = liste_cours[j + 1]
                liste_cours[j + 1] = temp
                
    return liste_cours

def quelle_semaine(jour): 
    """
    Calcule la date du lundi correspondant à la semaine du jour saisi par l'utilisateur.
    
    Parameters :
        - jour (list) : Date au format [année, mois, jour, heure, minute].
    
    Return :
        - (list) : Date du lundi à 00:00 [année, mois, jour, 0, 0].
    """
    return lundi_de_la_semaine(jour)


def affichage_calendrier(calendrier, date_pivot): 
    """
    Affiche les événements de la semaine correspondant à la date choisie.
    Utilise le formatage f"{valeur:02d}" pour l'affichage (ex: 08h05).

    Paramètres :
        - calendrier (list) : Liste d'événements triée.
        - date_pivot (list) : Date de référence pour déterminer la semaine à afficher.
            
    Sortie :
        - None (Affiche le planning du lundi au vendredi dans la console).
    """
    lundi = lundi_de_la_semaine(date_pivot)
    vendredi_soir = ajouter_jours(lundi, 5) 
    jour_fin_affichage = ajouter_jours(lundi, 4)
    
    semaine = liste_evenements(calendrier, lundi, vendredi_soir)
    
    print(f"\n####### SEMAINE DU {lundi[2]:02d}/{lundi[1]:02d} AU {jour_fin_affichage[2]:02d}/{jour_fin_affichage[1]:02d} #######")
    
    # Parcours des 5 jours de la semaine (du lundi au vendredi)
    for i in range(5):
        jour_actuel = ajouter_jours(lundi, i)
        print(f"\n# {jour_semaine(jour_actuel)} {jour_actuel[2]:02d}/{jour_actuel[1]:02d}/{jour_actuel[0]}")
        print("#####")
        
        # Recherche et affichage des cours correspondant au jour actuel
        for j in range(len(semaine)):
            ev = semaine[j]
            d_deb = extraire_date_event(ev)
            
            if d_deb[0] == jour_actuel[0] and d_deb[1] == jour_actuel[1] and d_deb[2] == jour_actuel[2]:
                d_fin = extraire_date_event(ev, False) 
                print(f"# de {d_deb[3]:02d}h{d_deb[4]:02d} à {d_fin[3]:02d}h{d_fin[4]:02d} : {ev[5]} ({ev[6]})")
                
    print("#############################")

def naviguer_semaine(commande, date_pivot): 
    """
    Permet de reculer ou d'avancer d'une semaine (touches 'p' ou 's').
    
    Parameters :
        - commande (str) : 's' pour suivante, 'p' pour précédente.
        - date_pivot (list) : La date actuelle affichée.
        
    Return :
        - (list) : La nouvelle date décalée de 7 jours.
    """
    if commande == 's' or commande == 'S':
        return ajouter_jours(date_pivot, 7)
    elif commande == 'p' or commande == 'P':
        return ajouter_jours(date_pivot, -7)
    return date_pivot


def trouver_IE(calendrier, date_actuelle): 
    """
    Recherche la prochaine évaluation (type 'Evaluation') après aujourd'hui.
   
    Parameters :
        - calendrier (list) : Liste d'événements triée.
        - date_actuelle (list) : Date système [année, mois, jour, heure, minute].
    
    Return :
        - (list) : L'événement de l'évaluation la plus proche, ou None.
    """
    # Parcours séquentiel du calendrier pour trouver la première évaluation future
    for i in range(len(calendrier)):
        ev = calendrier[i]
        date_ev = extraire_date_event(ev)
        
        if not est_avant(date_ev, date_actuelle):
            if "EV" in ev[6] or "Evaluation" in ev[6]:
                return ev
    return None

def affichage_pense_bete(calendrier): 
    """
    Affiche la date actuelle et les détails de la prochaine évaluation.

    Paramètres :
        - calendrier (list) : Liste complète des événements.
    """
    maintenant = aujourdhui()
    prochaine = trouver_IE(calendrier, maintenant)
    
    print(f"\nNous sommes le {jour_semaine(maintenant)} {maintenant[2]:02d}/{maintenant[1]:02d}/{maintenant[0]}.")
    
    if prochaine != None:
        d_deb = extraire_date_event(prochaine)
        d_fin = extraire_date_event(prochaine, False)
        print(f"La prochaine évaluation sera : {prochaine[5]} le {jour_semaine(d_deb)} {d_deb[2]:02d}/{d_deb[1]:02d}")
        print(f"de {d_deb[3]:02d}h{d_deb[4]:02d} à {d_fin[3]:02d}h{d_fin[4]:02d}.")
    else:
        print("PLUS D'IE, YOUPI !!!")


def affichage_liste_evaluations(calendrier): 
    """
    Affiche toutes les évaluations du semestre et détecte les vacances (écart > 7 jours).

    Paramètres :
        - calendrier (list) : Liste de tous les événements triée.
    """
    print("\n#### PROCHAINES ÉVALUATIONS ####")
    evaluations = []
    
    # Extraction de toutes les évaluations dans une liste dédiée
    for i in range(len(calendrier)):
        ev = calendrier[i]
        if "EV" in ev[6] or "Evaluation" in ev[6]:
            evaluations.append(ev)
    
    # Affichage de chaque évaluation avec détection des périodes sans examen (vacances)
    for i in range(len(evaluations)):
        ev = evaluations[i]
        di_deb = extraire_date_event(ev)
        di_fin = extraire_date_event(ev, False)
        
        if i > 0:
            di_prec_fin = extraire_date_event(evaluations[i-1], False)
            diff = di_vers_d(di_deb) - di_vers_d(di_prec_fin)
            # Si l'écart entre deux évaluations dépasse une semaine
            if diff.days > 7:
                print("## VACANCES ##")
        
        nom_jour = jour_semaine(di_deb)
        print(f"{nom_jour} {di_deb[2]:02d}/{di_deb[1]:02d} : {ev[5]} ({di_deb[3]:02d}h-{di_fin[3]:02d}h)")

def calcul_statistiques_matiere(calendrier): 
    """
    Calcule le volume horaire par type (CM, TD, TP, Éval) et par matière.

    Paramètres :
        - calendrier (list) : Liste complète des événements.
    """
    stats = {}
    
    # Parcours de tous les événements pour accumuler les heures par matière
    for i in range(len(calendrier)):
        ev = calendrier[i]
        matiere = ev[5]
        type_cours = ev[6]
        prof = ev[7]
        
        # Calcul de la durée du cours
        heure_deb = float(ev[3].replace(',', '.'))
        heure_fin = float(ev[4].replace(',', '.'))
        duree = heure_fin - heure_deb
        
        # Initialisation du dictionnaire pour une nouvelle matière
        if matiere not in stats:
            stats[matiere] = {"CM": 0.0, "TD": 0.0, "TP": 0.0, "EVAL": 0.0, "Profs": []}
        
        # Répartition de la durée selon le type de cours
        if "CM" in type_cours: 
            stats[matiere]["CM"] = stats[matiere]["CM"] + duree
        elif "TD" in type_cours: 
            stats[matiere]["TD"] = stats[matiere]["TD"] + duree
        elif "TP" in type_cours: 
            stats[matiere]["TP"] = stats[matiere]["TP"] + duree
        elif "EV" in type_cours or "Evaluation" in type_cours: 
            stats[matiere]["EVAL"] = stats[matiere]["EVAL"] + duree
        
        # Ajout de l'intervenant s'il n'est pas encore répertorié
        if prof not in stats[matiere]["Profs"]:
            stats[matiere]["Profs"].append(prof)

    print("\n#### VUE D'ENSEMBLE DU SEMESTRE ####")
    
    # Affichage du bilan final pour chaque matière
    for m in stats:
        s = stats[m]
        profs_str = ""
        
        # Construction de la chaîne de caractères listant les intervenants
        for j in range(len(s["Profs"])):
            if j > 0:
                profs_str = profs_str + ", "
            profs_str = profs_str + s["Profs"][j]
            
        print(f"{m} : {s['CM']}h CM, {s['TD']}h TD, {s['TP']}h TP, {s['EVAL']}h d'éval. (Intervenants: {profs_str})")


def quitter(quit_val): 
    """ Arrête le programme si quit_val est True. """
    q = False
    if quit_val == True:
        q = True
    return q 


def main():
    # Initialisation de l'environnement et chargement des données
    nom_fichier = "ISN/calendrier.csv"
    data = creer_calendrier(nom_fichier)
    calendrier_trie = trier_par_date(data)
    
    date_pivot = aujourdhui()
    en_cours = True

    # Affichage du pense-bête au démarrage du programme
    print("--- BIENVENUE DANS VOTRE CALENDRIER INTELLIGENT ---")
    affichage_pense_bete(calendrier_trie)
    
    # Boucle principale gérant l'interaction avec l'utilisateur
    while en_cours == True:
        affichage_calendrier(calendrier_trie, date_pivot) 
        
        print("\nActions : [s]uivante, [p]récédente, [b]onus, [q]uitter")
        choix = input("Votre choix : ")
        
        if choix == 'q' or choix == 'Q':
            en_cours = False
            print("Au revoir !")
        elif choix == 's' or choix == 'S':
            date_pivot = naviguer_semaine(choix, date_pivot)
        elif choix == 'p' or choix == 'P':
            date_pivot = naviguer_semaine(choix, date_pivot)
        elif choix == 'b' or choix == 'B':
            affichage_liste_evaluations(calendrier_trie)
            calcul_statistiques_matiere(calendrier_trie)
            input("\nAppuyez sur Entrée pour revenir au calendrier...")

if __name__ == "__main__":
    main()