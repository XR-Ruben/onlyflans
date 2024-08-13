from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Flan, ContactForm
from .forms import ContactFormForm, ContactModelForm
# ----------------------------------------------------------------------------------------------
## VIEWS DE PROYECTO ONLYFLANS

# Create your views here.

def home(req): 
    flanes_all = Flan.objects.all()
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(req, 'index.html', {"flanes_publicos": flanes_publicos})

def about(req): 
    context = {
        "mensaje": """Descubre el sabor auténtico en nuestra tienda de flanes. 
                      Disfruta de una variedad de deliciosos flanes, desde los clásicos de 
                      vainilla y caramelo hasta opciones gourmet como chocolate, coco y más. 
                      Perfectos para cualquier ocasión, nuestros flanes son el postre ideal para 
                      compartir en familia o sorprender a tus invitados. ¡Ven y endulza tu día con nosotros!"""

,
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


def welcome(request):
    private_flans = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {"private_flans": private_flans})


# *  <!-- apply FORM contacto -->

def contacto(request):
    if request.method == 'POST':
        
#         #* FORM
        form = ContactFormForm(request.POST) 
        if form.is_valid():
             #* MODEL - Guardamos la data en nuestra DB en la TABLA CONACTFORM
            ContactForm.objects.create(**form.cleaned_data) # pasamos la data del diccionario .cleaned_data a argumentos
            return HttpResponseRedirect('/exito')
    else: 
        form = ContactModelForm()    
        return render(request, 'contacto.html', {'form':form})

# *  --- apply ContactModelForm ---

# # # *  <!-- apply MODEL-FORM contacto -->

# *  --- apply ContactModelForm ---


def exito(request):
    return render(request, 'exito.html', {})

