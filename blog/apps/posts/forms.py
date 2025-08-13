from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Post, Comentario

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'subtitulo', 'texto', 'imagen', 'categoria', 'destacado']
        widgets = {
            'texto': CKEditorWidget(),
        }

class PostCommentForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['com_texto']

    def __init__(self, *args, **kwargs):
        super(PostCommentForm, self).__init__(*args,**kwargs)
        self.fields['com_texto'].widget.attrs\
            .update({
                'placeholder': 'Inserte un comentario',
        })