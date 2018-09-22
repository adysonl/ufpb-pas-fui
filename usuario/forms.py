from django import forms

USUARIOS_CHOICE = (
    ("kg", "King"),
    ("am", "Animal")
)

class usuario_form(forms.Form):
    tipo = forms.ChoiceField(label="Tipo de Usuário:", choices=USUARIOS_CHOICE, widget=forms.RadioSelect())
    nome = forms.CharField(label="Primeiro nome:", max_length=100)
    sobrenome = forms.CharField(label="Sobrenome nome:", max_length=100)
    email = forms.EmailField(label="Seu email:", max_length=100)
    senha = forms.CharField(label='Senha:', widget=forms.PasswordInput())