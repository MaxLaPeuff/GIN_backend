from django.db import models
from django.conf import settings
import uuid

class DomaineStage(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nom

class DemandeStage(models.Model):
    STATUT_CHOICES = [
        ('en_cours', 'En cours de traitement'),
        ('accepte', 'Accepté'),
        ('refuse', 'Refusé'),
    ]
    
    code_unique = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)  # ✅ corrigé
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
        if not self.code_unique:
            self.code_unique = uuid.uuid4()
        super().save(*args, **kwargs)