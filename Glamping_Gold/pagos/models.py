from django.db import models

class Pago(models.Model):
    fecha = models.DateField( )
    metodo_pago = models.CharField(max_length=200)
    valor = models.IntegerField( )
    status = models.BooleanField(default=True)
    reserva = models.ForeignKey('reservas.Reserva', on_delete= models.DO_NOTHING)
    
    def __str__(self):
        return self.reserva


    
    

    
# Create your models here.
