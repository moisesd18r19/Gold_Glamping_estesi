from django.shortcuts import render, redirect 
from servicios.models import Servicio
from .forms import ServicioForm
from django.http import JsonResponse
from django.contrib import messages

def servicios(request):
    servicios_list = Servicio.objects.all()
    return render(request, 'servicios/index.html', {'servicios_list': servicios_list})  

def change_status_servicio(request, servicio_id):
    servicio = Servicio.objects.get(pk=servicio_id)
    servicio.status = not servicio.status
    servicio.save()
    return redirect('servicios')

def create_servicio(request):
    form = ServicioForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('servicios')    
    return render(request, 'servicios/create.html', {'form': form})


def detail_servicio(request, servicio_id):
    servicio = Servicio.objects.get(pk=servicio_id)
    data = { 'nombre' : servicio.nombre, 'precio' : servicio.precio, 'descripcion' : servicio.descripcion }    
    return JsonResponse(data)

def delete_servicio(request, servicio_id):
    servicio = Servicio.objects.get(pk=servicio_id)
    try:
        servicio.delete()        
        messages.success(request, 'Servicio eliminado correctamente.')
    except:

        messages.error(request, 'No se puede eliminar el servicio porque está asociado a una reserva.')
    return redirect('servicios')

def edit_servicio(request, servicio_id):
    servicio = Servicio.objects.get(pk=servicio_id)
    form = ServicioForm(request.POST or None, request.FILES or None, instance=servicio)
    if form.is_valid() and request.method == 'POST':
        try:
            form.save()
            messages.success(request, 'Servicio actualizado correctamente.')
        except:
            messages.error(request, 'Ocurrió un error al editar el servicio.')        
        return redirect('servicios')    
    return render(request, 'servicios/editar.html', {'form': form})

    messages.error(request, 'No se puede eliminar el servicio porque está asociado a un libro.')
    return redirect('servicios')

