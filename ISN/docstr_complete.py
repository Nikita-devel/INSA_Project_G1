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
def affichage_pense_bete(calendrier): #donné sur Moodle
    """
    Affiche la date actuelle ainsi que la prochaine évaluation à venir.

    Paramètres :
        - calendrier (liste) : calendrier csv 

    Sortie :
        - affichage du calendrier

    """
    
def retour_debut(retour): #Elora
    """
    Permet à l'utilisateur de retourner sur l'interface du début (afin de redemander l'affichage du calendrier d'une autre semaine) si retour est True

    Parameters:
    - retour : bool. True si l'utilisateur veut revenir au début
    
    Return:
    None
    
    """

def quitter(quit=False): #Elora
    """
    Permet à l'utilisateur de quitter le calendrier si quit est True
   
    Parameters:
    - quit: bool. True si l'utilisateur veut sortir du calendrier
    
    Return:
    None 
    
    """

def trouver_IE(): #Elora 
    """
    Renvoie la date de la prochaine IE à partir de la date d'aujourd'hui
   
    Parameters:
    - None 
    
    Return
    - date_IE: date. Date de la plus proche IE. Renvoie None si c'est la fin de l'année. 
    
    """

def quelle_semaine(jour): #Elora 
    """
    Trouve la semaine associée au jour donné par l'utilisateur
    
    Parameters:
    - jour: date. Jour saisi par l'utilisateur 
    
    Return
    
    - semaine: int. Numero de la semaine 
    
    """
    
def ma_fonction_2(liste, colonne):  #Eloise 
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

    
    return
    ----------------
    list
        La liste triée par année, puis par jour, puis par heure croissante.
"""








