from django.urls import path
from .views import RealisationListCreateView, RealisationRetrieveUpdateDestroyView

urlpatterns = [
    path('realisation', RealisationListCreateView.as_view(), name='realisation-list'),
    path('<int:pk>/realisation-update', RealisationRetrieveUpdateDestroyView.as_view(), name='realisation-detail'),
]