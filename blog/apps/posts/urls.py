from django.urls import path

from .views import *


urlpatterns = [
    path('', index),
    path('post/<int:pk>', PostDetailView.as_view(), name='post')
]