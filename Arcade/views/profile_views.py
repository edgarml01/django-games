
import json
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from ..forms import PersonaForm
from ..models import Persona, JuegoSnake

@login_required
def config(request, id_user):
    # Obtiene el usuario actual
    user = get_object_or_404(User, id=id_user)

    # Verificar si el usuario tiene permisos para agregar o editar una persona, o si pertenece al grupo "Jugador"
    if not (user.has_perm('Arcade.add_persona') or user.has_perm('Arcade.change_persona') or user.groups.filter(name='Jugador').exists()):
        messages.error(request, "No tienes permisos para acceder a esta sección.")
        return redirect('home')  # Redirige al home o a una página de acceso denegado

    # Obtiene o crea una instancia vacía de Persona asociada al usuario
    persona, created = Persona.objects.get_or_create(user=user)

    # Formularios inicializados con instancias
    formPersona = PersonaForm(instance=persona)

    if request.method == 'POST':
        if 'nombre' in request.POST:  # Formulario de datos personales
            formPersona = PersonaForm(request.POST, request.FILES, instance=persona)
            if formPersona.is_valid():
                formPersona.save()
                messages.success(request, "¡Datos personales guardados correctamente!")
                return redirect('config', id_user=id_user)
            else:
                messages.error(request, "Por favor corrige los errores en el formulario de datos personales.")

        elif 'username' in request.POST:  # Formulario de usuario
            username = request.POST.get('username', '').strip()
            password_actual = request.POST.get('password-actual', '')
            password_new = request.POST.get('password-new', '')
            password_confirm = request.POST.get('password-confirm', '')

            # Validar contraseña actual
            if not user.check_password(password_actual):
                messages.error(request, "La contraseña actual no es correcta.")
            elif password_new != password_confirm:
                messages.error(request, "La nueva contraseña no coincide con la confirmación.")
            else:
                # Actualizar usuario
                if username:
                    user.username = username
                if password_new:
                    user.set_password(password_new)
                user.save()
                update_session_auth_hash(request, user)  # Mantiene la sesión activa tras cambiar la contraseña
                messages.success(request, "¡Datos de usuario guardados correctamente!")
                return redirect('config', id_user=id_user)
            

            # Comprobar si el usuario tiene el permiso o pertenece al grupo 'Jugador'
            view_persona = (
                request.user.has_perm('Arcade.view_persona') or 
                request.user.groups.filter(name='Jugador').exists()
            )
            change_persona = (
                request.user.has_perm('Arcade.change_persona') or 
                request.user.groups.filter(name='Jugador').exists()
            )

    return render(request, 'configuracion.html', {'user': user, 'persona': persona, 'formPersona': formPersona , 'view_persona': view_persona, 'change_persona': change_persona})

@login_required
def perfil(request, id_user):
    user = get_object_or_404(User, id=id_user)
    persona = get_object_or_404(Persona, user=user)
    sknake = JuegoSnake.objects.filter(user=user).order_by('-puntaje')

    # Comprobar si el usuario tiene el permiso o pertenece al grupo 'Jugador'
    view_persona = (
        request.user.has_perm('Arcade.view_persona') or 
        request.user.groups.filter(name='Jugador').exists()
    )
    change_persona = (
        request.user.has_perm('Arcade.change_persona') or 
        request.user.groups.filter(name='Jugador').exists()
    )


    return render(request, 'perfil.html', {'user': user, 'persona':persona ,'sknake':sknake, 'view_persona': view_persona, 'change_persona': change_persona}) 

@login_required
def delete_account(request, id_user):
    user = get_object_or_404(User, id=id_user)
    
    if request.method == "POST":
        # Elimina la cuenta
        user.delete()
        messages.success(request, "Tu cuenta ha sido eliminada con éxito.")
        
        # Cierra la sesión
        logout(request)
        
        # Redirige al login
        return redirect('login')

    return redirect('config', id_user=id_user)