from .models import Event
from django import forms
from django.forms import ModelForm

class event_form(ModelForm):
    forms.DateInput.input_type = "date"
    class Meta:
        model = Event
        fields = '__all__'
        exclude = ('king',)