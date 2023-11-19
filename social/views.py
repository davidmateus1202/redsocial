from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
from store.models import Producto
from tarjetas.models import CartItem




def feed(request):

    posts = Post.objects.all()

    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = get_object_or_404(User, pk = request.user.pk)
            post.save()
            return redirect('feed')
    else:
        form = PostForm()

    current_time = timezone.now()
    stories = Story.objects.filter(created_at__gte=current_time - timezone.timedelta(days=1))

    context = {
        'posts':posts,
        'form':form,
        'stories': stories,
        
    }
    return render(request, 'social/feed.html', context)



def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
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
            user=None
            posts = None
            return redirect('feed')
            
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

    if request.method == 'POST':
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid():
            story = form.save(commit=False)
            story.user = request.user
            story.save()
            messages.success(request, 'Tu historia se ha agregado exitosamente.')
            return redirect('feed')  # Redirige a la página principal después de agregar la historia
        else:
            messages.error(request, 'Hubo un error en el formulario. Por favor, corrige los errores.')

    form = StoryForm()
    

    context = {
        'posts':posts,
        'user':user,
        'form': form
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


def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('feed')

def updated_profile(request):
  
    if request.method == 'POST':
        form_1 = updated_user(request.POST, instance=request.user)
        form = profile_updated(request.POST, request.FILES, instance=request.user.profile)
        
        if form.is_valid() and form_1.is_valid():
            form_1.save()
            form.save()
            return redirect('feed')
    else:
        form = profile_updated()
        form_1 = updated_user()
    context = {
        'form':form,
        'form_1':form_1
    }
    return render(request, 'social/actualizar.html', context)



def likes(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    current_likes = post.likes
    liked = Like.objects.filter(user=user, post=post).exists()

    if liked:
        Like.objects.filter(user=user, post=post).delete()
        current_likes = current_likes - 1
    else:
        like = Like(user=user, post=post)
        like.save()
        current_likes = current_likes + 1

    post.likes = current_likes
    post.save()
    return redirect('feed')


def marketplace(request):
    cart_items = CartItem.objects.all()
    products = Producto.objects.all().filter(is_available=True)
    content = {
        'products': products,
        'cart_items': cart_items,

    }
    return render(request, 'index.html', content)



