from django.urls import path
from . import views

app_name = 'chat'
urlpatterns = [
    path('room/', views.chat_users, name='chat_users'),
    path('room/<int:room_id>/', views.room, name='room'),
]
