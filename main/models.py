from django.contrib.auth.models import User
from django.db import models
from user.models import User_animal
from event.models import Event

# Create your models here.

class Rating(models.Model):
    user = models.ForeignKey(User_animal, on_delete=models.CASCADE, blank=True, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.CharField(max_length=250, blank=True, null=True)
    note = models.IntegerField()

    def __str__(self):
        return self.note
