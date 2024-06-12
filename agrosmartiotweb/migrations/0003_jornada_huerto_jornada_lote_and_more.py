# Generated by Django 4.2.3 on 2023-08-27 17:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agrosmartiotweb', '0002_jornada_sector_alter_procesos_hora_creacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='jornada',
            name='huerto',
            field=models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, to='agrosmartiotweb.huerto'),
        ),
        migrations.AddField(
            model_name='jornada',
            name='lote',
            field=models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, to='agrosmartiotweb.lote'),
        ),
        migrations.AlterField(
            model_name='procesos',
            name='hora_creacion',
            field=models.TimeField(default=datetime.time(13, 22, 52, 753215), editable=False),
        ),
    ]