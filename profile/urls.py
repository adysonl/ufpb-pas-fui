from django.urls import path

from profile.views import profile, add_photo, edit_profile

urlpatterns = [
    path('', profile, name='profile'),
    path('edit_photos', add_photo, name='edit_photo'),
    path('edit_profile', edit_profile, name='edit_profile')
]