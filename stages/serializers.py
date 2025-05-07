# Import du module de sérialisation de DRF
from rest_framework import serializers
# Import des modèles à sérialiser
from .models import DomaineStage, DemandeStage

class DomaineStageSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour le modèle DomaineStage.
    
    Permet la sérialisation et désérialisation des domaines de stage.
    Inclut tous les champs du modèle.
    """
    class Meta:
        # Définition du modèle associé
        model = DomaineStage
        # Inclusion de tous les champs du modèle
        fields = '__all__'

class DemandeStageSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour le modèle DemandeStage.
    
    Permet la sérialisation et désérialisation des demandes de stage.
    Inclut tous les champs du modèle sauf le code_unique qui est généré automatiquement.
    """
    # Champ supplémentaire pour le nom du domaine, en lecture seule
    domaine_nom = serializers.CharField(source='domaine.nom', read_only=True)
    
    class Meta:
        # Définition du modèle associé
        model = DemandeStage
        # Liste des champs à inclure dans la sérialisation
        fields = ['id', 'email', 'cv', 'domaine', 'requete', 'statut', 
                 'date_demande', 'date_modification', 'code_unique','domaine_nom']
        # Champs qui ne peuvent pas être modifiés directement
        read_only_fields = ['code_unique', 'statut', 'date_demande', 'date_modification']

class VerificationStatutSerializer(serializers.Serializer):
    """
    Sérialiseur pour la vérification du statut d'une demande.
    Utilisé uniquement pour la validation du code unique.
    """
    # Champ pour le code unique de la demande
    code_unique = serializers.UUIDField()

class StatutDemandeSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour l'affichage du statut d'une demande.
    Version simplifiée du DemandeStageSerializer.
    """
    # Champ supplémentaire pour le nom du domaine, en lecture seule
    domaine_nom = serializers.CharField(source='domaine.nom', read_only=True)
    
    class Meta:
        # Définition du modèle associé
        model = DemandeStage
        # Liste des champs à inclure dans la sérialisation
        fields = ['code_unique', 'email', 'domaine_nom', 'statut', 'date_demande'] 