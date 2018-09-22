from django import forms

USUARIOS_CHOICE = (
    ("kg", "King"),
    ("am", "Animal")
)

class usuario_form(forms.Form):
    tipo = forms.ChoiceField(label="Tipo de Usuário:", choices=USUARIOS_CHOICE, widget=forms.RadioSelect())
    nome = forms.CharField(label="Primeiro nome:", max_length=100)
    sobrenome = forms.CharField(label="Sobrenome nome:", max_length=100)
    rg = forms.CharField(max_length=15,
        widget=forms.TextInput(attrs={'placeholder':'000.000.000'})
    )
    cpf = forms.CharField(max_length=20,
        widget=forms.TextInput(attrs={'placeholder':'000.000.000-00'})
    )
    email = forms.EmailField(label="Seu email:", max_length=100,
        widget=forms.TextInput(attrs={'placeholder':'email@email.com'})
    )
    telefone = forms.CharField(max_length=15,
        widget=forms.TextInput(attrs={'placeholder':'(00) 00000-0000'})
    )
    senha = forms.CharField(label='Senha:', widget=forms.PasswordInput())
    #endereço
    rua = forms.CharField(max_length=15)
    numero = forms.CharField(max_length=15)
    cidade = forms.CharField(max_length=15)
    bairro = forms.CharField(max_length=15)
    uf = forms.CharField(max_length=15)