from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import event_form, rating_event, event_tags_form
from django.contrib.auth.models import User
from .models import Event, EventTags
from main.models import Rating
from user.models import User_animal, Wishes
from profile.forms import wishes_form
# Create your views here.

@login_required
def create_event(request):
    if (request.method == 'POST'):
        form = event_form(request.POST, request.FILES, None)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('profile')
    form = event_form()
    return render(request, 'event/new.html', {'form':form})

@login_required
def edit_event(request, id):
    event = Event.objects.get(id=id)
    form = event_form(request.POST or None, instance=event)
    if form.is_valid():
        event = form.save(commit=False)
        event.user = request.user
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
        events = Event.objects.filter(user=user)
    except events.DoesNotExist:
        render(request, 'event/new.html')
    return render(request, 'event/list.html', {'user': user, 'events':events})

@login_required
def rating_events(request, id):
    event = Event.objects.get(id=id)
    user = User.objects.get(id=event.user.id)
    ratings = Rating.objects.filter(event_rated=id)
    for rating in ratings:
        if rating.user_rater == request.user:
            return edite_rating(request, rating.id)
    if (request.method == 'POST'):
        form = rating_event(request.POST or None)
        if form.is_valid:
            rating = form.save(commit=False)
            rating.user = request.user.first_name
            rating.user_rater = request.user
            rating.event_rated = Event.objects.get(id=id)
            rating.save()
            calculate_average(id)
            calculate_average_user(user)
            return details_event(request, rating.event_rated.id)
    form = rating_event()
    return render(request, 'event/comment.html', {'form': form, 'event_name':event.name})

def calculate_average_user(user):
    overall = 0
    count = 0
    events = Event.objects.all()
    user_anl = User_animal.objects.get(user=user)
    for event in events:
        overall+=event.rate
        count+=1
    if count >= 1:
        user_anl.rate = overall/count
    else:
        user_anl.rate = 0
    user_anl.number_ratings = count
    user_anl.save()

def calculate_average(id_event):
    event = Event.objects.get(id = id_event)
    rating = Rating.objects.all()
    count=0
    overall=0
    for i in rating:
        if i.event_rated == event:
            overall+=i.note
            count+=1
    if count >= 1:
        event.rate = overall/count
    else:
        event.rate = 0
    event.number_ratings = count
    event.save()

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
    event = Event.objects.get(id=rating.event_rated.id)
    user = User.objects.get(id=event.user.id)
    rating_f = rating_event(request.POST or None, instance=rating)
    if rating_f.is_valid() and request.user.username == rating.user:
        rating_f.save()
        calculate_average(event.id)
        calculate_average_user(user)
        return details_event(request, rating.event_rated.id)
    return render(request, 'event/comment.html', {'form':rating_f, 'event_name':event.name})

@login_required
def delete_rating(request, id):
    rating = Rating.objects.get(id=id)
    event = Event.objects.get(id=rating.event_rated.id)
    user = User.objects.get(id=event.user.id)
    rating.delete()
    calculate_average(event.id)
    calculate_average_user(user)
    return details_event(request, event.id)

@login_required
def event_tags(request, id):
    event = Event.objects.get(id=id)
    try:
        tags = event.tags
        form = event_tags_form(request.POST or None, instance=tags)
        if form.is_valid():
            event.tags = form
            event.save()
            return redirect('profile')
    except:
        if (request.method == 'POST'):
            form = event_tags_form(request.POST or None)
            if form.is_valid():
                tags = form.save()
                event.tags = tags
                event.save()
                return redirect('profile')
        form = event_tags_form()
    return render(request, 'event/event_tags.html', {'form':form})

