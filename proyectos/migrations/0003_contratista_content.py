# Generated by Django 4.0.4 on 2022-08-13 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0002_contratista'),
    ]

    operations = [
        migrations.AddField(
            model_name='contratista',
            name='content',
            field=models.TextField(blank=True, verbose_name='Comentarios'),
        ),
    ]
