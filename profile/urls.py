from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from user.views import update_to_king
from profile.views import profile, add_photo, edit_profile, list_event,edit_event,delete_event

urlpatterns = [
    path('', profile, name='profile'),
    path('edit_photos', add_photo, name='edit_photo'),
    path('edit_profile', edit_profile, name='edit_profile'),
    path('edit_event/<int:id>', edit_event, name='edit_event'),
    path('delete_event/<int:id>', delete_event, name='delete_event'),
    path('update_to_king', update_to_king, name='update_to_king'),
    path('list_event', list_event, name='list_event')
]+ static(settings.MEDIA_URL, dcument_root = settings.MEDIA_ROOT)