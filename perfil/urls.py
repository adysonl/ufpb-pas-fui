from django.urls import path

from perfil.views import perfil, add_photo, edite_perfil

urlpatterns = [
    path('', perfil, name='perfil'),
    path('edit_photos', add_photo, name='edit_photo'),
    path('edite_perfil', edite_perfil, name='edite_perfil')
]