from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Endereco(models.Model):
    rua = models.CharField(max_length=50)
    numero = models.CharField(max_length=20)
    cidade = models.CharField(max_length=20)
    bairro = models.CharField(max_length=20)
    uf = models.CharField(max_length=15)

    def __str__(self):
        return self.cidade + " " + self.uf

class Usuario(models.Model):

    user = models.OneToOneField(User, related_name="user", on_delete=models.CASCADE)
    tipo = models.CharField(max_length=6, blank=True, null=True)
    endereco = models.OneToOneField(Endereco, related_name="endereco", on_delete=models.CASCADE, blank=True, null=True)
    rg = models.CharField(max_length=15, blank=True, null=True)
    cpf = models.CharField(max_length=20, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    photo = models.ImageField(upload_to='media/clients_photos', null=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name