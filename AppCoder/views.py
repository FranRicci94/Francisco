from http.client import HTTPResponse
from django.shortcuts import render
from AppCoder.models import Hermanos
from AppCoder.models import Nietos
from AppCoder.models import Padres

def hermanos(request, nombre, edad, apellido):
    hermano= Hermanos(nombre=nombre, edad=edad, apellido=apellido)
    hermano.save()
    DocumentoDeTexto= (f"--->nombre: {hermano.nombre}, edad: {hermano.edad}, apellido: {hermano.apellido} se agrego")
    
    return HTTPResponse(DocumentoDeTexto)

def padres(request, nombre, edad, apellido):
    padre= Padres(nombre=nombre, edad=edad, apellido=apellido)
    padre.save()
    DocumentoDeTexto= (f"--->nombre: {padre.nombre}, edad: {padre.edad}, apellido: {padre.apellido} se agrego")
    
    return HTTPResponse(DocumentoDeTexto)

def nietos(request, nombre, edad, apellido):
    nieto= Nietos(nombre=nombre, edad=edad, apellido=apellido)
    nieto.save()
    DocumentoDeTexto= (f"--->nombre: {nieto.nombre}, edad: {nieto.edad}, apellido: {nieto.apellido} se agrego")

    return HTTPResponse(DocumentoDeTexto)


def lista_hermanos(request):

    lista= Hermanos.objects.all()

    return  render(request, "lista_hermanos.html", {"lista_hermanos": lista})

def lista_padres(request):

    lista= Padres.objects.all()

    return  render(request, "lista_padres.html", {"lista_padres": lista})

def lista_nietos(request):

    lista= Nietos.objects.all()

    return  render(request, "lista_nietos.html", {"lista_nietos": lista})