# Generated by Django 4.0.4 on 2022-11-10 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0053_alter_proyecto1_adicional_contratista_casa'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proyecto1',
            options={'verbose_name': 'Registro', 'verbose_name_plural': 'EcoTerra Santa Ana'},
        ),
        migrations.AlterModelOptions(
            name='proyecto1_adicional',
            options={'verbose_name': 'Registro', 'verbose_name_plural': 'EcoTerra Santa Ana (Add)'},
        ),
        migrations.AlterField(
            model_name='agrupaciones',
            name='codigo',
            field=models.CharField(max_length=100, unique=True, verbose_name='Codigo'),
        ),
        migrations.AlterField(
            model_name='agrupaciones',
            name='modelo_casa',
            field=models.CharField(max_length=100, verbose_name='Modelo'),
        ),
        migrations.AlterField(
            model_name='agrupaciones',
            name='nombre_agru',
            field=models.CharField(default='AGRUPACION N°', max_length=100, verbose_name='Agrupaciones'),
        ),
    ]