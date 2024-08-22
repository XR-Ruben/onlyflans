from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Flan, ContactForm
from .forms import ContactFormForm, ContactModelForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm, UserForm
from django.contrib.auth import login
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

@login_required
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

@login_required
def gallery(request):
    return render(request, 'gallery.html', {})


@login_required
def profile_view(request):
    # Verificar que el User tiene un Perfil 
    user_id = request.user.id 
    
    user = request.user
    #* User de no tener un Profile, crea la relación
    if not hasattr(user, 'profile'):
        Profile.objects.create(user=user)
        profile = Profile.objects.get(user_id=user_id)
        print(f'user profile get -> {profile.__dict__}')
        
    #* ARMADO POST - crea (guarda en la tabla) - y redirect
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # Redirigir a la misma página después de guardar
            return redirect('/welcome')
    #* GET FORM - Creamos los forms con los datos de la DB de ese user
    else: 
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() #* Se guarda el user en la DB
            login(request, user) #* Se logea
            return redirect('welcome')  # Redirige a la vista de perfil u otra vista
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
