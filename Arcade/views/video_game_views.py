
import json
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from ..forms import videojuegoForm
from ..models import Videojuego

def lista_videojuegos(request):
    videojuegos = Videojuego.objects.all()
    return render(request, 'lista_videojuegos.html', {'consolas': videojuegos})

def editar_videojuego(request, id_videojuego):
    consola = get_object_or_404(Videojuego, id=id_videojuego)
    form = videojuegoForm( instance=consola)

    if request.method == 'POST':
        form = videojuegoForm(request.POST, instance=consola)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Videjuego editada correctamente!")
            return redirect('lista_videojuegos')
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")

    return render(request, 'ver-editar_videojuego.html', {'form': form})

def crear_videojuego(request):
    form = videojuegoForm()
    if request.method == 'POST':
        form = videojuegoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Videojuego creada correctamente!")
            return redirect('lista_videojuegos')
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")

    return render(request, 'crear_videojuego.html', {'form': form})

def eliminar_videojuego(request, id_videojuego):
    consola = get_object_or_404(Videojuego, id=id_videojuego)
    consola.delete()
    messages.success(request, "¡Videojuego eliminada correctamente!")
    return redirect('lista_videojuegos')