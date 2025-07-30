from django.shortcuts import render, redirect
from .models import Post, Categoria
from django.views import generic, View
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse
from .forms import BlogPostForm,PostCommentForm
#from django.views.generic import CreateView
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
        context['form'] = PostCommentForm
        return context

class PostCommentFormView(LoginRequiredMixin, SingleObjectMixin, FormView):
    template_name = 'post_detail.html'
    form_class = PostCommentForm
    model = Post

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self,form):
        f = form.save(commit=False)
        f.autor = self.request.user
        f.post = self.object
        f.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('post', kwargs={'pk': self.object.pk}) + '#comentarios'

class PostView(View):
    def get(self, request, *args, **kwargs):
        view = PostDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostCommentFormView.as_view()
        return view(request, *args, **kwargs)

    
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
    
class CrearPost(generic.CreateView):
    login_url = 'login'
    form_class = BlogPostForm
    template_name = "crearpost.html"
    success_url = '/'
    success_message = "Tu post se ha creado exitosamente"


