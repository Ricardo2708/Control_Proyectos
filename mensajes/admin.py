from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display=( 
        'mensaje',
    )


# Register your models here.
admin.site.register(Message,MessageAdmin)
