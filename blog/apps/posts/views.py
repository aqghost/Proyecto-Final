from django.shortcuts import render
from .models import Post, Categoria
from django.views import generic 
# Create your views here.

def index(request):
    posts = Post.objects.all()
    categorias = Categoria.objects.all()
    destacado = Post.objects.filter(destacado=True)[:3]

    context = {
        'posts': posts,
        'categorias': categorias,
        'destacado': destacado
    }

    return render (request, 'index.html', context=context)

class PostDetailView(generic.DetailView):
    model = Post
    template_name='post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context
    
def user_logout(request):
    logout(request)
    return render(request, 'registration/logged_out.html', {})