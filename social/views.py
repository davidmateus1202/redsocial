from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, PostForm
from django.contrib.auth.decorators import login_required
from chat import models

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
            return redirect('loguin')
    else:
        form = UserRegisterForm()
    context = {
        'form':form
    }
    return render(request, 'social/registro.html', context)
@login_required
def post(request):
    current_user = get_object_or_404(User, pk = request.user.pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('feed')
    else:
        form = PostForm()
    context = {
        'form':form
    }
    return render(request, 'social/post.html', context)




def buscar_perfil(request, username = None):
    current_user = request.user 
    username = request.GET.get('username')

    if username and username != current_user.username:
        try:
            user = User.objects.get(username=username)
            posts = user.posts.all()
        except User.DoesNotExist:
            messages.error(request, f'El usuario {username} proporcionado no existe')
            user=None
            posts = None
            return render(request, 'social/feed.html')
    else:
        user = current_user
        posts = current_user.posts.all()

    context = {
        'posts': posts,
        'user': user
    }
    return render(request, 'social/profile.html', context)

def profile(request, username = None):
    current_user = request.user
    if username and username != current_user:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user
    context = {
        'posts':posts,
        'user':user
    }
    return render(request, 'social/profile.html', context)

def follow(request, username):
    current_user = request.user
    to_user = User.objects.get(username = username)
    to_user_id = to_user
    rel = Relationship(from_user=current_user, to_user=to_user_id)
    rel.save()
    messages.success(request, f'sigues a {username}')
    return redirect('feed')

def unfollow(request, username):
    current_user = request.user
    to_user = User.objects.get(username = username)
    to_user_id = to_user
    rel = Relationship.objects.filter(
    from_user=current_user, to_user=to_user_id
    ).first()

    if rel:
        rel.delete()
        messages.success(request, f'ya no sigues a {username}')
    return redirect('feed')