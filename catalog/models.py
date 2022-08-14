from django.db import models
from django.urls import reverse

class Movie(models.Model):
    title = models.CharField(max_length=64, help_text='Pon el nombre de la película')
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    By_Bone = models.CharField(max_length=80, help_text='Comentarios')

    def get_absolute_url(self):
        return reverse('movie-detail', args=[str(self.id)])

    def __str__(self):
        return self.title

class Director(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    By_Bone = models.CharField(max_length=80, help_text='Comentarios')
    
    def get_absolute_url(self):
        return reverse('director-detail', args=[str(self.id)])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"