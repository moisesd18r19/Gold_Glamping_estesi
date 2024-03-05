from django.db import models
from tipocabañas.models import Tipocabaña

class Cabaña(models.Model):
    nombre= models.CharField(max_length=50)
    capacidad = models.IntegerField()
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=250)
    imagen = models.FileField(upload_to='static/images_cabaña', null=True)
    status = models.BooleanField(default=True)
    tipocabaña = models.ForeignKey('tipocabañas.Tipocabaña', on_delete=models.DO_NOTHING)
    
    
    
    def __str__(self):
        return self.nombre 
    
    
# Create your models here.
