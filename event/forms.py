from .models import Event
from main.models import Rating
from django import forms
from django.forms import ModelForm

class event_form(ModelForm):
    forms.DateInput.input_type = "date"
    class Meta:
        model = Event
        fields = '__all__'
        exclude = ('king',)

class rating_event(ModelForm):
    class Meta:
        model = Rating
        fields = ['user', 'commented', 'comment', 'note']
        exclude = ('type',)