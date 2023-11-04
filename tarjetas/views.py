from django.shortcuts import render, redirect, get_object_or_404
from store.models import Producto
from .models import Cart, CartItem

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def remove_cart(request, producto_id):

    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Producto, id=producto_id)
    cart_items = CartItem.objects.get(producto=product, cart=cart)

    if cart_items.cantidad > 1:
        cart_items.cantidad -= 1
        cart_items.save()
    else:
        cart_items.delete()
    
    return redirect('cart')

def delete_cart(request, producto_id):

    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Producto, id=producto_id)
    cart_items = CartItem.objects.get(producto=product, cart=cart)

    cart_items.delete()

    return redirect('cart')


def add_cart(request, producto_id):
    product = Producto.objects.get(id=producto_id)

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))

    cart.save() 

    try:
        cart_item = CartItem.objects.get(producto=product, cart=cart)
        cart_item.cantidad += 1
        cart_item.save()
    except CartItem.DoesNotExist:

        cart_item = CartItem.objects.create(
            producto = product,
            cantidad = 1,
            cart = cart
        )
        cart_item.save()

    return redirect('cart')



def cart(request, total=0, cantidad=0, cart_items=None):

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, activo=True)

        for cart_item in cart_items:
            total += (cart_item.producto.precio * cart_item.cantidad)
            cantidad += cart_item.cantidad
        impuesto = (total *0.19)

        grand_total = (total + impuesto)
    except:
        pass

    context = {

        'cart_items': cart_items,
        'total': total,
        'cantidad': cantidad,
        'impuesto': impuesto,
        'grand_total': grand_total,
    }


    return render(request, 'tarjetas/cart.html', context)