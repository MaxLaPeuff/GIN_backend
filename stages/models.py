from django.db import models
from django.contrib.auth.models import User
import uuid

class DomaineStage(models.Model):
    """
    Modèle représentant un domaine de stage disponible.
    
    Attributes:
        nom (str): Nom unique du domaine de stage
        description (str): Description détaillée du domaine
    """
    nom = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nom

class DemandeStage(models.Model):
    """
    Modèle représentant une demande de stage.
    
    Attributes:
        code_unique (UUID): Code unique généré automatiquement pour le suivi
        utilisateur (User): Utilisateur associé à la demande (optionnel)
        email (str): Email du candidat
        cv (File): Fichier CV du candidat
        domaine (DomaineStage): Domaine de stage choisi
        requete (str): Message/motivation du candidat
        statut (str): Statut de la demande (en_cours, accepte, refuse)
        date_demande (datetime): Date de création de la demande
        date_modification (datetime): Date de dernière modification
    """
    STATUT_CHOICES = [
        ('en_cours', 'En cours de traitement'),
        ('accepte', 'Accepté'),
        ('refuse', 'Refusé'),
    ]
    
    code_unique = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField()
    cv = models.FileField(upload_to='cvs/')
    domaine = models.ForeignKey(DomaineStage, on_delete=models.CASCADE)
    requete = models.TextField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_cours')
    date_demande = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Demande de {self.email} - {self.domaine.nom} - {self.statut}"
    
    def save(self, *args, **kwargs):
        """
        Surcharge de la méthode save pour s'assurer qu'un code unique est généré.
        """
        if not self.code_unique:
            self.code_unique = uuid.uuid4()
        super().save(*args, **kwargs)
