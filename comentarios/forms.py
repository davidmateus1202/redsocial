from django import forms
from .models import Comentarios


class ComentarioForm(forms.ModelForm):

    text = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'floatingInput',
        'placeholder':'Escribe un comentario...'

    }))


    class Meta:
        model = Comentarios
        fields = ['text']