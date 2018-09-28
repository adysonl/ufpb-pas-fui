from django.db import models
from user.views import User_animal, Address

# Create your models here.

class Event(models.Model):

    MODALITY_CHOICES = (
        ('fr','Free'),
        ('pd','Paid')
    )

    TYPE_EVENT_CHOICES = (
        ('p', 'Rolê Pequeno'),
        ('m', 'Rolê Médio'),
        ('g', 'Moster grande porte')
    )

    name = models.CharField(max_length=50, blank=True, null=True)
    king = models.IntegerField(null=True)
    modality = models.CharField(max_length=2, choices=MODALITY_CHOICES, blank=True, null=True)
    forbidden = models.BooleanField(default = False)
    drinks = models.BooleanField(default = False)
    type = models.CharField(max_length=2, choices=TYPE_EVENT_CHOICES, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    capacity = models.IntegerField(default=10)
    image = models.ImageField(upload_to='event_logo/', default='event_logo/default.jpg')

    def __str__(self):
        return self.name