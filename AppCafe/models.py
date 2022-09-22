from django.db import models

# Create your models here.


class Cafe(models.Model):

    origen = models.CharField(max_length=100)
    molienda = models.CharField(max_length=100)

class Metodos(models.Model):
    metodo = models.CharField(max_length=100)

class Peso(models.Model):
    gramos = models.IntegerField()