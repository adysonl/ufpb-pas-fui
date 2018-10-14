from django.contrib.auth.models import User
from django.db import models
from user.models import User_animal
from event.models import Event

# Create your models here.

class Rating(models.Model):
    user = models.IntegerField(null=True)
    commented = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=250, blank=True, null=True)
    note = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=10,blank=True, null=True)

    def __str__(self):
        return self.note
