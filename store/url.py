from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('stor/', views.store, name='store'),
    path('publicar/', views.publicar, name='publicar'),
    path('perfil/', views.perfil, name='perfil'),
    path('editar_perfil', views.editar_perfil, name='editar_perfil'),
    path('<str:categoria_nombre_categoria>/', views.store, name='productos_por_categoria'),
    path('<str:categoria_nombre_categoria>/<str:nombre_producto>/', views.detalle_producto, name='detalle_producto'),
    
    
]