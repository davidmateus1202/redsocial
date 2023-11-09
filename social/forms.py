from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
PALABRAS_PROHIBIDAS = ["mierda", "chet", "hp","gg","ez","nigga"]
class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'floatingInput',
        'placeholder':'Username'

    }), required=True)

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'class':'form-control',
        'id':'floatingInput',
        'placeholder':'user@example.com',
        
    }), required=True)
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'id':'floatingPassword',
        'placeholder':'Contraseña',
        
    }), required=True)
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'id':'floatingPassword',
        'placeholder':'Confirma contraseña',
        
    }), required=True)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:"" for k in fields}
class PostForm(forms.ModelForm):

    content = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'floatingInput',
        'placeholder':'¿Qué estás pensando hoy?',
        'rows':2
    }))
    class Meta:
        model = Post
        fields = ['content', 'image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'imagen'})
        }
class updated_user(forms.ModelForm):

    username = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'floatingInput',
        'placeholder':'Username'

    }))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'class':'form-control',
        'id':'floatingInput',
        'placeholder':'user@example.com',
        
    }))

    class Meta:
        model = User
        fields = ['username','email']
        help_texts = {k:"" for k in fields}


class profile_updated(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']

        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }
        

    def clean_content(self):
        content = self.cleaned_data.get('content', '')

        # Verifica si el contenido contiene palabras o frases prohibidas
        for palabra_prohibida in PALABRAS_PROHIBIDAS:
            if palabra_prohibida in content.lower():
                raise forms.ValidationError(f'La palabra o frase "{palabra_prohibida}" no está permitida en el contenido.')

        return content