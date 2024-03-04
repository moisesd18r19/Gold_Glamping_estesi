from django import forms
from .models import Reserva
from cliente.models import Cliente

class ReservaForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.filter(status=True).order_by('nombre'))
    class Meta:
        model = Reserva
        fields = "__all__"
        exclude = ['estado']
        labels = {
           'fecha_reserva' : 'Fecha de la reserva',
           'fecha_inicio' : 'Fecha de inicio',
           'fecha_fin' : 'Fecha fin',
           'precio' : 'Precio',
           'cliente' : 'Cliente',
           
                                        
        }
        widgets = {
            'fecha_reserva' : forms. DateInput(attrs={'type': 'date'}),
            'fecha_inicio' : forms.DateInput(attrs={'type':'date'}),
            'fecha_fin' : forms.DateInput(attrs={'type':'date'}),
            'precio' : forms.NumberInput(attrs={'placeholder':'Ingrese precio'}),
            'cliente' : forms.SelectMultiple(attrs={'placeholder':'Ingrese cliente'})
             
            
        }