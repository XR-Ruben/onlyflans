from django.shortcuts import render
from .models import Flan
# ----------------------------------------------------------------------------------------------
## VIEWS DE PROYECTO ONLYFLANS

# Create your views here.

def home(req): 
    flanes_all = Flan.objects.all()
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(req, 'index.html', {"flanes_publicos": flanes_publicos})

def about(req): 
    context = {
        "mensaje": "Aplicación creada para vender flanes de diferentes variedades...",
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

