from django.shortcuts import render
from django.http import HttpResponse
# ----------------------------------------------------------------------------------------------
## VIEWS DE PROYECTO ONLYFLANS

# Create your views here.

def home(req): 
    context = {
        "mensaje": "Elija sus postres:",
        "productos": [{"name": "tv", "url":"vvv"},{"name": "celu", "url":"www"},{"name": "mesa", "url":"zzz"}]
    }
    return render(req, 'index.html', context)

def about(req): 
    context = {
        "mensaje": "Creado por Rubén Mario Ramírez para >> Desafío Latam 2024 <<",
    }
    return render(req, 'about.html', context)

def header(req): 
    context = {
    
    }
    return render(req, 'header.html', context)

def footer(req): 
    context = {
    
    }
    return render(req, 'footer.html', context)

def welcome(req): 
    context = {
        "mensaje": "¡BIENVENIDO A LA MEJOR TIENDA ONLINE DE FLANES...!!!",
    
    }
    return render(req, 'welcome.html', context)

