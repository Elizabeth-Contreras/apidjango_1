# Generated by Django 3.2.4 on 2023-11-25 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('correo_electronico', models.CharField(max_length=60, unique=True)),
                ('telefono', models.IntegerField(max_length=11)),
                ('mensaje', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Informacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('pregunta1', models.CharField(max_length=6)),
                ('pregunta2', models.CharField(max_length=6)),
                ('pregunta3', models.CharField(max_length=1500)),
                ('pregunta4', models.CharField(max_length=1500)),
                ('pregunta5', models.CharField(max_length=1500)),
                ('pregunta6', models.CharField(max_length=30)),
                ('pregunta7', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usuario', models.CharField(max_length=20, unique=True)),
                ('correo', models.CharField(max_length=60, unique=True)),
                ('contrasena', models.CharField(max_length=15)),
            ],
        ),
    ]
