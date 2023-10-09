from django.db import models
from django.urls import reverse
from categoria.models import Categoria

# Create your models here.

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    descripcion = models.TextField(max_length=255, blank=True)
    precio = models.IntegerField()
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    product_image = models.ImageField()

    def get_url(self):
        return reverse('detalle_producto', kwargs={'categoria_nombre_categoria': self.categoria.nombre_categoria, 'nombre_producto': self.nombre_producto})


    def __str__(self):
        return f'Producto: {self.nombre_producto}'
