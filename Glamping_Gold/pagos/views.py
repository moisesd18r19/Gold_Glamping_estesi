from django.shortcuts import render, redirect
from .models import Pago
from .forms import  PagoForm
from django.http import JsonResponse
from django.contrib import messages

from django.shortcuts import render
from datetime import datetime
from django.shortcuts import redirect

from reservas.models import Reserva
from django.db import models
from . models import Pago
from django.contrib.auth.decorators import user_passes_test,login_required

def is_admin_or_staff(user):
    return user.is_authenticated and (user.is_staff or user.groups.filter(name='Administradores').exists())
@login_required
@user_passes_test(is_admin_or_staff)
def pagos(request):    
    pagos_list = Pago.objects.all()    
    return render(request, 'pagos/index.html', {'pagos_list': pagos_list})

def change_status_pago(request, pago_id):
    pago = Pago.objects.get(pk=pago_id)
    pago.estado = not pago.estado
    pago.save()
    return redirect('pagos')


def create_pagos(request):
    form = PagoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('pagos')    
    return render(request, 'pagos/create.html', {'form': form})


def detail_pago(request, pago_id):
    pago = Pago.objects.get(pk=pago_id)
    data = { 'fecha': pago.fecha, 'valor': pago.valor, 'metodo_pago': pago.metodo_pago}    
    return JsonResponse(data)

def delete_pago(request, pago_id):
    pago = Pago.objects.get(pk=pago_id)
    try:
        pago.delete()        
        messages.success(request, 'Pago eliminado correctamente.')
    except:
        messages.error(request, 'No se puede eliminar el pago porque está asociado a una reserva.')
    return redirect('pagos')

def edit_pago(request, pago_id):
    pago = Pago.objects.get(pk=pago_id)
    form = PagoForm(request.POST or None, request.FILES or None, instance=pago)
    if form.is_valid() and request.metodo_pago == 'POST':
        try:
            form.save()
            messages.success(request, 'Pago actualizado correctamente.')
        except:
            messages.error(request, 'Ocurrió un error al editar el pago.')
        return redirect('pagos')    
    return render(request, 'pagos/editar.html', {'form': form})

def index(request):
    pagos_list = Pago.objects.all()
    return render(request, 'pagos/index.html', {'pagos_list': pagos_list})

def pago_reserva(request, id):
    reserva = Reserva.objects.get(id=id)
    total_pagos = Pago.objects.filter(reserva_id=id).aggregate(total=models.Sum('valor'))
    if total_pagos['total'] is not None:
        total_pagos = total_pagos['total']
    else:
        total_pagos = 0    
    if request.method == 'POST':
        metodo_pago = request.POST['metodo_pago']
        fecha = datetime.now().date()
        valor = request.POST['valor']
        pago_reserva = request.POST['pago_reserva']
        pago = Pago.objects.create(
            metodo_pago = metodo_pago,
            fecha=fecha,
            valor=int(valor),
            reserva=reserva,
            estado=True
        )
        try:
            pago.save()     
            total_p = Pago.objects.filter(reserva_id=id).aggregate(total=models.Sum('valor'))       
            if  int(total_p['total']) >= (reserva.precio / 2) and int(total_p['total']) < reserva.precio:
                reserva.estado = 'Confirmada'
            elif int(total_p['total']) >= reserva.precio:
                reserva.estado = 'En ejecución'        
            reserva.save()
            return redirect('reservas') 
        
        except Exception as e:
            return redirect('reservas')         
    return render(request, 'pago.html', {'reserva': reserva, 'total_pagos': total_pagos})
#