# Generated by Django 4.0.4 on 2022-08-25 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0010_rename_proyecto2_proyecto1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyecto1',
            name='progreso_casa',
        ),
    ]
