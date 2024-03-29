from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='perfil.jpg')
    
    def __str__(self):
        return f'Perfil de {self.user.username}'
    
    def following(self):
        user_ids = Relationship.objects.filter(from_user=self.user)\
                                .values_list('to_user_id',flat=True)
        return User.objects.filter(id__in =user_ids)
    def followers(self):
        user_ids = Relationship.objects.filter(to_user=self.user)\
                                .values_list('from_user_id',flat=True)
        return User.objects.filter(id__in =user_ids)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts',null=False)
    image = models.ImageField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    likes = models.IntegerField(default=0)
    time = models.DateTimeField(default=timezone.now)
    class Meta:

        ordering = ['-time']

    def __str__(self) -> str:
        return f'{self.user.username} {self.content}'


class Relationship(models.Model):
    from_user = models.ForeignKey(User,related_name='relationships',on_delete=models.CASCADE)
    to_user = models.ForeignKey(User,related_name='related_to',on_delete=models.CASCADE)   


    def __str__(self) -> str:
        return f'{self.from_user} to {self.to_user}'

    class Meta:
        indexes= [
            models.Index(fields=['from_user','to_user',]),

        ] 

class Like(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes')



class Story(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stories')
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    duration_days = models.IntegerField(default=1)  # Número de días que durará la historia

    class Meta:
        ordering = ['-created_at']

    def _str_(self):
        return f'{self.user.username} Story - {self.created_at}'