from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import usuario_form, usuario_form_authenticated, event_form
from django.contrib.auth.models import User
from user.models import User_animal, Address, Event
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


from django.contrib.auth.hashers import make_password

# Create your views here.
names = ['username', 'name', 'last_name', 'rg', 'cpf', 'email', 'telephone', 'password', 'street', 'number', 'city', 'neighborhood', 'df']

def cadastro_usuario(request):
    if (request.method == 'POST'):
        fields = {'username':'', 'name':'', 'last_name':'', 'rg':'', 'cpf':'', 'email':'', 'telephone':'', 'password':'', 'street':'', 'number':'', 'city':'', 'neighborhood':'', 'df':''}
        if request.user.is_authenticated:
            del fields['password']
            del names[7]
            form = usuario_form_authenticated(request.POST)
        else:
            form = usuario_form(request.POST)
        
        if (form.is_valid()):
            for i in range(len(names)):
                fields[names[i]] = form.cleaned_data[names[i]]
            try:
                user_test = User.objects.get(username = fields['username'])
                old_usuario = User_animal.objects.get(user=user_test.id)
                if request.user.is_authenticated:
                    Address.objects.filter(id=old_usuario.address.id).update(id=old_usuario.address.id,
                    street=fields['street'],number=fields['number'], city=fields['city'],neighborhood=fields['neighborhood'], df=fields['df'])
                    User_animal.objects.filter(user=user_test.id).update(type='Animal', user=user_test.id,address=old_usuario.address.id,
                    rg=fields['rg'], cpf=fields['cpf'],telephone=fields['telephone'])
                    User.objects.filter(id=user_test.id).update(username=old_usuario.user.username, first_name=fields['name'], last_name=fields['last_name']
                    ,email=fields['email'])
                    user = User.objects.get(username=fields['username'])
                    login(request, user)
                    return redirect('profile')
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
                return redirect('login')
    else:
        form = usuario_form()

    context_dict = {'form': form}
    return render(request, 'signup/signup.html', context_dict)

def update_to_king(request):
    User_animal.objects.filter(user=request.user.id).update(type='King')
    return redirect('profile')

def delete_user(request):
    user = request.user
    usuario = User_animal.objects.get(user = user.id)
    usuario.address.delete()
    user.delete()
    usuario.delete()
    return redirect('logout')

def create_event(request):
    if (request.method == 'POST'):
        form = event_form(request.POST, request.FILES)
        if form.is_valid():
            event = Event(name=form.cleaned_data['name'], king=request.user.id, modality=form.cleaned_data['modality'],
                          forbidden=form.cleaned_data['forbidden'], drinks=form.cleaned_data['drinks'], type=form.cleaned_data['type'],
                          description=form.cleaned_data['description'], capacity=form.cleaned_data['capacity'],image=form.cleaned_data['image'])
            event.save()

            return redirect('profile')
    form = event_form()
    return render(request, 'event/new.html', {'form':form})
