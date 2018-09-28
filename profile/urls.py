from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from profile.views import profile, add_photo, edit_profile

urlpatterns = [
    path('', profile, name='profile'),
    path('edit_photos', add_photo, name='edit_photo'),
    path('edit_profile', edit_profile, name='edit_profile')
]+ static(settings.MEDIA_URL, dcument_root = settings.MEDIA_ROOT)