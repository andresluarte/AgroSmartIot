# Generated by Django 4.2.3 on 2023-08-27 02:50

import datetime
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('tipo_consulta', models.IntegerField(choices=[[0, 'Consulta'], [1, 'Reclamo'], [2, 'Sugerencia'], [3, 'Felicitaciones']])),
                ('mensaje', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Huerto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lotes', to='agrosmartiotweb.huerto')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, null=True)),
                ('rut', models.CharField(max_length=12, null=True)),
                ('fecha_ingreso', models.DateField(default=datetime.date.today)),
                ('fecha_termino_contrato', models.DateField()),
                ('tipo_contraro', models.CharField(choices=[('Indefinido', 'Indefinido'), ('Plazo fijo', 'Plazo fijo'), ('Honorario', 'Honorario'), ('Sin Contraro', 'Sin Contrato')], default='Sin Contrato', max_length=15)),
                ('cobro', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('trabajo_a_realizar', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Procesos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trabajo', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('estado', models.CharField(choices=[('Por Realizar', 'Por Realizar'), ('En Proceso', 'En Proceso'), ('Terminado', 'Terminado')], default='Por Realizar', max_length=15)),
                ('hora_asignada', models.TimeField(null=True)),
                ('hora_creacion', models.TimeField(default=datetime.time(22, 50, 35, 582308), editable=False)),
                ('presupuesto', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('observacion', models.CharField(blank=True, max_length=100, null=True)),
                ('asignado', models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, to='agrosmartiotweb.trabajador')),
            ],
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('huerto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agrosmartiotweb.huerto')),
            ],
        ),
        migrations.CreateModel(
            name='Jornada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_jornada', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('nombre_tarea_1', models.CharField(max_length=100)),
                ('hora_inicio_tarea_1', models.TimeField()),
                ('hora_fin_tarea_1', models.TimeField()),
                ('cobro_tarea_1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('nombre_tarea_2', models.CharField(blank=True, max_length=100, null=True)),
                ('hora_inicio_tarea_2', models.TimeField(blank=True, null=True)),
                ('hora_fin_tarea_2', models.TimeField(blank=True, null=True)),
                ('cobro_tarea_2', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('nombre_tarea_3', models.CharField(blank=True, max_length=100, null=True)),
                ('hora_inicio_tarea_3', models.TimeField(blank=True, null=True)),
                ('hora_fin_tarea_3', models.TimeField(blank=True, null=True)),
                ('cobro_tarea_3', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('asignado', models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, to='agrosmartiotweb.trabajador')),
            ],
        ),
        migrations.AddField(
            model_name='huerto',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agrosmartiotweb.sector'),
        ),
    ]