from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Formation(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    prerecquis = models.TextField(verbose_name="Pré-requis")
    acquis=models.TextField(verbose_name="acquis")
    debouche = models.TextField(verbose_name="Débouchés")
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    lieu = models.CharField(max_length=100)

    def __str__(self):
        return self.titre

    def clean(self):
        if self.date_fin and self.date_fin < self.date_debut:
            raise ValidationError("La date de fin doit être postérieure à la date de début.")
    
