# Generated by Django 5.1.2 on 2024-10-24 20:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorias', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
                ('apellido', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel', models.CharField(max_length=255)),
                ('contacto', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provincia', models.CharField(max_length=255, unique=True)),
                ('ciudad', models.CharField(max_length=255, unique=True)),
                ('calle', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Habitaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_habitacion', models.IntegerField(unique=True)),
                ('categoria', models.ManyToManyField(to='api.categoria')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Reservas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_entrada', models.DateTimeField(auto_now_add=True)),
                ('fecha_salida', models.DateTimeField()),
                ('clientes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.clientes')),
                ('habitaciones', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.habitaciones')),
            ],
        ),
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.IntegerField()),
                ('fecha_pago', models.DateTimeField(auto_now_add=True)),
                ('reservas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.reservas')),
            ],
        ),
        migrations.AddField(
            model_name='hotel',
            name='ubicacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ubicacion'),
        ),
    ]
