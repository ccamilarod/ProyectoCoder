from django.shortcuts import render
from django.http import HttpResponse
from AppCafe.models import Cafe
from AppCafe.models import Metodos
from AppCafe.models import Peso
from AppCafe.forms import *

# Create your views here.
def inicio(request):
    return render(request, "AppCafe/inicio.html")

def cafe(request):
    
    C = Cafe(origen = "Colombia", molienda = "Gruesa",)
    C.save()

    return render(request, "AppCafe/cafe.html")

def metodos(request):
    m = Metodos(metodo = "Chemex",)
    m.save()
    return render(request, "AppCafe/metodo.html")

def peso(request):
    p = Peso(gramos = 250)
    p.save()
    return render(request, "AppCafe/peso.html")

def cafeFormulario(request):

    if request.method == "POST":
        formulario1 = CafeFormulario(request.POST)
        if formulario1.is_valid():
            info = formulario1.cleaned_data
            cafe = Cafe(origen=info["origen"], molienda = info["molienda"])
            cafe.save()
            return render(request, "AppCafe/inicio.html")
    else:
        formulario1= CafeFormulario()
    return render(request, "AppCafe/cafeFormulario.html", {"form1":formulario1})

def metodoFormulario(request):

    if request.method == "POST":
        formulario2 = MetodoFormulario(request.POST)
        if formulario2.is_valid():
            info = formulario2.cleaned_data
            metodos = Metodos(metodo=info["metodo"])
            metodos.save()
            return render(request, "AppCafe/inicio.html")
    else:
        formulario2= MetodoFormulario()
    return render(request, "AppCafe/metodoFormulario.html", {"form2":formulario2})

def pesoFormulario(request):

    if request.method == "POST":
        formulario3 = PesoFormulario(request.POST)
        if formulario3.is_valid():
            info = formulario3.cleaned_data
            gr = Peso(gramos=info["gramos"])
            gr.save()
            return render(request, "AppCafe/inicio.html")
    else:
        formulario3= PesoFormulario()
    return render(request, "AppCafe/pesoFormulario.html", {"form3":formulario3})











def busquedaOrigen(request):

    return render(request,"AppCafe/inicio.html")

def resultados(request):
    if request.GET["origen"]:
        origen =request.GET["origen"]
        cafe = Cafe.objects.filter(origen__icontains=origen)

        return render(request,"AppCafe/inicio.html", {"cafe": cafe, "origen": origen})
    else:
        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)