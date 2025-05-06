from rest_framework import permissions
from .models import User


class IsAdminUser(permissions.BasePermission):
    """
    Vérification des permissions pour les administrateurs uniquement.
    """
    message = "Only administrators can perform this action."

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == User.Roles.ADMIN


class IsEditorUser(permissions.BasePermission):
    """
    Vérification des permissions pour les éditeurs de contenu.
    """
    message = "Only content editors can perform this action."

    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.role == User.Roles.EDITOR or 
            request.user.role == User.Roles.ADMIN
        )


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Vérification des permissions pour la propriété d'objet ou le rôle d'administrateur.
    """
    message = "You must be the owner of this object or an administrator."

    def has_object_permission(self, request, view, obj):        # If the user is an admin, allow access
        if request.user.role == User.Roles.ADMIN:
            return True
            
        # Vérifier si l'objet a un champ utilisateur ou un champ propriétaire
        if hasattr(obj, 'user'):
            return obj.user == request.user
        elif hasattr(obj, 'owner'):
            return obj.owner == request.user
        elif hasattr(obj, 'created_by'):
            return obj.created_by == request.user
        
        return False


class ReadOnly(permissions.BasePermission):
    """
    Vérification des permissions pour l'accès en lecture seule.
    """
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
