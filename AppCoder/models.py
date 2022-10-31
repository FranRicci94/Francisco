from django.db import models


class Padres(models.Model):

    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    apellido = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.nombre}, {self.apellido}'

class Hermanos(models.Model):

    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    apellido = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.nombre}, {self.apellido}'

class Nietos(models.Model):

    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    apellido = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return f'{self.nombre}, {self.apellido}'