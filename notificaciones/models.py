from django.db import models
# Create your models here.

class Notificacion(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre:", default="Administrador:")
    content = models.TextField(verbose_name="Contenido:")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado El ')
    updated_at = models.DateTimeField(auto_now =True, verbose_name='Actualizado El ')
    
    class Meta:
        verbose_name = "Notificacion"
        verbose_name_plural = "Notificaciones"
        
    def __str__(self):
        return f'{self.nombre}'