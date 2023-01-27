from contextvars import Context
import os
from django.http import HttpResponse
from jinja2 import Template
from django.shortcuts import render

from Proyecto1.models import Equipaje, Pasajero, Viaje

def inicio(request):
    
    return render(request, 'index.html')


def ingresoPasajero(request):
    
    if request.method == 'POST':
        
        pasajero = Pasajero(nombre=request.POST['nombre'],edad=request.POST['edad'])
        pasajero.save()
        return render(request, 'index.html')

        
    return render(request, 'ingresoPasajero.html')

def ingresoViaje(request):
    
    if request.method == 'POST':
        
        viaje = Viaje(pasajero=request.POST['pasajero'],origen=request.POST['origen'],destino=request.POST['destino'])
        viaje.save()
        return render(request, 'index.html')

        
    return render(request, 'ingresoViaje.html')


def ingresoEquipaje(request):
    
    if request.method == 'POST':
        
        equipaje = Equipaje(pasajero=request.POST['pasajero'],peso=request.POST['peso'],tipo=request.POST['tipo'])
        equipaje.save()
        return render(request, 'index.html')

        
    return render(request, 'ingresoEquipaje.html')


def busquedaPasajero(request):
    
    if request.method == 'POST':
        
        nombre=request.POST['nombre']
        pasajeros = Pasajero.objects.filter(nombre=nombre)
        return render(request, 'busquedaPasajero.html', {"pasajeros": pasajeros})

        
    return render(request, 'busquedaPasajero.html')
