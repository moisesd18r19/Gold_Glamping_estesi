from django.shortcuts import render, redirect
from .models import Pago
from .forms import  PagoForm
from django.http import JsonResponse
from django.contrib import messages


def pagos(request):    
    pagos_list = Pago.objects.all()    
    return render(request, 'pagos/index.html', {'pagos_list': pagos_list})

def change_status_pago(request, pago_id):
    pago = Pago.objects.get(pk=pago_id)
    pago.status = not pago.status
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
    if form.is_valid() and request.method == 'POST':
        try:
            form.save()
            messages.success(request, 'Pago actualizado correctamente.')
        except:
            messages.error(request, 'Ocurrió un error al editar el pago.')
        return redirect('pagos')    
    return render(request, 'pagos/editar.html', {'form': form})

#