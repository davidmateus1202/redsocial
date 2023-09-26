from django.shortcuts import render,redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from .form import RoomForm
from .models import *
from django.contrib.auth.models import User
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
import random 
import time
from django.http import HttpResponseRedirect, HttpResponseBadRequest
@login_required
def room(request, room_id):
    try:
        room = request.user.rooms_joined.get(id=room_id)
    except:
        return HttpResponseForbidden()

    return render(request, 'chat/room.html', {'room':room})

# views.py
def room_detail(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    return render(request, 'chatp.html', {'room': room})
@login_required
def login():
    
    current_user = request.user

    
@login_required
def create_room(request):
    try:
        name = request.GET.get('name', '')  # Nombre de la sala
        current_user = request.user  # Usuario autenticado

        # Obtiene una lista de usuarios disponibles (excluyendo al usuario autenticado)
        available_users = User.objects.exclude(id=current_user.id)

        if available_users:
            # Selecciona aleatoriamente un usuario de la lista
            user_to_find = random.choice(available_users)

            # Agrega un sufijo único al nombre de la sala (por ejemplo, un timestamp)
            room_name = f'Sala de chat entre {current_user.username} y {user_to_find.username} ({int(time.time())})'

            # Crea la sala de chat y agrega los usuarios
            # Verifica si el usuario actual es diferente del usuario al que quieres unir
            if current_user.id == user_to_find.id:
                return HttpResponseBadRequest("No puedes unirte a una sala contigo mismo.")

            # Intenta encontrar una sala que ya contenga a ambos usuarios
            room = Room.objects.filter(users=current_user).filter(users=user_to_find.id).first()

            # Si no se encuentra una sala con ambos usuarios, crea una nueva
            if not room:
                # Crea una sala de chat
                room = Room.objects.create(room_name)

                # Agrega los usuarios a la sala
                room.users.add(current_user, user_to_find.id)

            # Redirige al usuario a la página de la sala de chat
            return HttpResponseRedirect(f'/chat/room/{room.id}/')  # Ajusta la URL a tu estructura de URLs
    except json.JSONDecodeError:
        return JsonResponse({'message': 'Error en el formato JSON.'}, status=400)

    return JsonResponse({'message': 'Método no válido.'}, status=405)
    


@login_required
def chat_users(request):
    users = User.objects.all()
    return render(request, 'base.html', {
        'users':users
    })




