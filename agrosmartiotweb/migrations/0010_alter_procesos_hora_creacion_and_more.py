# Generated by Django 4.2.3 on 2023-09-08 02:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agrosmartiotweb', '0009_alter_procesos_hora_creacion_alter_procesos_huerto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procesos',
            name='hora_creacion',
            field=models.TimeField(default=datetime.time(23, 7, 29, 700332), editable=False),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='fecha_termino_contrato',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='tipo_contraro',
            field=models.CharField(choices=[('Indefinido', 'Indefinido'), ('Plazo fijo', 'Plazo fijo'), ('Honorario', 'Honorario'), ('Sin Contraro', 'Sin Contrato')], default='Plazo fijo', max_length=15),
        ),
    ]
