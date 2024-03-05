from django.shortcuts import render, redirect
from .models import Cabaña
from cabañas.forms import CabañaForm
from django.http import JsonResponse
from django.contrib import messages

def cabañas(request):    
    cabañas_list = Cabaña.objects.all()    
    return render(request, 'cabañas/index.html', {'cabañas_list': cabañas_list})

def change_status_cabaña(request, cabaña_id):
    cabaña = Cabaña.objects.get(pk=cabaña_id)
    cabaña.status = not cabaña.status
    cabaña.save()
    return redirect('cabañas')

def create_cabaña(request):
    form = CabañaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('cabañas')    
    return render(request, 'cabañas/create.html', {'form': form})

def detail_cabaña(request, cabaña_id):
    cabaña = Cabaña.objects.get(pk=cabaña_id)
    data = { 'nombre': cabaña.nombre, 'capacidad': cabaña.capacidad, 'descripcion': cabaña.descripcion }    
    return JsonResponse(data)

def detail_cabaña(request, cabaña_id):
    cabaña = Cabaña.objects.get(pk=cabaña_id)
    data = { 'nombre': cabaña.nombre, 'capacidad': cabaña.capacidad, 'precio' : cabaña.precio, 'descripcion' : cabaña.descripcion}    
    return JsonResponse(data)


def delete_cabaña(request, cabaña_id):
    cabaña = Cabaña.objects.get(pk=cabaña_id)
    try:
        cabaña.delete()        

        messages.success(request, 'cabaña eliminada correctamente.')
    except:
        messages.error(request, 'No se puede eliminar la cabaña porque está asociado a otra tabla.')
    return redirect('cabañas')


def edit_cabaña(request, cabaña_id):
    cabaña = Cabaña.objects.get(pk=cabaña_id)
    form = CabañaForm(request.POST or None, request.FILES or None, instance=cabaña)
    if form.is_valid() and request.method == 'POST':
        try:
            form.save()
            messages.success(request, 'Cabaña actualizada correctamente.')
        except:
            messages.error(request, 'Ocurrió un error al editar la cabaña.')
        return redirect('cabañas')    
    return render(request, 'cabañas/editar.html', {'form': form})
