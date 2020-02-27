from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect

from ..entidades import reunioes
from ..forms import *
from ..services import reuniao_service, alerta_services



@login_required()
def listar(request):
    usuario = reuniao_service.usuario_logado(request)
    notificacao = alerta_services.contar(request.user)
    alertas=alerta_services.listar_todos(request.user)
    contador=0
    if request.method == "POST":
        try:
            id = request.POST['id']
            alerta_services.apagar_alerta(id)
        # if request.POST['id'] ==None:
        except:
            id = request.POST['status']
            alerta_services.visualizar_alerta(id)


        return redirect("listar")
    return render(request, 'alertas/listagem.html', {"notificacao": notificacao,"alertas":alertas,"usuario":usuario})
