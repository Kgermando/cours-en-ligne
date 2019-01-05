from django.db import models

# Create your models here.

class Formateurs(models.Model):
    ''' pour ce model il faudra ajouter les champs nombre 
    de cours postés et un lien vers ces cours'''

    full_name = models.CharField(max_length=50)
    profile = models.ImageField(upload_to='profile', max_length=100, blank=True)
    citation = models.CharField(max_length=250)

    def __str__(self):
        return self.full_name

