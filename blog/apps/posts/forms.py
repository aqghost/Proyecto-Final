from django import forms
from .models import Post, Comentario

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('fecha','categoria','destacado','publicado')

class PostCommentForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['cont_comentario']