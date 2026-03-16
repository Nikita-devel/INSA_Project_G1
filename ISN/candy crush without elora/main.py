from logique import *
from interface import *

def main():
    points_max = 100
    score = 0
    en_cours = True
    
    # Affichage des règles au lancement
    afficher_regles()
    
    # Génération et validation de la grille initiale
    nom_fichier = "exemple_grille.csv"
    grille = creer_grille(nom_fichier)
    
    # On s'assure qu'il n'y a pas de combinaison dès le départ (Exigence du barème)
    grille = validation_grille(grille) 
    
    # 3. Boucle principale du jeu
    while en_cours == True:
        afficher_grille(grille)
        afficher_compteur(score)
        
        # Saisie des coordonnées par le joueur (Simplifié FIMI)
        print("\n--- À VOTRE TOUR ---")
        print("Entrez les coordonnées de la première case :")
        x1 = int(input("Ligne 1 : "))
        y1 = int(input("Colonne 1 : "))
        
        print("Entrez les coordonnées de la deuxième case :")
        x2 = int(input("Ligne 2 : "))
        y2 = int(input("Colonne 2 : "))
        
        coo_1 = [x1, y1]
        coo_2 = [x2, y2]
        
        # Étape 1 : Vérifier si les cases sont bien côte à côte
        if sont_voisins(coo_1, coo_2) == True:
            
            # Étape 2 : On simule l'échange
            grille = echange_les_cases(grille, coo_1, coo_2)
            
            # Étape 3 : On vérifie si l'échange a créé un alignement
            if trois_alignes(grille) == True:
                
                # DÉBUT DES CASCADES (Réactions en chaîne)
                cascade_en_cours = True
                while cascade_en_cours == True:
                    
                    # a. Trouver les bonbons alignés
                    cases_alignees = selectionner_les_cases(grille)
                    
                    # b. Ajouter les voisins de même couleur
                    cases_a_detruire = ya_voisin(grille, cases_alignees)
                    
                    # c. Calcul et ajout des points (ex: 10 pts par bonbon)
                    points_gagnes = len(cases_a_detruire) * 10
                    score = score + points_gagnes
                    
                    # d. Détruire les cases (mettre la valeur à -1)
                    grille = detruire_cases(grille, cases_a_detruire)
                    print("\nBOOM ! Destruction des bonbons :")
                    afficher_grille(grille)
                    
                    # e. Faire tomber les bonbons et générer les nouveaux
                    grille = generer_cases(grille)
                    print("\nChute de nouveaux bonbons :")
                    afficher_grille(grille)
                    
                    # f. Vérifier si la chute a créé une nouvelle combinaison
                    if trois_alignes(grille) == False:
                        cascade_en_cours = False # Arrêt de la réaction en chaîne
                
            else:
                # Si l'échange n'a rien donné, on annule (on ré-échange)
                print("\nÉchange invalide (aucune combinaison formée). On annule.")
                grille = echange_les_cases(grille, coo_1, coo_2)
                
        else:
            print("\nErreur : Les cases ne sont pas voisines. Réessayez.")
            
        # 4. Vérification de la condition de victoire
        if score >= points_max:
            en_cours = False
            afficher_fin_jeu()
            
        # (Bonus à faire plus tard : Vérifier s'il reste des échanges possibles pour afficher "Dommage")

if __name__ == "__main__":
    main()