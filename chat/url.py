from django.urls import path
from . import views

app_name = 'chat'
urlpatterns = [
    path('room/<int:room_id>/', views.room, name='room'),
    path('creat/', views.create_room, name='room_detail')
]
