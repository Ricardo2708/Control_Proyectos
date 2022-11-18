# Generated by Django 4.0.4 on 2022-09-26 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0033_sauce_proyecto1_obra'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agrupaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100, unique=True, verbose_name='Codigo De Obra')),
                ('nombre_agru', models.CharField(default='AGRUPACION N°', max_length=100, unique=True, verbose_name='Agrupacion')),
                ('descripcion_material', models.CharField(max_length=100, verbose_name='Descripcion')),
                ('precio_casa', models.FloatField(default=0, verbose_name='Precio Interno')),
                ('precio_contratista', models.FloatField(default=0, verbose_name='Precio Contratista')),
                ('content', models.CharField(blank=True, default='N° () / Precio C: $', max_length=100, verbose_name='Informacion')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado El ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado El ')),
            ],
            options={
                'verbose_name': 'Codigo De Obra',
                'verbose_name_plural': '🗂️ Codigos De Obra',
            },
        ),
        migrations.DeleteModel(
            name='Sauce',
        ),
        migrations.AlterField(
            model_name='proyecto1',
            name='obra',
            field=models.ManyToManyField(related_name='sandwiches', to='proyectos.agrupaciones'),
        ),
    ]