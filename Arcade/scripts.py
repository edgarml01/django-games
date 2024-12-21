from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Persona  # Ajusta según tu aplicación

def create_jugador_group():
    # Crear grupo "Jugador"
    jugador_group, created = Group.objects.get_or_create(name="Jugador")

    if created:
        print("Grupo 'Jugador' creado.")

    # Obtener el permiso de cambiar Persona
    content_type = ContentType.objects.get_for_model(Persona)
    change_persona_permission = Permission.objects.get(
        codename="change_persona",
        content_type=content_type
    )

    # Asignar permiso al grupo
    jugador_group.permissions.add(change_persona_permission)
    print(f"Permiso '{change_persona_permission}' asignado al grupo 'Jugador'.")

# Llama a la función al iniciar tu aplicación o desde un comando
create_jugador_group()
