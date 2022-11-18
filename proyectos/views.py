from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db import connection
# Create your views here.





def index(request):
    if request.method == 'GET':
        name_db= "proyectos_proyecto1"
        name_proyecto = "Ecoterra Maquilishuat"
        name_array = name_db.split('_')
        if len(name_array) > 2:
            final_path = f"{name_array[1]}_{name_array[2]}"
        else:
            final_path = f"{name_array[1]}"
        name_path = f'/proyectos/{final_path}/'
        with connection.cursor() as cursor:

            #? Busqueda Del Porcentaje De Estado de Obra

            cursor.execute(f"SELECT estado_casa FROM {name_db} WHERE estado_casa = 'Inicio'")
            datos = cursor.fetchall()

            cursor.execute(f"SELECT estado_casa FROM {name_db} WHERE estado_casa = 'Cobro'")
            datos2 = cursor.fetchall()

            cursor.execute(f"SELECT estado_casa FROM {name_db} WHERE estado_casa = 'Final'")
            datos3 = cursor.fetchall()

            #? Busqueda del cambio de contratista

            cursor.execute(f"SELECT estado_contratista FROM {name_db} WHERE estado_contratista = 1")
            datos4 = cursor.fetchall()

            cursor.execute(f"SELECT estado_contratista FROM {name_db} WHERE estado_contratista = 0")
            datos4_2 = cursor.fetchall()

            #? Busqueda Del Porcentaje De Las casas

            cursor.execute(f"SELECT porcentaje_casa FROM {name_db} WHERE porcentaje_casa = 0")
            datos5 = cursor.fetchall()

            cursor.execute(f"SELECT porcentaje_casa FROM {name_db} WHERE porcentaje_casa = 50")
            datos6 = cursor.fetchall()

            cursor.execute(f"SELECT porcentaje_casa FROM {name_db} WHERE porcentaje_casa = 100")
            datos7 = cursor.fetchall()

            cursor.close()
        return JsonResponse({'inicio': datos, 
                            'cobro' : datos2, 
                            'final' : datos3, 
                            'activo': datos4, 
                            'inactivo':datos4_2,
                            'proyecto' : name_proyecto,
                            'porcentaje1': datos5,
                            'porcentaje2': datos6,
                            'porcentaje3': datos7,
                            'path': name_path})
    else:
        return HttpResponse("Peticion no valida")
