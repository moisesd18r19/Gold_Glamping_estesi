from django.shortcuts import get_object_or_404, render, redirect
from servicios.models import Servicio
from .models import Reserva
from reservas.forms import Reserva
from pagos.models import Pago
from reservas_servicios.models import Reserva_servicio
from reservas_cabañas.models import Reserva_cabaña
from servicios.models import Servicio
from cliente.models import Cliente
from cabañas.models import Cabaña
from datetime import datetime
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime



def reservas(request):    
    reservas_list = Reserva.objects.all()    
    return render(request, 'reservas/index.html', {'reservas_list': reservas_list})



def create_reserva(request):
    cliente_list = Cliente.objects.all()
    cabañas_list = Cabaña.objects.all()
    servicios_list = Servicio.objects.all()
    
    if request.method == 'POST':
        fecha_inicio_str = request.POST['fecha_inicio']
        fecha_fin_str = request.POST['fecha_fin']
        fecha_inicio = datetime.strptime(fecha_inicio_str, '%Y-%m-%d')
        fecha_fin = datetime.strptime(fecha_fin_str, '%Y-%m-%d')
        
        reserva = Reserva.objects.create(
            fecha_reserva=datetime.now().date(),
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            valor=request.POST['totalValue'],
            estado='Reservado',
            cliente_id=request.POST['cliente']       
        )
        
        reserva.save()
        cabañas_id = request.POST.getlist('cabañaId[]')
        cabañas_precio = request.POST.getlist('cabaña_precio[]')
        servicios_id = request.POST.getlist('servicioId[]')
        servicios_precio = request.POST.getlist('servicio_precio[]')
        

        for i in range (len(cabañas_id)):
            cabaña = Cabaña.objects.get(pk=int(cabañas_id[i]))
            reserva_cabaña = Reserva_cabaña.objects.create(
                reserva=reserva,
                cabaña=cabaña,
                valor=cabañas_precio[i]
        )
            reserva_cabaña.save()
    
        for i in range(len(servicios_id)):
          servicio = Servicio.objects.get(pk=int(servicios_id[i]))
          reserva_servicio = Reserva_servicio.objects.create(
             reserva=reserva,
             servicio=servicio,
             valor=servicios_precio[i]
          )
          reserva_servicio.save()
        messages.success(request, 'Reserva creada con éxito.')
        return redirect('reservas')
    return render(request, 'reservas/create.html',{'clientes_list':cliente_list, 'cabañas_list':cabañas_list, 'servicios_list':servicios_list})
   
       

def detail_Reserva(request, reserva_id):
    reserva = Reserva.objects.get(pk=reserva_id)
    reserva_cabañas = Reserva_cabaña.objects.filter(id_reserva=reserva)
    reserva_servicios = Reserva_servicio.objects.filter(id_reserva=reserva)
    print(reserva_cabañas)
    print(reserva_servicios)

    pagos = Pago.objects.filter(reserva=reserva)  # Corregido aquí
    return render(request, 'reservas/detail.html', {'reserva': reserva, 'reserva_cabañas': reserva_cabañas, 'reserva_servicios': reserva_servicios, 'pagos': pagos})

    
def cancel_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    reserva.estado = 'Cancelada'
    reserva.save()
    messages.success(request, 'Reserva cancelada correctamente.')

    return redirect('reservas')



