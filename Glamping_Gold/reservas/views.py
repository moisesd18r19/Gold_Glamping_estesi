from django.shortcuts import render, redirect


from servicios.models import Servicio
from .models import Reserva
from reservas.forms import ReservaForm
from django.http import JsonResponse
from pagos.models import Pago
from reservas_servicios.models import Reserva_servicio
from servicios.models import Servicio
from reservas_cabañas.models import reservas_cabañas
from cliente.models import Cliente
from cabañas.models import Cabaña
from datetime import datetime
from django.contrib import messages


def reservas(request):    
    reservas_list = Reserva.objects.all()    
    return render(request, 'reservas/index.html', {'reservas_list': reservas_list})

def create_reserva(request):
    cliente_list = Cliente.objects.all()
    cabañas_list = Cabaña.objects.all()
    servicios_list = Servicio.objects.all()
    
    if request.method == 'POTS':
        fecha_inicio_str = request.POST['fecha_inicio']
        fecha_fin_str = request.POST['fecha_fin']
        fecha_inicio = datetime.strptime(fecha_inicio_str, '%Y-%M-%D')
        fecha_fin = datetime.strptime(fecha_fin_str, '%Y-%M-%D')
        
        reserva = Reserva.objects.create(
            fecha_reserva = datetime.now().date(),
            fecha_inicio = fecha_inicio,
            fecha_fin = fecha_fin,
            valor = request.POST['valortotal'],
            estado = 'Reservado',
            cliente_id = request.POST['cliente']       
        )
        
        reserva.save()
        cabañas_id = request.POST.getlist('cabañaId[]')
        cabañas_precio = request.POST.getlist('cabaña_precio[]')
        servicios_id = request.POST.getlist('servicioId[]')
        servicios_precio = request.POST.getlist('servicio_precio[]')
        
        for i in range(len(cabañas_id)):
            cabaña = Cabaña.objects.get(pk=(servicios_id [i]))
            reserva_servicio = Reserva_servicio.objects.create(
                cabaña = cabaña,
                servicio = servicio,
                valor = cabañas_precio[i]
            )
            reservas_cabañas.save()
        messages.success(request, 'Reserva creada con éxito.')
        return redirect('reservas')
    return render(request, 'reservas/create.html',{'cliente_list':cliente_list, 'cabañas_list':cabañas_list, 'servicios_list':servicios_list})

def detail_reserva(request, reserva_id):
    reserva = Reserva.objects.get(pk=reserva_id)
    reserva_cabaña = reservas_cabañas.objects.filter(reserva=reserva)
    reserva_servicio = Reserva_servicio.objects.filter(reserva=reserva)
    pagos = Pago.objects.filter(reserva=reserva)
    return render(request, 'reservas/detail.html', {'reserva': reserva, 'reserva_cabañas': reservas_cabañas, 'reserva_servicios': reserva_servicio, 'pagos': pagos})
  
def delete_reserva(request, reserva_id):
    reserva = Reserva.objects.get(pk=reserva_id)
    try:
        reserva.delete()        
        messages.success(request, 'Reserva eliminado correctamente.')
    except:
        messages.error(request, 'No se puede eliminar la reserva porque está asociado a otra tabla.')
    return redirect('reservas')
# Create your views here.
