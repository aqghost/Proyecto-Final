from django import forms
from .models import Post

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('fecha','categoria','destacado','publicado')