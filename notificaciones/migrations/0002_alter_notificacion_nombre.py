# Generated by Django 4.0.4 on 2022-11-10 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notificaciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificacion',
            name='nombre',
            field=models.CharField(default='Administrador:', max_length=100, verbose_name='Nombre:'),
        ),
    ]
