from django.db import models
from django.urls import reverse
from categoria.models import Categoria
from django.contrib.auth.models import User

# Create your models here.

class PerfilVentas(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfilventas')
    nombre_vendedor = models.CharField(max_length=50, default='Editar nombre de vendendor')
    descripcion_venta = models.TextField(max_length=255, blank=True, default='Editar descripcion de vendendor')
    biografia_venta = models.TextField(max_length=500, blank=True, default='Editar biografia de vendendor')

    def __str__(self):
        return self.nombre_vendedor

class Producto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publicaciones')
    nombre_producto = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    descripcion = models.TextField(max_length=1000, blank=True)
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
    
class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ManyToManyField(Producto)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    telefono = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255, blank=True)
    ciudad = models.CharField(max_length=255, blank=True)
    departamento = models.CharField(max_length=255, blank=True)
    pais = models.CharField(max_length=255, blank=True)
    comentario = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        productos = ', '.join([producto.nombre_producto for producto in self.producto.all()])
        return f'Pedido: {self.id} - Productos: {productos}'