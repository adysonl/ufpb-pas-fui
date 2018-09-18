from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import LoginForm

def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponse('Logado')
    else:
        form = LoginForm()
    context_dict = {'form': form}
    return render(request, 'index.html', context=context_dict)

