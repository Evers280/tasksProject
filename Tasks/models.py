from django.db import models

# Create your models here.
class Tasks (models.Model) :

    PRIORITE_CHOICES = [
        ('faible','low'),
        ('moyenne','medium'),
        ('haute','high'),
    ]

    STATUS_CHOICES = [
        ('à faire','to do'),
        ('en cours', 'in progress'),
        ('terminé', 'finished')

    ]

    titre = models.CharField(max_length=100, unique = True)
    description = models.TextField()
    date_echeance = models.DateTimeField()
    priorite = models.CharField(choices = PRIORITE_CHOICES, default = 'faible') # Correction de la valeur par défaut
    status = models.CharField(choices = STATUS_CHOICES, default = 'à faire') # Correction de la valeur par défaut

    masters = models.ForeignKey('Users.Masters', on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return f"{self.titre} {self.date_echeance} {self.priorite} {self.status}"
