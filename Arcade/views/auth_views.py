import json
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from ..forms import UserForm

# Vista para el login
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        # Autenticación con Django
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Iniciar sesión
            auth_login(request, user)
            return redirect('home')  # Redirigir al home
        else:
            # Si las credenciales son inválidas, muestra un mensaje de error
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    
    return render(request, 'login.html')  # Renderiza la plantilla de login


    # ...existing code...
def logout(request):
    auth_logout(request)  # Cerrar sesión
    return redirect('login')  # Redirige al login

def register(request):
    form=   UserForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        # Validación de contraseñas
        if password1 != password2:
            return render(request, 'register.html', {'error': 'Las contraseñas no coinciden'})
        # Crear usuario
        try:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            return redirect('login')
        except Exception as e:
            return render(request, 'register.html', {'error': str(e)})
    return render(request, 'register.html', {'form': form})

