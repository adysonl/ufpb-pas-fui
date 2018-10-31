from django import forms
from user.models import User_animal, Wishes

class edit_photo_form(forms.Form):
    photo = forms.ImageField()

    class meta:
        model = User_animal
        fields = ['photo']

class wishes_form(forms.ModelForm):
    class Meta:
        model = Wishes
        fields = '__all__'
        exclude = ('user',)