from django.shortcuts import render, redirect
from .models import Post, Categoria
from django.views import generic 
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.utils import timezone
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import SingleObjectMixin

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context

class CategoryListView(generic.ListView):
    model = Post
    template_name = 'categorias.html'

    def get_queryset(self):
        query = self.request.path.replace('/categoria/','')
        post_list = Post.objects.filter(categoria__nombre = query).filter(
            publicado__lte=timezone.now()
        )

        return post_list
    
class EditPostView(generic.UpdateView):
    model = Post
    template_name = "posts/editar_post.html"
    fields = ['titulo','subtitulo', 'texto']

class DeletePostView(generic.DeleteView):
    model = Post
    template_name = "posts/eliminar_post.html"
    success_url = reverse_lazy()


def user_logout(request):
    logout(request) # type: ignore
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
