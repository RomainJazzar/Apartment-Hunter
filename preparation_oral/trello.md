# Tableau Trello – Apartment Hunter

Nom du tableau : **Apartment Hunter**

Créer 3 listes : **À FAIRE** | **EN COURS** | **TERMINÉ**

Le projet est terminé, donc à la fin toutes les cartes sont dans **TERMINÉ**.
Pour la présentation, c'est plus parlant de faire une capture d'écran à mi-parcours (quelques cartes dans chaque colonne), puis une capture finale.

Pour chaque carte : le titre, une description courte, une date d'échéance si tu veux, et une étiquette de couleur par type (Données / Modèle / Application / Documentation).

| # | Titre de la carte | Description | Étiquette | Durée |
|---|---|---|---|---|
| 1 | Mise en place du projet | Lire le sujet, choisir le dataset (King County), créer le repo GitHub `Apartment-Hunter` et le Trello | Documentation | 0,5 j |
| 2 | Comprendre les données | Charger le CSV dans Colab, lire la description des variables, `head` / `info` / `describe` | Données | 0,5 j |
| 3 | Nettoyage des données | Valeurs manquantes, doublons, colonnes inutiles, valeurs incohérentes, outliers du prix | Données | 0,5 j |
| 4 | Analyse exploratoire | 7 graphiques dans le notebook + `dashboard.html` (remplace Power BI) | Données | 0,5 j |
| 5 | Sélection des variables | Corrélation + sélection forward, choisir la liste finale | Modèle | 0,5 j |
| 6 | Entraîner et comparer 3 modèles | Régression linéaire, arbre de décision, forêt aléatoire. Tableau MAE / RMSE / R² en validation croisée sur le train | Modèle | 1 j |
| 7 | Grid Search + modèle final | GridSearchCV sur la forêt aléatoire, comparaison avant/après, évaluation unique sur le test, sauvegarde `model.pkl` | Modèle | 0,5 j |
| 8 | Application Flask | `app.py`, formulaire HTML, CSS, test d'une prédiction | Application | 1 j |
| 9 | Docker | `Dockerfile` + `requirements.txt`, test du conteneur | Application | 0,5 j |
| 10 | README et veille | README complet : contexte, données, algorithmes avec schémas, résultats, conclusion, veille | Documentation | 0,5 j |
| 11 | Présentation | Slides + entraînement à l'oral | Documentation | 0,5 j |

Membres assignés (même répartition que dans les slides) :
- **Romain** : cartes 3, 4 (nettoyage, analyse exploratoire)
- **Yannis** : cartes 5, 6 (sélection des variables, modèles)
- **Lisa** : cartes 7, 8, 9 (Grid Search, modèle final, Flask, Docker)
- **Équipe** : cartes 1, 2, 10, 11 (mise en place, compréhension des données, README, présentation)
