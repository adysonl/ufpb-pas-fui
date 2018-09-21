from django.urls import path

from perfil.views import perfil

urlpatterns = [
    path('', perfil)
]