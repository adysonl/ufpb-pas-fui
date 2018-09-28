from forms import event_form
from django.shortcuts import render, redirect

# Create your views here.

def create_event(request):
    if (request.method == 'POST'):
        form = event_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
        form = event_form()
        return render(request, 'event/event.html', {'form':form})

