from django.urls import path
from . import views

app_name = 'comentarios'

urlpatterns = [

    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('delete/<int:comentario_id>', views.delete_comment, name='delete_comment'),

]