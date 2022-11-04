# Generated by Django 4.0.4 on 2022-09-26 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0037_contratista'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto1',
            name='contratista2_casa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='opcion2', to='proyectos.contratista', verbose_name='Contratista De Pintura:'),
        ),
        migrations.AlterField(
            model_name='proyecto1',
            name='contratista_casa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='opcion1', to='proyectos.contratista', verbose_name='Contratista De Estuco'),
        ),
    ]
