from django.db import models


class Padres(models.Model):

    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    apellido = models.CharField(max_length=30)


class Hermanos(models.Model):

    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    apellido = models.CharField(max_length=30)


class Nietos(models.Model):

    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    apellido = models.CharField(max_length=30)
