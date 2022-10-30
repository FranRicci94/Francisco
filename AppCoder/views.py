# from http.client import HttpResponse

from cgitb import html
from django.http import HttpResponse
from django.shortcuts import render

from AppCoder.models import Hermanos, Nietos, Padres


def hermanos(request, nombre, edad, apellido) -> HttpResponse:
    hermano = Hermanos(nombre=nombre, edad=edad, apellido=apellido)
    hermano.save()
    DocumentoDeTexto = f"--->nombre: {hermano.nombre}, edad: {hermano.edad}, apellido: {hermano.apellido} se agrego"

    return HttpResponse(DocumentoDeTexto)


def padres(request, nombre, edad, apellido) -> HttpResponse:
    padre = Padres(nombre=nombre, edad=edad, apellido=apellido)
    padre.save()
    DocumentoDeTexto = f"--->nombre: {padre.nombre}, edad: {padre.edad}, apellido: {padre.apellido} se agrego"

    return HttpResponse(DocumentoDeTexto)


def nietos(request, nombre, edad, apellido) -> HttpResponse:
    nieto = Nietos(nombre=nombre, edad=edad, apellido=apellido)
    nieto.save()
    DocumentoDeTexto = f"--->nombre: {nieto.nombre}, edad: {nieto.edad}, apellido: {nieto.apellido} se agrego"

    return HttpResponse(DocumentoDeTexto)


def lista_hermanos(request) -> HttpResponse:

    lista = Hermanos.objects.all()

    return render(request, "lista_hermanos.html", {"lista_hermanos": lista})


def lista_padres(request) -> HttpResponse:

    lista = Padres.objects.all()

    return render(request, "lista_padres.html", {"lista_padres": lista})


def lista_nietos(request) -> HttpResponse:

    lista = Nietos.objects.all()

    return render(request, "lista_nietos.html", {"lista_nietos": lista})


def inicio(request):

    return render(request,"vista_inicio.html")

def padres(request):

    return render(request,"lista_padres.html")

def hermanos(request):

    return render(request,"lista_hermanos.html")

def nietos(request):

    return render(request,"lista_nietos.html")