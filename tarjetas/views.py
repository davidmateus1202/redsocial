from audioop import reverse
from django.shortcuts import render, redirect, get_object_or_404
from store.models import PerfilVentas, Producto
from .models import Cart, CartItem
from django.http import FileResponse
from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.templatetags.static import static
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Spacer
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet

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


def checkout(request, total=0, cantidad=0, cart_items=None):
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
    return render(request, 'tarjetas/checkout.html',context)
class PDFReceiptBuilder:
    def __init__(self, buffer, title, total, cantidad, cart_items):
        self.buffer = buffer
        self.title = title
        self.total = total
        self.cantidad = cantidad
        self.cart_items = cart_items
        self.elements = []

    def build_pdf(self):
        doc = SimpleDocTemplate(self.buffer, pagesize=letter)
        styles = getSampleStyleSheet()
        title_style = styles["Title"]
        title = Paragraph(self.title, title_style)
        self.elements.append(title)

        # Agregar una imagen al documento PDF
        


        # Agregar información del carrito al recibo
        cart_info = f"Total: {self.total}, Cantidad: {self.cantidad}"
        cart_info_paragraph = Paragraph(cart_info, styles["Normal"])
        self.elements.append(cart_info_paragraph)

        # Agregar detalles de los elementos del carrito
        if self.cart_items:
            item_style = styles["Bullet"]
            for item in self.cart_items:
                item_info = f"Producto: {item.producto.nombre_producto}, Cantidad: {item.cantidad}"
                image_path = "{item.producto.product_image.url}"  # Reemplaza con la ruta de tu imagen
                print(image_path)
                image = Image(image_path, width=200, height=100)  # Especifica el ancho y alto deseados
                item_paragraph = Paragraph(item_info, item_style)
                self.elements.append(image)  # Agrega la imagen
                self.elements.append(Spacer(1, 12))  # Agrega espacio entre la imagen y el párrafo
                self.elements.append(item_paragraph)    
                

        doc.build(self.elements)

def generate_pdf_receipt(request, total=0, cantidad=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, activo=True)

        for cart_item in cart_items:
            total += (cart_item.producto.precio * cart_item.cantidad)
            cantidad += cart_item.cantidad
        impuesto = (total * 0.19)

        grand_total = (total + impuesto)
    except:
        pass

    current_user = request.user
    perfil_vendedor = PerfilVentas.objects.get(user=current_user)

    # Crear un buffer en memoria para almacenar el PDF
    buffer = BytesIO()

    # Crear un PDFReceiptBuilder y construir el recibo
    pdf_title = f"Easy Market, Vendedor: {perfil_vendedor.user.username}"
    pdf_builder = PDFReceiptBuilder(buffer, pdf_title, grand_total, cantidad, cart_items)
    pdf_builder.build_pdf()

    # Obtener el contenido del PDF desde el buffer
    pdf_buffer = buffer.getvalue()
    buffer.close()

    # Devolver el PDF como respuesta
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="receipt.pdf"'
    response.write(pdf_buffer)

    return response


