from django.urls import path
from . import views
#from chat.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView




urlpatterns = [

    path('', views.feed, name='feed'),
    path('perfil/', views.profile, name='profile'),
    path('perfil/<str:username>/', views.profile, name='profile'),
    path('buscar_perfil/', views.buscar_perfil, name='buscar_perfil'),
    path('register/', views.register, name='register'),
    path('loguin/', LoginView.as_view(template_name = 'social/loguin.html'), name='loguin'),
    path('logout/', LogoutView.as_view(template_name = 'social/logout.html'), name='logout'),
    path('post/', views.post, name='post'),



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)