#from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):

    def es_colaborador(self):
        return self.groups.filter(name="Colaborador").exists()
    
    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

