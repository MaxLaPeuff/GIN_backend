from django.urls import path
from . import views

urlpatterns = [
    path('domaines/', views.DomaineStageListView.as_view(), name='domaines-list'),
    path('demande/', views.DemandeStageCreateView.as_view(), name='demande-create'),
    path('verification-statut/', views.VerificationStatutView.as_view(), name='verification-statut'),
    path('demande/<uuid:code_unique>/', views.DemandeStageDetailView.as_view(), name='demande-detail'),
] 