
import json
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from ..forms import consolaForm
from ..models import Consola

def lista_consolas(request):
    consolas = Consola.objects.all()
    return render(request, 'lista_consolas.html', {'consolas': consolas})

def editar_consola(request, id_consola):
    consola = get_object_or_404(Consola, id=id_consola)
    form = consolaForm( instance=consola)

    if request.method == 'POST':
        form = consolaForm(request.POST, instance=consola)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Consola editada correctamente!")
            return redirect('lista_consolas')
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")

    return render(request, 'ver-editar_consolas.html', {'form': form})

def eliminar_consola(request, id_consola):
    consola = get_object_or_404(Consola, id=id_consola)
    consola.delete()
    messages.success(request, "¡Consola eliminada correctamente!")
    return redirect('lista_consolas')

def crear_consola(request):
    form = consolaForm()
    if request.method == 'POST':
        form = consolaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Consola creada correctamente!")
            return redirect('lista_consolas')
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")

    return render(request, 'crear_consola.html', {'form': form})