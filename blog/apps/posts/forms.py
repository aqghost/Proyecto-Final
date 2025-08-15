from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Post, Comentario
from django.core.validators import EmailValidator

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

class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre")
    correo = forms.EmailField(label="Correo electrónico")
    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5}),
        label="Mensaje"
    )