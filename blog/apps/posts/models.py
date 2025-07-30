from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=30, null=False)

    def get_absolute_url(self):
        return reverse("categoria", kwargs={"nombre": self.nombre})

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    subtitulo = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default='Sin categoria')
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    destacado = models.BooleanField(default=False)
    publicado = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(blank=True, null=True, upload_to='imagenes_posts/')

    class Meta:
        ordering = ('-publicado',)

    def __str__(self):
        return self.titulo    

    def get_absolute_url(self):
        return reverse('index')