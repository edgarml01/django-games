from django import forms
from django.contrib.auth.models import User
from .models import Persona, Consola, Videojuego
class UserForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Ingrese su contraseña',
                    'aria-label': 'Confirm Password',  }), )
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Confirme su contraseña',
                    'aria-label': 'Confirm Password',  }), )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
                'username': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Username',
                    'aria-label': 'Username',
                }),
                'email': forms.EmailInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Correo Electrónico',
                    'aria-label': 'Correo Electrónico', 
                }),
                
               
            }


class videojuegoForm(forms.ModelForm):
    class Meta:
        model = Videojuego 
        fields = ['nombre', 'genero', 'consola', 'fecha_lanzamiento', 'descripcion']

        labels = {
            'nombre': 'Nombre',
            'genero': 'Genero',
            'consola': 'Consola',
            'fecha_lanzamiento': 'Fecha de Lanzamiento',
            'descripcion': 'Descripción',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre',
                'aria-label': 'Nombre',
            }),
            'genero': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Genero',
                'aria-label': 'Genero',
            }),
            'consola': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Consola',
                'aria-label': 'Consola',
            }),
            'fecha_lanzamiento': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'aria-label': 'Fecha de Lanzamiento',
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción',
                'rows': 3,
                'aria-label': 'Descripción',
            }),
        }


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'ap_paterno', 'ap_materno', 'fecha_nacimiento', 'correo', 'telefono', 'domicilio', 'foto_perfil']   

        labels = {
            'nombre': 'Nombre',
            'ap_paterno': 'Apellido Paterno',
            'ap_materno': 'Apellido Materno',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'correo': 'Correo Electrónico',
            'telefono': 'Teléfono',
            'domicilio': 'Domicilio',
            'foto_perfil': 'Foto de Perfil',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre',
                'aria-label': 'Nombre',
                
            }),
            'ap_paterno': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido Paterno',
                'aria-label': 'Apellido Paterno',
            }),
            'ap_materno': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido Materno',
                'aria-label': 'Apellido Materno',
            }),
            'fecha_nacimiento': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'aria-label': 'Fecha de Nacimiento',
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Correo Electrónico',
                'aria-label': 'Correo Electrónico',
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Teléfono',
                'aria-label': 'Teléfono',
            }),
            'domicilio': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Domicilio',
                'aria-label': 'Domicilio',
            }),
            'foto_perfil': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'id': 'inputGroupFile01',
            }),
        }

class consolaForm(forms.ModelForm):
    class Meta:
        model = Consola
        fields = ['nombre', 'marca', 'modelo', 'fecha_lanzamiento', 'descripcion']

        labels = {
            'nombre': 'Nombre',
            'marca': 'Marca',
            'modelo': 'Modelo',
            'fecha_lanzamiento': 'Fecha de Lanzamiento',
            'descripcion': 'Descripción',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre',
                'aria-label': 'Nombre',
            }),
            'marca': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Marca',
                'aria-label': 'Marca',
            }),
            'modelo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Modelo',
                'aria-label': 'Modelo',
            }),
            'fecha_lanzamiento': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'aria-label': 'Fecha de Lanzamiento',
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción',
                'rows': 3,
                'aria-label': 'Descripción',
            }),
        }