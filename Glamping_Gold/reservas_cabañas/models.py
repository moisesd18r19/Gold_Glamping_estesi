from django.db import models


class reservas_cabañas(models.Model):
    id_reserva = models.ForeignKey('reservas.Reserva', on_delete=models.DO_NOTHING)
    id_cabaña = models.ForeignKey('cabañas.Cabaña', on_delete=models.DO_NOTHING)
    valor = models.IntegerField()
# Create your models here.
