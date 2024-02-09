from django import forms
from . models import Tipocabaña

class TipocabañaForm(forms.ModelForm):
    class Meta:
        model = Tipocabaña
        fields = "__all__"
        exclude = ['status']
        labels = {
            'name': 'Nombre',
                                
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ingresa el nombre'}),
                   
        }