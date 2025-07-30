from django.shortcuts import render
from .models import Post, Categoria
from django.views import generic 
from django.utils import timezone
from django.views.generic import CreateView
# Create your views here.

def index(request):
    posts = Post.objects.all()
    categorias = Categoria.objects.all()
    destacado = Post.objects.filter(destacado=True)[:3]
    orden = request.GET.get('orden', 'desc')

    if orden == 'asc':
        posts = Post.objects.all().order_by('publicado')
    elif orden == 'desc':
        posts = Post.objects.all().order_by('-publicado')
    elif orden == 'az':
        posts = Post.objects.all().order_by('titulo')
    else:
        posts = Post.objects.all().order_by('-titulo')

    context = {
        'posts': posts,
        'categorias': categorias,
        'destacado': destacado,
        'orden': orden
    }

    return render (request, 'index.html', context=context)

class PostDetailView(generic.DetailView):
    model = Post
    template_name='post_detail.html'

    
def user_logout(request):
    logout(request) # type: ignore
    return render(request, 'registration/logged_out.html', {})

class CategoryListView(generic.ListView):
    model = Post
    template_name = 'categorias.html'

    def get_queryset(self):
        query = self.request.path.replace('/categoria/','')
        post_list = Post.objects.filter(categoria__nombre = query).filter(
            publicado__lte=timezone.now()
        )

        return post_list
    
class AddPostView(CreateView):
    model = Post
    template_name = 'crearpost.html'
    fields = ["titulo","subtitulo","texto","imagen"]