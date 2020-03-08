import re
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from ..models import User,Alerta,Departamento
from ..admin import UserCreationForm,UserCreationForm2

def decidir_usuario(request):
    return render(request, 'usuarios/cadastro_usuario.html')


def cadastarar_servidor(request):
    mensagem = ""
    sucesso = ""
    if request.method == "POST":
        form_usuario = UserCreationForm2(request.POST)

        if form_usuario.is_valid():
            cpf = form_usuario.cleaned_data['cpf']
            if not re.search(r'\d\d\d\d\d\d\d\d\d\d\d', str(cpf)):
                mensagem = {"erro CPF": "CPF Inválido"}
            else:
                adm1 = User.objects.get(email="jonasaraujo23137@gmail.com")
                usuario=form_usuario.save()
                chefe=Departamento.objects.get(nome=form_usuario.cleaned_data['lotacao'])

                titulo = "Novo Usuario Solicitando Acesso"
                informacoes = "Nome do Solicitante:" + usuario.nome + " Email:" + usuario.email
                Alerta.objects.create(titulo=titulo, identificador=usuario.id, url="listar_usuarios",
                                      informacoes=informacoes,
                                      usuario=chefe.chefia, status="1")
                Alerta.objects.create(titulo=titulo, identificador=usuario.id, url="listar_usuarios",
                                      informacoes=informacoes,
                                      usuario=adm1, status="1")


                sucesso = "ok"

        else:
            mensagem = form_usuario.errors
    else:
        form_usuario = UserCreationForm2()

    return render(request, 'usuarios/form_cadastro_servidor.html',
                  {"form_usuario": form_usuario, 'mensagem': mensagem,'sucesso':sucesso})

def cadastarar_aluno(request):
    mensagem = ""
    sucesso=""
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            matricula=form_usuario.cleaned_data['registro']

            if not re.search(r'\d\d\d\d\d\d\d\d\d\d\d', str(matricula)):
                mensagem={"erro matricula": "Matricula Inválida"}
            else:
                form_usuario.save()
                sucesso="ok"

        else:
            mensagem=form_usuario.errors
    else:
        form_usuario = UserCreationForm()

    return render(request, 'usuarios/form_cadastro_aluno.html',
                  {"form_usuario": form_usuario,'mensagem':mensagem,'sucesso':sucesso})


def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username,password=password)
        try:
            if (not User.objects.get(email=username).is_active):
                messages.error(request, "Usuário não autorizado")
                return redirect('logar_usuario')
            elif usuario is not None:
                login(request,usuario)
                return redirect('calendario')
            else:
                messages.error(request,"Senha incoreta")
                return redirect('logar_usuario')
        except:
            messages.error(request, "Usuário incorreto")
            return redirect('logar_usuario')
    else:
        form_login = AuthenticationForm()
    return render(request,'usuarios/form_login.html',{"form_login":form_login})


def deslogar_usuario(request):
    logout(request)
    return redirect('logar_usuario')

