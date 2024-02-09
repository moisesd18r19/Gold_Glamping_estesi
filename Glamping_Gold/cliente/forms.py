from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"
        exclude = ['status']
        labels = {
           'nombre': 'Nombre',
           'documento': 'Documento',
           'email': 'Email',
           'telefone': 'Telefono',
           'nacionalidad': 'Nacionalidad',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre'}),
            'documento': forms.TextInput(attrs={'placeholder': 'Ingrese el documento'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Ingrese el correo'}),
            'telefone': forms.TextInput(attrs={'placeholder': 'Ingrese el telefono'}),
            'nacionalidad': forms.TextInput(attrs={'placeholder': 'Ingrese la nacionalidad'}),
        }