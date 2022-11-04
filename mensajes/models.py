from django.db import models
from django.contrib import admin

# Create your models here.
class Message(models.Model):
    mensaje = models.CharField(max_length=100, verbose_name="Mensaje")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado El ')
    updated_at = models.DateTimeField(auto_now =True, verbose_name='Actualizado El ')

    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Mensajes"

    def clean(self):
        new_title = self.mensaje
        subtitle = "Administracion"

        admin.site.site_header =  new_title
        admin.site.site_title = new_title
        admin.site.index_title = subtitle

    def save(self, *args, **kwargs):
        super(Message, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.mensaje}'