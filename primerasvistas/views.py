from django.http import HttpResponse
from datetime import datetime
from django.template import loader

from primerasvistas.models import Perro

def inicio(request):
    return HttpResponse('Hola soy mi primer vista en django')

def ver_fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f'Fecha actual: {fecha_actual}')

def saludo(request, nombre):
    return HttpResponse(f'Hola {nombre}')

def mi_template(request):
    template1 = loader.get_template('prueba.html')
    nombre = 'manuelito'
    apellido = 'danieli'
    lista = [1,2,3,4,5,6,7]
    perro = Perro(nombre='Leon', edad=12)
    perro.save()
    render1 = template1.render({'nombre':nombre, 'apellido':apellido, 'edad':55, 'lista' : lista, 'perro': perro })
    return HttpResponse(render1)
