from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm

def logout_final(request):
    logout(request)
    return redirect('logout')

