from django.db import models
from store.models import Producto
from django.contrib.auth.models import User

class Cart(models.Model):

    cart_id = models.CharField(max_length=250, blank=True)
    ahora_agregado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id
    
class CartItem(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    activo = models.BooleanField(default=True)

    def sub_total(self):
        return self.producto.precio * self.cantidad

    def __str__(self):
        return self.producto