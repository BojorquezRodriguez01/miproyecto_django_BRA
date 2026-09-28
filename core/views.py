from django.shortcuts import render
from django.db import connection

def inicio(request):
    info_bd = connection.settings_dict
    contexto = {
        'motor': info_bd['ENGINE'],
        'host': info_bd['HOST'],
    }
    return render(request, 'core/inicio.html', contexto)

def servicios(request):
    lista_servicios = [
        {'nombre': 'Tutorías de programación', 'precio': 150},
        {'nombre': 'Diseño de logotipos', 'precio': 300},
        {'nombre': 'Repostería por encargo', 'precio': 120},
    ]
    return render(request, 'core/servicios.html', {'servicios': lista_servicios})