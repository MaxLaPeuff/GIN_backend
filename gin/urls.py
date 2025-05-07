from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import FormationViewSet, ServiceViewSet

#On crée un objet router
router =DefaultRouter()
#On enregistre les viewsets avec une url racine 
router.register(r"formations",FormationViewSet)
router.register(r"services",ServiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
