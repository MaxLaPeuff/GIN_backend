from rest_framework import serializers
from .models import Formation

class ModuleSerializer(serializers.Serializer):
    titre = serializers.CharField()
    contenus = serializers.ListField(child=serializers.CharField())

class FormationSerializer(serializers.ModelSerializer):
    programme = ModuleSerializer(many=True)

    class Meta:
        model = Formation
        fields = '__all__'
