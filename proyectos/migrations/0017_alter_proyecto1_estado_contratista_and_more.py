# Generated by Django 4.0.4 on 2022-09-06 13:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0016_remove_proyecto1_agrupacion_casa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto1',
            name='estado_contratista',
            field=models.BooleanField(default=True, help_text='Contratista Activo O Inactivo', verbose_name='Estado Del Contratista'),
        ),
        migrations.AlterField(
            model_name='proyecto1',
            name='obra_casa',
            field=models.CharField(choices=[('4587', 'AGRUPACION N°1'), ('4211', 'AGRUPACION N°2'), ('4208', 'AGRUPACION N°3'), ('7897', 'AGRUPACION N°4')], max_length=50, verbose_name='Codigo & Agrupacion'),
        ),
        migrations.AlterField(
            model_name='proyecto1',
            name='porcentaje_casa',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)], verbose_name='Porcentaje %'),
        ),
    ]
