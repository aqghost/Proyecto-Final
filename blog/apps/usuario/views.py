from django.shortcuts import render

# apps/usuario/views.py
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        # (opcional) agregarlo al grupo "Colaboradores"
        return response


