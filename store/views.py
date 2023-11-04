from django.shortcuts import get_object_or_404, render, redirect
from .models import Producto
from categoria.models import Categoria
from django.contrib.auth.decorators import login_required
from .form import ProductoForm, PerfilVentaForm
from django.contrib.auth.models import User
from tarjetas.models import CartItem
from tarjetas.views import _cart_id

def store(request, categoria_nombre_categoria=None):
    cart_items = CartItem.objects.all()
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
        'numero_productos': numero_productos,
        'cart_items': cart_items,
    }
    return render(request, 'store/store.html', content)

def detalle_producto(request, categoria_nombre_categoria=None, nombre_producto=None):
    try:
        products = Producto.objects.get(categoria__nombre_categoria=categoria_nombre_categoria, nombre_producto=nombre_producto)
        # Busca el producto relacionado con la categoría y el nombre específicos.
        producto = get_object_or_404(Producto, categoria__nombre_categoria=categoria_nombre_categoria, nombre_producto=nombre_producto)

        in_cart = CartItem.objects.filter(cart__cart_id = _cart_id(request), producto = producto).exists()
    except Exception as e:
        raise e
    content = {
        'products': products,
        'in_cart': in_cart,
    } 
    return render(request, 'store/detalle_producto.html', content)
  

def publicar(request):
    current_user = get_object_or_404(User, pk = request.user.pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.user = current_user
            producto.save()
            return redirect('store')
    else:
        form = ProductoForm()
    context = {
        'form':form
    }
        
    return render(request, 'store/publicacion.html', context)

def perfil(request, username=None):
    current_user = request.user
    if username and username != current_user:
        user = User.objects.get(username=username)
        posts = user.publicaciones.all()
    else:
        posts = current_user.publicaciones.all()
        user = current_user
    try:
        perfil_vendedor = PerfilVentas.objects.get(user=current_user)
    except PerfilVentas.DoesNotExist:
        perfil_vendedor = None

    context = {
        'posts': posts,
        'user': user,
        'perfil_vendedor': perfil_vendedor,
    }
    return render(request, 'store/perfil_store.html', context)


from .models import PerfilVentas

def editar_perfil(request):
    try:
        perfil_vendedor = PerfilVentas.objects.get(user=request.user)
    except PerfilVentas.DoesNotExist:
        perfil_vendedor = None

    if request.method == 'POST':
        form = PerfilVentaForm(request.POST, instance=perfil_vendedor)
        if form.is_valid():
            perfil_vendedor = form.save(commit=False)
            perfil_vendedor.user = request.user
            perfil_vendedor.save()
            return redirect('perfil')
    else:
        form = PerfilVentaForm()
    
    print(perfil_vendedor)
    context = {
        'perfil_vendedor': perfil_vendedor,
        'form': form,
        
    }
    return render(request, 'store/editar_perfil.html', context)
