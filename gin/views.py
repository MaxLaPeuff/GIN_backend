from rest_framework import viewsets
from .models import Formation
from .serializer import FormationSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiExample

@extend_schema_view(
    list=extend_schema(
        summary="Lister toutes les formations",
        description="Retourne la liste de toutes les formations disponibles."
    ),
    retrieve=extend_schema(
        summary="Détail d'une formation",
        description="Retourne les détails d'une formation spécifique."
    ),
    create=extend_schema(
        summary="Créer une formation",
        description="Crée une nouvelle formation avec modules et contenus.",
        examples=[
            OpenApiExample(
                name="Exemple complet de formation",
                value={
                "titre": "Automatisation avec Python",
                "description": "Formation pratique sur les techniques d'automatisation avec Python.",
                "objectifs": [
                    "Automatiser les tâches répétitives",
                    "Utiliser des bibliothèques Python pour le web scraping",
                    "Gérer les fichiers et dossiers via scripts"
                ],
                "programme": [
                    {
                    "titre": "Module 1 : Introduction à l'automatisation",
                    "contenus": [
                        "Concepts fondamentaux",
                        "Outils et bibliothèques Python",
                        "Cas d'usage courants"
                    ]
                    },
                    {
                    "titre": "Module 2 : Techniques d'automatisation",
                    "contenus": [
                        "Manipulation de fichiers",
                        "Automatisation du web avec Selenium",
                        "Traitement de données en masse avec Pandas"
                    ]
                    },
                    {
                    "titre": "Module 3 : Travail collaboratif",
                    "contenus": [
                        "Utilisation de Git pour les projets Python",
                        "Documentation des scripts et processus",
                        "Collaboration avec GitHub"
                    ]
                    }
                ],
                "prerecquis": [
                    "Connaissance de base en Python",
                    "Savoir utiliser un éditeur de code"
                ],
                "acquis": "Capacité à développer et maintenir des scripts d'automatisation robustes",
                "debouche": "Développeur Python junior, Assistant RPA, Testeur QA automatisé",
                "prix": "200000.00",
                "date_debut": "2025-06-10",
                "date_fin": "2025-08-20",
                "lieu": "Dakar"
                },
                request_only=True
            )
        ]
    ),
    update=extend_schema(summary="Mettre à jour une formation"),
    partial_update=extend_schema(summary="Mise à jour partielle"),
    destroy=extend_schema(summary="Supprimer une formation"),
)
class FormationViewSet(viewsets.ModelViewSet):
    queryset = Formation.objects.all()
    serializer_class = FormationSerializer
