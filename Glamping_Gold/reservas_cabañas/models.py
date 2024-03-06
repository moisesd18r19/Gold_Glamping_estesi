from django.db import models


class Reserva_cabaña(models.Model):
    id_reserva = models.ForeignKey('reservas.Reserva', on_delete=models.DO_NOTHING)
    id_cabaña = models.ForeignKey('cabañas.Cabaña', on_delete=models.DO_NOTHING)
    precio_C = models.IntegerField()

    

# Create your models here.
    
