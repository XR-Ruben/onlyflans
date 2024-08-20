from django import forms
from .models import ContactForm
from django.contrib.auth.models import User
from .models import Profile


#*  --- apply ContactFormForm --- 

class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label='Correo')
    customer_name = forms.CharField(max_length=64, label='Nombre')
    message = forms.CharField(label='Mensaje')

#*  --- apply ContactModelForm ---

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']
        
        
#* PROFILE FORMS 
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']        
"""
ContactForm que contenga los 
siguientes atributos:
● contact_form_uuid del tipo UUIDField, con valor por defecto uuid.uuid4, no 
editable
● customer_email del tipo EmailField
● customer_name del tipo CharField (largo máximo 64 caracteres)
● message del tipo TextField
"""
