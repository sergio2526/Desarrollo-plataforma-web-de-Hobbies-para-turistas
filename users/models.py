from __future__ import unicode_literals
from django.contrib.auth.models import User
from djongo import models

class Profile(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    seudonimo =models.CharField(max_length=20, blank=True)
    nombre = models.CharField(max_length=20, blank=True)
    apellido = models.CharField(max_length=20, blank=True)
    edad = models.CharField(max_length=20, blank=True)
    sexo =models.CharField(max_length=20, blank=True)
    hubicacion_inicial=models.CharField(max_length=20, blank=True)
    pasa_tiempos_dia=models.CharField(max_length=20, blank=True)
    pasa_tiempos_medio_dia =models.CharField(max_length=20, blank=True)
    pasa_tiempos_noche =models.CharField(max_length=20, blank=True)
    biography=models.TextField(blank=True)
    picture=models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )

    def __str__(self):
         return self.user.username


