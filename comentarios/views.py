
from social.models import Post
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from .forms import ComentarioForm
from .models import Comentarios
from django.http import HttpResponseRedirect
from django.urls import reverse


def post_detail(request, post_id):

    post = Post.objects.get(id=post_id)
    comentarios = Comentarios.objects.filter(post=post)


    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.user = request.user
            comentario.post = post
            comentario.save()
            return HttpResponseRedirect(reverse('comentarios:post_detail', args=[post_id]))
    else:
        form = ComentarioForm()
    context = {

        'post': post,
        'comentarios':comentarios,
        'form':form,

    }

    return render(request, 'post_detail.html', context)

def delete_comment(request, comentario_id):
    comentario = get_object_or_404(Comentarios, pk=comentario_id)
    comentario.delete()
    return HttpResponseRedirect(reverse('comentarios:post_detail', args=[comentario.post.id]))






