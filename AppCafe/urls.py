from django.urls import path
from AppCafe.views import *

urlpatterns = [
    path("", inicio, name= "Home"),
    path("cafe/", cafe, name= "Cafe"),
    path("metodo/", metodos, name = "Metodos"),
    path("cantidad/", peso, name = "Cantidad"),
    path("cafeformulario/", cafeFormulario, name = "Formulario"),
    path("metodoformulario/", metodoFormulario, name = "Formulario Metodos"),
    path("pesoformulario/", pesoFormulario, name = "Formulario Cantidad"),
    path("buscar/", busquedaOrigen, name="BuscarOrigen"),
    path("resultado/", resultados, name="ResultadoBusqueda"),


]
