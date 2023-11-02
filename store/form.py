from django import forms
from  categoria.models import Categoria
from .models import Producto, PerfilVentas


class ProductoForm(forms.ModelForm):

    categorias = Categoria.objects.all()

    nombre_producto = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder':'Nombre del producto',
        'id':'floatingInput',
        'type':'text',
    }), required=True)

    slug = forms.CharField(label='' ,widget=forms.TextInput(attrs={

        'class': 'form-control',
        'placeholder':'Codigo del producto',
        'id':'floatingInput',
        'type':'text',

    }), required=True)

    descripcion = forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'description':'Descripcion del producto',
        'id':'floatingarea',
        'type':'text',
    }))
    precio = forms.IntegerField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder':'Precio del producto',
        'arial-label':'Amount (to the nearest dollar)',

    }))
    stock = forms.IntegerField(label='', widget=forms.NumberInput(attrs={

        'class': 'form-control',
        'placeholder':'Stock del producto',
        'id':'floatingInput',
        'type':'number',

    }))
    categoria = forms.ModelChoiceField( queryset=categorias, widget=forms.Select(attrs={
        'class': 'form-control',
 
        

    }))
    product_image = forms.ImageField(label='Imagen del producto',widget=forms.FileInput(attrs={
        'class':'form-control',
        'type':'file',
        'id':'formFileMultiple',
    }))

    class Meta:
        model = Producto
        fields = ['nombre_producto', 'slug', 'descripcion', 'precio', 'stock', 'categoria', 'product_image']
        help_texts = {k: "" for k in fields}


class PerfilVentaForm(forms.ModelForm):

    nombre_vendedor = forms.CharField(label='', widget=forms.TextInput(attrs={

        'class': 'form-control',
        'placeholder':'Nombre del vendedor',
        'id':'floatingInput',
        'type':'text',

    }), required=True)

    descripcion_venta = forms.CharField(label='',widget=forms.TextInput(attrs={

        'class': 'form-control',
        'placeholder':'Descripcion',
        'id':'floatingarea',
        'type':'text',

    }), required=True)

    biografia_venta = forms.CharField(label='', widget=forms.Textarea(attrs={

        'class': 'form-control',
        'placeholder':'Biografia',
        'id':'floatingarea3',
        'type':'text',
            
    }), required=True)

    class Meta:
        model = PerfilVentas
        fields = ['nombre_vendedor', 'descripcion_venta', 'biografia_venta']