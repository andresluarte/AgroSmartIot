# Generated by Django 4.2.3 on 2023-12-22 04:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agrosmartiotweb', '0045_alter_trabajador_options_alter_jornada_hora_creacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jornada',
            name='hora_creacion',
            field=models.TimeField(default=datetime.time(1, 14, 50, 653921), editable=False),
        ),
        migrations.AlterField(
            model_name='procesos',
            name='hora_creacion',
            field=models.TimeField(default=datetime.time(1, 14, 50, 652924), editable=False),
        ),
    ]
