from django.shortcuts import render, redirect
from .models import Reserva
from reservas.forms import ReservaForm
from django.http import JsonResponse

def reservas(request):    
    reservas_list = Reserva.objects.all()    
    return render(request, 'reservas/index.html', {'reservas_list': reservas_list})



def create_reserva(request):
    form = ReservaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('reservas')    
    return render(request, 'reservas/create.html', {'form': form})


def detail_reserva(request, reserva_id):
    reserva = Reserva.objects.get(pk=reserva_id)
    data = { 'coder': reserva.coder, 'fecha_reserva': reserva.fecha_reserva, 'fecha_inicio' : reserva.fecha_inicio, 'fecha_fin': reserva.fecha_fin, 'valor' : reserva.valor}    
    return JsonResponse(data)

from django.contrib import messages

def delete_reserva(request, reserva_id):
    reserva = Reserva.objects.get(pk=reserva_id)
    try:
        reserva.delete()        
        messages.success(request, 'Reserva eliminado correctamente.')
    except:
        messages.error(request, 'No se puede eliminar la reserva porque está asociado a otra tabla.')
    return redirect('reservas')
# Create your views here.
