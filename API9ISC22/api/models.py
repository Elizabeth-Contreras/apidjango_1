from django.db import models

class Usuario(models.Model):
    id_usuario = models.CharField(max_length=20, unique=True)
    correo = models.CharField(max_length=60)
    contrasena = models.CharField(max_length=15)
# Create your models here.
