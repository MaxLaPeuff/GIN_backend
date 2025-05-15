"""
Module de gestion des middleware personnalisés.
"""
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class DisableCSRFMiddleware:
    """
    Middleware pour désactiver la protection CSRF pour les routes d'API spécifiques.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Vérifier si la requête concerne une API
        if request.path.startswith('/api/'):
            # Désactiver la vérification CSRF pour les routes d'API
            setattr(request, '_dont_enforce_csrf_checks', True)
        
        response = self.get_response(request)
        return response


def csrf_exempt_class(view):
    """
    Décorateur de classe pour désactiver CSRF sur une vue spécifique.
    Permet de contourner la vérification CSRF pour les vues API REST.
    """
    return method_decorator(csrf_exempt, name='dispatch')(view)
