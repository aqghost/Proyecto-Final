from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'subtitulo', 'texto', 'imagen', 'categoria', 'destacado']
        widgets = {
            'texto': CKEditorWidget(),
        }
