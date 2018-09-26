from django.shortcuts import render
from django.http import HttpResponse
from .forms import usuario_form
from django.contrib.auth.models import User
from user.models import User_animal, Address
from django.contrib import messages

# Create your views here.

def cadastro_usuario(request):
    if (request.method == 'POST'):
        form = usuario_form(request.POST)
        print(form)
        if (form.is_valid()):
            username = form.cleaned_data['username']
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            rg = form.cleaned_data['rg']
            cpf = form.cleaned_data['cpf']
            email = form.cleaned_data['email']
            telephone = form.cleaned_data['telephone']
            password = form.cleaned_data['password']
            street = form.cleaned_data['street']
            number = form.cleaned_data['number']
            city = form.cleaned_data['city']
            neighborhood = form.cleaned_data['neighborhood']
            df = form.cleaned_data['df']

            try:
                user_test = User.objects.get(username = username)
                if user_test:
                    messages.error(request, 'Usuário existe!')
            except User.DoesNotExist:
                user = User.objects.create_user(username=username, first_name=name, last_name=last_name, email=email, password=password)
                address = Address(street=street, number=number, city=city, neighborhood=neighborhood, df=df)
                address.save()
                user_animal = User_animal(type='Animal', user=user, address=address, rg=rg, cpf=cpf, telephone=telephone)
                user_animal.save()
                messages.success(request, 'Usuário cadastrado com sucesso!')
                form = usuario_form()
                return render(request, 'home/index.html')
    else:
        form = usuario_form()
    context_dict = {'form': form}
    return render(request, 'signup/signup.html', context_dict)