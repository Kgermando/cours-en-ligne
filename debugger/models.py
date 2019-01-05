from django.db import models

# Create your models here.
class Debugger(models.Model):  # s'occupe de buggue lié aux languages de programmations
    name_debug = models.CharField(max_length=50)
    cours_debug = models.TextField(max_length=300, help_text='Introduction du cours', blank=True)
    image_debug = models.ImageField(upload_to='', blank=True)
    cours_debug_2 = models.TextField(help_text='Devellopement du cours', blank=True)
    image_debug_2 = models.ImageField(upload_to='', blank=True)
    cours_debug_3 = models.TextField(max_length=500,help_text='conclusion du cours', blank=True)

    def __str__(self):
        return self.name_debug
