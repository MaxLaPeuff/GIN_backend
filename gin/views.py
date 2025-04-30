from rest_framework import viewsets
from .models import Formation, Service
from .serializer import FormationSerializer, ServiceSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view,OpenApiExample

"""
ON UTILISE LES VIEWSETS CAR C’EST PLUS RAPIDE ET SIMPLE,
ET ÇA PERMET DE FAIRE TOUTES LES OPÉRATIONS CRUD DANS UNE CLASSE EN SUIVANT LA LOGIQUE REST.
"""

@extend_schema_view(
    list=extend_schema(
        summary="Lister toutes les formations",
        description="Retourne la liste de toutes les formations enregistrées dans le système."
    ),
    retrieve=extend_schema(
        summary="Détail d'une formation",
        description="Retourne les informations détaillées d'une formation en fonction de son ID."
    ),
     create=extend_schema(
        summary="Créer une formation",
        description="Crée une nouvelle formation avec les informations fournies.",
        examples=[
            OpenApiExample(
                name="Exemple de création de formation",
                value={
                    "titre": "Développement Web",
                    "description": "Formation complète sur HTML, CSS, JavaScript, Django et React.",
                    "date_debut": "2025-05-10",
                    "date_fin": "2025-08-10"
                },
                request_only=True,
                response_only=False
            )
        ]
    ),
    update=extend_schema(
        summary="Mettre à jour une formation",
        description="Met à jour les informations d'une formation existante."
    ),
    partial_update=extend_schema(
        summary="Mettre à jour partiellement une formation",
        description="Modifie partiellement les champs d'une formation."
    ),
    destroy=extend_schema(
        summary="Supprimer une formation",
        description="Supprime une formation en fonction de son ID."
    ),
)
class FormationViewSet(viewsets.ModelViewSet):
    queryset = Formation.objects.all()
    serializer_class = FormationSerializer


@extend_schema_view(
    list=extend_schema(
        summary="Lister tous les services",  # 🛠️ corriger 'summarry' → 'summary'
        description="Retourne la liste de tous les services enregistrés dans le système."
    ),
    retrieve=extend_schema(
        summary="Détail d'un service",
        description="Retourne les informations détaillées d'un service en fonction de son ID."
    ),
    create=extend_schema(
        summary="Créer un service",
        description="Crée un nouveau service avec les informations fournies.",
        examples=[
            OpenApiExample(
                name="Exemple de création de service",
                value={
                    "nom": "Support technique",
                    "description": "Assistance aux utilisateurs pour résoudre leurs problèmes techniques."
                },
                request_only=True,
                response_only=False
            )
        ]
    ),
    update=extend_schema(
        summary="Mettre à jour un service",
        description="Met à jour les informations d'un service existant."
    ),
    partial_update=extend_schema(
        summary="Mettre à jour partiellement un service",
        description="Modifie partiellement les champs d'un service."
    ),
    destroy=extend_schema(
        summary="Supprimer un service",
        description="Supprime un service en fonction de son ID."
    ),
)
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
