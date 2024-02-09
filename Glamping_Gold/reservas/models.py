from django.db import models

class Reserva(models.Model):
    coder = models.CharField(max_length=255)
    fecha_reserva = models.DateField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    valor = models.IntegerField()
    cliente = models.ForeignKey('cliente.Cliente', on_delete= models.DO_NOTHING)

    def __str__(self):
        return self.coder
# Create your models here.
