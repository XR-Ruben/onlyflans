from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Flan, ContactForm
from .forms import ContactFormForm
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


def welcome(request):
    # private_flans = [{"name": "flan 7", "image_url": "https://pbs.twimg.com/media/CA5u_1pWYAE6FK0.jpg", "description": "flan 7"},
    #                  {"name": "flan 8", "image_url": "https://pbs.twimg.com/media/CA5u_1pWYAE6FK0.jpg", "description": "flan 8"},]
    # return render(request,'welcome.html',{'private_flans': private_flans})
    private_flans = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {"private_flans": private_flans})




# *  <!-- apply FORM contacto -->


def contacto(request):
    if request.method == 'POST':
        
        #* FORM
        form = ContactFormForm(request.POST) 
        if form.is_valid():
            #* MODEL - Guardamos la data en nuestra DB en la TABLA CONACTFORM
            ContactForm.objects.create(**form.cleaned_data) # pasamos la data del diccionario .cleaned_data a argumentos
            return HttpResponseRedirect('/exito')
    else: 
        form = ContactFormForm()    
    return render(request, 'contacto.html', {'form':form})

# *  --- apply ContactModelForm ---
# from .forms import ContactModelForm  # Asegúrate de importar el formulario correcto

# *  <!-- apply MODEL-FORM contacto -->
# def contacto(request):
#     return render(request, 'contacto.html', {})
# *  --- apply ContactModelForm ---


# * <!-- apply DAY 11 - 12 -->
def exito(request):
    return render(request, 'exito.html', {})


