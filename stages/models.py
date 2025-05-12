from django.db import models

    
    def __str__(self):
        return self.titre

class DemandeStage(models.Model):

    STATUT_CHOICES = [
        ('en_cours', 'En cours de traitement'),
        ('accepte', 'Accepté'),
        ('refuse', 'Refusé'),
    ]
>>>> develop
    email = models.EmailField()
    cv = models.FileField(upload_to='cvs/')
    offre = models.ForeignKey(OffreStage, on_delete=models.CASCADE)
    requete = models.TextField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_cours')
    date_demande = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Demande de {self.email} - {self.offre.titre} - {self.statut}"
    
    def save(self, *args, **kwargs):
