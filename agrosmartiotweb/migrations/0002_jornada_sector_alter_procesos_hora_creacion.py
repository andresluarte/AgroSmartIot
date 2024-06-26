# Generated by Django 4.2.3 on 2023-08-27 17:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agrosmartiotweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jornada',
            name='sector',
            field=models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, to='agrosmartiotweb.sector'),
        ),
        migrations.AlterField(
            model_name='procesos',
            name='hora_creacion',
            field=models.TimeField(default=datetime.time(13, 17, 35, 510334), editable=False),
        ),
    ]
