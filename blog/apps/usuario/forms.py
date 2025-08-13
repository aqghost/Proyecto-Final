from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario  # Tu modelo personalizado

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    class Meta:
        model = Usuario
        fields = ("username","first_name","last_name", "email")  # Agregá más campos si tu modelo los tiene