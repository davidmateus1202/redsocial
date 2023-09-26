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
from django.db.models import Q
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
def create_room(request):
    try:
        current_user = request.user  # Usuario autenticado

        # Obtén el ID del usuario seleccionado desde el parámetro user_id_to_find
        user_id_to_find = request.GET.get('user_id_to_find')

        # Convierte el ID del usuario seleccionado a un entero
        try:
            user_id_to_find = int(user_id_to_find)
        except (ValueError, TypeError):
            return HttpResponseBadRequest("El parámetro user_id_to_find es inválido.")

        # Verifica si el usuario actual es diferente del usuario al que quieres unir
        if current_user.id == user_id_to_find:
            return HttpResponseBadRequest("No puedes unirte a una sala contigo mismo.")

        # Obtén el objeto de usuario seleccionado usando el ID
        try:
            user_to_find = User.objects.get(id=user_id_to_find)
        except User.DoesNotExist:
            return HttpResponseBadRequest("El usuario seleccionado no existe.")

        # Busca las salas de ambos usuarios
        rooms_of_current_user = Room.objects.filter(users=current_user)
        rooms_of_user_to_find = Room.objects.filter(users=user_to_find)

        # Encuentra la sala común entre los dos usuarios (si existe)
        common_room = rooms_of_current_user.intersection(rooms_of_user_to_find).first()

        if common_room:
            # Si ya existe una sala común, redirige al usuario a esa sala
            return redirect('chat:room', room_id=common_room.id)
        else:
            # Si no existe una sala común, crea una nueva sala
            name = f'Sala de chat entre {current_user.username} y {user_to_find.username} ({int(time.time())})'
            room = Room.objects.create(name=name)

            # Agrega los usuarios a la nueva sala
            room.users.add(current_user, user_to_find)

            # Redirige al usuario a la página de la sala de chat
            return redirect('chat:room', room_id=room.id)  # Ajusta la URL a tu estructura de URLs

    except json.JSONDecodeError:
        return HttpResponseBadRequest("Error en el formato JSON.")

    return HttpResponseBadRequest("Método no válido.")
@login_required
def chat_users(request):
    users = User.objects.all()
    return render(request, 'base.html', {
        'users':users
    })


@login_required
def videocall(request): 
    try:
        name = request.GET.get('name', '')  # Nombre de la sala
        current_user = request.user  # Usuario autenticado

        # Obtiene una lista de usuarios disponibles (excluyendo al usuario autenticado)
        available_users = User.objects.exclude(id=current_user.id)

        if available_users:
            # Selecciona aleatoriamente un usuario de la lista
            user_to_find = random.choice(available_users)

            # Agrega un sufijo único al nombre de la sala (por ejemplo, un timestamp)
            rooms_of_current_user = Room.objects.filter(users=current_user.id)
            rooms_of_user_to_find = Room.objects.filter(users=user_to_find.id)

            # Encuentra la sala común entre los dos usuarios (si existe)
            common_room = rooms_of_current_user.intersection(rooms_of_user_to_find).first()
            print(common_room)
            
            if common_room:
                print(request.user.username)
                return render(request, 'videocam.html', {'name': request.user.username, 'room': room.id})
                
    except json.JSONDecodeError:
        return JsonResponse({'message': 'Error en el formato JSON.'}, status=400)

    return HttpResponseBadRequest("No se encontraron usuarios disponibles.")
    



