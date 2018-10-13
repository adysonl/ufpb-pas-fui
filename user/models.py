from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Address(models.Model):
    street = models.CharField(max_length=50)
    number = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    neighborhood = models.CharField(max_length=20)
    df = models.CharField(max_length=15)

    def __str__(self):
        return self.city + " " + self.df

class User_animal(models.Model):

    user = models.OneToOneField(User, related_name="user", on_delete=models.CASCADE)
    type = models.CharField(max_length=6, default='Animal')
    address = models.OneToOneField(Address, related_name="address", on_delete=models.CASCADE, blank=True, null=True)
    rg = models.CharField(max_length=15, blank=True, null=True)
    cpf = models.CharField(max_length=20, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    photo = models.ImageField(upload_to='clients_photos/', default='clients_photos/default.jpg')



    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

