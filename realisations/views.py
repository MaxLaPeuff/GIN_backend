from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAdminUser
from rest_framework.response import Response
from django.db.models import Count
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse, extend_schema_view
from rest_framework.views import APIView

from .models import Realisation, Categorie
from .serializers import (
    RealisationListSerializer,
    RealisationDetailSerializer,
    RealisationCreateUpdateSerializer
)
<<<<<<< HEAD
from backend.permissions import EstAdministrateur
from backend.middleware import csrf_exempt_class
=======
>>>>>>> 7fea0c47afe6e6c836d9115c11d73ff9ddfe8a74


class RealisationListView(generics.ListAPIView):
    """
    Vue pour lister toutes les réalisations.
    """
    serializer_class = RealisationListSerializer
    permission_classes = [AllowAny]
    
    @extend_schema(
        responses={
            200: RealisationListSerializer(many=True)
        },
        description="Liste toutes les réalisations disponibles",
        operation_id="list_realisations",
        tags=["Réalisations"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        """
        Retourne toutes les réalisations.
        """
        return Realisation.objects.all()


class RealisationDetailView(generics.RetrieveAPIView):
    """
    Vue pour afficher les détails d'une réalisation spécifique.
    """
    queryset = Realisation.objects.all()
    serializer_class = RealisationDetailSerializer
    permission_classes = [AllowAny]
    
    @extend_schema(
        responses={
            200: RealisationDetailSerializer, 
            404: OpenApiResponse(description="Réalisation non trouvée")
        },
        description="Récupère tous les détails d'une réalisation",
        operation_id="get_realisation_detail",
        tags=["Réalisations"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


@csrf_exempt_class
class RealisationCreateView(generics.CreateAPIView):
    """
    Vue pour créer une nouvelle réalisation.
    Seul l'administrateur peut créer des réalisations.
    """
    serializer_class = RealisationCreateUpdateSerializer
    permission_classes = [IsAdminUser]
    
    @extend_schema(
        request=RealisationCreateUpdateSerializer,
        responses={
            201: RealisationDetailSerializer,
            400: OpenApiResponse(description="Données invalides"),
            403: OpenApiResponse(description="Accès refusé - Réservé à l'administrateur")
        },
        description="Crée une nouvelle réalisation",
        operation_id="create_realisation",
        tags=["Réalisations - Administration"]
    )
    def post(self, request, *args, **kwargs):
        # Pour permettre l'utilisation de l'interface Swagger/OpenAPI
        # Si des noms de fichiers simples sont fournis pour les images, on les traite comme null
        # pour éviter l'erreur "The submitted data was not a file"
        data = request.data.copy()
        
        # Liste des champs d'image à vérifier
        image_fields = ['image1', 'image2', 'image3']
        
        for field in image_fields:
            if field in data and isinstance(data[field], str) and not data[field].startswith('/media/'):
                # Si c'est une simple chaîne et pas un chemin complet de média, on le traite comme null
                data[field] = None
        
        # Remplacer les données de la requête par nos données modifiées
        request._full_data = data
        
        return super().post(request, *args, **kwargs)


@csrf_exempt_class
class RealisationUpdateView(generics.UpdateAPIView):
    """
    Vue pour mettre à jour une réalisation existante.
    Seul l'administrateur peut mettre à jour des réalisations.
    """
    queryset = Realisation.objects.all()
    serializer_class = RealisationCreateUpdateSerializer
    permission_classes = [IsAdminUser]
    
    @extend_schema(
        request=RealisationCreateUpdateSerializer,
        responses={
            200: RealisationDetailSerializer,
            400: OpenApiResponse(description="Données invalides"),
            404: OpenApiResponse(description="Réalisation non trouvée")
        },
        description="Met à jour une réalisation existante",
        operation_id="update_realisation"
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    @extend_schema(
        request=RealisationCreateUpdateSerializer,
        responses={
            200: RealisationDetailSerializer,
            400: OpenApiResponse(description="Données invalides"),
            404: OpenApiResponse(description="Réalisation non trouvée")
        },
        description="Met à jour partiellement une réalisation existante",
        operation_id="partial_update_realisation"
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


@csrf_exempt_class
class RealisationDeleteView(generics.DestroyAPIView):
    """
    Vue pour supprimer une réalisation.
    Seul l'administrateur peut supprimer des réalisations.
    """
    queryset = Realisation.objects.all()
    permission_classes = [IsAdminUser]
    
    @extend_schema(
        responses={
            204: OpenApiResponse(description="Réalisation supprimée avec succès"),
            404: OpenApiResponse(description="Réalisation non trouvée")
        },
        description="Supprime une réalisation",
        operation_id="delete_realisation"
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


@api_view(['GET'])
@permission_classes([AllowAny])
@extend_schema(
    parameters=[
        OpenApiParameter(
            name='categorie',
            description='Filtre les réalisations par catégorie (ex: DEV_WEB, CYBERSECURITE). Si non fourni, retourne la liste des catégories.',
            required=False,
            type=str,
            location=OpenApiParameter.QUERY,
            enum=[c.value for c in Categorie],
        )
    ],
    responses={
        200: {
            "type": "object",
            "properties": {
                "categories": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "string"},
                            "name": {"type": "string"},
                            "count": {"type": "integer"}
                        }
                    }
                },
                "realisations": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "nomProjet": {"type": "string"},
                            "description": {"type": "string"},
                            "categorie": {"type": "string"}
                        }
                    }
                }
            }
        },
        400: OpenApiResponse(description="Paramètre 'categorie' invalide")
    },
    description="Récupère la liste des catégories disponibles et leur nombre de réalisations. Si un paramètre 'categorie' est fourni, retourne également les réalisations de cette catégorie.",
    operation_id="list_categories_and_filter",
    tags=["Catégories"]
)
def liste_categories(request):
    """
    Vue pour récupérer la liste des catégories disponibles et leur nombre de réalisations.
    Si un paramètre 'categorie' est fourni, retourne également les réalisations de cette catégorie.
    """
    categorie = request.query_params.get('categorie')

    if categorie:
        if categorie in dict(Categorie.choices):
            # Récupère les réalisations de la catégorie spécifiée
            realisations = Realisation.objects.filter(categorie=categorie)
            serializer = RealisationListSerializer(realisations, many=True)
            return Response({"realisations": serializer.data})
        else:
            return Response(
                {"error": f"Catégorie '{categorie}' invalide. Les valeurs possibles sont: {list(dict(Categorie.choices).keys())}"},
                status=status.HTTP_400_BAD_REQUEST
            )

    # Récupère les catégories distinctes qui ont au moins une réalisation
    categories = Realisation.objects.values('categorie').annotate(count=Count('id')).order_by('categorie')

    # Prépare la réponse
    formatted_categories = []
    for cat in categories:
        cat_value = cat['categorie']
        cat_name = dict(Categorie.choices).get(cat_value, cat_value)
        formatted_categories.append({
            'id': cat_value,
            'name': cat_name,
            'count': cat['count']
        })

    # Ajoute également toutes les catégories possibles même si elles n'ont pas de réalisations
    all_categories = dict(Categorie.choices)
    existing_cats = {cat['id'] for cat in formatted_categories}

    for cat_value, cat_name in all_categories.items():
        if cat_value not in existing_cats:
            formatted_categories.append({
                'id': cat_value,
                'name': cat_name,
                'count': 0
            })

    return Response({"categories": formatted_categories})


class RealisationByCategoryView(APIView):
    """
    Vue pour lister les réalisations d'une catégorie spécifique.
    """
    permission_classes = [AllowAny]

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='categorie',
                description='Filtre les réalisations par catégorie (ex: DEV_WEB, CYBERSECURITE).',
                required=False,
                type=str,
                location=OpenApiParameter.QUERY,
                enum=[c.value for c in Categorie],
            )
        ],
        responses={
            200: RealisationListSerializer(many=True),
            400: OpenApiResponse(description="Paramètre 'categorie' invalide ou manquant")
        },
        description="Liste les réalisations d'une catégorie spécifique. Les catégories disponibles sont : DEV_WEB, DEV_MOBILE, CYBERSECURITE, RESEAU_INFRA, IA.",
        operation_id="list_realisations_by_category",
        tags=["Réalisations"]
    )
    def get(self, request, *args, **kwargs):
        categorie = request.query_params.get('categorie')
        if categorie and categorie not in dict(Categorie.choices):
            return Response(
                {"error": "Paramètre 'categorie' invalide. Les valeurs possibles sont : {}".format(list(dict(Categorie.choices).keys()))},
                status=400
            )

        queryset = Realisation.objects.filter(categorie=categorie) if categorie else Realisation.objects.all()
        serializer = RealisationListSerializer(queryset, many=True)
        return Response(serializer.data)


class RealisationFilterByCategoryView(APIView):
    """
    Vue pour filtrer les réalisations par catégorie spécifique.
    """
    permission_classes = [AllowAny]

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='categorie',
                description='Filtre les réalisations par catégorie (ex: DEV_WEB, DEV_MOBILE, CYBERSECURITE, RESEAU_INFRA, IA).',
                required=True,
                type=str,
                location=OpenApiParameter.QUERY,
                enum=[c.value for c in Categorie],
            )
        ],
        responses={
            200: RealisationListSerializer(many=True),
            400: OpenApiResponse(description="Paramètre 'categorie' manquant ou invalide")
        },
        description="Filtre les réalisations par catégorie. Les catégories disponibles sont : DEV_WEB, DEV_MOBILE, CYBERSECURITE, RESEAU_INFRA, IA.",
        operation_id="filter_realisations_by_category",
        tags=["Réalisations"]
    )
    def get(self, request, *args, **kwargs):
        categorie = request.query_params.get('categorie')
        if not categorie:
            return Response(
                {"error": "Le paramètre 'categorie' est obligatoire."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if categorie not in dict(Categorie.choices):
            return Response(
                {"error": f"Catégorie '{categorie}' invalide. Les valeurs possibles sont : {list(dict(Categorie.choices).keys())}"},
                status=status.HTTP_400_BAD_REQUEST
            )

        queryset = Realisation.objects.filter(categorie=categorie)
        serializer = RealisationListSerializer(queryset, many=True)
        return Response(serializer.data)
