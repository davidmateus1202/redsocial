from django.shortcuts import get_object_or_404, render
from .models import Producto
from categoria.models import Categoria
from django.contrib.auth.decorators import login_required


def store(request, categoria_nombre_categoria=None):
    categoria = None
    products = None
    if categoria_nombre_categoria != None:
        categoria = get_object_or_404(Categoria, nombre_categoria=categoria_nombre_categoria)
        products = Producto.objects.filter(categoria=categoria, is_available=True)
        numero_productos = products.count()
    else:
        products = Producto.objects.all().filter(is_available=True)
        numero_productos = products.count()
    
    content = {
        'products': products,
        'numero_productos': numero_productos
    }
    return render(request, 'store/store.html', content)

def detalle_producto(request, categoria_nombre_categoria=None, nombre_producto=None):
    try:
        products = Producto.objects.get(categoria__nombre_categoria=categoria_nombre_categoria, nombre_producto=nombre_producto)
    except Exception as e:
        raise e
    content = {
        'products': products
    } 
    return render(request, 'store/detalle_producto.html', content)
  

def publicar_2(request):
    return render(request, 'store/publicacion.html')

