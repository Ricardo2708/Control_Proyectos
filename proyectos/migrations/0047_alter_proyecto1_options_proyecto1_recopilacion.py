# Generated by Django 4.0.4 on 2022-10-04 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0046_remove_proyecto1_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proyecto1',
            options={'verbose_name': 'Registro', 'verbose_name_plural': '📋 Nueva San Miguel'},
        ),
        migrations.AddField(
            model_name='proyecto1',
            name='recopilacion',
            field=models.CharField(default=1, editable=False, max_length=100, verbose_name='recopilacion:'),
            preserve_default=False,
        ),
    ]
