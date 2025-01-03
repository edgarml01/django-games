# Generated by Django 5.1.3 on 2024-11-27 14:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arcade', '0003_alter_persona_fecha_nacimiento'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JuegoSnake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntaje', models.IntegerField(default=0, verbose_name='Puntaje')),
                ('tiempoMax', models.IntegerField(default=0, verbose_name='Tiempo Máximo')),
                ('nivelMax', models.IntegerField(default=0, verbose_name='Nivel Máximo')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='juego_snake', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Juego Snake',
                'verbose_name_plural': 'Juegos Snake',
                'db_table': 'JuegoSnake',
            },
        ),
    ]
