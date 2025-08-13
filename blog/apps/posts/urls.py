from django.urls import path
from .views import index, PostDetailView, crear_post
from .upload_views import upload_image

urlpatterns = [
    path('', index, name='post_list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('nuevo/', crear_post, name='crear_post'),
    path('upload/', upload_image, name='upload_image'),
]
