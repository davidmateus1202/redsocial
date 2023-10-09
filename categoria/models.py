from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.urls import reverse


class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    descripcion = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)

    def get_url(self):
        return reverse('productos_por_categoria', args=[self.nombre_categoria])

    def __str__(self):
        return f'Categoria: {self.nombre_categoria}'


