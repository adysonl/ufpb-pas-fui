from django import forms
from .models import Event

class usuario_form(forms.Form):
    username = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    rg = forms.CharField(max_length=15,
        widget=forms.TextInput(attrs={'placeholder':'000.000.000'})
    )
    cpf = forms.CharField(max_length=14,
        widget=forms.TextInput(attrs={'placeholder':'000.000.000-00'})
    )
    email = forms.EmailField(max_length=100,
        widget=forms.TextInput(attrs={'placeholder':'email@email.com'})
    )
    telephone = forms.CharField(max_length=15,
        widget=forms.TextInput(attrs={'placeholder':'(00) 00000-0000'})
    )
    password = forms.CharField(widget=forms.PasswordInput())
    #endereço
    street = forms.CharField(max_length=50)
    number = forms.CharField(max_length=5)
    city = forms.CharField(max_length=20)
    neighborhood = forms.CharField(max_length=20)
    df = forms.CharField(max_length=2)

class usuario_form_authenticated(forms.Form):
    username = forms.CharField(max_length=100)
    name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=100)
    rg = forms.CharField(max_length=15,
        widget=forms.TextInput(attrs={'placeholder':'000.000.000'})
    )
    cpf = forms.CharField(max_length=14,
        widget=forms.TextInput(attrs={'placeholder':'000.000.000-00'})
    )
    email = forms.EmailField(max_length=100,
        widget=forms.TextInput(attrs={'placeholder':'email@email.com'})
    )
    telephone = forms.CharField(max_length=15,
        widget=forms.TextInput(attrs={'placeholder':'(00) 00000-0000'})
    )
    #endereço
    street = forms.CharField(max_length=15)
    number = forms.CharField(max_length=5)
    city = forms.CharField(max_length=20)
    neighborhood = forms.CharField(max_length=20)
    df = forms.CharField(max_length=2)

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
    forms.DateInput.input_type = "date"
    name = forms.CharField(max_length=50)
    modality = forms.ChoiceField(choices = MODALITY_CHOICES)
    forbidden = forms.BooleanField(required=False)
    drinks = forms.BooleanField(required=False)
    type = forms.ChoiceField(choices = TYPE_EVENT_CHOICES)
    capacity = forms.IntegerField(required=False)
    image = forms.ImageField()
    description = forms.CharField(max_length=250)
    start_date = forms.DateField(widget=forms.widgets.DateInput(format="%m/%d/%Y"))
    end_date = forms.DateField(widget=forms.widgets.DateInput(format="%m/%d/%Y"))

    class Meta:
        model = Event
        fiels = '__all__'
