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
            template = get_template('pdf/invoice.html')
            context = {
                'title': 'Mi primer Pdf'}
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            pisa_status = pisa.CreatePDF(
                html, dest=response,)
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('erp:Pagos'))
    
    