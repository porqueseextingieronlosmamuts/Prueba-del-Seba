from django.db import models

# Create your models here.
class Visita(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    motivo_de_visita = models.TextField()
    hora_de_entrada_y_salida = models.DateTimeField(auto_now_add=True)