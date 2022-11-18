from django.contrib import admin
from .models import Notificacion
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
# Register your models here.

class NotificacionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
        search_fields=('nombre',)
        list_filter=('nombre',)
        list_per_page = 3
        date_hierarchy = 'created_at'
        list_display=( 
        'nombre',
        'content')

admin.site.register(Notificacion, NotificacionAdmin)