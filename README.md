# Projet Capstone  
## Prédiction des Prix Immobiliers en Mauritanie

Ce projet vise à construire une solution complète de Data Science permettant de prédire les prix de l’immobilier en Mauritanie, depuis la collecte de données réelles jusqu’au déploiement d’une application web interactive.

Le projet couvre l’ensemble du pipeline data : web scraping, enrichissement géographique, analyse exploratoire des données (EDA), modélisation en machine learning et intégration dans une application web.

---

## Présentation générale

Ce projet est réalisé dans le cadre du **Cours de Machine Learning – Master 1** à **SupNum (Institut Supérieur du Numérique)**.

Il a pour objectif de concevoir un outil intelligent capable d’estimer le prix d’un bien immobilier à Nouakchott et Nouadhibou à partir de caractéristiques réelles du marché.

- Durée : 4 à 6 semaines  
- Encadrant : Mohamed  
- Année académique : 2025 – 2026  

---

## Problématique

Le marché immobilier mauritanien souffre d’un manque de transparence et de structuration des données :

- Absence de base de données publique fiable  
- Annonces dispersées sur plusieurs plateformes  
- Prix négociés de manière informelle  
- Aucun outil de référence pour l’estimation des biens  

L’objectif de ce projet est donc de créer un modèle de prédiction des prix immobiliers destiné aux particuliers, agences immobilières, investisseurs et analystes du marché.

---

## Objectifs pédagogiques et intérêts du projet

Ce projet permet de :

- Mettre en pratique les compétences clés en Data Science  
- Travailler sur des données réelles, bruitées et imparfaites  
- Comprendre l’ensemble du cycle de vie d’un projet data  
- Construire un projet valorisable sur un CV ou un portfolio  

Les compétences mobilisées incluent :

- Web Scraping  
- Nettoyage et préparation des données  
- Analyse Exploratoire des Données (EDA)  
- Feature Engineering  
- Modélisation Machine Learning  
- Développement d’API backend  
- Développement frontend avec Next.js  
- Travail collaboratif avec Git et GitHub  

---

## Architecture globale du projet

Le projet est structuré en cinq grandes phases successives :

Scraping → Enrichissement géographique → EDA → Modélisation → Application Web

Chaque phase alimente la suivante afin de garantir une cohérence complète du pipeline data.

---

## Détail des phases du projet

### Phase 1 – Web Scraping et collecte des données

Cette phase consiste à collecter des annonces immobilières réelles depuis plusieurs plateformes mauritaniennes.

Les informations extraites incluent notamment le type de bien, le prix, la surface, le nombre de chambres, le quartier, la ville, la description et la date de publication.

Les règles éthiques du scraping sont respectées, incluant les pauses entre requêtes et le respect du fichier robots.txt.

Livrable principal : données brutes issues du scraping.

---

### Phase 2 – Enrichissement géographique

L’objectif est d’ajouter une dimension spatiale aux données immobilières.

Les quartiers sont géocodés afin d’obtenir leurs coordonnées géographiques. Des distances vers des points clés (centre-ville, aéroport, plage) sont calculées, et des points d’intérêt sont intégrés pour enrichir l’analyse.

Livrable principal : dataset enrichi géographiquement.

---

### Phase 3 – Analyse Exploratoire des Données (EDA)

Cette phase vise à comprendre la structure et la qualité des données avant la modélisation.

Elle inclut l’analyse des distributions, le traitement des valeurs manquantes, la détection et la gestion des outliers, ainsi que des analyses univariées, bivariées et multivariées accompagnées de visualisations.

Livrable principal : notebook d’EDA complet.

---

### Phase 4 – Feature Engineering et Modélisation

Des variables pertinentes sont créées afin d’améliorer la performance des modèles, telles que le prix au mètre carré ou la transformation logarithmique du prix.

Plusieurs modèles de machine learning sont testés et comparés à l’aide de métriques standards (RMSE, MAE, R²). Le meilleur modèle est sélectionné et sauvegardé.

Livrable principal : modèle de prédiction entraîné et sauvegardé.

---

### Phase 5 – API et Application Web

Le modèle est exposé via une API backend développée avec Flask ou FastAPI.

Une application frontend développée avec Next.js permet aux utilisateurs de saisir les caractéristiques d’un bien et d’obtenir une estimation du prix de manière interactive.

Livrable principal : application web fonctionnelle.

---

## Conclusion

Ce projet constitue une expérience complète et réaliste de Data Science appliquée, avec un fort impact local pour la Mauritanie.

Il illustre la capacité de l’équipe à travailler sur des données réelles, à collaborer efficacement et à transformer une problématique concrète en une solution technologique opérationnelle.
