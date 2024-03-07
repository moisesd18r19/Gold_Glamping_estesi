from django.db import models

# Define tu modelo Pago
class Pago(models.Model):
    metodo_pago = models.CharField(max_length=255)
    fecha = models.DateField()
    valor = models.FloatField(max_length=50)
    reserva = models.ForeignKey('reservas.Reserva', on_delete=models.DO_NOTHING)
    estado = models.BooleanField(default=True)

    def _str_(self):
        return str(self.valor)

    # Define un método que ejecuta el código
    def calcular_total(self):
        total_valor = Pago.objects.aggregate(total=models.Sum('valor'))['total']
        return total_valor
        


    
    

    
# Create your models here.
