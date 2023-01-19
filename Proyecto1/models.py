from django.db import models

class Pasajero(models.Model):
    
    id=models.AutoField()
    nombre=models.CharField(max_length=40)
    edad=models.IntegerField()
    

class Viaje(models.Model):
    
    id=models.AutoField()
    origen=models.CharField(max_length=80)
    destino=models.CharField(max_length=80)
    
    
class Equipaje(models.Model):
    
    id=models.AutoField()
    peso=models.DecimalField()
    tipo=models.IntegerField()