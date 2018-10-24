from django.db import models


# Create your models here.

class EventTags(models.Model):
    TYPE_CHOICES = (
        ('C', 'Cultural'),
        ('F', 'Festas'),
        ('S', 'Shows'),
        ('E', 'Exposições')
    )
    TASTE_CHOICES = (
        ('S', 'Sertanejo'),
        ('F', 'Funk'),
        ('R', 'Rock'),
        ('O', 'Outros')
    )
    YN_CHOICES = (
        ('Y', 'Sim'),
        ('N', 'Não'),
    )
    PRICE_CHOICES = (
        ('free', 'Sim'),
        ('10~20', 'De R$10 até R$20'),
        ('20~30', 'De R$20 até R$30'),
        ('>30', 'Mais de R$30'),
    )

    type = models.CharField(max_length=2, choices=TYPE_CHOICES, blank=True, null=True)
    music_taste = models.CharField(max_length=2, choices=TASTE_CHOICES, blank=True, null=True)
    drink = models.CharField(max_length=2, choices=YN_CHOICES, blank=True, null=True)
    price = models.CharField(max_length=5, choices=PRICE_CHOICES, blank=True, null=True)
    distance = models.CharField(max_length=2, choices=YN_CHOICES, blank=True, null=True)

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
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    rate = models.IntegerField(default=0,blank=True, null=True)
    number_ratings = models.IntegerField(default=0)
    tags = models.ForeignKey(EventTags, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

