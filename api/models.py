from django.db import models

class Usuario(models.Model):
    id_usuario = models.CharField(max_length=20, unique=True)
    correo = models.CharField(max_length=60, unique=True)
    contrasena = models.CharField(max_length=15)


class Informacion(models.Model):
    nombre = models.CharField(max_length=100)
    pregunta1 = models.CharField(max_length=6)
    pregunta2 = models.CharField(max_length=6)
    pregunta3 = models.CharField(max_length=1500)
    pregunta4 = models.CharField(max_length=1500)
    pregunta5 = models.CharField(max_length=1500)
    pregunta6 = models.CharField(max_length=30)
    pregunta7 = models.CharField(max_length=30)
    
class Contactame(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.CharField(max_length=60, unique=True)
    telefono = models.IntegerField(max_length=11)
    mensaje = models.CharField(max_length=500)
# Create your models here.
