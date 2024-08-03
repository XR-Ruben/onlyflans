from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(req):
    return HttpResponse("MI PAGINA DE INICIO DE LA APP")

def hola_mundo(req):
    return HttpResponse("Hola Mundo!!!")

def adios_mundo(req):
    return HttpResponse("BYE BYE BYE, Adios Mundo Cruel!!!")

def part_html(req):
    return HttpResponse("<h1>HOLA SOY UN H1 >>> MUNDO!!!</h1>")

def template_dinamico(req):
    context = {
        "message": "Estoy utilizando un template dinámico!!!"
    }
    return render(req, 'index.html', context)