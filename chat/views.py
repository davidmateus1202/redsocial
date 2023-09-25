from django.shortcuts import render,redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from .form import RoomForm
from .models import *
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
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

@csrf_exempt
def create_room(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        users = data.get('users', [])
        name = data.get('name', '')
        
        if len(users) != 0 and name:
            room = creatRoom.objects.create(name=name)
            room.users.add(*users)
            return JsonResponse({'message': 'Sala de chat creada con éxito.'}, status=201)
    
    return JsonResponse({'message': 'Hubo un error en la solicitud.'}, status=400)