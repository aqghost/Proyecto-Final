from django.db import models
from django.utils import timezone
from django.conf import settings
from ckeditor.fields import RichTextField
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from ..usuario.models import Usuario



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
    texto = RichTextUploadingField()
    imagen = models.ImageField(upload_to='posts/', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default='Sin categoria')
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    destacado = models.BooleanField(default=False)
    publicado = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(Usuario, related_name='blog_post')


    def total_likes(self):
        return self.likes.count()
    
    class Meta:
        ordering = ('-publicado',)

    def get_absolute_url(self):
        return reverse('post_detail', args=(str(self.id)))
    
    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    post = models.ForeignKey(Post, related_name="comentarios", on_delete=models.CASCADE)
    com_autor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    com_texto = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-fecha_publicacion',)

    def __str__(self):
        return '%s - %s' % (self.post.titulo, self.com_autor)
