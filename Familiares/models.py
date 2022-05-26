from django.db import models

# Create your models here.
class Familiares(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=20)
    DNI = models.IntegerField(unique= True)
    fecha_nacimiento = models.DateField()
    active = models.BooleanField(default=True)