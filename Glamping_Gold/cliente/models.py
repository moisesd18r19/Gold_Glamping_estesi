from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    documento = models.IntegerField(unique=True)
    email = models.CharField(max_length=50, unique=True)
    telefone = models.IntegerField(unique=True)
    nacionalidad = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre