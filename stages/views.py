from django.shortcuts import render
from rest_framework import status, viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import OffreStage, DemandeStage
from .serializers import DemandeStageSerializer, OffreStageSerializer

class OffreStageViewSet(viewsets.ModelViewSet):
    """

    queryset = OffreStage.objects.all()
    serializer_class = OffreStageSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

class DemandeStageViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les demandes de stage.
    
    Permet de :
    - Lister les demandes (admin uniquement)
    - Créer une nouvelle demande (public)
    - Récupérer une demande spécifique (admin uniquement)
    - Mettre à jour une demande (admin uniquement)
    - Supprimer une demande (admin uniquement)
    """
    queryset = DemandeStage.objects.all()
    serializer_class = DemandeStageSerializer
    
    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return DemandeStage.objects.all()
        return DemandeStage.objects.none()  # Les utilisateurs non-admin ne voient rien

    @action(detail=True, methods=['post'])
    def update_status(self, request, pk=None):
        """
        Action personnalisée pour mettre à jour le statut d'une demande.
        Accessible uniquement aux administrateurs.
        
        Args:
            request: La requête HTTP
            pk: L'identifiant de la demande
            
        Returns:
            Response: La réponse HTTP avec les données mises à jour
        """
        if not request.user.is_staff:
            return Response(
                {'error': 'Permission denied'},
                status=status.HTTP_403_FORBIDDEN
            )
            
        demande = self.get_object()
        new_status = request.data.get('status')
        
        if new_status not in dict(DemandeStage.STATUT_CHOICES):
            return Response(
                {'error': 'Invalid status'},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        demande.statut = new_status
        demande.save()
        
        serializer = self.get_serializer(demande)
        return Response(serializer.data)
