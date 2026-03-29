##Jeu de tests 

#Fonction: validation_grille 
def test_validation_grille():
    res = True

    #grille sans alignement
    grille_valide = [
        [1,2,3],
        [2,3,1],
        [3,1,2]    ]
    
    if validation_grille(grille_valide) != True:
        print("Test faux : validation_grille(grille_valide) devrait etre True")
        res = False

    #grille avec 3 alignes
    grille_invalide = [
        [1,1,1],
        [2,3,2],
        [3,2,3] ]
    
    if validation_grille(grille_invalide) != False:
        print("Test faux : validation_grille(grille_invalide) devrait etre False")
        res = False

    return res

#Fonction: creer_grille_aleatoire 
def test_creer_grille_aleatoire():
    res = True
    grille = creer_grille_aleatoire(3, 4, 5)

    #test le nombre de lignes
    if len(grille) != 3:
        print("Test faux : nombre de lignes incorrect")
        res = False

    #test le nombre de colonnes
    if len(grille[0]) != 4:
        print("Test faux : nombre de colonnes incorrect")
        res = False

    #test si les valeurs sont dans l'intervalle
    for ligne in grille:
        for val in ligne:
            if val < 0 or val >= 5:
                print("Test faux : valeur hors limites")
                res = False
    return res