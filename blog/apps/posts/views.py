from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Categoria, Comentario
from django.views import generic 
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import PostForm, PostCommentForm
from django.utils import timezone
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponseRedirect

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

        post_like = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = post_like.total_likes()

        liked = False
        if post_like.likes.filter(id=self.request.user.id).exists():
            liked = True

        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        context['form'] = PostCommentForm()
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context

class PostCommentFormView(LoginRequiredMixin, SingleObjectMixin, generic.FormView):
    template_name = 'post_detail.html'
    form_class= PostCommentForm
    model = Post

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        f = form.save(commit=False)
        f.com_autor = self.request.user
        f.post = self.object
        f.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk}) + '#comentarios'
    
class PostView(generic.View):
    
    def get(self, request, *args, **kwargs):
        view = PostDetailView.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = PostCommentFormView.as_view()
        return view(request, *args, **kwargs)

class CategoryListView(generic.ListView):
    model = Post
    template_name = 'categorias.html'
    
    def get_queryset(self):
        query = self.request.path.replace('/categoria/','')
        orden = self.request.GET.get('orden', 'desc')

        post_list = Post.objects.filter(categoria__nombre = query).filter(
            publicado__lte=timezone.now()
        )

        if orden == 'asc':
            post_list = post_list.order_by('publicado')
        elif orden == 'desc':
            post_list = post_list.order_by('-publicado')
        elif orden == 'az':
            post_list = post_list.order_by('titulo')
        else:
            post_list = post_list.order_by('-titulo')

        return post_list
    
class EditPostView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Post
    template_name = "posts/editar_post.html"
    fields = ['titulo','subtitulo', 'texto', 'imagen', 'categoria', 'destacado']
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name='Colaborador').exists()

class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Post
    template_name = "posts/eliminar_post.html"
    success_url = reverse_lazy('index')
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name='Colaborador').exists()

class PostCommentEditView(generic.UpdateView):
    model = Comentario
    fields = ['com_texto']
    template_name = "posts/editar_comentario.html"
    success_url = "/post/{post_id}/"

class PostCommentDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Comentario
    template_name = 'posts/eliminar_comentario.html'
    success_url ="/post/{post_id}/"

def user_logout(request):
    logout(request) # type: ignore
    return render(request, 'registration/logged_out.html', {})

def es_colaborador(user):
    return user.is_superuser or user.groups.filter(name='Colaborador').exists()

@user_passes_test(es_colaborador, lambda u: u.is_superuser)
@login_required
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user  # Asigna automáticamente el autor
            post.save()
            return redirect('post_detail', pk=post.pk)  # O a 'post_list' si preferís
    else:
        form = PostForm()

    categorias = Categoria.objects.all()
    return render(request, 'posts/crear_post.html', {'form': form, 'categorias': categorias})

def LikeView(request, pk):
    post = Post.objects.get(id=pk)
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True

    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))

def AboutView(request):
     return render (request, 'about.html')

from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages

def ContactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Acá podrías enviar un correo o guardar el mensaje
            messages.success(request, 'Mensaje enviado correctamente.')
            form = ContactForm()  # Limpia el formulario
    else:
        form = ContactForm()
    return render(request, 'contacto.html', {'form': form})