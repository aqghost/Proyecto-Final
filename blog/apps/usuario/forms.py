from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario  # Tu modelo personalizado

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ("username", "email")  # Agregá más campos si tu modelo los tiene