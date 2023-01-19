from contextvars import Context
import os
from django.http import HttpResponse
from jinja2 import Template

def saludo(request):
    
    mihtml = open(os.getcwd() + '/Proyecto1/plantillas/ejemplo.html')
    plantilla = Template(mihtml.read())
    
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)

