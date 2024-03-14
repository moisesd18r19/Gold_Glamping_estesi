from django import forms
from . models import Pago
from reservas.models import Reserva


class PagoForm(forms.ModelForm):
    reserva = forms.ModelChoiceField(queryset= Reserva.objects)
    class Meta:
        model = Pago
        fields = "__all__"
        exclude = ['estado']
        labels = {
            'fecha': 'Fecha',
            'metodo_pago': 'Metodo Pago',
            'valor': 'Valor',  
            'reserva': 'Reserva',
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'metodo_pago': forms.TextInput(attrs={'placeholder': 'Ingresa el metodo de pago'}),
            'valor': forms.NumberInput(attrs={'placeholder': 'Ingresa el valor a pagar'}),  
            'reserva': forms.SelectMultiple(attrs={'placeholder': 'Ingrese reserva'})          
        }