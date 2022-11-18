# Generated by Django 4.0.4 on 2022-09-06 14:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0017_alter_proyecto1_estado_contratista_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto1',
            name='contratista_casa',
            field=models.CharField(max_length=50, verbose_name='Contratista'),
        ),
        migrations.AlterField(
            model_name='proyecto1',
            name='estado_contratista',
            field=models.BooleanField(default=True, help_text='Activo / Inactivo', verbose_name='Estado Del Contratista'),
        ),
        migrations.AlterField(
            model_name='proyecto1',
            name='modelo_casa',
            field=models.CharField(max_length=50, verbose_name='Modelo'),
        ),
        migrations.AlterField(
            model_name='proyecto1',
            name='obra_casa',
            field=models.CharField(choices=[('N°1 (Estucos)  / Precio: $752 / Precio C:  $275,06', '4587'), ('N°2 (Resanes) / Precio: 20500.0 / Precio C: 4512.0', '4211'), ('N°3 (Pinturas) / Precio: 150.0 / Precio C: 150.0', '4208'), ('N°4 (Textury) / Precio: 1234.0 / Precio C: 1234.0', '7897')], max_length=50, verbose_name='Codigo'),
        ),
        migrations.AlterField(
            model_name='proyecto1',
            name='poligono_casa',
            field=models.CharField(max_length=50, verbose_name='Poligono'),
        ),
        migrations.AlterField(
            model_name='proyecto1',
            name='vales_casa',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(0)], verbose_name='N° Vales'),
        ),
    ]