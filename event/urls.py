from event import views
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('list_event', views.list_event, name='list_event'),
    path('edit_event/<int:id>', views.edit_event, name='edit_event'),
    path('create_event/', views.create_event, name='create_event'),
    path('delete_event/<int:id>', views.delete_event, name='delete_event')

]+ static(settings.MEDIA_URL, dcument_root = settings.MEDIA_ROOT)