from django import forms
from user.models import Usuario

class edit_photo_form(forms.Form):
    photo = forms.ImageField()

    class meta:
        model = Usuario
        fields = ['photo']
