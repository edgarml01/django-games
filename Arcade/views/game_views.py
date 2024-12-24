import json
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from ..models import JuegoSnake
from django.contrib.auth.models import User

def Adventure(request):
    # Comprobar si el usuario tiene el permiso o pertenece al grupo 'Jugador'
    view_persona = (
        request.user.has_perm('Arcade.view_persona') or 
        request.user.groups.filter(name='Jugador').exists()
    )
    change_persona = (
        request.user.has_perm('Arcade.change_persona') or 
        request.user.groups.filter(name='Jugador').exists()
    )

    return render(request, 'games/Adventure.html', {'view_persona': view_persona, 'change_persona': change_persona})
  
@csrf_exempt  # Solo para pruebas locales; elimina esta línea en producción
@login_required
def snake(request, id_user):
    user = get_object_or_404(User, id=id_user)

    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Leer el cuerpo JSON
            puntaje = data.get("puntaje", 0)
            tiempo = data.get("tiempo", 0)
            nivel = data.get("nivel", 0)

            # Crear un nuevo registro de juego para el usuario
            JuegoSnake.objects.create(
                user=user,
                puntaje=puntaje,
                tiempoMax=tiempo,
                nivelMax=nivel
            )

            return JsonResponse({"success": True, "message": "Partida registrada correctamente."})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})

    # Comprobar si el usuario tiene el permiso o pertenece al grupo 'Jugador'
    view_persona = (
        request.user.has_perm('Arcade.view_persona') or 
        request.user.groups.filter(name='Jugador').exists()
    )
    change_persona = (
        request.user.has_perm('Arcade.change_persona') or 
        request.user.groups.filter(name='Jugador').exists()
    )



    return render(request, 'games/snake.html', {'view_persona': view_persona, 'change_persona': change_persona})


def dinosaur_run(request):
    # Comprobar si el usuario tiene el permiso o pertenece al grupo 'Jugador'
    view_persona = (
        request.user.has_perm('Arcade.view_persona') or 
        request.user.groups.filter(name='Jugador').exists()
    )
    change_persona = (
        request.user.has_perm('Arcade.change_persona') or 
        request.user.groups.filter(name='Jugador').exists()
    )
    return render(request, 'games/Dino_Runner.html' , {'view_persona': view_persona, 'change_persona': change_persona})

def memory_game(request):

    # Comprobar si el usuario tiene el permiso o pertenece al grupo 'Jugador'
    view_persona = (
        request.user.has_perm('Arcade.view_persona') or 
        request.user.groups.filter(name='Jugador').exists()
    )
    change_persona = (
        request.user.has_perm('Arcade.change_persona') or 
        request.user.groups.filter(name='Jugador').exists()
    )
    return render(request, 'games/memory_game.html', {'view_persona': view_persona, 'change_persona': change_persona})