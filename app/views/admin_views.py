import re
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from ..models import User, Tipo
from ..forms import FormTipo
from ..services import admin_services, alerta_services,reuniao_service
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
    if request.user.is_admin or request.user.servidor:
        usuario = reuniao_service.usuario_logado(request)
        notificacao = alerta_services.contar(request.user)
        usuarios=User.objects.filter(is_active=False).all()
        if request.method == "POST":
            try:
                id = request.POST['excluir']
                acao='excluir'
            except:
                id = request.POST['autorizar']
                acao = 'autorizar'
            if acao =='excluir':
                usuario_bd = User.objects.get(id=id)
                alerta=alerta_services.alerta_reuniao(id,request.user)
                alerta_services.visualizar_alerta(alerta.id)
                usuario_bd.delete()
                return redirect("listar")
            elif acao =='autorizar':

                usuario_bd=User.objects.get(id=id)
                alerta=alerta_services.alerta_reuniao(id,request.user)
                usuario_bd.is_active=True
                usuario_bd.save(force_update=True)
                alerta_services.visualizar_alerta(alerta.id)
                return redirect("listar")

        return render(request, 'usuarios/listagem_usuarios.html', {"usuarios": usuarios,"usuario":usuario,"notificacao":notificacao})
    else:
        return render(request,'excecoes/acesso_negado.html')



def adm(request):
    return render(request, 'admin/paginas/index.html')

