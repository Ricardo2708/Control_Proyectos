# Generated by Django 4.0.4 on 2022-09-13 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0025_alter_proyecto1_options_remove_proyecto1_obra_casa_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto1',
            name='contratista2_casa',
            field=models.CharField(choices=[('Josue Vega', 'Josue Vega'), ('Ricardo Martinez', 'Ricardo Martinez'), ('Ricardo Vega', 'Ricardo Vega')], default=1, max_length=100, verbose_name='Contratista De Pintura:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='proyecto1',
            name='contratista_casa',
            field=models.CharField(choices=[('Josue Vega', 'Josue Vega'), ('Ricardo Martinez', 'Ricardo Martinez'), ('Ricardo Vega', 'Ricardo Vega')], max_length=100, verbose_name='Contratista De Estuco:'),
        ),
        migrations.AlterField(
            model_name='proyecto1',
            name='orden_casa',
            field=models.CharField(help_text='No Se Recomiendo Usar Caracteres Extraños: */_&%$#', max_length=100, verbose_name='N° De Orden:'),
        ),
    ]