# Generated by Django 4.2.3 on 2023-09-08 02:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agrosmartiotweb', '0012_alter_procesos_hora_creacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procesos',
            name='hora_creacion',
            field=models.TimeField(default=datetime.time(23, 43, 52, 79568), editable=False),
        ),
    ]
