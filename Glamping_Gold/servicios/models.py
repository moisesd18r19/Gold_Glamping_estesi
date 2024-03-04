from django.db import models

class Servicio(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='static/images_servicio', null=True)
    status = models.BooleanField(default=True)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
