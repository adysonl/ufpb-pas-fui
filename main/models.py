from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Usuario(models.Model):
    TIPO_CHOICES=(
        ("kg" , "King"),
        ("am" , "Animal")
    )

    user = models.OneToOneField(User, related_name="user", on_delete=models.PROTECT)
    tipo = models.CharField(max_length=6, choices=TIPO_CHOICES)

    def __str__(self):
        return self.user.fist_name+ " " + self.user.last_name
