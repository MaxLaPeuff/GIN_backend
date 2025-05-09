from rest_framework import viewsets
from .models import Formation
from .serializer import FormationSerializer
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

