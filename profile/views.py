from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from user.models import User_animal, Event, Address, User
from django.contrib.auth.decorators import login_required
from profile.forms import edit_photo_form
from user.forms import user_form,event_form,address_form,auth_user_on

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
    user_anl = User_animal.objects.get(user=user)
    address = Address.objects.get(id=user_anl.address.id)
    address_f = address_form(request.POST or None, instance=address)
    auth_f = auth_user_on(request.POST or None, instance=user)
    user_f = user_form(request.POST or None, instance=user_anl)
    if address_f.is_valid() and user_f.is_valid() and auth_f.is_valid():
        print('affffffffffffffffffffffffffff')
        address = address_f.save()
        user = auth_f.save()
        user_anl = user_f.save(commit=False)
        user_anl.address = address
        user_anl.user = user
        user_anl.save()
        return redirect('profile')
    context_dict = {'address_f': address_f, 'auth_f':auth_f,
    'user_f':user_f, 'user':user,'user_anl':user_anl,'address':address}
    return render(request, 'signup/signup.html', context_dict)

@login_required
def list_event(request):
    user = request.user
    events = Event
    try:
        events = Event.objects.filter(king=user.id)
    except events.DoesNotExist:
        render(request, 'event/new.html')
    return render(request, 'event/list.html', {'user': user, 'events':events})

@login_required
def edit_event(request, id):
    event = Event.objects.get(id=id)
    form = event_form(request.POST or None, instance=event)

    if form.is_valid():
        event = form.save()
        return render(request, 'event/list.html')
    context = {'form': form, 'event':event}
    return render(request, 'event/new.html', context)

@login_required
def delete_event(request, id):
    event = Event.objects.get(id=id)
    event.delete()
    return redirect('list_event')
