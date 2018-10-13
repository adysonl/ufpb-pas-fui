from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import event_form
from .models import Event

# Create your views here.

@login_required
def create_event(request):
    if (request.method == 'POST'):
        form = event_form(request.POST, request.FILES, None)
        if form.is_valid():
            event = form.save(commit=False)
            event.king = request.user.id
            event.save()
            return redirect('profile')
    form = event_form()
    return render(request, 'event/new.html', {'form':form})

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

@login_required
def list_event(request):
    user = request.user
    events = Event
    try:
        events = Event.objects.filter(king=user.id)
    except events.DoesNotExist:
        render(request, 'event/new.html')
    return render(request, 'event/list.html', {'user': user, 'events':events})