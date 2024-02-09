from django import forms
from . models import Servicio

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = "__all__"
        exclude = ['status']
        labels = {
            'nombre': 'Nombre',
            'precio': 'Precio',
            'imagen': 'Imagen',  
            'descripcion': 'Descripción',                 
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingresa el nombre'}),
            'precio': forms.NumberInput(attrs={'placeholder': 'Ingresa el precio'}),
            'imagen': forms.FileInput(attrs={'placeholder': 'Selecciona imagen'}), 
            'descripcion': forms.TextInput(attrs={'placeholder': 'Ingresa la descripción'}),      
        }  