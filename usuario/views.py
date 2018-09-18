from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from usuario.forms import usuario_form
from django.contrib.auth.models import User
from main.models import Usuario
from django.contrib import messages

# Create your views here.

def cadastro_usuario(request):
    context_dict = {}
    if (request.method == 'POST'):
        form = usuario_form(request.POST)
        if (form.is_valid()):
            nome = form.cleaned_data['nome']
            sobrenome = form.cleaned_data['sobrenome']
            email = form.cleaned_data['email']
            password = form.cleaned_data['senha']
            tipo = form.cleaned_data['tipo']
            user = User.objects.create_user(
                username=email, first_name=nome, last_name=sobrenome, email=email, password=password)

            usuario = Usuario(tipo=tipo, user=user)
            usuario.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            context_dict = {'form': form,
                    'usuario': usuario}
    else:
        form = usuario_form()
    return render(request, 'signup/signup.html', {'form': form})
