# ⚽ Football Predictive Analytics Platform (Premier League 2024–2025)

## 🚀 Contexte du projet

Ce projet innovant vise à **développer une solution complète d’analyse prédictive pour le football professionnel**.  
En exploitant les **données massives** issues du site *FBref*, notre objectif est de construire un **écosystème data-driven** capable :
- d’anticiper les résultats des matchs,  
- d’optimiser les stratégies sportives des équipes,  
- et d’offrir des visualisations interactives via un **dashboard Streamlit**.

---

## 🧩 Architecture générale du projet

Le projet s’articule autour de quatre grandes étapes :

1. **Collecte des données (Web Scraping)**
2. **Transformation et nettoyage des données**
3. **Stockage et modélisation (PostgreSQL)**
4. **Analyse et visualisation (SQL + Streamlit)**

---

## 🕸️ 1. Web Scraping

**Objectif :** Collecter les données de football à partir du site [FBref](https://fbref.com) pour la **Premier League 2024–2025**.

**Technologies utilisées :**
- `Python`
- `Selenium`
- `pandas`

**Étapes principales :**
- Extraction des informations sur les équipes participantes.
- Récupération des données détaillées sur les joueurs : nom, poste, nationalité, etc.
- Collecte des statistiques des matchs (buts, passes décisives, cartons, etc.).
- Exportation des données structurées au format **CSV** pour l’étape suivante.

---

## 🧹 2. Transformation des données

**Objectif :** Garantir la qualité, la cohérence et l’homogénéité des données avant leur intégration.

**Étapes de transformation :**
- 🔍 **Nettoyage (Bronze)** : suppression ou imputation des valeurs manquantes / incohérentes.  
- ⚙️ **Standardisation (Silver)** : uniformisation des formats de date, unités, noms de colonnes, etc.  
- 💾 **Structuration (Gold)** : préparation des fichiers CSV conformes au modèle de base de données.

---

## 🏗️ 3. Modélisation et stockage des données

Les données sont ensuite intégrées dans une **base de données relationnelle PostgreSQL**.  
Le modèle est conçu selon une approche **conceptuelle et logique UML**.

### 📘 Modèle relationnel

Un **diagramme UML** accompagne la conception pour visualiser les relations entre entités.

---

## 📊 4. Analyse des données

**Objectif :** Explorer et extraire les indicateurs clés de performance à l’aide de requêtes SQL.

### Analyses principales :
- 🥇 **Top 10 des meilleurs buteurs**
- 🎯 **Joueurs les plus décisifs** (buts + passes)
- 🟥 **Joueurs les plus disciplinés** (cartons)
- 🌍 **Répartition des nationalités par équipe**
- ⚡ **Nombre total de buts par équipe**
- ⚖️ **Moyenne de buts marqués et encaissés par match**
- 🏆 **Classement des équipes (3 pts victoire, 1 pt nul)**
- 🧱 **Meilleure défense (buts concédés)**
- 👟 **Meilleur buteur par équipe**
- 📅 **Nombre total de matchs joués par équipe**

---

## 📈 5. Dashboard interactif (Streamlit)

**Objectif :** Fournir une interface interactive pour visualiser les analyses et interagir avec les données.

**Technologies :**
- `Python`
- `Streamlit`
- `SQLAlchemy`
- `Plotly / Matplotlib`
- `pandas`

### Fonctionnalités :
- Connexion à la base de données via SQLAlchemy  
- Exécution dynamique de requêtes SQL  
- Visualisations interactives (graphiques et tableaux)  
- Filtres pour sélectionner la saison, l’équipe ou le joueur  
- Téléchargement des données filtrées au format **CSV**