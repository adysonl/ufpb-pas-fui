from django import forms

class usuario_form(forms.Form):
    username = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    rg = forms.CharField(max_length=15,
        widget=forms.TextInput(attrs={'placeholder':'000.000.000'})
    )
    cpf = forms.CharField(max_length=20,
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
    street = forms.CharField(max_length=15)
    number = forms.CharField(max_length=15)
    city = forms.CharField(max_length=15)
    neighborhood = forms.CharField(max_length=15)
    df = forms.CharField(max_length=15)

class usuario_form_authenticated(forms.Form):
    username = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    rg = forms.CharField(max_length=15,
        widget=forms.TextInput(attrs={'placeholder':'000.000.000'})
    )
    cpf = forms.CharField(max_length=20,
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
    number = forms.CharField(max_length=15)
    city = forms.CharField(max_length=15)
    neighborhood = forms.CharField(max_length=15)
    df = forms.CharField(max_length=15)
