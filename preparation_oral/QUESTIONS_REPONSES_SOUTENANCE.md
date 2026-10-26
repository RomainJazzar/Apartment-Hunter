# QUESTIONS / RÉPONSES – SOUTENANCE APARTMENT HUNTER

Réponses courtes de secours (1 à 2 phrases). La colonne « Qui » indique qui répond en priorité, mais **tout le monde** doit connaître les questions marquées ★ (les plus probables).

Si le prof insiste, une piste pour aller un peu plus loin est donnée après « ↳ ».

---

## 1. Projet et organisation (Romain)

**★ Q : En une phrase, que fait votre projet ?**
R : Il estime le prix d'une maison à partir de 8 caractéristiques, grâce à une Random Forest utilisée dans une application Flask.

**★ Q : Quelle est votre problématique, et quelle est la réponse ?**
R : « Peut-on estimer le prix d'une maison à partir de ses caractéristiques ? » Oui : le modèle explique environ 87,7 % de la variation des prix sur des maisons jamais vues, avec environ 72 000 $ d'erreur moyenne.

**Q : Comment vous êtes-vous répartis le travail ?**
R : Romain sur les données, le nettoyage et l'analyse exploratoire ; Yannis sur la sélection des variables et les modèles ; Lisa sur le Grid Search, le modèle final, Flask et Docker. La mise en place et la documentation ont été faites ensemble.

**Q : À quoi sert le Trello ?**
R : À suivre l'avancement en Kanban : chaque tâche est une carte qui passe de « À faire » à « En cours » puis « Terminé ».

**Q : Quelles ressources matérielles avez-vous utilisées ?**
R : Nos ordinateurs portables, Google Colab, GitHub, Trello et Docker Desktop. Pas besoin de GPU : tout s'entraîne en quelques minutes.

**Q : Pourquoi pas Power BI ?**
R : On n'y avait pas accès. On a fait la même analyse avec matplotlib dans le notebook et on l'a regroupée dans `dashboard.html`, consultable dans un navigateur.

---

## 2. Données et nettoyage (Romain)

**★ Q : Pourquoi King County et pas Madrid ?**
R : Moins de colonnes, pas de texte libre et des variables bien documentées : plus simple à nettoyer et à expliquer.

**Q : Combien de données au départ et à la fin ?**
R : 21 613 lignes et 21 colonnes au départ ; 21 596 lignes et 16 colonnes après nettoyage.

**Q : Y avait-il des valeurs manquantes ou des doublons ?**
R : Aucune valeur manquante et aucune ligne en double. 177 maisons apparaissent deux fois, mais à des dates différentes : ce sont de vraies reventes, on les a gardées.

**★ Q : Pourquoi supprimer `id` ?**
R : C'est un identifiant : le numéro d'une vente n'explique pas son prix.

**★ Q : Pourquoi supprimer la date ?**
R : Les ventes ne couvrent qu'environ 13 mois (2 mai 2014 → 27 mai 2015), et on a choisi de ne pas étudier l'effet du temps pour garder le projet simple.
↳ Pour l'utiliser, il aurait fallu transformer le texte en mois ou en année : c'est une piste d'amélioration.

**★ Q : Pourquoi ne pas utiliser le code postal ?**
R : C'est un code, pas une quantité (98178 n'est pas « plus » que 98125). La latitude et la longitude donnent déjà la position avec de vrais nombres.
↳ Pour l'utiliser correctement, il aurait fallu un encodage spécial (une colonne par code postal, soit 70 colonnes).

**Q : Pourquoi supprimer `sqft_above` et `sqft_basement` ?**
R : On a vérifié que leur somme est exactement égale à `sqft_living` pour toutes les maisons : c'était de l'information en double.

**★ Q : Pourquoi ne pas avoir supprimé les maisons très chères ?**
R : Ce sont des maisons de luxe réelles, pas des erreurs ; les 5 plus chères font entre 8 000 et 12 000 pieds² avec un grade de 11 à 13.
↳ La méthode IQR en trouve 1 145 (5,3 %) : les supprimer empêcherait le modèle d'estimer les grandes maisons.

**Q : Alors qu'est-ce que vous avez supprimé ?**
R : 17 lignes impossibles : une maison à 33 chambres pour 1 620 pieds² (sûrement 3 chambres) et 16 maisons sans chambre ou sans salle de bain.

**Q : C'est quoi la méthode IQR ?**
R : On calcule l'écart entre le 1er et le 3ᵉ quartile du prix ; tout ce qui dépasse 3ᵉ quartile + 1,5 × cet écart est considéré comme une valeur extrême (ici ≈ 1,13 M$).

**Q : Pourquoi pas de normalisation ou de standardisation ?**
R : Les arbres découpent avec des seuils, donc l'échelle ne change rien ; pour la régression linéaire, ça change les coefficients mais pas les prédictions.

**Q : Que montrent vos graphiques ?**
R : Le prix dépend surtout de la surface (corrélation 0,70), de la qualité de construction et de l'emplacement.

**Q : Pourquoi la surface est en pieds² ?**
R : Ce sont des données américaines ; on a gardé l'unité d'origine (1 m² ≈ 10,76 pieds²) et l'application l'indique.

---

## 3. Variables et préparation (Yannis)

**★ Q : Pourquoi seulement 8 variables ?**
R : On a la même précision qu'avec les 15 (R² 0,855 contre 0,856), avec un modèle plus simple et un formulaire plus court.

**★ Q : Quelles sont les 8 variables ?**
R : Surface habitable, qualité de construction (grade), latitude, longitude, vue sur l'eau, surface du terrain, nombre de chambres et année de rénovation.

**Q : Pourquoi deux méthodes de sélection ?**
R : La corrélation ne voit que les liens en ligne droite et regarde chaque variable seule ; la sélection forward regarde ce qu'une variable apporte en plus des autres.

**★ Q : C'est quoi la sélection forward ?**
R : On commence avec aucune variable, puis on ajoute à chaque étape celle qui améliore le plus le modèle, jusqu'à en avoir 8.

**Q : Quel modèle avez-vous utilisé dans la sélection forward ?**
R : Un arbre de décision limité à 10 niveaux : il est rapide et il voit les relations qui ne sont pas en ligne droite, comme l'effet de la position.

**★ Q : Pourquoi garder la longitude alors que sa corrélation est de 0,02 ?**
R : L'emplacement compte beaucoup (on le voit sur la carte), mais pas en ligne droite ; la sélection forward l'a gardée et c'est le 4ᵉ facteur du modèle final.

**Q : Pourquoi `bathrooms` n'est pas gardée ?**
R : Elle est très liée à la surface (corrélation 0,76) : une fois la surface connue, elle n'apporte presque rien de plus.

**Q : `bedrooms` et `yr_renovated` servent très peu dans le modèle final, pourquoi les garder ?**
R : Elles ont été choisies par la sélection, et le nombre de chambres est une information naturelle à demander ; leur importance est faible (0,006 et 0,003) mais elles ne gênent pas.

**Q : Pourquoi pas Boruta ?**
R : C'était un exemple du sujet ; deux méthodes plus simples suffisaient et donnaient la même précision qu'avec toutes les variables.

**★ Q : Pourquoi séparer train et test ?**
R : Pour vérifier le modèle sur des maisons qu'il n'a jamais vues : 80 % (17 276) pour apprendre, 20 % (4 320) pour le test final.

**Q : Pourquoi `random_state=42` ?**
R : Pour que le découpage et les modèles donnent toujours le même résultat à chaque exécution ; 42 est juste une valeur fixe classique.

**Q : Pourquoi la sélection seulement sur le train ?**
R : Pour que le test reste complètement nouveau : si on choisissait les variables en regardant le test, le score final serait trop optimiste.

---

## 4. Modèles et métriques (Yannis)

**★ Q : Pourquoi ces 3 modèles ?**
R : Ce sont trois idées différentes et faciles à expliquer : une formule, une suite de questions, et la moyenne de beaucoup d'arbres.

**★ Q : Pourquoi la Random Forest ?**
R : Elle donnait les meilleurs résultats en validation croisée et représente mieux les relations complexes qu'une régression linéaire, tout en limitant les faiblesses d'un arbre seul.

**Q : Pourquoi la régression linéaire est-elle moins bonne ?**
R : Elle ne fait que des lignes droites, alors que l'effet de l'emplacement n'est pas linéaire (R² 0,652).

**★ Q : C'est quoi le surapprentissage ?**
R : Le modèle apprend par cœur : l'arbre seul fait 0,999 sur les maisons apprises mais seulement 0,740 sur les autres.

**Q : Comment la Random Forest limite le surapprentissage ?**
R : Chaque arbre est entraîné sur un tirage différent des maisons ; en faisant la moyenne de leurs prix, leurs erreurs se compensent.

**Q : Les arbres de la Random Forest votent ?**
R : Non, en régression ils donnent chacun un prix et on fait la moyenne ; le vote, c'est pour la classification.

**★ Q : C'est quoi la validation croisée ?**
R : On coupe le train en 3 parts, on entraîne sur 2 et on mesure sur la 3ᵉ, trois fois, puis on fait la moyenne : ça permet de comparer sans utiliser le test.

**Q : Pourquoi 3 parts et pas 5 ?**
R : Pour que le Grid Search reste rapide sur Colab ; avec plus de 17 000 maisons, chaque part reste assez grande.

**★ Q : Que veut dire MAE ?**
R : L'erreur moyenne en dollars : notre modèle se trompe en moyenne de 71 718 $ sur le test.

**Q : Que veut dire RMSE, et pourquoi il est plus grand que le MAE ?**
R : C'est une erreur en dollars où les grosses erreurs comptent plus ; il est plus grand (126 924 $) parce qu'il y a quelques grosses erreurs.

**★ Q : Que veut dire R² = 0,877 ?**
R : Le modèle explique environ 87,7 % de la variation des prix dans le jeu de test.
↳ Attention : ça ne veut **pas** dire que 87,7 % des prix sont justes.

**★ Q : Comment avez-vous choisi le modèle sans tricher ?**
R : Tous les choix par validation croisée sur le train ; le test n'a servi qu'une seule fois, à la fin, sur le modèle déjà choisi.

---

## 5. Grid Search et modèle final (Lisa)

**★ Q : C'est quoi Grid Search ?**
R : Une méthode qui teste automatiquement plusieurs réglages d'un modèle et garde le meilleur ; ce n'est pas un modèle de prédiction.

**Q : Quels paramètres avez-vous testés ?**
R : Le nombre d'arbres (100, 200), la profondeur maximale (10, 15, sans limite) et `min_samples_split` (2, 10) : 12 combinaisons, chacune en validation croisée à 3 parts.

**Q : Quel est le meilleur réglage ?**
R : 200 arbres, profondeur maximale de 15, `min_samples_split` = 2.

**Q : C'est quoi `min_samples_split` ?**
R : Le nombre minimum de maisons qu'il faut dans un groupe pour pouvoir encore le couper en deux.

**★ Q : Pourquoi le Grid Search a si peu amélioré le modèle ?**
R : Les réglages par défaut étaient déjà bons : on gagne seulement environ 500 $ d'erreur moyenne en validation croisée.

**Q : Pourquoi une si petite grille ?**
R : 12 combinaisons suffisent pour appliquer la méthode, et une grille plus grande prendrait beaucoup plus de temps pour un gain probablement très faible.

**★ Q : Pourquoi le test (0,877) est meilleur que la validation croisée (0,856) ?**
R : En validation croisée chaque modèle n'apprend que sur 2/3 du train, alors que le modèle final apprend sur tout le train ; l'important, c'est que les deux scores sont proches.

**Q : 72 000 $ d'erreur, ce n'est pas beaucoup ?**
R : C'est environ 16 % du prix médian (450 000 $) : correct pour une première estimation, mais ce n'est pas un prix exact.

**Q : Le modèle marche pour une maison à Paris ?**
R : Non : il a appris uniquement sur des ventes de 2014-2015 dans la région de Seattle.

**Q : Quelles sont les limites du projet ?**
R : Données anciennes et d'une seule région, quelques grosses erreurs, et l'utilisateur doit connaître la latitude et la longitude.

---

## 6. Sauvegarde, Flask et Docker (Lisa)

**★ Q : Pourquoi `model.pkl` ?**
R : Pour sauvegarder le modèle déjà entraîné et éviter de le réentraîner à chaque lancement de l'application.

**Q : Pourquoi joblib ?**
R : C'est l'outil présenté dans la documentation de scikit-learn pour enregistrer et recharger un modèle, et il gère bien les gros modèles.

**Q : Pourquoi `compress=3` ?**
R : Pour que le fichier fasse 26,3 Mo et reste sous la limite de 100 Mo par fichier de GitHub.

**★ Q : Pourquoi Flask ?**
R : Pour rendre le modèle utilisable depuis une interface web simple.

**★ Q : Que se passe-t-il quand on clique sur « Estimer » ?**
R : Flask récupère les 8 valeurs du formulaire, les met dans un DataFrame pandas, les donne à la Random Forest déjà chargée et renvoie le prix dans la page.

**Q : Le modèle est chargé à chaque clic ?**
R : Non, une seule fois au démarrage de `app.py` ; à chaque clic, on appelle seulement `predict`.

**Q : Pourquoi un DataFrame et pas une simple liste ?**
R : Le modèle a été entraîné avec un tableau pandas : on lui redonne les 8 colonnes avec les mêmes noms et dans le même ordre.

**Q : C'est une API ?**
R : Non, c'est une page web avec un formulaire ; on n'a pas fait d'API.

**★ Q : Pourquoi Docker ?**
R : Pour fournir la même application avec le même environnement et les mêmes librairies sur n'importe quelle machine.

**★ Q : Flask et Docker, c'est la même chose ?**
R : Non : Flask fait fonctionner l'application, Docker transporte et exécute tout son environnement (Python, librairies, fichiers).

**Q : Que fait le Dockerfile ?**
R : Il part de Python 3.12, installe les librairies de `requirements.txt`, copie l'application et le modèle, ouvre le port 5000 et lance `python app.py`.

**Q : Que veut dire `-p 5000:5000` ?**
R : Ça relie le port 5000 de l'ordinateur au port 5000 du conteneur, pour ouvrir l'application sur `http://localhost:5000`.

**Q : Pourquoi `host="0.0.0.0"` dans `app.py` ?**
R : Pour que l'application accepte les connexions venant de l'extérieur du conteneur ; sinon elle ne serait visible que depuis l'intérieur.

**Q : Pourquoi fixer les versions dans `requirements.txt` ?**
R : Un modèle sauvegardé avec une version de scikit-learn peut mal se recharger avec une autre : on fixe la version 1.8.0 utilisée pour créer `model.pkl`.

---

## 7. Questions pièges

**Q : Si vous deviez améliorer le projet, vous feriez quoi en premier ?**
R : Des données plus récentes et l'effet de la date ; puis une saisie d'adresse au lieu des coordonnées dans l'application.

**Q : Pourquoi ne pas avoir essayé des modèles plus puissants (XGBoost, réseaux de neurones) ?**
R : On voulait des modèles qu'on comprend et qu'on peut expliquer ; la Random Forest donnait déjà de bons résultats. Le gradient boosting est une piste d'amélioration.

**Q : Votre modèle peut-il prédire un prix négatif ou absurde ?**
R : Une Random Forest fait la moyenne de prix réels vus pendant l'apprentissage, donc elle reste dans la plage des prix connus ; par contre elle ne sait pas bien extrapoler au-delà.

**Q : Qu'est-ce qui se passe si on entre une maison hors de la région ?**
R : Le formulaire limite la latitude et la longitude à la zone du comté de King ; en dehors, le modèle n'aurait de toute façon aucun exemple pour apprendre.
