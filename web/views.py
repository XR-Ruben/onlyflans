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
    private_flans = [{"name": "Pineapple Dessert 'Cream' - Dutch", "image_url": "https://www.cookiedoughandovenmitt.com/wp-content/uploads/2021/03/Mint-Chocolate-Dessert-10-Photo-Cookie-Dough-and-Oven-Mitt.jpg", "description": "Reserve some of the crushed pineapple for garnish. Sprinkle gelatin over water in small saucepan; "},
                     {"name": "Guiltless Pumpkin Dessert", "image_url": "https://supersisterfitness.com/wp-content/uploads/2013/11/pumpkinpie-1024x10241.jpg", "description": "Mix the pudding and the milk together as instructed on the box. Allow to set for 5 minutes. Mix together the pumpkin and pumpkin pie spice. Then fold in (don't beat) with the pudding mixture. Layer on the crumbs and then top with Cool Whip. "},]
    return render(request,'welcome.html',{'private_flans': private_flans})
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


