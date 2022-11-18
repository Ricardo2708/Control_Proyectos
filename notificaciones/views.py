from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db import connection
# Create your views here.
def index2(request):
    if request.method == 'GET':
        with connection.cursor() as cursor:
            cursor.execute("SELECT nombre,content,created_at FROM notificaciones_notificacion")
            datos = cursor.fetchall()
            cursor.close()
        return JsonResponse({'Mensajes': datos,})
    else:
        return HttpResponse("Peticion no valida")