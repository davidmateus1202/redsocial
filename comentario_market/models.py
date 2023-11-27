from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from store.models import Producto

class Comentarios_marcketplace(models.Model):

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='producto_comentarios')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000, null=True, blank=True)
    time = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-time']

