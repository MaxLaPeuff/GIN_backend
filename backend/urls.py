from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path,include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

schema_view = get_schema_view(
   openapi.Info(
      title="GIN API",
      default_version='v1',
      description="Documentation de l'API backend de GIN",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="maxaraye18@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('gin.urls')),

    # Schema
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # Documentation Swagger avec drf_spectacular
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # Redoc (optionnel)
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]