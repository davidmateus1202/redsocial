from django.shortcuts import render, redirect
from store.models import *


def home(request):
    products = Producto.objects.all().filter(is_available=True)
    content = {
        'products': products
    }
    return render(request, 'index.html', content)