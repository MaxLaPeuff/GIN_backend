"""
Module de gestion de l'administrateur.
Ce module définit les modèles et la logique d'authentification pour l'administrateur.
"""
from django.db import models
from django.contrib.auth.models import User, Group, UserManager as DjangoUserManager
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class CustomUserManager(DjangoUserManager):
    """
    Manager personnalisé pour le modèle User afin de garantir que les superusers
    sont automatiquement assignés au rôle ADMIN.
    """
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        """
        Crée et sauvegarde un superuser avec le nom d'utilisateur, email et mot de passe donnés.
        S'assure que tous les superusers sont assignés au rôle ADMIN.
        """
        # Appel à la méthode parente pour créer le superuser
        user = super().create_superuser(username, email, password, **extra_fields)
        
        # S'assurer que l'utilisateur est bien un superuser
        if not user.is_superuser:
            raise ValueError('Un superuser doit avoir is_superuser=True')
        
        # Créer un administrateur lié à ce superuser s'il n'existe pas déjà
        Administrateur.objects.get_or_create(
            utilisateur=user,
            defaults={'date_creation': timezone.now()}
        )
        
        return user


# Remplacer le UserManager standard par notre version personnalisée
User.objects = CustomUserManager()


class Administrateur(models.Model):
    """
    Modèle représentant les administrateurs du système.
    """
    utilisateur = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='administrateur',
        verbose_name=_("Compte utilisateur associé"),
        help_text=_("Compte utilisateur Django associé à cet administrateur"),
        null=True,  # Permettre temporairement null pour la migration
    )
    date_creation = models.DateTimeField(
        default=timezone.now,  # Utiliser default au lieu de auto_now_add pour la migration
        verbose_name=_("Date de création")
    )
    
    # Conserver temporairement le champ ManyToMany pour la migration
    utilisateurs = models.ManyToManyField(
        User,
        related_name='administrateurs',
        verbose_name=_("Comptes utilisateurs associés (legacy)"),
        help_text=_("Ancien champ - ne pas utiliser"),
        blank=True
    )

    class Meta:
        verbose_name = _("Administrateur")
        verbose_name_plural = _("Administrateurs")

    def __str__(self):
        """Représentation textuelle de l'administrateur."""
        if self.utilisateur:
            return f"Administrateur: {self.utilisateur.username}"
        return "Administrateur sans utilisateur associé"


@receiver(post_save, sender=User)
def create_admin_for_superuser(sender, instance, created, **kwargs):
    """
    Signal pour créer automatiquement un profil d'administrateur
    lorsqu'un superuser est créé ou mis à jour.
    """
    if instance.is_superuser:
        Administrateur.objects.get_or_create(
            utilisateur=instance,
            defaults={'date_creation': timezone.now()}
        )
