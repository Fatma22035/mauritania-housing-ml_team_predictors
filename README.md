# 🏠 Prédiction des Prix Immobiliers à Nouakchott 🇲🇷

[![Kaggle](https://img.shields.io/badge/Kaggle-Competition-blue)](https://www.kaggle.com/competitions/prediction-des-prix-immobiliers-a-nouakchott)
[![Python](https://img.shields.io/badge/Python-3.9+-green)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-lightgrey)](https://flask.palletsprojects.com/)
[![Next.js](https://img.shields.io/badge/Next.js-14-black)](https://nextjs.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

---

## 👥 ÉQUIPE

| **Nom de l'équipe** | The Predictors |
|---------------------|----------------|
| **Membres** | Vatma Elwavi<br>Mariem Tfeil<br>Hafsa Bilal |
| **Encadrant** | Beydia Mohamed - Instructeur, SupNum |

---

## 🌐 LIENS IMPORTANTS

| Élément | Lien |
|---------|------|
| **Application déployée (Frontend)** | [https://frontend-capistonepredictors.vercel.app](https://frontend-capistonepredictors.vercel.app) |
| **API Backend** | [https://api-capstone-predictors-4.onrender.com/api/predict) |
| **Repo GitHub (principal)** | [https://github.com/Fatma22035/mauritania-housing-ml_team_predictors?authuser=0) |
| **Repo API** | [https://github.com/Fatma22035/api_mauritania-housing-ml_team_predictors?authuser=0) |
| **Repo Frontend** | [https://github.com/Fatma22035/Frontend_-mauritania-housing-ml_team_predictors?authuser=0) |
| **Support de présentation** | [https://www.canva.com/design/DAHEHHFkgrM/4NHtAeXu0P29F2TiD0qNYg/view?utm_content=DAHEHHFkgrM&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=hfd724869c3&authuser=0#1) |

---

## 🎯 Contexte

En Mauritanie, il n'existe aucune base de données publique sur les prix de l'immobilier. Les transactions se font de gré à gré, les annonces sont dispersées sur plusieurs plateformes, et aucun outil de référence ne permet d'estimer la valeur d'un bien.

Ce projet a été réalisé dans le cadre du **Master 1 Machine Learning** à **SupNum (Institut Supérieur du Numérique, Mauritanie)**.

---

## 🎯 Objectif

Construire un pipeline complet de **prédiction des prix immobiliers** à Nouakchott :

- ✅ **Web Scraping** de sites d'annonces mauritaniens
- ✅ **Géo-enrichissement** avec OpenStreetMap (Nominatim, Overpass API)
- ✅ **Analyse Exploratoire** complète (EDA)
- ✅ **Feature Engineering** avancé
- ✅ **Modélisation** avec 6 algorithmes de régression
- ✅ **Application web** interactive (Next.js + Flask)
- ✅ **Déploiement** sur Render (backend) et Vercel (frontend)

---


## 🏗 Architecture du projet

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Phase 1    │ -> │  Phase 2    │ -> │  Phase 3    │ -> │  Phase 4    │ -> │  Phase 5    │
│ Web Scraping│    │    Géo      │    │     EDA     │    │   Feature   │    │ Modélisation│
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
                                                                                   │
                                                                                   ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Phase 6    │ <- │   Backend   │ <- │   Frontend  │
│ Application │    │  Flask API  │    │  Next.js    │
└─────────────┘    └─────────────┘    └─────────────┘
```

## 📁 Structure du repository

```
CAPSTONE_PROJECT/
├── 01_scrapping/
│   ├── data/
│   │   ├── EDA-Phase_data/                    # Données après analyse exploratoire
│   │   ├── feature_engineering_data/          # Données avec features créées
│   │   ├── geo_enrichissement_data/           # Données avec coordonnées GPS et POIs
│   │   ├── moedlisation_data/                 # Données prêtes pour la modélisation
│   │   └── raw/                               # Données brutes du scraping
│   ├── model/                                 # Modèles entraînés
│   │   ├── best_model_joblib                  # Meilleur modèle (Gradient Boosting)
│   │   ├── encoder_joblib                     # Encodeur pour variables catégorielles
│   │   ├── imputer_joblib                     # Imputeur pour valeurs manquantes
│   │   └── scaler_joblib                      # Scaler pour normalisation
│   ├── notebooks/                             # Notebooks Jupyter
│   │   ├── 01_geo_enrichment_test.ipynb      # Géo-enrichissement (test)
│   │   ├── 01_geo_enrichment_train.ipynb     # Géo-enrichissement (train)
│   │   ├── 02_eda.ipynb                      # Analyse exploratoire
│   │   ├── 03_feature_engineering_test.ipynb # Feature engineering (test)
│   │   ├── 03_feature_engineering_train.ipynb# Feature engineering (train)
│   │   ├── 04_modeling1.ipynb                # Modélisation - version 1
│   │   ├── 04_modeling2.ipynb                # Modélisation - version 2
│   │   └── 04_modeling3_final.ipynb          # Modélisation - version finale
│   ├── README.md                              # Documentation du projet
│   └── requirements.txt                       # Dépendances Python
|   └── Rapport_final.pdf   
```

## 🚀 Installation

### Prérequis
- Python 3.9+
- Node.js 18+
- Git

### Backend (Python)

```bash
# Cloner le repository
git clone https://github.com/Fatma22035/mauritania-housing-ml_team_predictors?authuser=0
cd mauritania-housing-ml_team_predictors

# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Installer les dépendances
pip install -r requirements.txt
```

### Frontend (Next.js)

```bash
cd frontend
npm install
```

## 🕷 Phase 1: Web Scraping

### Sources scrapées (9)
- [voursa.com](https://voursa.com)
- [lagence-mr.com](https://lagence-mr.com)
- [afribaba.com](https://mr.afribaba.com)
- [mauri-home.com](https://mauri-home.com)
- [untoitenrim.com](https://untoitenrim.com)
- [menazel.org](https://menazel.org/fr)
- [elminassa.com](https://www.elminassa.com/app.html?v=20250405)
- [wassit.info](http://wassit.info./)
- https://www.elminassa.com/app.html?v=20250405

  
### Technologies
- **BeautifulSoup4** : Parsing HTML
- **Requests** : Requêtes HTTP
- **Selenium** : Sites dynamiques
- **Time** : Gestion des pauses

### Données extraites
| Champ | Type | Description |
|-------|------|-------------|
| `id` | int | Identifiant unique |
| `titre` | string | Titre de l'annonce |
| `prix` | float | Prix en MRU |
| `surface_m2` | float | Surface en m² |
| `nb_chambres` | int | Nombre de chambres |
| `nb_salons` | int | Nombre de salons |
| `nb_sdb` | int | Nombre de salles de bain |
| `quartier` | string | Quartier |
| `description` | text | Description détaillée |
| `caracteristiques` | text | Caractéristiques (garage, clim, etc.) |
| `source` | string | Site source |
| `date_publication` | date | Date de publication |

### Résultats
- **+6k annonces** collectées
- **8 quartiers** couverts

### Éthique
- Respect du `robots.txt`
- Pauses de 2 secondes entre requêtes
- Anonymisation des numéros de téléphone
- Usage académique uniquement

## 🗺 Phase 2: Géo-enrichissement

### 1. Géocodage avec Nominatim
```python
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

geolocator = Nominatim(user_agent="capstone_project")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
```

**Coordonnées obtenues** :
| Quartier | Latitude | Longitude |
|----------|----------|-----------|
| Tevragh Zeina | 18.1111 | -16.0038 |
| Arafat | 18.0460 | -15.9633 |
| Ksar | 18.1049 | -15.9644 |
| Dar Naim | 18.1266 | -15.9175 |
| Toujounine | 18.0724 | -15.9099 |
| Sebkha | 18.0712 | -16.0026 |
| Riyadh | 18.0107 | -15.9553 |
| Teyarett | 18.1591 | -15.9272 |

### 2. Distances stratégiques (Formule de Haversine)
```python
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Rayon Terre en km
    # Calcul de la distance à vol d'oiseau
    return distance
```

**Features créées** :
- `dist_centre_ville_km` (Ksar)
- `dist_aeroport_km` (Aéroport Oumtounsy)
- `dist_plage_km` (Côte atlantique)

### 3. Points d'Intérêt avec Overpass API
```python
import overpy
api = overpy.Overpass()

def count_pois(lat, lon, poi_type):
    # Requête Overpass pour compter écoles, mosquées, commerces, hôpitaux
    # Rayon de 1 km
    return count
```

**Types de POIs** :
- 🏫 Écoles (`amenity=school`)
- 🕌 Mosquées (`amenity=place_of_worship` + `religion=muslim`)
- 🏪 Commerces (`shop=*`)
- 🏥 Hôpitaux (`amenity=hospital` ou `clinic`)

**Résultats** :
| Quartier | Écoles | Mosquées | Commerces | Hôpitaux | Total |
|----------|--------|----------|-----------|----------|-------|
| Ksar | 6 | 3 | 60 | 5 | 74 |
| Tevragh Zeina | 3 | 3 | 16 | 0 | 22 |
| Arafat | 14 | 21 | 23 | 2 | 60 |
| Sebkha | 7 | 10 | 49 | 0 | 66 |
| Riyadh | 5 | 27 | 2 | 1 | 35 |
| Toujounine | 6 | 5 | 4 | 1 | 16 |
| Dar Naim | 2 | 8 | 2 | 1 | 13 |
| Teyarett | 0 | 0 | 0 | 0 | 0 |

## 📊 Phase 3: Analyse Exploratoire (EDA)

### Valeurs manquantes
| Colonne | Manquantes | Traitement |
|---------|------------|------------|
| `caracteristiques` | 157 (13.6%) | Remplacées par "" |
| `nb_chambres` | 14 (1.2%) | Remplacées par médiane (4) |

### Outliers (méthode IQR)
- **54 outliers** sur les prix (4.7%)
- Conservés car correspondent à des biens de luxe réels

### Statistiques clés
| Quartier | Prix moyen | Prix médian | Nb biens |
|----------|------------|-------------|----------|
| Tevragh Zeina | 8.0M | 6.5M | 373 |
| Ksar | 3.6M | 2.9M | 46 |
| Sebkha | 3.8M | 3.8M | 10 |
| Arafat | 1.7M | 1.3M | 244 |
| Toujounine | 1.6M | 1.1M | 115 |

### Corrélations
- Prix vs Surface : **+0.65**
- Prix vs Distance centre : **-0.42**
- Prix vs Nombre POIs : **+0.38**

## 🔧 Phase 4: Feature Engineering

### 1. Features de base
```python
df['prix_m2'] = df['prix'] / df['surface_m2']
df['nb_pieces_total'] = df['nb_chambres'] + df['nb_salons']
df['surface_par_chambre'] = df['surface_m2'] / (df['nb_chambres'] + 1)
```

### 2. Extraction des caractéristiques
```python
keywords = {
    'garage': ['garage', 'كراج', 'parking'],
    'jardin': ['jardin', 'حديقة', 'حوش'],
    'piscine': ['piscine', 'بسين', 'مسبح'],
    'clim': ['climatisation', 'تكييف', 'clim'],
    'meuble': ['meublé', 'مفروش'],
    'titre_foncier': ['titre foncier', 'تيتر']
}
```

**Résultats** :
| Feature | Présence | Impact prix |
|---------|----------|-------------|
| `has_garage` | 44.1% | +0.5M |
| `has_jardin` | 1.8% | +3.6M |
| `has_piscine` | 0.3% | +13.8M |
| `has_balcon` | 69.4% | +0.3M |
| `has_titre_foncier` | 44.4% | +0.4M |

### 3. Features temporelles
```python
df['age_annonce'] = (date_ref - df['date_publication']).dt.days
df['mois_publication'] = df['date_publication'].dt.month
df['saison'] = df['mois_publication'].map(season_map)
```

### 4. Interactions géographiques
```python
df['centre_x_plage'] = df['dist_centre_ville_km'] * df['dist_plage_km']
df['pois_density'] = df['nb_total_pois'] / (df['dist_centre_ville_km'] + 0.1)
df['score_equipement'] = df[equip_features].sum(axis=1)
```

### 5. Encodage
```python
type_dummies = pd.get_dummies(df['type_bien'], prefix='type')
saison_dummies = pd.get_dummies(df['saison'], prefix='saison')
```

**Résultat** : **23 nouvelles features**, passage de 36 à 59 colonnes.

## 🤖 Phase 5: Modélisation

### Métrique : RMSLE
```python
def rmsle(y_true, y_pred):
    y_pred = np.maximum(y_pred, 0)
    return np.sqrt(np.mean((np.log1p(y_pred) - np.log1p(y_true)) ** 2))
```
**Baseline** : 0.997 (prédiction par la médiane)

### Modèles testés (6)
| Modèle | Description |
|--------|-------------|
| Linear Regression | Régression linéaire simple |
| Ridge | Ridge avec régularisation L2 |
| Lasso | Lasso avec régularisation L1 |
| Random Forest | Ensemble d'arbres de décision |
| Gradient Boosting | Boosting séquentiel |
| XGBoost | Version optimisée |

### Résultats
| Modèle | CV RMSLE | Test RMSLE | Test R² |
|--------|----------|------------|---------|
| Linear Regression | 2.6766 | 2.1649 | 0.4025 |
| Ridge | 2.5543 | 2.1628 | 0.4034 |
| Random Forest | 0.7214 | 0.6505 | 0.2605 |
| **Gradient Boosting** | **0.9421** | **0.62506** | **0.2222** |
| XGBoost | 1.0675 | 1.2149 | 0.0010 |

🏆 **Meilleur modèle**: Gradient Boosting avec **0.62506 RMSLE** (35.2% mieux que baseline)

### Optimisation des hyperparamètres
```python
param_grid = {
    'n_estimators': [200, 300, 400],
    'max_depth': [10, 15, 20],
    'learning_rate': [0.03, 0.05, 0.1]
}
grid_search = RandomizedSearchCV(model, param_grid, n_iter=20, cv=5)
```

## 💻 Phase 6: Application Web

### Architecture
```
Frontend (Next.js) ←→ API (Flask) ←→ Modèle (.pkl)
```

### Backend - Flask API
```python
from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return jsonify({'prix': float(prediction)})
```

**Endpoint unique** : `POST /api/predict`

### Frontend - Next.js
- **Formulaire** : saisie des caractéristiques
- **Carte interactive** (Leaflet) : visualisation du quartier
- **Résultat** : prix estimé en MRU

### Communication (Axios)
```typescript
const response = await axios.post(
  `${API_URL}/api/predict`,
  formData
);
setResult(response.data.prix);
```

## 🚀 Déploiement

### Backend sur Render
https://api-capstone-predictors-4.onrender.com/api/predict

### Frontend sur Vercel
https://frontend-capistonepredictors.vercel.app/


## 📄 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## 🙏 Remerciements

- **SupNum** - Institut Supérieur du Numérique
- **Beydia Mohamed** - Pour l'encadrement et les conseils

---

⭐ **Si ce projet vous a été utile, n'hésitez pas à lui laisser une étoile sur GitHub !** ⭐
