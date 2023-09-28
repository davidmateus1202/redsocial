from django.urls import path
from . import views

app_name = 'chat'
urlpatterns = [
    path('room/', views.chat_users, name='chat_users'),
    path('room/<int:room_id>/', views.room, name='room'),
    path('room2/<int:room_id>/', views.room_detail, name='room_detail'),
    path('create_room/', views.create_room, name='create_room'),
    path('call/',views.videocall, name='call'),
     path('call_voz/',views.call, name='call_voz'),
]
