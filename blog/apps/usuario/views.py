from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import RegisterForm

# Create your views here.

class UserRegistration(FormView):
    template_name = 'users/registro.html'
    form_class = RegisterForm
    success_url = reverse_lazy('/')

    def form_valid(self, form):
        form.save()
        return super(UserRegistration, self).form_valid(form)