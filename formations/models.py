from django.db import models

# Create your models here.
class Formations(models.Model):
    pass


class Teachers(models.Model):
    name = models.CharField(max_length=50)
    profetion = models.CharField(max_length=50)
    