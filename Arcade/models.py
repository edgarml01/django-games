from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Persona(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="persona")
    nombre = models.CharField(max_length=100,blank=True, null=True, verbose_name="Nombre")
    ap_paterno = models.CharField(max_length=100,blank=True, null=True ,verbose_name="Apellido Paterno")
    ap_materno = models.CharField(max_length=100,blank=True, null=True, verbose_name="Apellido Materno")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento", blank=True, null=True)
    correo = models.EmailField(max_length=100,blank=True, null=True , verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=20, blank=True, null=True, verbose_name="Teléfono")
    domicilio = models.CharField(max_length=200, blank=True, null=True, verbose_name="Domicilio")
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True, verbose_name="Foto de Perfil")
    class Meta:
        db_table = 'Persona'
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):  
        return f'{self.nombre} {self.ap_paterno} {self.ap_materno}' 
    
 

class JuegoSnake(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="juego_snake")
    puntaje = models.IntegerField(default=0, verbose_name="Puntaje")
    tiempoMax = models.IntegerField(default=0, verbose_name="Tiempo Máximo")
    nivelMax = models.IntegerField(default=0, verbose_name="Nivel Máximo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'JuegoSnake'
        verbose_name = 'Juego Snake'
        verbose_name_plural = 'Juegos Snake'

    def _str_(self):
        return f"{self.user.username} - Puntaje: {self.puntaje}, Nivel Máximo: {self.nivelMax}, Tiempo Máximo: {self.tiempoMax}"

class Consola(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre", null=True)
    marca = models.CharField(max_length=100, verbose_name="Marca", null=True)
    modelo = models.CharField(max_length=100, verbose_name="Modelo", null=True)
    fecha_lanzamiento = models.DateField(verbose_name="Fecha de Lanzamiento", null=True)
    descripcion = models.TextField(verbose_name="Descripción", null=True)
    class Meta:
        db_table = 'Consola'
        verbose_name = 'Consola'
        verbose_name_plural = 'Consolas'

    def _str_(self):  
        return f'{self.nombre} {self.marca} {self.modelo}'

class Videojuego (models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre", null=True)
    genero= models.CharField(max_length=100, verbose_name="Genero", null=True)
    fecha_lanzamiento = models.DateField(verbose_name="Fecha de Lanzamiento", null=True)
    descripcion = models.TextField(verbose_name="Descripción", null=True)
    consola = models.TextField(verbose_name="id_consola", null=True)
    class Meta:
        db_table = 'Videojuego'
        verbose_name = 'Videojuego'
        verbose_name_plural = 'Videojuegos'

    def _str_(self):  
        return f'{self.nombre} {self.genero} {self.descripcion} {self.consola}'