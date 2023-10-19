from django import forms
from  categoria.models import Categoria
from .models import Producto


class ProductoForm(forms.ModelForm):

    categorias = Categoria.objects.all()

    nombre_producto = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id':'floatingInput',
        'type':'text',
    }), required=True)

    slug = forms.CharField(widget=forms.TextInput(attrs={

        'class': 'form-control',
        'id':'floatingInput',
        'type':'text',

    }), required=True)

    descripcion = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id':'floatingarea',
        'type':'text',
    }))
    precio = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'arial-label':'Amount (to the nearest dollar)',

    }))
    stock = forms.IntegerField(widget=forms.NumberInput(attrs={

        'class': 'form-control',
        'id':'floatingInput',
        'type':'number',

    }))
    categoria = forms.ModelChoiceField(queryset=categorias, widget=forms.Select(attrs={
        'class': 'form-control',
        

    }))
    product_image = forms.ImageField(widget=forms.FileInput(attrs={
        'class':'form-control',
        'type':'file',
        'id':'formFileMultiple',
    }))

    class Meta:
        model = Producto
        fields = ['nombre_producto', 'slug', 'descripcion', 'precio', 'stock', 'categoria', 'product_image']
        help_texts = {k: "" for k in fields}
