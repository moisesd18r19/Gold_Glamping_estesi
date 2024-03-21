from django.shortcuts import get_object_or_404, render, redirect

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from servicios.models import Servicio
from .models import Reserva
from reservas.forms import Reserva
from pagos.models import Pago
from reservas_servicios.models import Reserva_servicio
from servicios.models import Servicio
from reservas_cabañas.models import Reserva_cabaña
from cliente.models import Cliente
from cabañas.models import Cabaña
from datetime import datetime   
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render

def reservas(request):    
    reservas_list = Reserva.objects.all()    
    return render(request, 'reservas/index.html', {'reservas_list': reservas_list})


def create_reserva(request):
    cliente_list = Cliente.objects.all()
    cabañas_list = Cabaña.objects.all()
    servicios_list = Servicio.objects.all()
    fecha_actual = datetime.now().date()  # Obtener la fecha actual
    
   


    if request.method == 'POST':
        # Obtener el correo electrónico del cliente del formulario
        cliente_email = request.POST['cliente']
        # Intentar obtener el objeto Costumer correspondiente al correo electrónico
        try:
            cliente = Cliente.objects.get(email=cliente_email)
        except Cliente.DoesNotExist:
            # Manejar la situación en la que no se encuentra un Costumer
            cliente = None  # Asignar None para manejarlo en la lógica de creación de la reserva
        

    if request.method == 'POST':
        fecha_inicio_str = request.POST['fecha_inicio']
        fecha_fin_str = request.POST['fecha_fin']
        fecha_inicio = datetime.strptime(fecha_inicio_str, '%Y-%m-%d')
        fecha_fin = datetime.strptime(fecha_fin_str, '%Y-%m-%d')
        
        reserva = Reserva.objects.create(
            fecha_reserva=datetime.now().date(),
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            precio=request.POST['totalValue'],
            estado='Reservado',
            cliente=cliente      
        )
        
        reserva.save()
        
        id_cabaña = request.POST.getlist('cabañaId[]')
        cabañas_precio = request.POST.getlist('cabañaprecio[]')
        id_servicio= request.POST.getlist('servicioId[]')
        servicios_precio = request.POST.getlist('servicioPrecio[]')
        
        for i in range(len(id_cabaña)):            
            cabaña = Cabaña.objects.get(pk=int(id_cabaña[i]))
            reserva_cabaña = Reserva_cabaña.objects.create(
                id_reserva=reserva,
                id_cabaña=cabaña,
                precio_C=cabañas_precio[i]
            )
            reserva_cabaña.save()

    
        for i in range(len(id_servicio)):            
            servicio = Servicio.objects.get(pk=int(id_servicio[i]))
            reserva_servicio = Reserva_servicio.objects.create(
                id_reserva=reserva,
                id_servicio=servicio,
                precio_S=servicios_precio[i]
            )
            reserva_servicio.save()

        
        ## messages.success(request, 'Reserva creada con éxito.')
        return HttpResponseRedirect(reverse('reservas'))

    return render(request, 'reservas/create.html',{'cliente_list':cliente_list, 'cabañas_list':cabañas_list, 'servicios_list':servicios_list, 'fecha_actual': fecha_actual, })

def detail_reserva(request, reserva_id):
    reserva = Reserva.objects.get(pk=reserva_id)
    reserva_cabañas = Reserva_cabaña.objects.filter(id_reserva=reserva)
    reserva_servicios = Reserva_servicio.objects.filter(id_reserva=reserva)
    pagos = Pago.objects.filter(reserva=reserva)
    return render(request, 'reservas/detail.html', {'reserva': reserva, 'reserva_cabañas': reserva_cabañas, 'reserva_servicios': reserva_servicios, 'pagos': pagos})
    
def cancel_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    reserva.estado = 'Cancelada'
    reserva.save()
    messages.success(request, 'Reserva cancelada correctamente.')
    return redirect('reservas')


def edit_reserva(request, reserva_id):
    reserva = Reserva.objects.get(pk=reserva_id)
    cliente_list = Cliente.objects.all()
    cabañas_list = Cabaña.objects.all()
    servicios_list = Servicio.objects.all()
    cabañas_asociadas = Reserva_cabaña.objects.filter(id_reserva=reserva)
    servicios_asociados = Reserva_servicio.objects.filter(id_reserva=reserva)
    
    if request.method == 'POST':
        fecha_inicio_str = request.POST['fecha_inicio']
        fecha_fin_str = request.POST['fecha_fin']
        fecha_inicio = datetime.strptime(fecha_inicio_str, '%Y-%m-%d')
        fecha_fin = datetime.strptime(fecha_fin_str, '%Y-%m-%d')
        
        reserva.fecha_inicio = fecha_inicio
        reserva.fecha_fin = fecha_fin
        reserva.precio = request.POST['totalValue']
        reserva.cliente_id = request.POST['cliente']
        
        try:
            reserva.save()

            # Limpiar y actualizar las relaciones con cabañas
            reserva.reserva_cabaña_set.all().delete()
            id_cabaña = request.POST.getlist('cabañaId[]')
            cabañas_precio = request.POST.getlist('cabañaprecio[]')
            for i in range(len(id_cabaña)):            
                cabaña = Cabaña.objects.get(pk=int(id_cabaña[i]))
                reserva_cabaña = Reserva_cabaña.objects.create(
                    id_reserva=reserva,
                    id_cabaña=cabaña,
                    precio_C=cabañas_precio[i]
                )
                reserva_cabaña.save()
            
            # Limpiar y actualizar las relaciones con servicios
            reserva.reserva_servicio_set.all().delete()
            id_servicio= request.POST.getlist('servicioId[]')
            servicios_precio = request.POST.getlist('servicioPrecio[]')
            for i in range(len(id_servicio)):            
                servicio = Servicio.objects.get(pk=int(id_servicio[i]))
                reserva_servicio = Reserva_servicio.objects.create(
                    id_reserva=reserva,
                    id_servicio=servicio,
                    precio_S=servicios_precio[i]
                )
                reserva_servicio.save()

            messages.success(request, 'Reserva actualizada correctamente.')
        except Exception as e:
            messages.error(request, f'Ocurrió un error al editar la reserva: {str(e)}')
        
        return redirect('reservas')
    
    return render(request, 'reservas/edit.html', {'reserva': reserva, 'cliente_list': cliente_list, 'cabañas_list': cabañas_list, 'servicios_list': servicios_list, 'cabañas_asociadas': cabañas_asociadas, 'servicios_asociados': servicios_asociados})