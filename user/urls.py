from django.contrib import admin
from user import views
from django.urls import path
from django.conf.urls import include
from perfil import urls as perfil_urls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('perfil/', include(perfil_urls)),
    path('', views.cadastro_usuario, name = 'signup')


]+ static(settings.MEDIA_URL, dcument_root = settings.MEDIA_ROOT)