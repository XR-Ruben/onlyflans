import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Flan(models.Model):
    flan_uuid = models.UUIDField()
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()
    
    
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()
    
def __str__(self):
    return self.customer_name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # -> asocición - relación
    bio = models.TextField(max_length=500, blank=True) # el campo puede estar vacío
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True) # generalmente YYYY-MM-DD (por ejemplo, 2024-08-17).
    def __str__(self):
        return self.user.username