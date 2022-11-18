# Generated by Django 4.0.4 on 2022-10-08 10:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0050_proyecto1_adicional_proyecto1_contratista3_casa_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyecto1',
            name='adicional',
        ),
        migrations.RemoveField(
            model_name='proyecto1',
            name='contratista3_casa',
        ),
        migrations.RemoveField(
            model_name='proyecto1',
            name='porcentaje_casa2',
        ),
        migrations.CreateModel(
            name='Proyecto1_Adicional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cluster_casa', models.CharField(max_length=100, verbose_name='Cluster:')),
                ('poligono_casa', models.CharField(max_length=100, verbose_name='Poligono:')),
                ('numero_casa', models.IntegerField(verbose_name='Numero De Casa:')),
                ('modelo_casa', models.CharField(max_length=100, verbose_name='Modelo:')),
                ('porcentaje_casa', models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='Porcentaje %:')),
                ('estado_contratista', models.BooleanField(default=False, help_text='Si / No', verbose_name='Cambio De Contratista:')),
                ('orden_casa', models.CharField(help_text='No Se Recomiendo Usar Caracteres Extraños: */_&%$#', max_length=100, verbose_name='N° De Orden:')),
                ('estado_casa', models.CharField(choices=[('Inicio', 'Inicio'), ('Cobro', 'Cobro'), ('Final', 'Final')], default=('Inicio', 'Inicio'), help_text='Una Vez Finalizado No Se Podra Realizar Cambios', max_length=100, verbose_name='Orden De Trabajo:')),
                ('num_planilla', models.CharField(default='P', help_text='Numero De Planilla - Ejemplo:(P1)', max_length=100, verbose_name='Planilla:')),
                ('content', models.TextField(blank=True, help_text='Si No Tiene Comentarios Puede Dejar Este Campo Vacio', verbose_name='Comentarios:')),
                ('estado_final', models.BooleanField(default=False, editable=False, help_text='Si / No', verbose_name='Obra Finalizada:')),
                ('fecha_final', models.CharField(editable=False, max_length=100, verbose_name='Fecha De Actualizacion:')),
                ('precio', models.FloatField(default=0, verbose_name='Obra: $')),
                ('subtotal', models.FloatField(default=0, verbose_name='Sub Total: $')),
                ('total_casa', models.FloatField(default=0, verbose_name='Total: $')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha De Creacion El:')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha De Actualizacion:')),
                ('contratista2_casa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='opcion2_adicional', to='proyectos.contratista', verbose_name='Contratista De Pintura:')),
                ('contratista_casa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='opcion1_adicional', to='proyectos.contratista', verbose_name='Contratista De Estuco')),
                ('obra', models.ManyToManyField(to='proyectos.adicionales', verbose_name='Codigo De Obra')),
            ],
            options={
                'verbose_name': 'Registro',
                'verbose_name_plural': 'Nueva San Miguel',
            },
        ),
    ]