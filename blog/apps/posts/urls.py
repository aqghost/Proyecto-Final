from django.urls import path

from .views import *


urlpatterns = [
    path('', index),
    path('post/<int:pk>', PostView.as_view(), name='post'),
    path('categoria/<str:nombre>', CategoryListView.as_view(), name='categorias'),
    path('crearpost/', CrearPost.as_view(), name='crearpost')
]