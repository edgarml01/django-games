import json
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from ..models import JuegoSnake, Persona, Consola, Videojuego
from django.contrib.auth import update_session_auth_hash  # Para mantener la sesión activa tras cambiar la contraseña
from django.views.decorators.csrf import csrf_exempt
from .auth_views import login, logout, register
from .game_views import Adventure, snake, dinosaur_run, memory_game
from .profile_views import config, perfil, delete_account
from .console_views import lista_consolas, editar_consola, eliminar_consola, crear_consola
from .video_game_views import lista_videojuegos, editar_videojuego, eliminar_videojuego, crear_videojuego

# Vista para el home (requiere autenticación)
from django.db.models import Max
def home(request):
    # Obtener el ranking con los datos requeridos
    ranking = (
        JuegoSnake.objects.values("user__username")
        .annotate(
            max_puntaje=Max("puntaje"),
            max_nivel=Max("nivelMax"),
            max_tiempo=Max("tiempoMax"),
        )
        .order_by("-max_puntaje")
    )

    # Comprobar si el usuario tiene el permiso o pertenece al grupo 'Jugador'
    view_persona = (
        request.user.has_perm('Arcade.view_persona') or 
        request.user.groups.filter(name='Jugador').exists()
    )
    change_persona = (
        request.user.has_perm('Arcade.change_persona') or 
        request.user.groups.filter(name='Jugador').exists()
    )

    context = {
        "ranking": ranking,
        "view_persona": view_persona,
        "change_persona": change_persona,
    }
    return render(request, "home.html", context)# Renderiza la plantilla del home