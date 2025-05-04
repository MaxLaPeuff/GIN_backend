from django.shortcuts import render
from rest_framework import status, generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import PermissionDenied
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import DomaineStage, DemandeStage
from .serializers import (
    DomaineStageSerializer, 
    DemandeStageSerializer,
    VerificationStatutSerializer,
    StatutDemandeSerializer
)
from rest_framework.decorators import action

# Create your views here.

class DomaineStageViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les domaines de stage.
    
    Permet de lister, créer, modifier et supprimer les domaines de stage.
    Seuls les utilisateurs authentifiés peuvent effectuer des modifications.
    """
    queryset = DomaineStage.objects.all()
    serializer_class = DomaineStageSerializer
    
    def get_permissions(self):
        """
        Définit les permissions selon l'action :
        - Liste et détail : accessible à tous
        - Création, modification, suppression : utilisateurs authentifiés uniquement
        """
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAuthenticated()]

class DemandeStageViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les demandes de stage.
    
    Permet de :
    - Créer une nouvelle demande de stage
    - Vérifier le statut d'une demande via son code unique
    - Lister et gérer les demandes (admin uniquement)
    """
    queryset = DemandeStage.objects.all()
    serializer_class = DemandeStageSerializer
    
    def get_permissions(self):
        """
        Définit les permissions selon l'action :
        - Création et vérification de statut : accessible à tous
        - Autres actions : utilisateurs authentifiés uniquement
        """
        if self.action in ['create', 'verifier_statut']:
            return [AllowAny()]
        return [IsAuthenticated()]
    
    @action(detail=False, methods=['get'])
    def verifier_statut(self, request):
        """
        Vérifie le statut d'une demande de stage via son code unique.
        
        Args:
            request: Requête contenant le paramètre 'code_unique'
            
        Returns:
            Response: Statut de la demande ou message d'erreur
        """
        code = request.query_params.get('code_unique')
        if not code:
            return Response(
                {'error': 'Le code unique est requis'},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        try:
            demande = DemandeStage.objects.get(code_unique=code)
            serializer = self.get_serializer(demande)
            return Response(serializer.data)
        except DemandeStage.DoesNotExist:
            return Response(
                {'error': 'Demande non trouvée'},
                status=status.HTTP_404_NOT_FOUND
            )

class DomaineStageListView(generics.ListAPIView):
    queryset = DomaineStage.objects.all()
    serializer_class = DomaineStageSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Liste tous les domaines de stage disponibles",
        responses={
            200: DomaineStageSerializer(many=True),
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class DemandeStageCreateView(generics.CreateAPIView):
    queryset = DemandeStage.objects.all()
    serializer_class = DemandeStageSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Créer une nouvelle demande de stage",
        request_body=DemandeStageSerializer,
        responses={
            201: openapi.Response('Demande créée avec succès', DemandeStageSerializer),
            400: 'Données invalides'
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class VerificationStatutView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Vérifier le statut d'une demande de stage",
        request_body=VerificationStatutSerializer,
        responses={
            200: StatutDemandeSerializer,
            404: 'Demande non trouvée'
        }
    )
    def post(self, request):
        serializer = VerificationStatutSerializer(data=request.data)
        if serializer.is_valid():
            try:
                demande = DemandeStage.objects.get(code_unique=serializer.validated_data['code_unique'])
                return Response(StatutDemandeSerializer(demande).data)
            except DemandeStage.DoesNotExist:
                return Response(
                    {'error': 'Aucune demande trouvée avec ce code'},
                    status=status.HTTP_404_NOT_FOUND
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DemandeStageDetailView(generics.RetrieveUpdateAPIView):
    queryset = DemandeStage.objects.all()
    serializer_class = DemandeStageSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'code_unique'

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH']:
            return [IsAuthenticated()]
        return [AllowAny()]

    def check_object_permissions(self, request, obj):
        if request.method in ['PUT', 'PATCH']:
            if not request.user.is_staff:
                raise PermissionDenied("Seuls les administrateurs peuvent modifier le statut des demandes.")
        return super().check_object_permissions(request, obj)

    @swagger_auto_schema(
        operation_description="Récupérer ou mettre à jour une demande de stage",
        responses={
            200: DemandeStageSerializer,
            404: 'Demande non trouvée'
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Mettre à jour le statut d'une demande de stage",
        request_body=DemandeStageSerializer,
        responses={
            200: DemandeStageSerializer,
            400: 'Données invalides',
            403: 'Permission refusée',
            404: 'Demande non trouvée'
        }
    )
    def patch(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.check_object_permissions(request, instance)
            
            if 'statut' in request.data:
                instance.statut = request.data['statut']
                instance.save()
                return Response(self.get_serializer(instance).data)
            else:
                return Response(
                    {'error': 'Le champ statut est requis'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except PermissionDenied as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_403_FORBIDDEN
            )
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
