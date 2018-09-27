from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponse
from .forms import usuario_form
from django.contrib.auth.models import User
from user.models import User_animal, Address
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
names = ['username', 'name', 'last_name', 'rg', 'cpf', 'email', 'telephone', 'password', 'street', 'number', 'city', 'neighborhood', 'df']

def cadastro_usuario(request):
    if (request.method == 'POST'):
        form = usuario_form(request.POST)
        fields = {'username':'', 'name':'', 'last_name':'', 'rg':'', 'cpf':'', 'email':'', 'telephone':'', 'password':'', 'street':'', 'number':'', 'city':'', 'neighborhood':'', 'df':''}
        if (form.is_valid()):
            for i in range(len(names)):
                fields[names[i]] = form.cleaned_data[names[i]]
            try:
                user_test = User.objects.get(username = fields['username'])
                if user_test:
                    messages.error(request, 'Usuário existe!')
            except User.DoesNotExist:
                user = User.objects.create_user(username=fields['username'], first_name=fields['name'], last_name=fields['last_name'], email=fields['email'], password=fields['password'])
                address = Address(street=fields['street'], number=fields['number'], city=fields['city'], neighborhood=fields['neighborhood'], df=fields['df'])
                address.save()
                user_animal = User_animal(type='Animal', user=user, address=address, rg=fields['rg'], cpf=fields['cpf'], telephone=fields['telephone'])
                user_animal.save()
                messages.success(request, 'Usuário cadastrado com sucesso!')
                form = usuario_form()
                return render(request, 'home/index.html')
    else:
        form = usuario_form()
    context_dict = {'form': form}
    return render(request, 'signup/signup.html', context_dict)