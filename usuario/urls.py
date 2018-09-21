from django.contrib import admin
from usuario import views
from django.urls import path
from django.conf.urls import include
from perfil import urls as perfil_urls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('cadastrar/', views.cadastro_usuario),
    path('perfil/', include(perfil_urls))


]+ static(settings.MEDIA_URL, dcument_root = settings.MEDIA_ROOT)