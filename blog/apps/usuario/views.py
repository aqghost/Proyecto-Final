from django.shortcuts import render
from django.contrib.auth.models import Group

# apps/usuario/views.py
from .models import Usuario
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object 
        try:
            grupo_default= Group.objects.get(name='Miembro')
            grupo_default.user_set.add(user)
        except Group.DoesNotExist:
            pass
        # (opcional) agregarlo al grupo "Colaboradores"
        return response
