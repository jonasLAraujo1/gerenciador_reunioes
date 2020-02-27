import re
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from ..models import User, Tipo
from ..forms import FormTipo
from ..services import admin_services
@login_required()
def agendar_tipo(request):
    if request.user.is_admin:
        titulo = "Novo Tipo"
        mensagem = ""
        if request.method == "POST":
            form_tipo = FormTipo(request.POST)
            if form_tipo.is_valid():
                titulo = form_tipo.cleaned_data["titulo"]
                novo_tipo = Tipo(titulo=titulo)
                admin_services.salvar_tipo(novo_tipo)
                return redirect('agendar_reuniao')
            else:
                mensagem = form_tipo.errors
        else:
            form_tipo = FormTipo()
        return render(request, 'reunioes/criar_tipo.html',
                      {"titulo": titulo, "mensagem":mensagem, "form_tipo": form_tipo})
    else:
        return render(request,'excecoes/acesso_negado.html')

@login_required()
def listar_usuarios(request):
    if request.user.is_admin:
        usuarios=User.objects.all()
        if request.method == "POST":
            try:
                id = request.POST['excluir']
                usuarios_bd = User.objects.get(id=id)
                usuarios_bd.delete()
            except:
                id = request.POST['autorizar']
                usuarios_bd=User.objects.get(id=id)
                usuarios_bd.is_active=True
                usuarios_bd.save(force_update=True)
                usuarios=User.objects.all()
        return render(request, 'usuarios/listagem_usuarios.html', {"usuarios": usuarios})
    else:
        return render(request,'excecoes/acesso_negado.html')
def adm(request):
    return render(request, 'admin/paginas/index.html')

