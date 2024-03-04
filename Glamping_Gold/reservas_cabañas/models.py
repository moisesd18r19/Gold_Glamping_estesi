from django.db import models


class Reserva_cabaña(models.Model):
    id_reserva = models.ForeignKey('reservas.Reserva', on_delete=models.DO_NOTHING)
    id_cabaña = models.ForeignKey('cabañas.Cabaña', on_delete=models.DO_NOTHING)
    valor = models.IntegerField()

    def __str__(self):
        return (self.valor) 

# Create your models here.
    
