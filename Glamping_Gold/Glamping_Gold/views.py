from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from cabañas.models import Cabaña
from Glamping_Gold.forms import RegisterForm
from cliente.models import Cliente
from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from reservas.models import Reserva
from reservas_cabañas.models import Reserva_cabaña
from reservas_servicios.models import Reserva_servicio
from django.template.loader import render_to_string
from io import BytesIO

import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders


def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render (request, 'register.html')

def landing(request):    
    cabañas_lan = Cabaña.objects.filter(status=True)   
    return render(request, 'landing.html', {'cabañas_lan': cabañas_lan})

def login(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        authenticated_user = authenticate(username=username, password=password)
        if authenticated_user is not None:
            auth_login(request, authenticated_user)
            return render(request, 'index.html', {'user': authenticated_user})
        else:
            error = 'Usuario o contraseña incorrectos.'
            return render(request, 'login.html', {'error': error})    
        
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)    
    return redirect('login')


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            documento = form.cleaned_data['documento']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            telefone = form.cleaned_data['telefone']
            username = email
            user = User.objects.create_user(username, email, password, first_name=nombre, last_name=apellido)
            user.save()
            group = Group.objects.get(name='clientes')
            user.groups.add(group)
            if user is not None:            
                cliente = Cliente.objects.filter(documento=documento).first()
                if cliente is None:
                    nombre = form.cleaned_data['nombre'] + ' ' + form.cleaned_data['apellido']
                    cliente = Cliente(None, nombre, documento=documento, email=email, telefone=telefone)
                    cliente.save()
                    return redirect('login')               
            return redirect('login')    
    return render(request, 'register.html', {'form': form})


class Pdfview(View):
    def get(self, request, *args, **kwargs):
        try:
            reserva_id = kwargs.get('pk')
            reserva = Reserva.objects.get(pk=reserva_id)
            reserva_cabañas = Reserva_cabaña.objects.filter(id_reserva=reserva)
            reserva_servicios = Reserva_servicio.objects.filter(id_reserva=reserva)
            
            # Renderizar el contenido del PDF directamente desde una cadena HTML
            html = render_to_string('pdfinvoice.html', {'reserva': reserva, 'reserva_cabañas': reserva_cabañas, 'reserva_servicios': reserva_servicios})
            
            # Crear un objeto BytesIO para almacenar el PDF
            buffer = BytesIO()
            pisa_status = pisa.CreatePDF(html, dest=buffer)
            
            if not pisa_status.err:
                # Si la generación del PDF fue exitosa, devolver el PDF como respuesta
                pdf = buffer.getvalue()
                buffer.close()
                response = HttpResponse(pdf, content_type='application/pdf')
                response['Content-Disposition'] = f'attachment; filename="report.pdf"'
                return response
        except Reserva.DoesNotExist:
            pass
        
        # En caso de excepción o si la reserva no existe, devolver una respuesta vacía con un código de estado 404
        return HttpResponse(status=404)
    
    