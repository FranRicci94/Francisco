
from django.urls import path

from  .views import (hermanos, inicio, lista_hermanos, lista_nietos,
                            lista_padres, nietos, padres)

urlpatterns = [
    path('padres/<nombre>/<edad>/<apellido>', padres),
    path('hermanos/<nombre>/<edad>/<apellido>', hermanos),
    path('nietos/<nombre>/<edad>/<apellido>', nietos),
    path("lista-hermanos", lista_hermanos, name="listahermanos"),
    path("lista-padres", lista_padres, name="listapadres"),
    path("padres/", padres),
    path("nietos/", nietos, name="Nietos"),
    path("hermanos/", hermanos),
    path("", inicio, name="inicio"),
]