from django.db import models

class Termek(models.Model):
    Azon = models.CharField(max_length=10)
    Nev = models.CharField(max_length=100)
    Kategoria = models.CharField(max_length=50)
    Kiszereles = models.CharField(max_length=10)
    Ar=models.IntegerField()
    
