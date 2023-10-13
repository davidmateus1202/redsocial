from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):

    nombre_producto = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id':'floatingInput',
        'type':'text',
    }), required=True)

    class Meta:
        model = Producto
        fields = ['nombre_producto', 'slug', 'descripcion', 'precio', 'stock', 'is_available', 'categoria', 'product_image']
        help_texts = {k: "" for k in fields}
