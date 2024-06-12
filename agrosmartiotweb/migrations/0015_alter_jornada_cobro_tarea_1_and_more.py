# Generated by Django 4.2.3 on 2023-09-08 04:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agrosmartiotweb', '0014_alter_jornada_cobro_tarea_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jornada',
            name='cobro_tarea_1',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='procesos',
            name='hora_creacion',
            field=models.TimeField(default=datetime.time(1, 5, 39, 695788), editable=False),
        ),
    ]