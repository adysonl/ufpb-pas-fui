from django import forms
from main.models import Usuario

class edit_photo_form(forms.Form):
    photo = forms.ImageField(label='photo')

    class meta:
        model = Usuario
        fields = ['photo']
