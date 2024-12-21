# Generated by Django 5.1.3 on 2024-11-28 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arcade', '0005_consola'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videojuego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, null=True, verbose_name='Nombre')),
                ('marca', models.CharField(max_length=100, null=True, verbose_name='Marca')),
                ('fecha_lanzamiento', models.DateField(null=True, verbose_name='Fecha de Lanzamiento')),
                ('descripcion', models.TextField(null=True, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Videojuego',
                'verbose_name_plural': 'Videojuegos',
                'db_table': 'Videojuego',
            },
        ),
    ]