from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm
from event.models import Event

# Create your views here.

def index(request):
    event_list_tags = Event.objects.filter(Q())
    event_list = Event.objects.all().order_by('-rate')
    paginator = Paginator(event_list, 3) # Show 25 contacts per page

    page = request.GET.get('page')
    events = paginator.get_page(page)
    context_dict = {'events': events}
    return render(request, 'home/index.html', context=context_dict)

def search(request):
    keyword = request.GET.get('search')
    events = list(Event.objects.filter(Q(name__contains=keyword) | Q(description__contains=keyword)))
    events.sort(key=lambda event: event.rate, reverse=True)
    return render(request, 'search/search.html', {'events':events})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponse('Wellcome')
    else:
        form = LoginForm()
    context_dict = {'form': form}
    return render(request, 'index.html', context=context_dict)

def logout_user(request):
    logout(request)
    return redirect('logout')
