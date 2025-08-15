from .models import Categoria

def procesar_categorias(request):
    categorias = Categoria.objects.all()
    return {
        'categorias': categorias
    }

def urlcategorias(request):
    urlsplit = request.path.split('/')
    return {
        'urlcategorias' : urlsplit
    }