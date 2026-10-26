# SCRIPT ORAL – ROMAIN, YANNIS, LISA

Exactement les mêmes notes que dans `Soutenance_Apartment_Hunter.pptx` (onglet Notes / mode Présentateur), regroupées ici pour réviser.

**Règle :** ne pas apprendre par cœur. Lire 2 ou 3 fois, retenir « Ce qu'il faut comprendre », puis le dire avec ses mots.

## Répartition et timing (≈ 20 minutes)

| Qui | Slides | Partie | Durée |
|---|---|---|---|
| Romain | 1 à 7 | projet, architecture, organisation, données, nettoyage, graphiques | 7 min 00 |
| Yannis | 8 à 12 | chemin des données, variables, modèles, mesures, comparaison | 6 min 40 |
| Lisa | 13 à 17 | Grid Search, test final, Flask, Docker, conclusion | 6 min 20 |
| Tous | 18 à 21 | annexes A à D : slides de secours pour les questions | hors temps |

**Passages de parole :** Romain → Yannis à la fin de la slide 7 ; Yannis → Lisa à la fin de la slide 12.

---

# ROMAIN

## Slide 1 – Apartment Hunter

**INTERVENANT :** ROMAIN  ·  **TEMPS CIBLE :** 0 min 30

### Ce qu'on dit
> Bonjour à tous. On va vous présenter Apartment Hunter, notre projet pour le sujet « Chasseurs d'appart' ».
>
> L'idée tient en une phrase : estimer le prix d'une maison à partir de ses caractéristiques. À droite, c'est notre application finale : on remplit un formulaire, et elle affiche un prix estimé.
>
> On est trois. Moi, Romain, je vous présente le projet, l'architecture et les données. Yannis présentera la sélection des variables, les modèles et la façon dont on les mesure. Lisa finira avec le modèle final, l'application Flask et Docker.

### Ce qu'il faut comprendre
- Le projet suit un chemin simple : des données → un modèle → une application.
- Annoncer tout de suite qui présente quoi : ça montre que le travail est organisé.

### Si le prof demande
- **« C'est quoi Apartment Hunter, en une phrase ? »**  
  → Un outil qui estime le prix d'une maison à partir de 8 caractéristiques, grâce à une Random Forest utilisée dans une application Flask.

## Slide 2 – La question de départ

**INTERVENANT :** ROMAIN  ·  **TEMPS CIBLE :** 0 min 50

### Ce qu'on dit
> Dans le scénario du sujet, on est des data scientists qui se reconvertissent en agents immobiliers. Et le travail d'un agent, c'est notamment d'estimer le prix des biens qu'il vend.
>
> Notre question, c'est donc : est-ce qu'on peut estimer le prix d'une maison à partir de ses caractéristiques ?
>
> Pour y répondre : on fait apprendre un modèle sur plus de 21 000 ventes réelles, puis on le rend utilisable dans une petite page web. Techniquement, c'est un problème de régression : on ne prédit pas une catégorie, on prédit un nombre, le prix.

### Ce qu'il faut comprendre
- Régression = prédire une valeur numérique (le prix).
- Toute la présentation sert à répondre à cette question ; la conclusion doit y répondre clairement.

### Si le prof demande
- **« Pourquoi c'est de la régression et pas de la classification ? »**  
  → Parce qu'on prédit un nombre continu, le prix, et pas une catégorie comme « cher / pas cher ».
- **« À qui servirait l'outil ? »**  
  → À un agent immobilier qui veut une première estimation rapide avant de visiter ou de fixer un prix.

## Slide 3 – Architecture globale du projet

**INTERVENANT :** ROMAIN  ·  **TEMPS CIBLE :** 1 min 50

### Ce qu'on dit
> Cette slide résume tout notre projet. On la lit de gauche à droite.
>
> 1. On commence avec les données : le fichier kc_house_data.csv, avec 21 613 ventes de maisons de la région de Seattle.
>
> 2. Le notebook Python, apartment_hunter.ipynb, sert à préparer les données et à entraîner le modèle. On descend la colonne de gauche : on nettoie d'abord les données, on fait l'analyse exploratoire, on sélectionne les variables, de 15 à 8, puis on sépare les maisons en train et test. Ensuite on remonte la colonne de droite : on compare trois algorithmes, régression linéaire, arbre de décision et Random Forest, avec une validation croisée ; on règle la Random Forest avec un Grid Search, et on obtient notre Random Forest finale, en vert.
>
> 3. On sauvegarde ce modèle déjà entraîné avec joblib, dans un fichier : model.pkl. À partir de là, on n'a plus besoin de réentraîner le modèle pour utiliser l'application. Tout ce qui est à gauche, on ne le fait qu'une fois.
>
> 4. À droite, l'application web. Flask, dans app.py, charge model.pkl au démarrage. L'utilisateur remplit le formulaire dans son navigateur, Flask récupère les huit valeurs, crée un DataFrame pandas, l'envoie au modèle avec predict, et affiche le prix estimé.
>
> Enfin, le cadre en pointillés, c'est Docker. Il contient Flask, Python, le modèle et toutes les librairies. Docker ne remplace pas Flask : Flask tourne à l'intérieur de Docker. Docker sert juste à rendre l'environnement reproductible, pour que l'application marche pareil sur n'importe quel ordinateur.

### Ce qu'il faut comprendre
- Deux moments : créer le modèle (notebook, une seule fois) et utiliser le modèle (application, à chaque estimation).
- model.pkl fait le lien entre les deux : c'est la sortie du notebook et l'entrée de l'application.
- Flask est l'application web ; Docker est la boîte qui contient Flask et son environnement.
- Le test n'intervient qu'à la fin du notebook, pour vérifier la Random Forest finale.

### Si le prof demande
- **« Est-ce que Docker entraîne le modèle ? »**  
  → Non. Le modèle est déjà entraîné dans le notebook. Docker ne fait que lancer l'application qui utilise model.pkl.
- **« Flask et Docker font la même chose ? »**  
  → Non. Flask est l'application web. Docker contient l'application et son environnement (Python, librairies, fichiers).
- **« Pourquoi model.pkl ? »**  
  → Pour réutiliser le modèle entraîné sans refaire tout le notebook à chaque lancement de l'application.

*ASTUCE : on peut revenir à cette slide pour répondre à presque toutes les questions sur l'organisation du code.*

## Slide 4 – Feuille de route et Trello

**INTERVENANT :** ROMAIN  ·  **TEMPS CIBLE :** 0 min 50

### Ce qu'on dit
> Avant de commencer, on a découpé le projet en tâches et estimé leur durée : environ six jours et demi au total. Les parties les plus longues sont les modèles et l'application.
>
> On s'est réparti le travail : moi sur le nettoyage et l'analyse exploratoire, Yannis sur la sélection des variables et les modèles, Lisa sur le Grid Search, le modèle final, Flask et Docker. On a fait ensemble la mise en place, la documentation et la présentation.
>
> Pour suivre l'avancement, on a utilisé un Trello en Kanban : trois colonnes, à faire, en cours et terminé, et on déplace les cartes au fur et à mesure. Côté matériel, pas besoin de grosse machine : nos ordinateurs portables et Google Colab suffisent.

### Ce qu'il faut comprendre
- Une feuille de route = des tâches, des durées, des personnes et du matériel.
- Kanban = visualiser l'avancement en déplaçant des cartes de « à faire » vers « terminé ».
- Pas de GPU : les modèles s'entraînent en quelques minutes.

### Si le prof demande
- **« Comment vous êtes-vous répartis le travail ? »**  
  → Une personne par grande partie : données (Romain), modèles (Yannis), modèle final et application (Lisa), et le reste ensemble.
- **« Vos estimations de durée étaient réalistes ? »**  
  → Globalement oui ; ce qui prend le plus de temps, c'est de bien vérifier les résultats et de les expliquer, pas d'écrire le code.

## Slide 5 – D'où viennent les données ?

**INTERVENANT :** ROMAIN  ·  **TEMPS CIBLE :** 0 min 50

### Ce qu'on dit
> On avait le choix entre deux jeux de données : Madrid et King County. On a pris King County, la région de Seattle, parce qu'il a moins de colonnes, pas de texte libre à traiter, et chaque variable est bien expliquée dans la description.
>
> Ça fait 21 613 ventes de maisons, sur environ 13 mois, de mai 2014 à mai 2015, avec 21 colonnes.
>
> Le tableau, c'est la vraie première ligne du fichier : une maison de 3 chambres, 1 salle de bain, 1 180 pieds carrés, une qualité de construction de 7, sa latitude et sa longitude, et son prix de vente : 221 900 dollars. Le prix, c'est notre cible : ce qu'on veut apprendre à prédire.

### Ce qu'il faut comprendre
- Une ligne = une vente de maison.
- La cible (target), c'est price ; les autres colonnes sont les variables (features).
- Les surfaces sont en pieds carrés : 1 m² ≈ 10,76 pieds².

### Si le prof demande
- **« Pourquoi ce dataset ? »**  
  → Plus simple à nettoyer et à expliquer : moins de colonnes, pas de texte, variables documentées.
- **« C'est quoi le grade ? »**  
  → Une note de qualité de construction de 1 à 13 donnée par le comté ; 7 correspond à une qualité moyenne.

## Slide 6 – Des données déjà propres

**INTERVENANT :** ROMAIN  ·  **TEMPS CIBLE :** 1 min 00

### Ce qu'on dit
> Bonne nouvelle : les données étaient déjà propres. On a vérifié : aucune valeur manquante et aucune ligne en double.
>
> On a enlevé cinq colonnes. L'id, parce que c'est juste un identifiant. La date, parce que les ventes ne couvrent que 13 mois et qu'on a choisi de ne pas étudier l'effet du temps pour garder le projet simple. Le code postal, parce que la latitude et la longitude donnent déjà la position. Et sqft_above et sqft_basement, parce que leur somme donne exactement la surface habitable : c'était de l'information en double.
>
> Côté lignes, on n'a supprimé que 17 erreurs évidentes : une maison de 33 chambres pour 150 mètres carrés, et 16 maisons sans chambre ou sans salle de bain.
>
> Par contre, on a gardé les maisons très chères. La méthode IQR en trouve 1 145 au-dessus de la limite, mais ce sont de vraies maisons de luxe, pas des erreurs. Notre règle : on supprime l'impossible, on garde l'extrême.

### Ce qu'il faut comprendre
- Valeur impossible (erreur de saisie) ≠ valeur extrême (maison de luxe).
- Chaque colonne supprimée a une raison simple.
- On a perdu moins de 0,1 % des lignes : 21 613 → 21 596.

### Si le prof demande
- **« Pourquoi ne pas supprimer les maisons très chères ? »**  
  → Elles sont réelles : les 5 plus chères font 8 000 à 12 000 pieds² avec un grade de 11 à 13. Les enlever empêcherait le modèle d'estimer les grandes maisons.
- **« C'est quoi la méthode IQR ? »**  
  → On prend l'écart entre le 1er et le 3e quartile du prix ; au-delà de 3e quartile + 1,5 × cet écart, c'est une valeur extrême. Ici, environ 1,13 million de dollars.
- **« Pourquoi pas de normalisation ? »**  
  → Les arbres découpent avec des seuils, donc l'échelle ne change rien ; pour la régression linéaire, ça change les coefficients mais pas les prédictions.

## Slide 7 – Ce que montrent les graphiques

**INTERVENANT :** ROMAIN  ·  **TEMPS CIBLE :** 1 min 10

### Ce qu'on dit
> Le sujet demandait une analyse exploratoire avec Power BI. On ne l'avait pas, donc on a fait les graphiques en Python avec matplotlib, et on les a regroupés dans une page HTML, dashboard.html, qui sert de tableau de bord.
>
> Trois choses ressortent. D'abord, plus la maison est grande, plus elle est chère : c'est le lien le plus fort, avec une corrélation de 0,70. Ensuite, le prix augmente globalement avec la qualité de construction : environ 380 000 dollars au grade 7, presque 3 millions au grade 13. Enfin, la carte montre qu'il y a des quartiers beaucoup plus chers que d'autres.
>
> Ce qui est intéressant, c'est que la longitude a une corrélation presque nulle avec le prix, 0,02, alors que l'emplacement compte clairement. Le lien n'est simplement pas en ligne droite. Yannis va vous montrer comment on en a tenu compte pour choisir les variables.

### Ce qu'il faut comprendre
- Les 3 grands facteurs du prix : surface, qualité de construction, emplacement.
- Une corrélation faible ne veut pas dire « pas de lien », seulement « pas de lien en ligne droite ».
- dashboard.html remplace le dashboard Power BI demandé.

### Si le prof demande
- **« Pourquoi le prix médian et pas la moyenne ? »**  
  → La médiane est moins influencée par les quelques maisons très chères.
- **« Le prix monte à chaque niveau de grade ? »**  
  → Globalement oui, mais pas parfaitement : le grade 3 est au-dessus du grade 4, sauf qu'il n'y a qu'1 et 27 maisons dans ces groupes.

*TRANSITION : « Je laisse la parole à Yannis pour la suite. »*

---

# YANNIS

## Slide 8 – Du CSV au prix estimé

**INTERVENANT :** YANNIS  ·  **TEMPS CIBLE :** 1 min 20

### Ce qu'on dit
> Merci Romain. Avant de parler des modèles, voilà le vrai chemin que suivent les données.
>
> On lit le fichier CSV avec pandas et on le nettoie. Ensuite on sépare deux choses : X, ce sont les variables qu'on donne au modèle pour prédire, c'est-à-dire les 8 caractéristiques de la maison ; et y, c'est la cible, le prix.
>
> À cette étape, on sépare aussi les maisons en deux parties. La majorité, 80 %, soit 17 276 maisons, sert à entraîner le modèle. On garde 20 %, soit 4 320 maisons, de côté pour vérifier à la fin si le modèle fonctionne sur des maisons qu'il n'a jamais vues.
>
> La Random Forest, c'est notre algorithme final : elle apprend sur le train. On la sauvegarde dans model.pkl, le modèle entraîné. Et Flask, c'est l'interface entre l'utilisateur et le modèle : il récupère le formulaire et affiche le prix estimé.

### Ce qu'il faut comprendre
- X = les variables utilisées pour prédire ; y = la cible (price).
- Le train sert à apprendre ; le test sert à l'évaluation finale, une seule fois.
- model.pkl = le modèle déjà entraîné ; Flask = le lien entre l'utilisateur et le modèle.

### Si le prof demande
- **« Pourquoi 80 / 20 ? »**  
  → C'est un découpage classique ; avec plus de 21 000 maisons, il reste assez de données des deux côtés.
- **« Pourquoi random_state=42 ? »**  
  → Pour avoir toujours le même découpage et les mêmes résultats à chaque exécution ; 42 est juste une valeur fixe.
- **« Pourquoi ne pas tester sur le train ? »**  
  → Le modèle a déjà vu ces maisons : le score serait trop optimiste, comme réviser avec les réponses de l'examen.

## Slide 9 – 15 variables → 8 variables

**INTERVENANT :** YANNIS  ·  **TEMPS CIBLE :** 1 min 20

### Ce qu'on dit
> Après le nettoyage, il restait 15 variables. On ne voulait pas toutes les garder sans raison, donc on a utilisé deux méthodes, uniquement sur les données d'entraînement.
>
> D'abord la corrélation avec le prix. C'est simple, mais ça ne voit que les liens en ligne droite. Par exemple, la longitude a une corrélation de 0,02, alors qu'on vient de voir sur la carte que l'emplacement compte.
>
> Ensuite la sélection forward. On commence avec aucune variable, puis à chaque étape on ajoute celle qui améliore le plus le modèle, jusqu'à en avoir 8. Pour tester les variables, on a utilisé un arbre de décision, parce qu'il est rapide et qu'il voit les liens qui ne sont pas en ligne droite. Résultat : elle a gardé la latitude et la longitude, et elle a laissé de côté des variables comme le nombre de salles de bain, qui répète l'information de la surface.
>
> Et on a vérifié qu'on ne perdait rien : avec une Random Forest en validation croisée, on a un R² de 0,856 avec les 15 variables, et 0,855 avec les 8. C'est presque pareil, avec un formulaire beaucoup plus court.

### Ce qu'il faut comprendre
- La corrélation regarde chaque variable seule ; la sélection forward regarde ce qu'une variable apporte en plus des autres.
- On a vérifié qu'on ne perdait pas de précision (0,856 → 0,855).
- La sélection est faite sur le train uniquement, pour ne pas « tricher » avec le test.

### Si le prof demande
- **« Pourquoi garder la longitude alors que sa corrélation est presque nulle ? »**  
  → L'emplacement compte mais pas en ligne droite ; la sélection forward l'a gardée et c'est le 4e facteur du modèle final.
- **« Pourquoi bathrooms n'est pas gardée ? »**  
  → Elle est très liée à la surface (corrélation 0,76) : une fois la surface connue, elle n'apporte presque rien de plus.
- **« Pourquoi pas Boruta ? »**  
  → C'était un exemple du sujet ; deux méthodes plus simples suffisaient et donnaient la même précision.

## Slide 10 – Trois modèles, trois idées

**INTERVENANT :** YANNIS  ·  **TEMPS CIBLE :** 1 min 30

### Ce qu'on dit
> On a testé trois modèles de régression, chacun avec une idée différente.
>
> La régression linéaire, c'est une formule : prix égale a fois la surface, plus b fois le grade, et ainsi de suite. L'algorithme cherche les coefficients qui font le moins d'erreurs. C'est simple, mais ça ne sait faire que des lignes droites.
>
> L'arbre de décision, c'est une suite de questions oui ou non : est-ce que la surface est plus grande que 2 500 pieds carrés ? est-ce que le grade est plus grand que 7 ? À la fin, la maison tombe dans un groupe, et on lui donne le prix moyen de ce groupe. C'est facile à comprendre, mais sans limite, l'arbre finit par apprendre les maisons par cœur.
>
> La Random Forest, c'est beaucoup d'arbres, 100 par défaut. Chaque arbre est entraîné sur un tirage au hasard des maisons, donc ils sont tous un peu différents. Chaque arbre donne un prix, et on fait la moyenne. Les erreurs des arbres se compensent.

### Ce qu'il faut comprendre
- Régression linéaire = une formule ; arbre = des questions ; Random Forest = la moyenne de beaucoup d'arbres.
- En régression, les arbres de la forêt ne votent pas : on fait la moyenne de leurs prix.
- Les seuils de l'arbre sur la slide sont un exemple pour expliquer, pas les vrais seuils du modèle.

### Si le prof demande
- **« Pourquoi ces trois modèles ? »**  
  → Ce sont trois idées différentes et faciles à expliquer, du plus simple au plus puissant.
- **« Les arbres de la forêt votent ? »**  
  → Non : en régression, chacun donne un prix et on fait la moyenne. Le vote, c'est pour la classification.

## Slide 11 – Mesurer sans tricher

**INTERVENANT :** YANNIS  ·  **TEMPS CIBLE :** 1 min 00

### Ce qu'on dit
> Pour comparer les modèles, on n'a pas touché au jeu de test. On a utilisé une validation croisée sur le train. On coupe le train en trois parts. Au premier tour, on apprend sur deux parts et on mesure l'erreur sur la troisième ; puis on change de part, trois fois, et on fait la moyenne. Comme ça, chaque maison du train sert une fois à mesurer, et le test reste caché jusqu'à la fin.
>
> On regarde trois mesures. Le MAE, c'est l'erreur moyenne en dollars : « en moyenne, on se trompe de tant ». Le RMSE, c'est aussi en dollars, mais les grosses erreurs comptent plus, donc il est toujours plus grand que le MAE. Et le R², c'est la part de la variation des prix que le modèle arrive à expliquer : 1, c'est parfait, et 0, c'est pas mieux que de donner le prix moyen à tout le monde.

### Ce qu'il faut comprendre
- La validation croisée sert à CHOISIR ; le test sert à VÉRIFIER, une seule fois, à la fin.
- MAE et RMSE : plus c'est petit, mieux c'est. R² : plus c'est proche de 1, mieux c'est.
- Si le RMSE est bien plus grand que le MAE, il y a quelques grosses erreurs.

### Si le prof demande
- **« Pourquoi ne pas utiliser le test pour comparer les modèles ? »**  
  → Parce qu'on veut garder le test complètement indépendant pour évaluer honnêtement le modèle final.
- **« Pourquoi 3 parts et pas 5 ? »**  
  → Pour que le Grid Search reste rapide sur Colab ; avec plus de 17 000 maisons, chaque part reste assez grande.

## Slide 12 – Quel modèle est le meilleur ?

**INTERVENANT :** YANNIS  ·  **TEMPS CIBLE :** 1 min 30

### Ce qu'on dit
> Voilà le résultat en validation croisée. Sur le graphique, c'est l'erreur moyenne : la régression linéaire se trompe en moyenne de 138 000 dollars, l'arbre de décision d'environ 103 000, et la Random Forest d'environ 74 000. La Random Forest est aussi la meilleure en RMSE et en R², avec 0,855.
>
> À droite, on regarde le surapprentissage. On compare le score sur les maisons que le modèle a apprises, et le score en validation croisée, sur des maisons qu'il n'a pas vues. La régression linéaire a presque le même score des deux côtés : pas de surapprentissage, mais elle est trop simple. L'arbre seul fait 0,999 sur les maisons apprises, presque parfait, mais seulement 0,740 sur les autres : il a appris par cœur. La Random Forest a aussi un écart, mais elle reste bien meilleure sur les maisons nouvelles.
>
> Donc on garde la Random Forest. Lisa va vous montrer comment on l'a réglée et ce qu'elle donne au test final.

### Ce qu'il faut comprendre
- Surapprentissage = très bon sur ce qu'on a appris, beaucoup moins bon sur du nouveau.
- On le détecte en comparant le score « appris » et le score en validation croisée.
- La Random Forest limite le surapprentissage en faisant la moyenne de beaucoup d'arbres.

### Si le prof demande
- **« Pourquoi la Random Forest ? »**  
  → Elle donnait les meilleurs résultats en validation croisée et représente mieux les relations complexes qu'une régression linéaire, tout en limitant les faiblesses d'un arbre seul.
- **« Pourquoi la régression linéaire est-elle si moins bonne ? »**  
  → Elle ne fait que des lignes droites, alors que l'effet de l'emplacement n'est pas linéaire.
- **« Comment la forêt limite le surapprentissage ? »**  
  → Chaque arbre voit un tirage différent des maisons ; en faisant la moyenne, leurs erreurs se compensent.

*TRANSITION : « Je passe la parole à Lisa. »*

---

# LISA

## Slide 13 – Régler la Random Forest

**INTERVENANT :** LISA  ·  **TEMPS CIBLE :** 1 min 20

### Ce qu'on dit
> Merci Yannis. Une fois la Random Forest choisie, on a essayé de la régler avec un Grid Search. Ce n'est pas un nouveau modèle : Grid Search teste plusieurs combinaisons de paramètres et conserve celle qui donne les meilleurs résultats.
>
> On a testé trois paramètres. n_estimators, c'est le nombre d'arbres dans la forêt. max_depth, c'est le nombre maximum de questions à la suite dans chaque arbre. Et min_samples_split, c'est le nombre minimum de maisons qu'il faut dans un groupe pour pouvoir encore le couper en deux. Ça fait deux fois trois fois deux, donc 12 combinaisons, et chacune est évaluée en validation croisée en 3 tours : 36 entraînements. Toujours sur le train, sans toucher au test.
>
> La meilleure combinaison, c'est 200 arbres, une profondeur maximale de 15, et min_samples_split à 2. Sur le graphique, la barre verte : le gain est très petit, environ 500 dollars d'erreur moyenne en moins. Les réglages par défaut étaient déjà bons. Le but, c'était surtout d'appliquer la méthode.

### Ce qu'il faut comprendre
- Grid Search = une méthode de réglage, pas un algorithme de prédiction.
- Les paramètres réglés s'appellent des hyperparamètres : on les choisit avant l'entraînement.
- Un petit gain est un résultat normal : il montre que le modèle par défaut était déjà bien réglé.

### Si le prof demande
- **« Pourquoi ne pas utiliser le test pendant le Grid Search ? »**  
  → Parce qu'on veut garder le test complètement indépendant pour évaluer honnêtement le modèle final.
- **« Pourquoi une si petite grille ? »**  
  → 12 combinaisons suffisent pour appliquer la méthode ; une grille plus grande prendrait beaucoup plus de temps pour un gain probablement très faible.
- **« C'est quoi max_depth ? »**  
  → La profondeur maximale de chaque arbre, c'est-à-dire le nombre maximum de questions à la suite ; la limiter évite que l'arbre apprenne par cœur.

## Slide 14 – Le test final, fait une seule fois

**INTERVENANT :** LISA  ·  **TEMPS CIBLE :** 1 min 10

### Ce qu'on dit
> C'est seulement maintenant, à la toute fin, qu'on utilise les 4 320 maisons du test, une seule fois, sur le modèle déjà choisi.
>
> Résultat : un R² de 0,877. Attention à la façon de le dire : ça veut dire que le modèle explique environ 87,7 % de la variation des prix dans le jeu de test. Ça ne veut pas dire que 87,7 % des prix sont justes. L'erreur moyenne est de 71 718 dollars, soit environ 16 % du prix médian, et le RMSE est de 126 924 dollars, plus grand, parce qu'il y a quelques grosses erreurs.
>
> Le score du test est proche de celui de la validation croisée, et même un peu meilleur, parce que le modèle final apprend sur tout le train. Donc pas de mauvaise surprise.
>
> Sur le graphique : ce qui compte le plus pour le modèle, c'est la surface et la qualité de construction, puis l'emplacement avec la latitude et la longitude. Ça confirme ce que Romain avait vu dans l'analyse exploratoire.

### Ce qu'il faut comprendre
- Le test sert à VÉRIFIER, une seule fois : il n'a servi à aucun choix.
- R² = part de la variation expliquée, pas un pourcentage de bonnes réponses.
- Surface + qualité ≈ 2/3 de l'importance ; puis l'emplacement.

### Si le prof demande
- **« Pourquoi le test est meilleur que la validation croisée ? »**  
  → En validation croisée, chaque modèle n'apprend que sur 2/3 du train ; le modèle final apprend sur tout le train. L'important, c'est que les deux scores sont proches.
- **« 72 000 $ d'erreur, ce n'est pas beaucoup ? »**  
  → C'est environ 16 % du prix médian : correct pour une première estimation, mais ce n'est pas un prix exact.
- **« Pourquoi bedrooms sert si peu ? »**  
  → L'information sur les chambres est déjà en grande partie dans la surface habitable.

## Slide 15 – Flask : du formulaire au prix

**INTERVENANT :** LISA  ·  **TEMPS CIBLE :** 1 min 20

### Ce qu'on dit
> Pour rendre le modèle utilisable, on a fait une petite application web avec Flask.
>
> Au démarrage, app.py charge model.pkl une seule fois avec joblib. Ensuite, l'utilisateur remplit les huit champs du formulaire et clique sur Estimer. Le formulaire HTML, dans templates/index.html, envoie les valeurs à Flask. app.py les récupère avec request.form, les convertit en nombres, et les met dans un DataFrame pandas d'une ligne, avec les colonnes dans le même ordre que pendant l'entraînement. Puis on appelle predict sur la Random Forest, et le prix s'affiche dans l'encadré vert.
>
> Sur la capture, c'est une vraie maison du jeu de test : le modèle estime 375 210 dollars, pour une maison vendue 415 000.

### Ce qu'il faut comprendre
- En une phrase : Flask récupère les 8 valeurs, les met dans un DataFrame, les donne à la Random Forest déjà chargée et renvoie le prix.
- Le modèle n'est pas rechargé à chaque clic, seulement au démarrage.
- Ce n'est pas une API : c'est une page web avec un formulaire.

### Si le prof demande
- **« Pourquoi un DataFrame et pas une simple liste ? »**  
  → Le modèle a été entraîné avec un tableau pandas : on lui redonne les mêmes colonnes, avec les mêmes noms et dans le même ordre.
- **« Le modèle est chargé à chaque clic ? »**  
  → Non, une seule fois au démarrage de app.py ; à chaque clic, on appelle seulement predict.
- **« Et si l'utilisateur tape n'importe quoi ? »**  
  → Les champs du formulaire sont de type nombre avec des minimums et maximums, par exemple la latitude limitée à la zone du comté de King.

*DÉMO OPTIONNELLE : lancer l'application avant la soutenance et garder un onglet sur http://localhost:5000. Valeurs : 3 chambres, 1 510 pieds², terrain 6 083, pas de vue sur l'eau, grade 6, jamais rénovée (0), latitude 47.6966, longitude -122.324 → 375 210 $. Si la démo ne marche pas, la capture suffit.*

## Slide 16 – Flask tourne dans Docker

**INTERVENANT :** LISA  ·  **TEMPS CIBLE :** 1 min 10

### Ce qu'on dit
> Un point qu'on confond souvent : Flask et Docker, ce n'est pas la même chose. Docker ne remplace pas Flask. Flask, c'est l'application web. Docker, c'est la boîte qui contient l'application et tout son environnement.
>
> À gauche, notre Dockerfile, c'est la recette. On part d'une image Python 3.12 légère, on se place dans le dossier /app, on copie requirements.txt et on installe les librairies : flask, pandas, scikit-learn et joblib. Puis on copie l'application : app.py, model.pkl, les templates et le CSS. On indique le port 5000, et la commande de démarrage : python app.py.
>
> À droite, ce que ça donne : un conteneur qui contient Python, les librairies, et à l'intérieur notre application Flask. Sans Docker, il faudrait installer Python et les bonnes versions des librairies à la main sur chaque machine. Avec Docker, il suffit de deux commandes : docker build pour construire l'image, et docker run pour lancer l'application sur le port 5000.

### Ce qu'il faut comprendre
- Flask fait fonctionner l'application ; Docker transporte et exécute tout son environnement.
- Le Dockerfile : partir de Python, installer les librairies, copier les fichiers, lancer app.py.
- -p 5000:5000 relie le port 5000 de l'ordinateur à celui du conteneur.

### Si le prof demande
- **« Pourquoi Docker ? »**  
  → Pour fournir la même application avec le même environnement et les mêmes dépendances sur n'importe quelle machine.
- **« Est-ce que Docker entraîne le modèle ? »**  
  → Non : le conteneur ne contient que l'application et model.pkl, déjà entraîné dans le notebook.
- **« Pourquoi fixer les versions dans requirements.txt ? »**  
  → Un modèle sauvegardé avec une version de scikit-learn peut mal se recharger avec une autre ; on fixe la version 1.8.0 qui a créé model.pkl.

*COMMANDES : docker build -t apartment-hunter .   puis   docker run --rm -p 5000:5000 apartment-hunter   (voir annexe D).*

## Slide 17 – Conclusion

**INTERVENANT :** LISA  ·  **TEMPS CIBLE :** 1 min 20

### Ce qu'on dit
> Pour conclure et répondre à notre question de départ : oui, on peut estimer le prix d'une maison à partir de ses caractéristiques, avec une précision correcte.
>
> Le modèle explique environ 87,7 % de la variation des prix sur des maisons qu'il n'a jamais vues, avec une erreur moyenne d'environ 72 000 dollars : c'est une estimation, pas un prix exact. Et ce qui compte le plus, c'est la surface, la qualité de construction et l'emplacement.
>
> Il y a des limites : les données datent de 2014-2015 et ne concernent que la région de Seattle, il reste quelques grosses erreurs, et l'utilisateur doit connaître la latitude et la longitude. Pour aller plus loin, on pourrait utiliser des données plus récentes, permettre de saisir une adresse, ou tester d'autres modèles.
>
> Merci de nous avoir écoutés, on est prêts pour vos questions.

### Ce qu'il faut comprendre
- La conclusion répond à la question de la slide 2.
- Être honnête sur les limites montre qu'on comprend ce que fait le modèle.
- Pendant les questions, chacun prend en priorité celles de sa partie ; les annexes A à D servent de support.

### Si le prof demande
- **« Le modèle marcherait pour une maison à Paris ? »**  
  → Non : il a appris uniquement sur des ventes de 2014-2015 dans la région de Seattle. Il faudrait le réentraîner sur des données françaises.
- **« Qu'est-ce que vous amélioreriez en premier ? »**  
  → Des données plus récentes avec l'effet de la date, puis une saisie d'adresse au lieu des coordonnées.

---

# ANNEXES

## Slide 18 – Où se trouve quoi dans le projet ?

**INTERVENANT :** TOUS (celui dont c'est la partie)  ·  **TEMPS CIBLE :** hors présentation · slide de secours

### Ce qu'on dit
> Slide de secours, si le professeur veut savoir où se trouve chaque élément.
>
> Le notebook apartment_hunter.ipynb contient tout le travail de data science : chargement, nettoyage, analyse exploratoire, sélection des variables, comparaison des modèles, Grid Search, test final et sauvegarde. Il lit data/kc_house_data.csv et produit model.pkl et les images.
>
> L'application, c'est app.py avec Flask, la page templates/index.html et le style static/style.css. requirements.txt liste les librairies avec leurs versions, et le Dockerfile décrit comment construire le conteneur.

### Ce qu'il faut comprendre
- Le notebook crée le modèle ; app.py l'utilise.
- model.pkl est le seul lien entre les deux parties.

### Si le prof demande
- **« Où est le code qui entraîne le modèle ? »**  
  → Dans le notebook, sections 9 à 11 ; app.py n'entraîne rien, il charge model.pkl.
- **« Où sont les graphiques ? »**  
  → Dans le dossier images/, générés par le notebook et regroupés dans dashboard.html.

## Slide 19 – Les 8 variables du modèle

**INTERVENANT :** TOUS (celui dont c'est la partie)  ·  **TEMPS CIBLE :** hors présentation · slide de secours

### Ce qu'on dit
> Slide de secours pour expliquer chaque variable gardée.
>
> sqft_living, c'est la surface habitable en pieds carrés ; grade, la qualité de construction de 1 à 13 ; lat et long, la position ; waterfront, la vue sur l'eau ; sqft_lot, la surface du terrain ; bedrooms, le nombre de chambres ; et yr_renovated, l'année de rénovation, avec 0 si la maison n'a jamais été rénovée.
>
> La barre, c'est l'importance de chaque variable dans la Random Forest finale : la somme fait 1. La surface et la qualité représentent presque deux tiers de l'importance, puis vient l'emplacement.

### Ce qu'il faut comprendre
- Ce sont exactement les 8 champs du formulaire de l'application.
- Importance = à quel point la variable aide le modèle à réduire son erreur.

### Si le prof demande
- **« Pourquoi garder bedrooms et yr_renovated s'ils servent si peu ? »**  
  → Ils ont été choisis par la sélection forward, et le nombre de chambres est une information naturelle à demander ; ils ne gênent pas.
- **« Pourquoi pas view ? »**  
  → Son information est en partie déjà dans waterfront et dans la position.

## Slide 20 – Questions fréquentes

**INTERVENANT :** TOUS (celui dont c'est la partie)  ·  **TEMPS CIBLE :** hors présentation · slide de secours

### Ce qu'on dit
> Slide de secours pour les questions. Chacun répond en priorité aux questions de sa partie.
>
> Questions bonus possibles, avec réponse courte :
>
> « Pourquoi pas de normalisation ? » → Les arbres n'en ont pas besoin, et ça ne change pas les prédictions de la régression linéaire.
>
> « Pourquoi la longitude alors que sa corrélation est 0,02 ? » → L'emplacement compte mais pas en ligne droite ; c'est le 4e facteur du modèle.
>
> « Pourquoi pas Power BI ? » → On n'y avait pas accès : analyse faite avec matplotlib et dashboard.html.
>
> « C'est une API ? » → Non, une page web avec un formulaire.
>
> « Pourquoi compress=3 ? » → Pour que model.pkl fasse 26,3 Mo et reste sous la limite de 100 Mo de GitHub.

### Ce qu'il faut comprendre
- Réponses courtes : 1 à 2 phrases, puis on s'arrête.
- Le fichier QUESTIONS_REPONSES_SOUTENANCE.md contient beaucoup d'autres réponses de secours.

### Si le prof demande
- **« Et si on ne connaît pas la réponse ? »**  
  → Le dire honnêtement, puis expliquer comment on vérifierait (par exemple dans le notebook).

## Slide 21 – Commandes de lancement

**INTERVENANT :** TOUS (celui dont c'est la partie)  ·  **TEMPS CIBLE :** hors présentation · slide de secours

### Ce qu'on dit
> Slide de secours si le professeur demande comment lancer le projet.
>
> En local : pip install -r requirements.txt installe Flask, pandas, scikit-learn et joblib, puis python app.py lance l'application sur le port 5000. On peut le faire dans un environnement virtuel (python -m venv .venv, puis .venv\Scripts\activate sur Windows).
>
> Avec Docker : docker build construit l'image à partir du Dockerfile et l'appelle apartment-hunter ; docker run lance un conteneur, -p 5000:5000 relie le port de l'ordinateur à celui du conteneur, et --rm supprime le conteneur quand on l'arrête.
>
> Le notebook a été conçu pour Google Colab : on crée un dossier data, on y dépose le CSV, et on exécute tout. Il recrée model.pkl et les graphiques.

### Ce qu'il faut comprendre
- Docker Desktop doit être ouvert pour utiliser les commandes docker.
- Dans tous les cas, l'application s'ouvre sur http://localhost:5000.

### Si le prof demande
- **« Pourquoi -p 5000:5000 ? »**  
  → Pour relier le port 5000 de l'ordinateur au port 5000 du conteneur, sinon on ne peut pas ouvrir l'application.
- **« Pourquoi host="0.0.0.0" dans app.py ? »**  
  → Pour que l'application accepte les connexions venant de l'extérieur du conteneur.
