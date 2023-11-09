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
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.units import inch

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
    def __init__(self, buffer, title, total, impuesto, cantidad, cart_items):
        self.buffer = buffer
        self.title = title
        self.total = total
        self.impuesto = impuesto
        self.cantidad = cantidad
        self.cart_items = cart_items
        self.elements = []

        self.styles = getSampleStyleSheet()
        self.styles.add(ParagraphStyle(name='CustomTitle', fontSize=18, alignment=TA_CENTER))
        self.styles.add(ParagraphStyle(name='CustomNormal', fontSize=12, alignment=TA_CENTER))
        self.styles.add(ParagraphStyle(name='Customtext', fontSize=12, alignment=TA_JUSTIFY))
        self.styles.add(ParagraphStyle(name='CustomBullet', fontSize=10, bulletIndent=10, leftIndent=20, bulletFontName='Helvetica-Bold', bulletFontSize=12, alignment=TA_CENTER))
        # Puedes definir más estilos personalizados según tus necesidades


    def build_pdf(self):
        top_margin = 0.5 * inch
        doc = SimpleDocTemplate(self.buffer, pagesize=letter, topMargin=top_margin)
        styles = getSampleStyleSheet()

        title = Paragraph(self.title, self.styles["CustomTitle"])
        self.elements.append(title)
        self.elements.append(Spacer(1, 0.2 * inch)) 

        # Agregar información del carrito al recibo
        espace_info = f"__________________________________________________________________________________"
        espace = Paragraph(espace_info)
        self.elements.append(espace)

        self.elements.append(Spacer(1, 0.2 * inch))


        cart_info = f"Total: {self.total}"
        cart_info_paragraph = Paragraph(cart_info, self.styles["CustomBullet"])
        self.elements.append(cart_info_paragraph)

        cart_info2 = f"Total impuesto agregado: {self.impuesto}"
        cart_info_paragraph2 = Paragraph(cart_info2, self.styles["CustomBullet"])
        self.elements.append(cart_info_paragraph2)

        cart_info3 = f"Numero de productos: {self.cantidad}"
        cart_info_paragraph3 = Paragraph(cart_info3, self.styles["CustomBullet"])
        self.elements.append(cart_info_paragraph3)

        # Agregar detalles de los elementos del carrito
        if self.cart_items:
            for item in self.cart_items:
                item_info = f"Producto: {item.producto.nombre_producto}, Cantidad: {item.cantidad}"
                item_paragraph = Paragraph(item_info, self.styles["CustomBullet"]) # Agrega la imagen # Agrega espacio entre la imagen y el párrafo
                self.elements.append(item_paragraph) 

        self.elements.append(Spacer(1, 0.2 * inch)) 

        espace_info2 = f"__________________________________________________________________________________"
        espace2 = Paragraph(espace_info2)
        self.elements.append(espace2)

        self.elements.append(Spacer(1, 0.1 * inch)) 

        text_info3 = f"Nos preocupamos por su satisfacción con nuestros productos y servicios. Si en algún momento encuentra alguna inconformidad con su compra, le informamos que tiene un plazo máximo de 15 días a partir de la fecha de recepción del producto para solicitar una devolución. Durante este período, estaremos encantados de asistirle y procesar su solicitud de devolución de manera eficiente. Su satisfacción es nuestra prioridad, y estamos aquí para garantizar que su experiencia de compra sea lo más satisfactoria posible."
        text3 = Paragraph(text_info3, self.styles["Customtext"])
        self.elements.append(text3)

        self.elements.append(Spacer(1, 0.1 * inch)) 

        espace_info3 = f"__________________________________________________________________________________"
        espace3 = Paragraph(espace_info3)
        self.elements.append(espace3)

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

        for cart_item in cart_items:
            producto = cart_item.producto
            if producto.stock >= cart_item.cantidad:
                producto.stock = (producto.stock - cart_item.cantidad)
                producto.save()
            else:
                pass
    except:
        pass

    current_user = request.user
    perfil_vendedor = PerfilVentas.objects.get(user=current_user)

    # Crear un buffer en memoria para almacenar el PDF
    buffer = BytesIO()

    # Crear un PDFReceiptBuilder y construir el recibo
    pdf_title = f"Easy Market, Vendedor: {perfil_vendedor.user.username}"
    pdf_builder = PDFReceiptBuilder(buffer, pdf_title, grand_total, impuesto, cantidad, cart_items)
    pdf_builder.build_pdf()

    # Obtener el contenido del PDF desde el buffer
    pdf_buffer = buffer.getvalue()
    buffer.close()

    # Devolver el PDF como respuesta
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="receipt.pdf"'
    response.write(pdf_buffer)

    return response


