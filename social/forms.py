from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
PALABRAS_PROHIBIDAS = ["mierda", "chet", "hp","gg","ez","nigga"]
class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:"" for k in fields}
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'text',
                'rows': 2,
                'placeholder': '¿Qué estás pensando hoy?'
            }),
            'image': forms.ClearableFileInput(attrs={'class': 'imagen'})
        }

    def clean_content(self):
        content = self.cleaned_data.get('content', '')

        # Verifica si el contenido contiene palabras o frases prohibidas
        for palabra_prohibida in PALABRAS_PROHIBIDAS:
            if palabra_prohibida in content.lower():
                raise forms.ValidationError(f'La palabra o frase "{palabra_prohibida}" no está permitida en el contenido.')

        return content