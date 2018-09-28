from django import forms
from event.models import Event

MODALITY_CHOICES = (
    ('fr','Free'),
    ('pd','Paid')
)

TYPE_EVENT_CHOICES = (
    ('p', 'Rolê Pequeno'),
    ('m', 'Rolê Médio'),
    ('g', 'Moster grande porte')

)
class event_form(forms.Form):
    name = forms.CharField(max_length=50)
    king = forms.IntegerField(required=False)
    modality = forms.ChoiceField(choices = MODALITY_CHOICES)
    forbidden = forms.BooleanField(required=False)
    drinks = forms.BooleanField(required=False)
    type = forms.ChoiceField(choices = TYPE_EVENT_CHOICES)
    capacity = forms.IntegerField(required=False)
    image = forms.ImageField()
    description = forms.CharField(max_length=250)
