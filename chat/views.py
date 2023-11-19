from django.shortcuts import render,redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect

from social.models import Post, Relationship
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
def room(request, room_id):
    current_user = request.user
    user_id_to_find = request.session['user_id_to_find']
    user_to_find = User.objects.get(id=user_id_to_find)

 # Obtén las relaciones de los usuarios que sigue el usuario actual.
    user_follow_relationships = Relationship.objects.filter(from_user=current_user)

    # Obten una lista de los usuarios seguidos por el usuario actual.
    users_followed = [relationship.to_user for relationship in user_follow_relationships]


    try:
        room = request.user.rooms_joined.get(id=room_id)
    except:
        return HttpResponseForbidden()

    content = {
        'room': room,
        'user_follow': users_followed,
        'userRegister': user_to_find,
    }

    return render(request, 'chat/room.html', content,)

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
        request.session['user_id_to_find'] = user_id_to_find
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
    current_user = request.user
    user_follow = Relationship.objects.filter(to_user=current_user)
    return render(request, 'chat/room.html', {
        'user_follow': user_follow, 
    })



@login_required
def videocall(request):
    try:
        # Verifica si la variable de sesión USER_ID_TO_FIND existe
        try:
            user_id_to_find = request.session['user_id_to_find']
        except KeyError:
            # La variable de sesión USER_ID_TO_FIND no existe
            return HttpResponseBadRequest("No se encontraron usuarios disponibles.")

        # Verifica si el usuario seleccionado existe
        try:
            user_to_find = User.objects.get(id=user_id_to_find)
            userlog = User.objects.get(id = request.user.id)
        except User.DoesNotExist:
            # El usuario seleccionado no existe
            return HttpResponseBadRequest("No se encontraron usuarios disponibles.")

        # Busca las salas de ambos usuarios
        rooms_of_current_user = Room.objects.filter(users=request.user)
        rooms_of_user_to_find = Room.objects.filter(users=user_to_find)

        # Encuentra la sala común entre los dos usuarios (si existe)
        common_room = rooms_of_current_user.intersection(rooms_of_user_to_find).first()
        
        if common_room:
            print(request.user.username)
            name = userlog.username
            return render(request, 'videocam.html', {'name': name, 'room': common_room.id})
                
    except json.JSONDecodeError:
        return JsonResponse({'message': 'Error en el formato JSON.'}, status=400)

    return HttpResponseBadRequest("No se encontraron usuarios disponibles.")
