# GIN Backend

Backend Django pour la gestion des inscriptions aux formations et des demandes de stage.

## Fonctionnalités

### Application Inscription
- Inscription des utilisateurs
- Authentification JWT
- Recherche de formations
- Inscription aux formations
- Intégration avec une API externe de formations

### Application Stages
- Gestion des domaines de stage
- Soumission des demandes de stage avec CV
- Système de code unique pour le suivi
- Vérification du statut des demandes
- Gestion des statuts par les administrateurs

## Installation

1. Cloner le repository :
```bash
git clone [URL_DU_REPO]
cd GIN_backend
```

2. Créer un environnement virtuel :
```bash
python -m venv env
source env/bin/activate  # Linux/Mac
# ou
.\env\Scripts\activate  # Windows
```

3. Installer les dépendances :
```bash
pip install -r requirements.txt
```

4. Configurer les variables d'environnement :
```bash
cp .env.example .env
# Éditer .env avec vos configurations
```

5. Appliquer les migrations :
```bash
python manage.py migrate
```

6. Créer un superutilisateur :
```bash
python manage.py createsuperuser
```

7. Lancer le serveur :
```bash
python manage.py runserver
```

## API Endpoints

### Inscription

#### Authentification
- `POST /api/inscription/register/` : Inscription d'un nouvel utilisateur
- `POST /api/inscription/login/` : Connexion utilisateur

#### Formations
- `POST /api/inscription/recherche-formation/` : Recherche de formations
- `POST /api/inscription/inscription/` : Inscription à une formation
- `GET /api/inscription/verification-statut/` : Vérification du statut d'inscription

### Stages

#### Domaines
- `GET /api/stages/domaines/` : Liste des domaines de stage disponibles

#### Demandes
- `POST /api/stages/demande/` : Création d'une demande de stage
- `POST /api/stages/verification-statut/` : Vérification du statut d'une demande
- `GET /api/stages/demande/<code_unique>/` : Détails d'une demande
- `PATCH /api/stages/demande/<code_unique>/` : Mise à jour du statut (admin uniquement)

## Documentation API

La documentation complète de l'API est disponible via Swagger UI à l'adresse :
```
http://localhost:8000/api/docs/
```

## Tests

Exécuter les tests :
```bash
python manage.py test inscription
python manage.py test stages
```

## Structure du Projet

```
GIN_backend/
├── backend/                 # Configuration principale
├── inscription/            # Application d'inscription
│   ├── models.py          # Modèles de données
│   ├── serializers.py     # Sérialiseurs
│   ├── views.py          # Vues et logique
│   └── tests.py          # Tests unitaires
├── stages/                # Application de stages
│   ├── models.py         # Modèles de données
│   ├── serializers.py    # Sérialiseurs
│   ├── views.py         # Vues et logique
│   └── tests.py         # Tests unitaires
└── manage.py             # Script de gestion Django
```

## Sécurité

- Authentification JWT
- Validation des données
- Gestion des permissions
- Protection CSRF
- Validation des fichiers uploadés

## Développement

### Bonnes Pratiques
1. Toujours créer une branche pour les nouvelles fonctionnalités
2. Écrire des tests pour les nouvelles fonctionnalités
3. Documenter les changements importants
4. Suivre les conventions PEP 8

### Workflow de Développement
1. Créer une branche feature
2. Développer et tester
3. Créer une pull request
4. Code review
5. Merge dans main

## Contribution

1. Fork le projet
2. Créer une branche feature
3. Commit les changements
4. Push vers la branche
5. Créer une pull request

## Licence

[Type de licence]
