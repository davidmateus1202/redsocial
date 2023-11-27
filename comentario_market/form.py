from django import forms
from .models import Comentarios_marcketplace
from spanlp.palabrota import Palabrota

class ComentarioMarketForm(forms.ModelForm):

    text = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'floatingInput',
        'placeholder':'Escribe un comentario...'

    }), required=True)


    class Meta:
        model = Comentarios_marcketplace
        fields = ['text']
    def clean_text(self):
        content = self.cleaned_data.get('text', '')
        print(content)
        palabraC = analisis(content)
        print(palabraC)
        return palabraC



def analisis(text):
    # Crea una instancia del validador de palabras ofensivas
    validador = Palabrota(censor_char='#')
    
    # Utiliza el validador para censurar palabras ofensivas en el texto
    texto_censurado = validador.censor(text)
    
    # Devuelve el texto censurado
    return texto_censurado