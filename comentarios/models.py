from django.db import models
from social.models import *
from django.contrib.auth.models import User

class Comentarios(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comentarios')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comentarios')
    text = models.CharField(max_length=1000, null=True, blank=True)
    time = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-time']

