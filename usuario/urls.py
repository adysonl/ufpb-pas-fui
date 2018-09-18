from django.contrib import admin
from usuario import views
from django.urls import path

urlpatterns = [
    path('cadastrar/', views.cadastro_usuario)
]