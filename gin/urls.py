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

# project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/inscription/', include('inscription.urls')),  # Ajoute le chemin vers l'application inscription    
    path('stages/', include('stages.urls')),  # Ceci vers 'api/stages/'
]


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, re_path, include

schema_view = get_schema_view(
   openapi.Info(
      title="API Documentation",
      default_version='v1',
      description="Documentation des endpoints d'inscription",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('api/inscription/', include('inscription.urls')),
    # Swagger UI
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
