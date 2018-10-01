from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from user.models import User_animal, Event
from django.contrib.auth.decorators import login_required
from profile.forms import edit_photo_form
from user.forms import usuario_form
from user import urls
from django.contrib import messages
# Create your views here.

@login_required
def profile(request):
    form = edit_photo_form()
    user = request.user
    user_animal = User_animal.objects.get(user=user.id)
    return render(request, 'profile/profile_animal.html', { 'user_animal':user_animal, 'form': form})


@login_required
def add_photo(request):
    if request.method == 'POST':
        form = edit_photo_form(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            user_animal = User_animal.objects.get(user=user.id)
            user_animal.photo = form.cleaned_data['photo']
            user_animal.save()
            return redirect('profile')
    else:
        form = edit_photo_form()
    return render(request, 'profile/profile_king.html', {'form':form})

@login_required
def edit_profile(request):
    user = request.user
    usuario = User_animal.objects.get(user=user.id)

    dados = {
        'username' : user.username,
        'password' : user.password,
        'name': user.first_name,
        'last_name': user.last_name,
        'rg': usuario.rg,
        'cpf': usuario.cpf,
        'email': usuario.user.email,
        'telephone': usuario.telephone,
        'street': usuario.address.street,
        'number': usuario.address.number,
        'city': usuario.address.city,
        'neighborhood': usuario.address.neighborhood,
        'df': usuario.address.df,

    }
    form = usuario_form(initial = dados)
    return render(request, 'signup/signup.html', {'form': form})

@login_required
def list_event(request):
    user = request.user
    events = Event
    try:
        events = Event.objects.filter(king=user.id)
    except events.DoesNotExist:
        render(request, 'event/new.html')
    return render(request, 'event/list.html', {'user': user, 'events':events})