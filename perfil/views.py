from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from main.models import Usuario
from django.contrib.auth.decorators import login_required
from perfil.forms import edit_photo_form
# Create your views here.

@login_required
def perfil(request):
    form = edit_photo_form()
    user = request.user
    usuario = Usuario.objects.get(user=user.id)
    if usuario.tipo == 'kg':
        return render(request, 'perfil/perfil_king.html', { 'usuario':usuario, 'form': form})


def add_photo(request):
    if request.method == 'POST':
        form = edit_photo_form(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            usuario = Usuario.objects.get(user=user.id)
            usuario.photo = form.cleaned_data['photo']
            usuario.save()
            return redirect('perfil')
    else:
        form = edit_photo_form()
    return render(request, 'perfil/perfil_king.html', {'form':form})


