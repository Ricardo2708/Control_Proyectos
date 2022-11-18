from django.contrib import admin
from .models import Proyecto1,Agrupaciones,Contratista,Adicionales,Proyecto1_Adicional
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from django.contrib.auth.admin import UserAdmin

# Inicio De Informacion
class AgrupacionesAdmin(ImportExportModelAdmin,admin.ModelAdmin):
        search_fields=('codigo','modelo_casa',)
        list_filter=('modelo_casa','descripcion_material',)
        list_per_page = 3
        list_display=( 
        'codigo',
        'modelo_casa',
        'nombre_agru',
        'descripcion_material',
        'precio_contratista',
    )

class AdicionalesAdmin(ImportExportModelAdmin,admin.ModelAdmin):
        search_fields=('codigo','modelo_casa',)
        list_filter=('modelo_casa','kit',)
        list_per_page = 3
        list_display=( 
        'modelo_casa',
        'codigo',
        'kit',
        'unidad_medida',
        'precio_pago',
    )
    
class ContratistaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields=('nombre_persona', 'dui_persona')
    list_filter=('created_at','updated_at','estado_contratista')
    list_per_page = 10
    list_display=( 
        'nombre_persona',
        'dui_persona',
        'nit_persona',
        'estado_contratista',
        'tel_persona',

        
    )

# Fin Informacion 

# Inicio De Modelos De los proyectos 
class Proyeto1Resource(resources.ModelResource):
    
    cluster = Field(attribute='cluster_casa', column_name='Cluster')
    poligono = Field(attribute='poligono_casa', column_name='Poligono')
    numero = Field(attribute='numero_casa', column_name='N° Casa')
    modelo = Field(attribute='modelo_casa', column_name='Modelo')
    obra = Field(attribute= 'get_products', column_name='Codigo De Obra')
    # obra2 = Field(attribute= 'get_products2', column_name='Agrupaciones')
    porcentaje = Field(attribute= 'porcentaje_casa', column_name='Porcentaje %')
    contratista1 = Field(attribute= 'contratista_casa', column_name='Contratista De Estuco')
    contratista2 = Field(attribute= 'contratista2_casa', column_name='Contratista De Pintura')
    orden = Field(attribute= 'orden_casa', column_name='N° Orden')
    estado = Field(attribute= 'estado_casa', column_name='Orden De Trabajo')
    planilla = Field(attribute= 'num_planilla', column_name='N° De Planilla')
    creacion = Field(attribute= 'get_fecha', column_name='Creado El:')
    final = Field(attribute= 'fecha_final', column_name='Finalizado El:')
    precio_casa = Field(attribute= 'precio', column_name='Precio:')
    subtotal_casa = Field(attribute= 'subtotal', column_name='Sub total:')
    total = Field(attribute= 'total_casa', column_name='Total:')
    class Meta:
        model = Proyecto1
        exclude = ('id',
            'cluster_casa',
            'poligono_casa',
            'numero_casa',
            'modelo_casa',
            'porcentaje_casa',
            'contratista_casa',
            'contratista2_casa',
            'orden_casa',
            'estado_casa',
            'num_planilla',
            'fecha_final', 
            'precio',
            'subtotal',
            'content', 
            'total_casa',
            'created_at',
            'updated_at',
            'estado_final',
            'estado_contratista'
        )
      
class Proyecto1Admin(ImportExportModelAdmin,admin.ModelAdmin):
    readonly_fields = ('precio','subtotal', 'total_casa')
    search_fields=('modelo_casa','poligono_casa','numero_casa', 'orden_casa','estado_casa', 'num_planilla')
    list_filter=('cluster_casa','poligono_casa', 'num_planilla','contratista_casa','contratista2_casa')
    list_per_page = 10
    resource_class = Proyeto1Resource
    date_hierarchy= 'created_at'
    list_display=( 
        'modelo_casa',
        'cluster_casa',
        'poligono_casa',
        'numero_casa',
        'orden_casa',
        'estado_casa',
        'estado_final'
    )
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Si El Objeto existe
            return self.readonly_fields + ('cluster_casa', 'poligono_casa', 'numero_casa', 'modelo_casa')
        return self.readonly_fields

    

    fieldsets = (
        (
            "Informacion Requerida", {
                "description" : "Datos Del Registro",
                "fields": ("cluster_casa", 
                            "poligono_casa", 
                            "numero_casa", 
                            "modelo_casa", 
                            "obra", 
                            "porcentaje_casa", 
                            "contratista_casa", 
                            "contratista2_casa", 
                            "estado_contratista", 
                            "orden_casa",
                            "estado_casa",
                            "num_planilla",)
            }
        ),
        
        (
            "Informe Del Registro", {
                "description" : "Informacion Adjunta",
                "classes": ("collapse",), 
                "fields": (
                        "precio",
                        "subtotal",
                        "total_casa",
                        "content")
            }
        ),
    )

class Proyeto1_AddResource(resources.ModelResource):
    
    cluster = Field(attribute='cluster_casa', column_name='Cluster')
    poligono = Field(attribute='poligono_casa', column_name='Poligono')
    numero = Field(attribute='numero_casa', column_name='N° Casa')
    modelo = Field(attribute='modelo_casa', column_name='Modelo')
    obra = Field(attribute= 'get_products', column_name='Codigo De Obra')
    # obra2 = Field(attribute= 'get_products2', column_name='Agrupaciones')
    porcentaje = Field(attribute= 'porcentaje_casa', column_name='Porcentaje %')
    contratista1 = Field(attribute= 'contratista_casa', column_name='Contratista De Estuco')
    orden = Field(attribute= 'orden_casa', column_name='N° Orden')
    estado = Field(attribute= 'estado_casa', column_name='Orden De Trabajo')
    planilla = Field(attribute= 'num_planilla', column_name='N° De Planilla')
    creacion = Field(attribute= 'get_fecha', column_name='Creado El:')
    final = Field(attribute= 'fecha_final', column_name='Finalizado El:')
    precio_casa = Field(attribute= 'precio', column_name='Precio:')
    subtotal_casa = Field(attribute= 'subtotal', column_name='Sub total:')
    total = Field(attribute= 'total_casa', column_name='Total:')
    class Meta:
        model = Proyecto1_Adicional
        exclude = ('id',
            'cluster_casa',
            'poligono_casa',
            'numero_casa',
            'modelo_casa',
            'porcentaje_casa',
            'contratista_casa',
            'orden_casa',
            'estado_casa',
            'num_planilla',
            'fecha_final', 
            'precio',
            'subtotal',
            'content', 
            'total_casa',
            'created_at',
            'updated_at',
            'estado_final',
            'estado_contratista'
        )
        
class Proyecto1_AddAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    readonly_fields = ('precio','subtotal', 'total_casa')
    search_fields=('modelo_casa','poligono_casa','numero_casa', 'orden_casa','estado_casa', 'num_planilla')
    list_filter=('cluster_casa','poligono_casa', 'num_planilla','contratista_casa')
    list_per_page = 10
    resource_class = Proyeto1_AddResource
    date_hierarchy= 'created_at'
    list_display=( 
        'modelo_casa',
        'cluster_casa',
        'poligono_casa',
        'numero_casa',
        'orden_casa',
        'estado_casa',
        'estado_final'
    )
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Si El Objeto existe
            return self.readonly_fields + ('cluster_casa', 'poligono_casa', 'numero_casa', 'modelo_casa')
        return self.readonly_fields
    fieldsets = (
        (
            "Informacion Requerida", {
                "description" : "Datos Del Registro",
                "fields": ("cluster_casa", 
                            "poligono_casa", 
                            "numero_casa", 
                            "modelo_casa", 
                            "obra", 
                            "porcentaje_casa", 
                            "contratista_casa", 
                            "estado_contratista", 
                            "orden_casa",
                            "estado_casa",
                            "num_planilla",)
            }
        ),
        (
            "Informe Del Registro", {
                "description" : "Informacion Adjunta",
                "classes": ("collapse",), 
                "fields": ("content",
                        "precio",
                        "subtotal",
                        "total_casa")
            }
        ),
    )
          





# Registro de modelos para el admin
admin.site.register(Agrupaciones,AgrupacionesAdmin)
admin.site.register(Adicionales,AdicionalesAdmin)
admin.site.register(Contratista,ContratistaAdmin)
admin.site.register(Proyecto1,Proyecto1Admin)
admin.site.register(Proyecto1_Adicional,Proyecto1_AddAdmin)
#Configuracion Del Panel
title = "Administracion"
subtitle = "Administracion"

admin.site.site_header =  title
admin.site.site_title = title
admin.site.index_title = subtitle