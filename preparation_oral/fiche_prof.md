# FICHE POUR EXPLIQUER LE PROJET AU PROF

## Les notions de base

**La régression**
Prédire un **nombre** (ici un prix) à partir d'autres informations. Si on prédisait une catégorie (par exemple « cher » / « pas cher »), ce serait de la classification.

**Une feature (variable explicative)**
Une information qu'on donne au modèle pour qu'il fasse sa prédiction : la surface, le nombre de chambres, le grade… On en a gardé 8.

**La target (la cible)**
Ce qu'on veut prédire : `price`.

**Pourquoi séparer train et test ?**
Le train (80 %) sert à apprendre **et à faire tous les choix** (variables, modèle, paramètres). Le test (20 %) sert une seule fois, à la fin, à vérifier le modèle final sur des maisons qu'il n'a jamais vues. Si on testait sur les maisons apprises, ou si on choisissait le modèle en regardant le test, le score serait trop beau, comme un élève qui révise avec les réponses de l'examen.

**Le surapprentissage (overfitting)**
Le modèle apprend les données d'entraînement par cœur au lieu de comprendre la tendance générale. Il est très bon sur les maisons qu'il a apprises et beaucoup moins bon sur les autres.
Dans le projet : l'arbre de décision a un R² de 0,999 sur les maisons apprises, mais seulement 0,740 en validation croisée.

**La validation croisée**
On coupe le train en 3 parts. On entraîne sur 2 parts et on teste sur la 3ᵉ, trois fois de suite, puis on fait la moyenne. Ça permet de comparer des choix (variables, modèles, paramètres) sans toucher au jeu de test. Dans le projet, c'est comme ça qu'on a comparé les 3 modèles et fait le Grid Search.

## Les mesures

**MAE (erreur absolue moyenne)**
En moyenne, de combien de dollars le modèle se trompe. Notre modèle final : 71 718 $.

**RMSE (racine de l'erreur quadratique moyenne)**
Aussi en dollars, mais on met les erreurs au carré avant de faire la moyenne, donc les grosses erreurs comptent beaucoup plus. Notre modèle : 126 924 $. Il est bien plus grand que le MAE, ce qui veut dire qu'il y a quelques grosses erreurs (souvent sur les maisons de luxe).

**R²**
La part des variations du prix que le modèle explique. 1 = parfait, 0 = pas mieux que de donner le prix moyen à toutes les maisons. Notre modèle : 0,877, donc il explique environ 88 % des variations.

## Les modèles

**Régression linéaire**
Elle cherche la meilleure formule du type « prix = a × surface + b × grade + … + constante ». Elle choisit les coefficients qui font les plus petites erreurs. Elle est simple mais ne voit que les relations en ligne droite. Ici : R² de 0,652 en validation croisée.

**Arbre de décision**
Il pose des questions oui/non (« surface > 2 500 ? », « grade > 7 ? ») pour séparer les maisons en groupes de prix proches. Le prix prédit est la moyenne des prix du groupe. Facile à comprendre, mais sans limite il apprend par cœur. Ici : R² de 0,740 en validation croisée.

**Forêt aléatoire (Random Forest)**
Beaucoup d'arbres (100, puis 200 après Grid Search). Chaque arbre est entraîné sur un tirage au hasard des maisons, donc ils sont tous un peu différents. On fait la moyenne de leurs prédictions : les erreurs se compensent. Ici : R² de 0,855 en validation croisée (0,856 après Grid Search), puis 0,877 sur le test à la fin.

## Les méthodes

**La sélection de variables (feature selection)**
Garder seulement les variables utiles. Le modèle est plus simple, plus rapide, et le formulaire de l'application plus court. On avait 15 variables, on en garde 8 avec la même précision (R² de 0,855 contre 0,856).

**La corrélation**
Un nombre entre -1 et 1 qui mesure si deux variables évoluent ensemble « en ligne droite ». Limite : elle ne voit pas les liens plus compliqués (la longitude a 0,02 de corrélation alors que l'emplacement compte beaucoup).

**La sélection forward**
On commence avec aucune variable, puis on ajoute à chaque étape celle qui améliore le plus le modèle, jusqu'à en avoir 8. Elle regarde ce qu'une variable apporte en plus de celles déjà choisies, donc elle évite les variables qui disent la même chose.

**Grid Search**
On donne une liste de valeurs pour quelques paramètres. Grid Search teste toutes les combinaisons (ici 2 × 3 × 2 = 12) avec une validation croisée, et garde la meilleure. Résultat : 200 arbres, profondeur max 15. Très petit gain en validation croisée : R² de 0,855 → 0,856, et MAE de 74 266 $ → 73 764 $.

## Les outils

**joblib**
Enregistre le modèle entraîné dans un fichier (`model.pkl`). L'application le recharge sans avoir à réentraîner. On a utilisé `compress=3` pour que le fichier fasse 26 Mo au lieu de beaucoup plus (limite GitHub : 100 Mo).

**Flask**
Une petite librairie Python pour faire des sites web. Notre `app.py` a une seule page : elle affiche le formulaire, et quand on clique sur Estimer, elle récupère les valeurs, appelle `model.predict()` et affiche le prix.

**Docker**
Permet de mettre l'application et toutes ses librairies dans un « conteneur », pour qu'elle fonctionne de la même manière sur n'importe quel ordinateur. Le Dockerfile dit : pars de Python 3.12, installe les librairies, copie les fichiers, lance `python app.py`.

---

# QUESTIONS QUE LE PROF PEUT ME POSER

**Q : Pourquoi avoir choisi King County et pas Madrid ?**
R : Moins de colonnes, pas de texte libre à traiter, et des variables bien documentées. C'était plus simple à nettoyer et à expliquer.

**Q : Pourquoi avoir supprimé `id` ?**
R : C'est juste un identifiant. Le numéro de la maison n'explique pas son prix.

**Q : Pourquoi avoir supprimé la date ?**
R : Les ventes ne couvrent qu'environ 13 mois (du 2 mai 2014 au 27 mai 2015). Il aurait fallu transformer le texte de la date en mois ou en année, et étudier l'effet du temps sur le prix. J'ai choisi de ne pas le faire pour garder le projet simple. C'est une piste d'amélioration.

**Q : Pourquoi ne pas avoir utilisé le code postal ?**
R : C'est un code, pas une quantité : 98178 n'est pas « plus » que 98125. Il aurait fallu un encodage spécial. La latitude et la longitude donnent déjà la position, et ce sont de vrais nombres.

**Q : Pourquoi ne pas avoir supprimé les maisons très chères ?**
R : Ce ne sont pas des erreurs, ce sont des maisons de luxe qui existent. Les 5 plus chères font entre 8 000 et 12 000 pieds² avec un grade de 11 à 13, donc leur prix est logique. Si on les enlevait (5 % des données), le modèle ne saurait plus estimer les grandes maisons.

**Q : Alors pourquoi avoir supprimé certaines lignes ?**
R : Seulement les erreurs évidentes : une maison de 33 chambres pour 150 m², et 16 maisons sans chambre ou sans salle de bain, dont une de 4 800 pieds² à 1,3 million. Ça fait 17 lignes sur 21 613.

**Q : Pourquoi ne pas avoir normalisé les données ?**
R : Les arbres et la forêt aléatoire découpent avec des seuils, donc l'échelle ne change rien. Pour la régression linéaire, ça change les coefficients mais pas les prédictions. Et ça garde l'application simple : on donne directement les valeurs tapées.

**Q : Pourquoi la longitude est gardée alors que sa corrélation est de 0,02 ?**
R : La corrélation ne voit que les liens en ligne droite. Sur la carte, on voit clairement des zones chères et d'autres moins chères, mais ce n'est pas « plus on va à l'est, plus c'est cher ». La sélection forward, qui utilise un arbre, l'a gardée. D'ailleurs, dans le modèle final, la position (latitude + longitude) est le 3ᵉ facteur le plus important.

**Q : Pourquoi `bathrooms` n'est pas dans les variables finales alors qu'elle est corrélée au prix ?**
R : Elle est très liée à la surface (corrélation de 0,76). Une fois qu'on a la surface, le nombre de salles de bain n'apporte presque rien de plus. La sélection forward l'a donc laissée de côté.

**Q : Pourquoi faire la sélection de variables seulement sur le train ?**
R : Pour que le jeu de test reste complètement « nouveau ». Si on choisissait les variables en regardant le test, le score final serait un peu trop optimiste. C'est la même règle pour le choix du modèle et le Grid Search : tout se fait sur le train.

**Q : Pourquoi avoir choisi la forêt aléatoire ?**
R : C'est la meilleure sur les trois mesures en validation croisée. Elle peut représenter des relations plus compliquées qu'une régression linéaire, comme l'effet de l'emplacement, et elle limite le surapprentissage d'un arbre seul en faisant la moyenne de beaucoup d'arbres.

**Q : Pourquoi la régression linéaire est-elle si moins bonne ?**
R : Elle ne peut faire qu'une formule en ligne droite. Or le prix dépend de la position de façon compliquée (des quartiers chers au milieu de la carte), ce qu'une formule linéaire ne peut pas représenter.

**Q : Le Grid Search a très peu amélioré le modèle, pourquoi ?**
R : Les paramètres par défaut de la forêt aléatoire sont déjà bons : on gagne seulement environ 500 $ d'erreur moyenne en validation croisée. La grille était volontairement petite (12 combinaisons) pour que ça tourne vite. Le but était surtout d'appliquer la méthode.

**Q : 72 000 $ d'erreur, ce n'est pas beaucoup ?**
R : Ça fait environ 16 % du prix médian. C'est correct pour une première estimation, mais ce n'est pas un prix exact. L'agent garde son rôle : visiter, regarder l'état de la maison, etc. Et certaines erreurs sont beaucoup plus grandes que la moyenne : c'est pour ça que le RMSE (126 924 $) est bien plus grand que le MAE.

**Q : Comment as-tu choisi le modèle sans tricher avec le jeu de test ?**
R : Tous les choix ont été faits par validation croisée sur le train : la comparaison des 3 modèles et le Grid Search. Le meilleur R² en validation croisée était la forêt optimisée (0,856). Ensuite seulement, je l'ai évaluée une seule fois sur le test.

**Q : Pourquoi le score sur le test (0,877) est meilleur qu'en validation croisée (0,856) ?**
R : En validation croisée, chaque modèle n'apprend que sur 2/3 du train. Le modèle final, lui, apprend sur tout le train, donc avec plus d'exemples. L'important, c'est que les deux scores sont proches : il n'y a pas de mauvaise surprise sur des maisons nouvelles.

**Q : Est-ce que ton modèle marcherait pour une maison à Paris ?**
R : Non. Il a appris uniquement sur des ventes de 2014-2015 dans la région de Seattle. Pour Paris, il faudrait réentraîner sur des données françaises.

**Q : Comment l'application fait une prédiction ?**
R : Au démarrage, elle charge `model.pkl`. Quand on envoie le formulaire, elle convertit les 8 valeurs en nombres, les met dans un tableau d'une ligne dans le même ordre que pendant l'entraînement, et appelle `model.predict()`.

**Q : À quoi sert Docker ici ?**
R : À ce que l'application marche partout de la même façon. Le conteneur contient Python, les bonnes versions des librairies et les fichiers du projet. N'importe qui peut la lancer avec `docker build` puis `docker run`, sans rien installer à part Docker.

**Q : Pourquoi tu n'as pas utilisé Power BI ?**
R : Je n'y avais pas accès. J'ai fait la même analyse avec matplotlib dans le notebook, et j'ai regroupé les graphiques dans `dashboard.html` pour avoir une version consultable.

**Q : Pourquoi tu n'as pas utilisé Boruta ?**
R : Le sujet demandait plusieurs méthodes, Boruta était un exemple. J'ai pris la corrélation et la sélection forward, qui sont plus simples à expliquer et qui suffisaient : avec 8 variables, j'ai la même précision qu'avec toutes.
