"""
Guide d'utilisation des APIs de réalisations
===========================================

Ce guide vous montre comment utiliser les différentes APIs pour accéder aux réalisations et aux catégories.

1. Liste de toutes les réalisations
-----------------------------------
Endpoint: GET /api/realisations/

Cette API retourne toutes les réalisations sans filtre.

Exemple avec curl:
```
curl -X GET "http://127.0.0.1:8000/api/realisations/" -H "accept: application/json"
```

2. Liste des catégories disponibles
-----------------------------------
Endpoint: GET /api/realisations/categories/

Cette API retourne la liste de toutes les catégories avec leur nombre de réalisations.

Exemple avec curl:
```
curl -X GET "http://127.0.0.1:8000/api/realisations/categories/" -H "accept: application/json"
```

3. Filtrage des réalisations par catégorie
------------------------------------------
Endpoint: GET /api/realisations/categories/?categorie=DEV_WEB

Cette API retourne la liste des catégories ET les réalisations de la catégorie spécifiée.

Exemples avec curl:
```
curl -X GET "http://127.0.0.1:8000/api/realisations/categories/?categorie=DEV_WEB" -H "accept: application/json"
curl -X GET "http://127.0.0.1:8000/api/realisations/categories/?categorie=CYBERSECURITE" -H "accept: application/json"
```

4. Détails d'une réalisation spécifique
---------------------------------------
Endpoint: GET /api/realisations/{id}/

Cette API retourne les détails complets d'une réalisation spécifique.

Exemple avec curl:
```
curl -X GET "http://127.0.0.1:8000/api/realisations/1/" -H "accept: application/json"
```

5. Comment utiliser dans un navigateur
--------------------------------------
Vous pouvez également utiliser ces URLs directement dans votre navigateur :

- http://127.0.0.1:8000/api/realisations/
- http://127.0.0.1:8000/api/realisations/categories/
- http://127.0.0.1:8000/api/realisations/categories/?categorie=DEV_WEB
- http://127.0.0.1:8000/api/realisations/1/
"""
