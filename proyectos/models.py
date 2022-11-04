from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import connection
from django.core.exceptions import ValidationError
from datetime import datetime
from django.db.models import Sum
from decimal import Decimal

ESTADO = (
    ('Inicio', 'Inicio'),
    ('Cobro', 'Cobro'),
    ('Final', 'Final'),
)

class Contratista(models.Model):
    nombre_persona = models.CharField(unique = True, max_length=100, verbose_name="Nombre")
    dui_persona = models.CharField(unique = True, max_length=100, verbose_name="Dui")
    nit_persona = models.CharField(unique = True, max_length=100, verbose_name="Nit")
    tel_persona = models.CharField(verbose_name='Telefono', blank=True, max_length=9, default='0000-0000', unique=True)
    estado_contratista = models.BooleanField(verbose_name="Estado Del Contratista", default=True)
    content = models.TextField(verbose_name="Comentarios", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado El ')
    updated_at = models.DateTimeField(auto_now =True, verbose_name='Actualizado El ')
    
    class Meta:
        verbose_name = "Contratista"
        verbose_name_plural = "Contratistas"
        
    def __str__(self):
        return f'{self.nombre_persona}'

class Agrupaciones(models.Model):
    codigo = models.CharField(unique = True, max_length=100, verbose_name="Codigo De Obra")
    modelo_casa = models.CharField(max_length=100, verbose_name="Modelo:")
    nombre_agru = models.CharField(max_length=100, verbose_name="Agrupacion" ,default='AGRUPACION N°')
    descripcion_material = models.CharField(max_length=100, verbose_name="Descripcion")
    precio_casa = models.FloatField(verbose_name="Precio Interno", default=0)
    precio_contratista = models.FloatField(verbose_name="Precio Contratista", default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado El ')
    updated_at = models.DateTimeField(auto_now =True, verbose_name='Actualizado El ')
    
    class Meta:
        verbose_name = "Codigo De Obra"
        verbose_name_plural = " Codigos De Obra"
    
    def clean(self):
        self.modelo_casa = (self.modelo_casa).upper()   
        self.descripcion_material = (self.descripcion_material).upper()   

    def save(self, *args, **kwargs):
        super(Agrupaciones, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.codigo} | {self.modelo_casa} | {self.nombre_agru} | {self.descripcion_material} | {self.precio_casa} | {self.precio_contratista}\n'

class Adicionales(models.Model):
    codigo = models.CharField(unique = True, max_length=100, verbose_name="Codigo De Obra")
    modelo_casa = models.CharField(max_length=100, verbose_name="Modelo:")
    kit = models.CharField(max_length=100, verbose_name="Kit De Vivienda")
    unidad_medida = models.CharField(max_length=100, verbose_name="Unidad De Medida")
    precio_cobro = models.FloatField(verbose_name="Precio Cobro", default=0)
    precio_pago = models.FloatField(verbose_name="Precio Pago", default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado El ')
    updated_at = models.DateTimeField(auto_now =True, verbose_name='Actualizado El ')
    
    class Meta:
        verbose_name = "Adicional"
        verbose_name_plural = "Adicionales"
    
    def clean(self):
        self.modelo_casa = (self.modelo_casa).upper()   
        self.kit = (self.kit).upper()   
        self.unidad_medida = (self.unidad_medida).upper()  

    def save(self, *args, **kwargs):
        super(Adicionales, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.codigo} | {self.modelo_casa} | {self.kit} | {self.unidad_medida} | {self.precio_cobro} | {self.precio_pago}\n'

# Create your models here.
class Proyecto1(models.Model):
    #* Campo General
    cluster_casa = models.CharField(max_length=100, verbose_name="Cluster:")
    poligono_casa = models.CharField(max_length=100, verbose_name="Poligono:")
    numero_casa = models.IntegerField(verbose_name="Numero De Casa:")
    modelo_casa = models.CharField(max_length=100, verbose_name="Modelo:")
    obra = models.ManyToManyField(Agrupaciones, verbose_name="Codigo De Obra")
    porcentaje_casa = models.FloatField(verbose_name="Porcentaje %:",default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ],)
    contratista_casa = models.ForeignKey(Contratista,verbose_name="Contratista De Estuco",on_delete=models.PROTECT, related_name='opcion1')
    contratista2_casa = models.ForeignKey(Contratista, verbose_name="Contratista De Pintura:",on_delete=models.PROTECT,related_name='opcion2')
    estado_contratista = models.BooleanField(verbose_name="Cambio De Contratista:", help_text='Si / No', default=False)
    orden_casa = models.CharField(max_length=100, verbose_name="N° De Orden:", help_text='No Se Recomiendo Usar Caracteres Extraños: */_&%$#')
    estado_casa = models.CharField(max_length=100, choices=ESTADO , verbose_name="Orden De Trabajo:",default=ESTADO[0], help_text='Una Vez Finalizado No Se Podra Realizar Cambios')
    num_planilla = models.CharField(max_length=100, verbose_name="Planilla:", default='P', help_text='Numero De Planilla - Ejemplo:(P1)')
    content = models.TextField(verbose_name="Comentarios:", blank=True, help_text='Si No Tiene Comentarios Puede Dejar Este Campo Vacio')
    estado_final = models.BooleanField(verbose_name="Obra Finalizada:", help_text='Si / No',default=False, editable=False)
    fecha_final = models.CharField(max_length=100,verbose_name='Fecha De Actualizacion:', editable=False)
    precio = models.FloatField(verbose_name="Obra: $", default=0)
    subtotal = models.FloatField(verbose_name="Sub Total: $", default=0)
    total_casa = models.FloatField(verbose_name="Total: $", default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha De Creacion El:')
    updated_at = models.DateTimeField(auto_now =True, verbose_name='Fecha De Actualizacion:')

    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Nueva San Miguel"

    def get_fecha(self):
        fecha = self.created_at
        fecha1 = fecha.strftime('%d/%m/%Y %H:%M')
        return fecha1

    def get_products(self):
        return ", ".join([p.codigo for p in self.obra.all()] )

    def clean(self): 
        try:
            if self.contratista_casa.estado_contratista != True:
                raise ValidationError(f"El Contratista {self.contratista_casa} Esta Inactivo")
            elif self.contratista2_casa.estado_contratista != True:
                raise ValidationError(f"El Contratista ({self.contratista2_casa}) Esta Inactivo")
        except:
            raise ValidationError(f"Ocurrio Un Error (Revisa Los Campos Marcados En Rojo)")

        self.poligono_casa = (self.poligono_casa).upper()   
        self.modelo_casa = (self.modelo_casa).upper()  
        if self.updated_at == None:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM proyectos_proyecto1 WHERE cluster_casa = '{self.cluster_casa}' AND poligono_casa = '{self.poligono_casa}' AND numero_casa = '{self.numero_casa}' ")
                datos = cursor.fetchall()
                cursor.close()
            if len(datos) > 0:
                raise ValidationError("Ya Existe Ese Registro De La Obra")

        if len(self.fecha_final) > 0:
            raise ValidationError("La Obra Ya Fue Finalizada")
        else:
            if self.estado_casa == 'Final':
                self.estado_final = True
                if self.estado_final:
                    today = datetime.today().strftime('%d/%m/%Y %H:%M')
                    self.fecha_final = today
            
    def save(self, *args, **kwargs):
        try:
            super(Proyecto1, self).save(*args, **kwargs)
        except:
            raise ValidationError("Se A Producido Un Error")
        
    def __str__(self, *args, **kwargs):
        if len(self.fecha_final) > 0:
            self.precio = self.precio
            self.subtotal = self.subtotal
            self.total_casa = self.total_casa
        else:
            #* Primer Calculo (Campo De: Obra)
            obras_suma = self.obra.all().aggregate(Sum('precio_casa'))
            resultado = obras_suma['precio_casa__sum']
            calculo = self.porcentaje_casa * resultado / 100
            self.precio = round(Decimal(calculo), 2) 

            #* Segundo Calculo (Campo De: Sub Total)
            obras_suma2 = self.obra.all().aggregate(Sum('precio_contratista'))
            resultado2 = obras_suma2['precio_contratista__sum']
            calculo2 = self.porcentaje_casa * resultado2 / 100
            self.subtotal = round(Decimal(calculo2), 2) 

            #* Tercer Calculo (Campo De: Total)
            obras_suma3 = self.obra.all().aggregate(Sum('precio_contratista'))
            resultado3 = obras_suma3['precio_contratista__sum']
            calculo3 = self.porcentaje_casa * resultado3 / 100
            final3 = round(calculo3, 2)
            total_calculo = final3 / 0.9
            self.total_casa = round(Decimal(total_calculo), 2) 
        
            super(Proyecto1, self).save(*args, **kwargs)
        datos = f'📂 Cluster: {self.cluster_casa} | Modelo: {self.modelo_casa} | Poligono: {self.poligono_casa} | N° De Casa: {self.numero_casa}'
        return datos

class Proyecto1_Adicional(models.Model):
    #* Campo General
    cluster_casa = models.CharField(max_length=100, verbose_name="Cluster:")
    poligono_casa = models.CharField(max_length=100, verbose_name="Poligono:")
    numero_casa = models.IntegerField(verbose_name="Numero De Casa:")
    modelo_casa = models.CharField(max_length=100, verbose_name="Modelo:")
    obra = models.ManyToManyField(Adicionales, verbose_name="Codigo De Obra")
    porcentaje_casa = models.FloatField(verbose_name="Porcentaje %:",default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ],)
    contratista_casa = models.ForeignKey(Contratista,verbose_name="Contratista",on_delete=models.PROTECT, related_name='opcion1_adicional')
    estado_contratista = models.BooleanField(verbose_name="Cambio De Contratista:", help_text='Si / No', default=False)
    orden_casa = models.CharField(max_length=100, verbose_name="N° De Orden:", help_text='No Se Recomiendo Usar Caracteres Extraños: */_&%$#')
    estado_casa = models.CharField(max_length=100, choices=ESTADO , verbose_name="Orden De Trabajo:",default=ESTADO[0], help_text='Una Vez Finalizado No Se Podra Realizar Cambios')
    num_planilla = models.CharField(max_length=100, verbose_name="Planilla:", default='P', help_text='Numero De Planilla - Ejemplo:(P1)')
    content = models.TextField(verbose_name="Comentarios:", blank=True, help_text='Si No Tiene Comentarios Puede Dejar Este Campo Vacio')
    estado_final = models.BooleanField(verbose_name="Obra Finalizada:", help_text='Si / No',default=False, editable=False)
    fecha_final = models.CharField(max_length=100,verbose_name='Fecha De Actualizacion:', editable=False)
    precio = models.FloatField(verbose_name="Obra: $", default=0)
    subtotal = models.FloatField(verbose_name="Sub Total: $", default=0)
    total_casa = models.FloatField(verbose_name="Total: $", default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha De Creacion El:')
    updated_at = models.DateTimeField(auto_now =True, verbose_name='Fecha De Actualizacion:')

    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Nueva San Miguel (Add)"

    def get_fecha(self):
        fecha = self.created_at
        fecha1 = fecha.strftime('%d/%m/%Y %H:%M')
        return fecha1

    def get_products(self):
        return ", ".join([p.codigo for p in self.obra.all()] )

    def clean(self): 
        try:
            if self.contratista_casa.estado_contratista != True:
                raise ValidationError(f"El Contratista {self.contratista_casa} Esta Inactivo")
            elif self.contratista2_casa.estado_contratista != True:
                raise ValidationError(f"El Contratista ({self.contratista2_casa}) Esta Inactivo")
        except:
            raise ValidationError(f"Ocurrio Un Error (Revisa Los Campos Marcados En Rojo)")

        self.poligono_casa = (self.poligono_casa).upper()   
        self.modelo_casa = (self.modelo_casa).upper()  
        if self.updated_at == None:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM proyectos_proyecto1 WHERE cluster_casa = '{self.cluster_casa}' AND poligono_casa = '{self.poligono_casa}' AND numero_casa = '{self.numero_casa}' ")
                datos = cursor.fetchall()
                cursor.close()
            if len(datos) > 0:
                raise ValidationError("Ya Existe Ese Registro De La Obra")

        if len(self.fecha_final) > 0:
            raise ValidationError("La Obra Ya Fue Finalizada")
        else:
            if self.estado_casa == 'Final':
                self.estado_final = True
                if self.estado_final:
                    today = datetime.today().strftime('%d/%m/%Y %H:%M')
                    self.fecha_final = today
            
    def save(self, *args, **kwargs):
        super(Proyecto1_Adicional, self).save(*args, **kwargs)
        
    def __str__(self, *args, **kwargs):
        if len(self.fecha_final) > 0:
            self.precio = self.precio
            self.subtotal = self.subtotal
            self.total_casa = self.total_casa
        else:
            #* Primer Calculo (Campo De: Obra)
            obras_suma = self.obra.all().aggregate(Sum('precio_cobro'))
            resultado = obras_suma['precio_cobro__sum']
            calculo = self.porcentaje_casa * resultado
            self.precio = round(Decimal(calculo), 2) 

            #* Segundo Calculo (Campo De: Sub Total)
            obras_suma2 = self.obra.all().aggregate(Sum('precio_pago'))
            resultado2 = obras_suma2['precio_pago__sum']
            calculo2 = self.porcentaje_casa * resultado2 
            self.subtotal = round(Decimal(calculo2), 2) 

            #* Tercer Calculo (Campo De: Total)
            obras_suma3 = self.obra.all().aggregate(Sum('precio_pago'))
            resultado3 = obras_suma3['precio_pago__sum']
            calculo3 = self.porcentaje_casa * resultado3
            final3 = round(calculo3, 2)
            total_calculo = final3 / 0.9
            self.total_casa = round(Decimal(total_calculo), 2) 
        
            super(Proyecto1_Adicional, self).save(*args, **kwargs)
        datos = f'📂 Cluster: {self.cluster_casa} | Modelo: {self.modelo_casa} | Poligono: {self.poligono_casa} | N° De Casa: {self.numero_casa}'
        return datos
