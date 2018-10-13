from django.urls import path
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from user.views import update_to_king
from profile.views import profile, add_photo, edit_profile

urlpatterns = [
    path('', profile, name='profile'),
    path('event',  include('event.urls')),
    path('edit_photos', add_photo, name='edit_photo'),
    path('edit_profile', edit_profile, name='edit_profile'),
    path('update_to_king', update_to_king, name='update_to_king'),
]+ static(settings.MEDIA_URL, dcument_root = settings.MEDIA_ROOT)