from django.db import models


class Reserva_servicio(models.Model):
    id_reserva = models.ForeignKey('reservas.Reserva', on_delete=models.DO_NOTHING)
    id_servicio = models.ForeignKey('servicios.Servicio', on_delete=models.DO_NOTHING)
    precio_S = models.IntegerField()

