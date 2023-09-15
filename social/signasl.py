from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import *
from django.dispatch import receiver

@receiver(post_save, sender = User)
def create_profile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    
