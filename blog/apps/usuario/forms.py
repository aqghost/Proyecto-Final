from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario  # Tu modelo personalizado

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100, required=True, label="Nombre")
    last_name = forms.CharField(max_length=100, required=True, label="Apellido")
    
    class Meta:
        model = Usuario
        fields = ("username", "first_name", "last_name", "email")
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Nombre de usuario"
        self.fields['username'].help_text = "Este será tu nombre público en comentarios y posts"