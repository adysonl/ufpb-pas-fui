from django.shortcuts import render
from django.http import HttpResponse
from .forms import usuario_form
from django.contrib.auth.models import User
from main.models import Usuario, Endereco
from django.contrib import messages

# Create your views here.

def cadastro_usuario(request):
    if (request.method == 'POST'):
        form = usuario_form(request.POST)
        if (form.is_valid()):
            tipo = form.cleaned_data['tipo']
            nome = form.cleaned_data['nome']
            sobrenome = form.cleaned_data['sobrenome']
            rg = form.cleaned_data['rg']
            cpf = form.cleaned_data['cpf']
            email = form.cleaned_data['email']
            telefone = form.cleaned_data['telefone']
            senha = form.cleaned_data['senha']
            rua = form.cleaned_data['rua']
            numero = form.cleaned_data['numero']
            cidade = form.cleaned_data['cidade']
            bairro = form.cleaned_data['bairro']
            uf = form.cleaned_data['uf']

            user = User.objects.create_user(username=email, first_name=nome, last_name=sobrenome, email=email, password=senha)
            endereco = Endereco(rua=rua, numero=numero, cidade=cidade, bairro=bairro, uf=uf)
            endereco.save()
            usuario = Usuario(tipo=tipo, user=user, endereco=endereco, rg=rg, cpf=cpf, telefone=telefone)
            usuario.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
    else:
        form = usuario_form()
    context_dict = {'form': form}
    return render(request, 'signup/signup.html', context_dict)