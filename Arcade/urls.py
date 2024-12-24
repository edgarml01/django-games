from django.urls import path
from Arcade.views.auth_views import login, logout, register
from Arcade.views.home_views import home
from Arcade.views.game_views import Adventure, snake, dinosaur_run, memory_game
from Arcade.views.profile_views import config, perfil, delete_account
from Arcade.views.console_views import lista_consolas, editar_consola, eliminar_consola, crear_consola
from Arcade.views.video_game_views import lista_videojuegos, editar_videojuego, eliminar_videojuego, crear_videojuego
from Arcade.views.video_game_views import lista_videojuegos, editar_videojuego, eliminar_videojuego, crear_videojuego

urlpatterns = [

    path('', login, name='login'),  # Ruta principal que apunta al login
    path('home/', home, name='home'),  # Ruta para el home

    path('logout/', logout, name='logout'),  # Ruta para el logout
    path('register/', register, name='register'),  # Ruta para el registro


    path('lista-consolas/', lista_consolas, name='lista_consolas'),
    path('crear_consola/', crear_consola, name='crear_consola'),
    path('editar_consola/<int:id_consola>/', editar_consola, name='editar_consola'),
    path('eliminar_consola/<int:id_consola>/', eliminar_consola, name='eliminar_consola'),

    path('lista-videojuegos/', lista_videojuegos, name='lista_videojuegos'),
    path('crear_videojuego/', crear_videojuego, name='crear_videojuego'),
    path('editar_videojuego/<int:id_videojuego>/', editar_videojuego, name='editar_videojuego'),
    path('eliminar_videojuego/<int:id_videojuego>/', eliminar_videojuego, name='eliminar_videojuego'),

    path('perfil/<int:id_user>/', perfil, name='perfil'),
    path('configuracion/<int:id_user>/', config, name='config'),
    path('Adventure/', Adventure, name='Adventure'),
    path('snake/<int:id_user>/', snake, name='snake'),
    path('delete-account/<int:id_user>/', delete_account, name='delete_account'),
    path('dinosaur-run/', dinosaur_run, name='dinosaur_run'),
    path('memory_game/', memory_game, name='memory_game'),
    
]
