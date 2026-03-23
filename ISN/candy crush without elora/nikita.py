import random

# PARTIE NIKITA : Moteur logique, détection et physique (Niveau 2)

def ajouter_sans_doublon(liste, x, y):
    """
    Fonction utilitaire : Ajoute les coordonnées [x, y] à la liste 
    uniquement si elles n'y sont pas déjà, sans utiliser l'opérateur 'in'.
    """
    present = False
    for i in range(len(liste)):
        if liste[i][0] == x and liste[i][1] == y:
            present = True
            
    if present == False:
        liste.append([x, y])
        
    return liste

def sont_voisins(coo_1, coo_2):
    """
    Vérifie si deux cases sont strictement voisines (haut, bas, gauche, droite).
    """
    x1 = coo_1[0]
    y1 = coo_1[1]
    x2 = coo_2[0]
    y2 = coo_2[1]
    voisins = False
    
    if x1 == x2 and (y1 == y2 + 1 or y1 == y2 - 1):
        voisins = True
    if y1 == y2 and (x1 == x2 + 1 or x1 == x2 - 1):
        voisins = True
        
    return voisins

def trois_alignes(grille):
    """
    Parcourt la grille pour détecter s'il existe au moins un alignement de 3.
    """
    lignes = len(grille)
    colonnes = len(grille[0])
    alignement_trouve = False
    
    # Vérification horizontale avec boucle while (Single Exit)
    i = 0
    while i < lignes and alignement_trouve == False:
        j = 0
        while j < colonnes - 2 and alignement_trouve == False:
            couleur = grille[i][j]
            if couleur != -1:
                if grille[i][j+1] == couleur and grille[i][j+2] == couleur:
                    alignement_trouve = True
            j = j + 1
        i = i + 1
                    
    # Vérification verticale
    i = 0
    while i < lignes - 2 and alignement_trouve == False:
        j = 0
        while j < colonnes and alignement_trouve == False:
            couleur = grille[i][j]
            if couleur != -1:
                if grille[i+1][j] == couleur and grille[i+2][j] == couleur:
                    alignement_trouve = True
            j = j + 1
        i = i + 1
                    
    return alignement_trouve

def selectionner_les_cases(grille):
    """
    Identifie toutes les coordonnées des bonbons alignés par 3 ou plus.
    """
    lignes = len(grille)
    colonnes = len(grille[0])
    a_detruire = []
    
    for i in range(lignes):
        for j in range(colonnes - 2):
            c = grille[i][j]
            if c != -1 and grille[i][j+1] == c and grille[i][j+2] == c:
                a_detruire = ajouter_sans_doublon(a_detruire, i, j)
                a_detruire = ajouter_sans_doublon(a_detruire, i, j+1)
                a_detruire = ajouter_sans_doublon(a_detruire, i, j+2)
                
    for i in range(lignes - 2):
        for j in range(colonnes):
            c = grille[i][j]
            if c != -1 and grille[i+1][j] == c and grille[i+2][j] == c:
                a_detruire = ajouter_sans_doublon(a_detruire, i, j)
                a_detruire = ajouter_sans_doublon(a_detruire, i+1, j)
                a_detruire = ajouter_sans_doublon(a_detruire, i+2, j)
                
    return a_detruire

def ya_voisin(grille, cases_alignees):
    """
    NIVEAU 2 : Trouve tous les voisins de même couleur en cascade.
    """
    lignes = len(grille)
    colonnes = len(grille[0])
    selection_finale = []
    
    for k in range(len(cases_alignees)):
        selection_finale.append(cases_alignees[k])
        
    i = 0
    while i < len(selection_finale):
        x = selection_finale[i][0]
        y = selection_finale[i][1]
        couleur = grille[x][y]
        
        # Haut
        if x - 1 >= 0:
            if grille[x-1][y] == couleur:
                selection_finale = ajouter_sans_doublon(selection_finale, x-1, y)
        # Bas
        if x + 1 < lignes:
            if grille[x+1][y] == couleur:
                selection_finale = ajouter_sans_doublon(selection_finale, x+1, y)
        # Gauche
        if y - 1 >= 0:
            if grille[x][y-1] == couleur:
                selection_finale = ajouter_sans_doublon(selection_finale, x, y-1)
        # Droite
        if y + 1 < colonnes:
            if grille[x][y+1] == couleur:
                selection_finale = ajouter_sans_doublon(selection_finale, x, y+1)
                
        i = i + 1
        
    return selection_finale

def generer_cases(grille, nb_couleurs=4):
    """
    Gravité : Fait tomber les bonbons au-dessus des cases à -1 et génère de nouveaux bonbons.
    """
    lignes = len(grille)
    colonnes = len(grille[0])
    
    for j in range(colonnes):
        colonne_temporaire = []
        
        for i in range(lignes):
            if grille[i][j] != -1:
                colonne_temporaire.append(grille[i][j])
                
        trous = lignes - len(colonne_temporaire)
        
        # On recrée la colonne : d'abord les nouveaux (en haut), puis les anciens
        nouvelle_col = []
        for k in range(trous):
            nouvelle_col.append(random.randint(0, nb_couleurs - 1))
            
        for k in range(len(colonne_temporaire)):
            nouvelle_col.append(colonne_temporaire[k])
            
        # On remplace dans la grille
        for i in range(lignes):
            grille[i][j] = nouvelle_col[i]
            
    return grille


def test_trois_alignes():
    # TEST 1 : Cas limite - Grille sans alignement
    grille_sans = [
        [0, 1, 2, 3],
        [1, 2, 3, 0],
        [2, 3, 0, 1],
        [3, 0, 1, 2]
    ]
    assert trois_alignes(grille_sans) == False, "Erreur TEST 1"

    # TEST 2 : Test général - Alignement horizontal
    grille_horizontale = [
        [0, 1, 2, 3],
        [1, 1, 1, 0],
        [2, 3, 0, 1],
        [3, 0, 1, 2]
    ]
    assert trois_alignes(grille_horizontale) == True, "Erreur TEST 2"

    # TEST 3 : Cas limite - Ignorer les cases détruites (-1)
    grille_detruite = [
        [-1, -1, -1, 3],
        [1, 2, 3, 0],
        [2, 3, 0, 1],
        [3, 0, 1, 2]
    ]
    assert trois_alignes(grille_detruite) == False, "Erreur TEST 3"

    print(" Tous les tests de trois_alignes() ont réussi !")

def est_identique(liste1, liste2):
    """ Fonction utilitaire pour comparer deux listes de coordonnées sans 'in' ni '==' global """
    if len(liste1) != len(liste2):
        return False
        
    identique = True
    for i in range(len(liste1)):
        # On vérifie si chaque élément de liste1 a une correspondance exacte à la même position dans liste2
        if liste1[i][0] != liste2[i][0] or liste1[i][1] != liste2[i][1]:
            identique = False
            
    return identique

def test_selectionner_les_cases():
    # TEST 4 : Cas limite - Alignement de 4 bonbons
    grille_quatre = [
        [1, 1, 1, 1],
        [2, 3, 0, 1],
        [3, 0, 1, 2],
        [0, 2, 3, 0]
    ]
    
    # Résultat attendu : Les 4 cases de la première ligne
    cases_attendues = [[0, 0], [0, 1], [0, 2], [0, 3]]
    resultat = selectionner_les_cases(grille_quatre)
    
    assert est_identique(resultat, cases_attendues) == True, "Erreur TEST 4"
        
    print(" Tous les tests de selectionner_les_cases() ont réussi !")

if __name__ == "__main__":
    print("Début des tests de détection...")
    test_trois_alignes()
    test_selectionner_les_cases()




import random

# =================================================================
# ЧАСТИНА NIKITA : Логічний рушій, детекція та фізика (Рівень 2)
# =================================================================

def ajouter_sans_doublon(liste, x, y):
    """
    Додає координати [x, y] до списку лише у разі їх відсутності.
    Це важливо, щоб не видаляти одну й ту саму клітинку двічі.
    """
    present = False  # Прапор: чи є вже така пара координат у списку?
    
    # Перебираємо весь список вручну (замість оператора 'in')
    for i in range(len(liste)):
        # Якщо x та y збігаються з елементом у списку
        if liste[i][0] == x and liste[i][1] == y:
            present = True # Знайшли дублікат
            
    # Якщо після перевірки всього списку дубліката немає
    if present == False:
        liste.append([x, y]) # Додаємо нові координати
        
    return liste # Повертаємо оновлений список

def sont_voisins(coo_1, coo_2):
    """
    Перевіряє, чи є дві клітинки сусідами (вгору, вниз, вліво, вправо).
    """
    x1, y1 = coo_1[0], coo_1[1] # Координати першої точки
    x2, y2 = coo_2[0], coo_2[1] # Координати другої точки
    voisins = False # Початково вважаємо, що вони не сусіди
    
    # Перевірка по вертикалі: X однакові, Y відрізняються на 1
    if x1 == x2 and (y1 == y2 + 1 or y1 == y2 - 1):
        voisins = True
    # Перевірка по горизонталі: Y однакові, X відрізняються на 1
    if y1 == y2 and (x1 == x2 + 1 or x1 == x2 - 1):
        voisins = True
        
    return voisins

def trois_alignes(grille):
    """
    Сканує ігрове поле на наявність хоча б одного ряду з 3-х однакових елементів.
    Використовується для швидкої перевірки стану гри.
    """
    lignes = len(grille) # Кількість рядків
    colonnes = len(grille[0]) # Кількість стовпців
    alignement_trouve = False # Прапор знаходження комбінації
    
    # ПЕРЕВІРКА ПО ГОРИЗОНТАЛІ
    i = 0
    while i < lignes and alignement_trouve == False:
        j = 0
        while j < colonnes - 2 and alignement_trouve == False:
            couleur = grille[i][j] # Беремо колір поточної клітинки
            if couleur != -1: # Якщо клітинка не порожня
                # Перевіряємо дві наступні клітинки праворуч
                if grille[i][j+1] == couleur and grille[i][j+2] == couleur:
                    alignement_trouve = True # Збіг знайдено!
            j = j + 1
        i = i + 1
                    
    # ПЕРЕВІРКА ПО ВЕРТИКАЛІ
    i = 0
    while i < lignes - 2 and alignement_trouve == False:
        j = 0
        while j < colonnes and alignement_trouve == False:
            couleur = grille[i][j]
            if couleur != -1:
                # Перевіряємо дві наступні клітинки знизу
                if grille[i+1][j] == couleur and grille[i+2][j] == couleur:
                    alignement_trouve = True # Збіг знайдено!
            j = j + 1
        i = i + 1
                    
    return alignement_trouve

def selectionner_les_cases(grille):
    """
    Знаходить і повертає координати ВСІХ цукерок, що утворюють лінії від 3 штук.
    """
    lignes = len(grille)
    colonnes = len(grille[0])
    a_detruire = [] # Список для збору координат на видалення
    
    # Горизонтальний пошук
    for i in range(lignes):
        for j in range(colonnes - 2):
            c = grille[i][j]
            # Якщо три поспіль однакові (і не порожні)
            if c != -1 and grille[i][j+1] == c and grille[i][j+2] == c:
                a_detruire = ajouter_sans_doublon(a_detruire, i, j)
                a_detruire = ajouter_sans_doublon(a_detruire, i, j+1)
                a_detruire = ajouter_sans_doublon(a_detruire, i, j+2)
                
    # Вертикальний пошук
    for i in range(lignes - 2):
        for j in range(colonnes):
            c = grille[i][j]
            if c != -1 and grille[i+1][j] == c and grille[i+2][j] == c:
                a_detruire = ajouter_sans_doublon(a_detruire, i, j)
                a_detruire = ajouter_sans_doublon(a_detruire, i+1, j)
                a_detruire = ajouter_sans_doublon(a_detruire, i+2, j)
                
    return a_detruire

def ya_voisin(grille, cases_alignees):
    """
    РІВЕНЬ 2: Знаходить усіх сусідів того ж кольору "каскадом".
    Якщо поруч із лінією є цукерка того ж кольору, вона теж додається до списку.
    """
    lignes = len(grille)
    colonnes = len(grille[0])
    selection_finale = [] # Фінальний список на видалення
    
    # Копіюємо початкові знайдені координати
    for k in range(len(cases_alignees)):
        selection_finale.append(cases_alignees[k])
        
    i = 0
    # Цикл іде по списку, який сам може розширюватися в процесі (хвильовий алгоритм)
    while i < len(selection_finale):
        x = selection_finale[i][0]
        y = selection_finale[i][1]
        couleur = grille[x][y] # Колір поточної клітинки, яку ми перевіряємо
        
        # Перевірка СУСІДА ЗВЕРХУ
        if x - 1 >= 0: # Чи не виходимо за межі поля
            if grille[x-1][y] == couleur: # Якщо колір збігається
                selection_finale = ajouter_sans_doublon(selection_finale, x-1, y)
        # ПЕРЕВІРКА ЗНИЗУ
        if x + 1 < lignes:
            if grille[x+1][y] == couleur:
                selection_finale = ajouter_sans_doublon(selection_finale, x+1, y)
        # ПЕРЕВІРКА ЗЛІВА
        if y - 1 >= 0:
            if grille[x][y-1] == couleur:
                selection_finale = ajouter_sans_doublon(selection_finale, x, y-1)
        # ПЕРЕВІРКА СПРАВА
        if y + 1 < colonnes:
            if grille[x][y+1] == couleur:
                selection_finale = ajouter_sans_doublon(selection_finale, x, y+1)
                
        i = i + 1 # Переходимо до наступної клітинки у списку на перевірку
        
    return selection_finale

def generer_cases(grille, nb_couleurs=4):
    """
    Гравітація: змушує цукерки падати в порожні місця (-1) 
    і заповнює верхні клітинки новими випадковими кольорами.
    """
    lignes = len(grille)
    colonnes = len(grille[0])
    
    for j in range(colonnes): # Обробляємо кожен стовпець окремо
        colonne_temporaire = [] # Тимчасовий список для "живих" цукерок стовпця
        
        # 1. Збираємо зверху вниз усі цукерки, які НЕ були видалені (-1)
        for i in range(lignes):
            if grille[i][j] != -1:
                colonne_temporaire.append(grille[i][j])
                
        # 2. Вираховуємо кількість порожніх місць (трюків)
        trous = lignes - len(colonne_temporaire)
        
        # 3. Формуємо новий склад стовпця
        nouvelle_col = []
        # Спочатку додаємо нові випадкові цукерки (вони з'являться зверху)
        for k in range(trous):
            nouvelle_col.append(random.randint(0, nb_couleurs - 1))
            
        # Потім додаємо ті, що впали (зберігаємо їх відносний порядок)
        for k in range(len(colonne_temporaire)):
            nouvelle_col.append(colonne_temporaire[k])
            
        # 4. Повертаємо сформований стовпець назад у двовимірний масив (гріду)
        for i in range(lignes):
            grille[i][j] = nouvelle_col[i]
            
    return grille


def test_trois_alignes():
    # Тест: порожнє поле без збігів
    grille_sans = [
        [0, 1, 2, 3],
        [1, 2, 3, 0],
        [2, 3, 0, 1],
        [3, 0, 1, 2]
    ]
    assert trois_alignes(grille_sans) == False, "Помилка: знайдено збіг там, де його нема"

    # Тест: горизонтальний збіг (три одиниці в другому рядку)
    grille_horizontale = [
        [0, 1, 2, 3],
        [1, 1, 1, 0],
        [2, 3, 0, 1],
        [3, 0, 1, 2]
    ]
    assert trois_alignes(grille_horizontale) == True, "Помилка: не знайдено горизонтальний ряд"

    print("✅ Тести trois_alignes() пройшли успішно!")

def est_identique(liste1, liste2):
    """ Допоміжна функція для порівняння двох списків координат. """
    if len(liste1) != len(liste2):
        return False
    for i in range(len(liste1)):
        if liste1[i][0] != liste2[i][0] or liste1[i][1] != liste2[i][1]:
            return False
    return True

def test_selectionner_les_cases():
    # Тест: Лінія з 4-х елементів
    grille_quatre = [
        [1, 1, 1, 1],
        [2, 3, 0, 1],
        [3, 0, 1, 2],
        [0, 2, 3, 0]
    ]
    cases_attendues = [[0, 0], [0, 1], [0, 2], [0, 3]]
    resultat = selectionner_les_cases(grille_quatre)
    
    assert est_identique(resultat, cases_attendues) == True, "Помилка: невірна вибірка координат"
    print("✅ Тести selectionner_les_cases() пройшли успішно!")

# Точка входу в програму
if __name__ == "__main__":
    print("🚀 Запуск тестів логіки гри...")
    test_trois_alignes()
    test_selectionner_les_cases()