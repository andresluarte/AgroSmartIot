# Generated by Django 4.2.3 on 2024-06-12 09:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agrosmartiotweb', '0052_alter_jornada_hora_creacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jornada',
            name='hora_creacion',
            field=models.TimeField(default=datetime.time(5, 18, 29, 190128), editable=False),
        ),
        migrations.AlterField(
            model_name='procesos',
            name='hora_creacion',
            field=models.TimeField(default=datetime.time(5, 18, 29, 190128), editable=False),
        ),
    ]