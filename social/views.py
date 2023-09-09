from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def feed(request):
    posts = Post.objects.all()

    context = {
        'posts':posts
    }
    return render(request, 'social/feed.html', context)

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'El usuario {username} ha sido creado exitosamente!')
            return redirect('feed')
    else:
        form = UserRegisterForm()
    context = {
        'form':form
    }
    return render(request, 'social/registro.html', context)



def profile(request):
    return render(request, 'social/profile.html')