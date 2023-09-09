from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='red_social/media/perfil.jpg')
    
    def __str__(self):
        return f'Perfil de {self.user.username}'

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    time = models.DateTimeField(default=timezone.now)
    content = models.TextField(default='')

    class Meta:

        ordering = ['-time']

    def __str__(self) -> str:
        return f'{self.user.username} {self.content}'