from django.db import models

class Pasajero(models.Model):

    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=40)
    edad=models.IntegerField()
    

class Viaje(models.Model):
    
    id=models.AutoField(primary_key=True)
    pasajero=models.CharField(max_length=80)
    origen=models.CharField(max_length=80)
    destino=models.CharField(max_length=80)
    
    
class Equipaje(models.Model):
    
    id=models.AutoField(primary_key=True)
    pasajero=models.CharField(max_length=80)
    peso=models.DecimalField(decimal_places=2,max_digits=10)
    tipo=models.CharField(max_length=80)