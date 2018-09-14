from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'nome_do_prato': "Pizza de Pepperoni"}
    return render(request, 'home/index.html', context=context_dict)
