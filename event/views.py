from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import event_form, rating_event
from .models import Event
from main.models import Rating
from user.models import User_animal
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
        return redirect('list_event')
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

@login_required
def rating_events(request, id):
    ratings = Rating.objects.filter(event_rated=id)
    for rating in ratings:
        if rating.user == request.user.username:
            return edite_rating(request, rating.id)
    if (request.method == 'POST'):
        form = rating_event(request.POST or None)
        if form.is_valid:
            rating = form.save(commit=False)
            rating.user = request.user.first_name
            rating.event_rated = Event.objects.get(id=id)
            rating.save()
            calculate_average(id)
            calculate_average_user(rating.event_rated.king, rating.event_rated.rate)
            return details_event(request, rating.event_rated.id)
    form = rating_event()
    return render(request, 'event/comment.html', {'form': form, 'event_name':rating.event_rated.name})

def calculate_average_user(user, rate):
    user_rated = User_animal.objects.get(id=user)
    total_rate = user_rated.rate*user_rated.number_ratings
    user_rated.number_ratings += 1
    new_rate = (total_rate+rate)/user_rated.number_ratings
    user_rated.rate = new_rate
    user_rated.save()

def calculate_average(id_event):
    event = Event.objects.get(id = id_event)
    rating = Rating.objects.all()
    count=0
    overall=0
    for i in rating:
        if i.event_rated == event:
            overall+=i.note
            count+=1
    if count > 0:
        event.rate = overall/count
    else:
        event.rate = 0
    event.number_ratings = count
    event.save()
    return event.rate

def details_event(request, id):
    try:
        event = Event.objects.get(id=id)
        ratings_filter = Rating.objects.filter(event_rated=id)
        paginator = Paginator(ratings_filter, 3)
        page = request.GET.get('page')
        ratings = paginator.get_page(page)
    except:
        pass
    return render(request, 'event/event_details.html', {'event':event, 'ratings':ratings})

@login_required
def edite_rating(request, id):
    rating = Rating.objects.get(id=id)
    rating_f = rating_event(request.POST or None, instance=rating)
    if rating_f.is_valid() and request.user.username == rating.user:
        event = Event.objects.get(id=rating.event_rated.id)
        user = User_animal.objects.get(id=event.king)
        rating_f.save()
        calculate_average(event.id)
        calculate_average_user(user.id, event.rate)
        return details_event(request, rating.event_rated.id)
    return render(request, 'event/comment.html', {'form':rating_f})

@login_required
def delete_rating(request, id):
    rating = Rating.objects.get(id=id)
    event = Event.objects.get(id=rating.event_rated.id)
    rating.delete()
    calculate_average(event.id)
    return details_event(request, event.id)