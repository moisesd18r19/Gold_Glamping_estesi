from django.db import models

class Reserva(models.Model):       
    fecha_reserva = models.DateField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    valor = models.IntegerField()
    estado = models.CharField(max_length=20, default='Reservado')
    cliente = models.ForeignKey('cliente.Cliente', on_delete= models.DO_NOTHING)


    def __str__(self):

        return (self.cliente) 
        

        return f"Reserva #{self.id} - Cliente: {self.cliente}, Fecha de inicio: {self.fecha_inicio}, Fecha de fin: {self.fecha_fin}"



