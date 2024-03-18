from django.shortcuts import render, redirect
from .forms import ClienteForm
from .models import Cliente  
from django.http import JsonResponse

from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test,login_required

def is_admin_or_staff(user):
    return user.is_authenticated and (user.is_staff or user.groups.filter(name='Administradores').exists())
@login_required
@user_passes_test(is_admin_or_staff)
def cliente(request):    
    cliente_list = Cliente.objects.all()  
    return render(request, 'cliente/index.html', {'cliente_list': cliente_list})

def change_status_cliente(request, cliente_id):
    cliente_instance = Cliente.objects.get(pk=cliente_id) 
    cliente_instance.status = not cliente_instance.status
    cliente_instance.save()
    return redirect('cliente')

def create_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        try:
            form.save()
            messages.success(request, 'Cliente creado correctamente')
            return redirect('cliente')    
        except:
            messages.error(request, 'No se puede crear el cliente')
    return render(request, 'cliente/create.html', {'form': form})



def detail_cliente(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    data = { 'nombre': cliente.nombre, 'documento' : cliente.documento, 'email' : cliente.email, 'telefone' : cliente.telefone, 'nacionalidad' : cliente.nacionalidad}
    return JsonResponse(data)

def delete_cliente(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    try:
        cliente.delete()        
        messages.success(request, 'Cliente eliminado correctamente.')
    except:
        messages.error(request, 'No se puede eliminar el cliente porque está asociado a una reserva.')
    return redirect('cliente')

def edit_cliente(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid() and request.method == 'POST':
        try:
            form.save()
            messages.success(request, 'Cliente actualizado correctamente.')
        except:
            messages.error(request, 'Ocurrió un error al editar el cliente')        
        return redirect('cliente')    
    return render(request, 'cliente/editar.html', {'form': form})

#f

