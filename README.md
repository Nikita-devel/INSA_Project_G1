# INSA_Project_G1
Voici le guide détaillé du flux quotidien, avec une section spéciale pour résoudre les erreurs courantes, à partager avec ton groupe :

---

### 🔄 Flux de travail quotidien (Workflow détaillé)

Suivez strictement ces étapes dans l'ordre pour que tout se passe bien :

#### 1. Actualiser son projet (Le matin ou avant de coder)

Avant de toucher au code, récupérez le travail des autres :

```bash
git pull origin main

```

#### 2. Travailler sur vos fichiers

Modifiez vos fichiers ou créez-en de nouveaux.
*Note : Si vous ne travaillez pas sur les mêmes fichiers, Git fusionnera tout automatiquement sans problème.*

#### 3. Sauvegarder localement (Commit)

Une fois votre tâche terminée :

```bash
git add .
git commit -m "Explication de ce que vous avez fait"

```

#### 4. Envoyer au groupe (Push)

```bash
git push origin main

```

---

### 🛠 Que faire en cas d'erreur ? (Le guide de secours)

#### ❌ Erreur n°1 : "Rejected - fetch first"

Cela arrive quand quelqu'un a fait un `push` avant vous. Votre historique n'est plus à jour.

* **Solution :**
1. Faites un `git pull origin main`.
2. Si Git demande un message de "Merge" (écran noir), tapez simplement `:wq` puis `Entrée`.
3. Refaites votre `git push origin main`.



#### ❌ Erreur n°2 : Bloqué dans l'écran noir (Éditeur Vim)

Parfois, après un `pull`, Git ouvre un éditeur étrange dans le terminal pour valider la fusion.

* **Solution pour sortir de là :**
1. Appuyez sur la touche **Echap** (ESC).
2. Tapez précisément `:wq` (cela signifie *write* et *quit*).
3. Appuyez sur **Entrée**.



#### ❌ Erreur n°3 : "Your local changes would be overwritten"

Cela arrive si vous faites un `pull` alors que vous avez des modifications non sauvegardées.

* **Solution :**
1. Faites d'abord un `git add .` et `git commit -m "Sauvegarde temporaire"`.
2. Refaites le `git pull origin main`.



---

**Conseil :** Si vous avez un doute, ne forcez jamais avec un `--force`. Demandez a Nikita
