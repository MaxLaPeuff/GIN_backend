from rest_framework import generics
from .models import Realisation
from .serializers import RealisationSerializer

class RealisationListCreateView(generics.ListCreateAPIView):
    queryset = Realisation.objects.all()
    serializer_class = RealisationSerializer

class RealisationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Realisation.objects.all()
    serializer_class = RealisationSerializer
