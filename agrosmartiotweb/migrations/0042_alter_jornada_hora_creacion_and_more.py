# Generated by Django 4.2.3 on 2023-10-24 00:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agrosmartiotweb', '0041_alter_jornada_hora_creacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jornada',
            name='hora_creacion',
            field=models.TimeField(default=datetime.time(21, 48, 48, 168495), editable=False),
        ),
        migrations.AlterField(
            model_name='procesos',
            name='hora_creacion',
            field=models.TimeField(default=datetime.time(21, 48, 48, 167670), editable=False),
        ),
    ]
