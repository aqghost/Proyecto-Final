from django.urls import path
from .views import index, PostDetailView, CategoryListView, crear_post, EditPostView, DeletePostView
from .upload_views import upload_image

urlpatterns = [
    path('', index, name='index'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('categoria/<str:nombre>', CategoryListView.as_view(), name='categorias'),
    path('nuevo/', crear_post, name='crear_post'),
    path('upload/', upload_image, name='upload_image'),
    path('post/editar/<int:pk>', EditPostView.as_view(), name="editar_post"),
    path('post/eliminar/<int:pk>', DeletePostView.as_view(), name="eliminar_post"),
]
