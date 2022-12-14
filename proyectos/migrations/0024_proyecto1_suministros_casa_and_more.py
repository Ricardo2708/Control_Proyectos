# Generated by Django 4.0.4 on 2022-09-09 10:26

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0023_alter_proyecto1_num_planilla'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto1',
            name='suministros_casa',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Inicio', 'Inicio'), ('Cobro', 'Cobro'), ('Final', 'Final')], default=1, max_length=18, verbose_name='Suministros De Materiales'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='proyecto1',
            name='contratista_casa',
            field=models.CharField(choices=[('Ricardo Martinez', 'Ricardo Martinez')], max_length=100, verbose_name='Contratista'),
        ),
        migrations.AlterField(
            model_name='proyecto1',
            name='estado_contratista',
            field=models.BooleanField(default=False, help_text='Si / No', verbose_name='Cambio De Contratista'),
        ),
        migrations.AlterField(
            model_name='proyecto1',
            name='num_planilla',
            field=models.CharField(default='P', max_length=100, verbose_name='Planilla'),
        ),
    ]
