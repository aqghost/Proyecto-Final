from django.urls import path
from django.views.generic import TemplateView
from .views import *
app_name = 'user'

urlpatterns = [
    path('registro/', UserRegistration.as_view(), name='registro'),
    path('success/', TemplateView.as_view(template_name='success_registro.html'), name='success')
]