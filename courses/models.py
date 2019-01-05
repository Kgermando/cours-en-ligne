from django.db import models
from django.urls import reverse

# Create your models here.
class Courses(models.Model):
    # category = models.ManyToManyField(category)
    name = models.CharField(max_length=50)
    cours_1 = models.TextField(max_length=300, help_text='Introduction du cours', blank=True)
    image = models.ImageField(upload_to='', blank=True)
    cours_2 = models.TextField(help_text='Devellopement du cours', blank=True)
    image_2 = models.ImageField(upload_to='', blank=True)
    cours_3 = models.TextField(max_length=500,help_text='conclusion du cours', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('courses:details', kwargs={'id': self.id})

class Category(models.Model):
    name_category = models.CharField(max_length=50)
    prix = models.CharField(max_length=50)
    image = models.ImageField(upload_to='courses')
    resume = models.CharField(max_length=300, help_text='Petit resumé de votre cours')
    auteur = models.CharField(max_length=255)
    image_auteur = models.ImageField(upload_to='auteur')
    
    def __str__(self):
        return self.name_category

    def get_absolute_url(self):      
        return reverse('courses:details', kwargs={'id': self.id})

class Category_index(models.Model):
    ''' class  category for page index  '''
    name_category = models.CharField(max_length=50)
    prix = models.CharField(max_length=50)
    image = models.ImageField(upload_to='courses')
    resume = models.CharField(
        max_length=300, help_text='Petit resumé de votre cours')
    auteur = models.CharField(max_length=255)
    image_auteur = models.ImageField(upload_to='auteur')

    def __str__(self):
        return self.name_category

    def get_absolute_url(self):
        return reverse('courses:details', kwargs={'id': self.id})
