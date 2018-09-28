from django.conf.urls.static import static
from django.conf import settings

from django.urls import path

urlpatterns = [


]+ static(settings.MEDIA_URL, dcument_root = settings.MEDIA_ROOT)