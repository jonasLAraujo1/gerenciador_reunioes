from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
# from ..forms import FormProfile

def cadastarar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        # form_perfil = FormProfile(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('logar_usuario')
    else:
        form_usuario = UserCreationForm()
        # form_perfil = FormProfile()
    return render(request, 'usuarios/form_cadastro_usuario.html',
                  {"form_usuario": form_usuario})

def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username,password=password)
        if usuario is not None:
            login(request,usuario)
            return redirect('calendario')
        else:
            messages.error(request,"Usuario ou senha incoretos")
            return redirect('logar_usuario')
    else:
        form_login = AuthenticationForm()
    return render(request,'usuarios/form_login.html',{"form_login":form_login})
def deslogar_usuario(request):
    logout(request)
    return redirect('logar_usuario')