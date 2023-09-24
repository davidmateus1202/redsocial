from django.shortcuts import render,redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .models import creaRoom
from .form import RoomCreationForm

@login_required
def room(request, room_id):
    try:
        room = request.user.rooms_joined.get(id=room_id)
    except:
        return HttpResponseForbidden()

    return render(request, 'chat/room.html', {'room':room})
# views.py
def create_room(request):
    if request.method == 'POST':
        # Si se envió un formulario POST, procesa los datos
        form = RoomCreationForm(request.POST)
        if form.is_valid():
            # Crea una nueva instancia de la sala, pero aún no la guarda en la base de datos
            new_room = form.save(commit=False)
            # Aquí puedes realizar cualquier otra modificación antes de guardarla
            new_room.save()
            # Redirecciona a la página de detalles de la sala recién creada
            return redirect('room_detail', room_id=new_room.id)
    else:
        # Si no se envió un formulario POST, muestra el formulario de creación
        form = RoomCreationForm()
    
    return render(request, 'roomp.html', {'form': form})
