from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(req):
    return HttpResponse("Bienvenidos a ONLYFLANS")

def hola_mundo(req):
    return HttpResponse("Hola Mundo!!!")

def adios_mundo(req):
    return HttpResponse("BYE BYE BYE, Adios Mundo Cruel!!!")

def part_html(req):
    return HttpResponse("<h1>HOLA SOY UN H1 >>> MUNDO!!!</h1>")


def home(req):
    context = {
        "message": "ONLYFLANS"
    }
    return render(req, 'base.html', context)