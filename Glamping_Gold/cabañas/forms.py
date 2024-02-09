from django import forms
from tipocabañas.models import Tipocabaña
from cabañas.models import Cabaña

class CabañaForm(forms.ModelForm):
    tipocabaña = forms.ModelChoiceField(queryset=Tipocabaña.objects.filter(status=True).order_by('nombre'))
    class Meta:
        model = Cabaña
        fields = "__all__"
        exclude = ['status']
        labels = {
           'nombre' : 'Nombre',
           'capacidad' : 'Capacidad',
           'precio' : 'Precio',
           'descripcion' : 'Descripcion',
           'imagen' : 'Imagen',
           'tipocabaña' : 'Tipocabaña'
           
                                        
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingresa el nombre'}),
            'capacidad': forms.NumberInput(attrs={'placeholder': 'Ingresa capacidad'}),
            'precio': forms.NumberInput(attrs={'placeholder': 'Ingresa el precio'}),
            'descripcion': forms.TextInput(attrs={'placeholder': 'Ingresa la descripción'}),  
            'imagen': forms.FileInput(attrs={'placeholder': 'Selecciona imagen'}), 
            'tipocabaña': forms.SelectMultiple(attrs={'placeholder': 'Ingrese tipo cabaña'})
        }