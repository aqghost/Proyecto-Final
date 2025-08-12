from django.shortcuts import render
from .models import Post, Categoria
from django.views import generic 
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import PostForm
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

@login_required
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user  # Asigna automáticamente el autor
            post.save()
            return redirect('post_detail', pk=post.pk)  # O a 'post_list' si preferís
    else:
        form = PostForm()

    categorias = Categoria.objects.all()
    return render(request, 'posts/crear_post.html', {'form': form, 'categorias': categorias})
