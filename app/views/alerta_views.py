from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect

from ..entidades import reunioes
from ..forms import *
from ..services import reuniao_service, alerta_services



@login_required()
def resultado_busca(request):
    notificacao = alerta_services.contar(request.user)
    if request.method == "POST":
        semestre = request.POST['busca']
        resultados = reuniao_service.retornar_por_semestre(semestre)
    return render(request, 'reunioes/busca.html', { "notificacao": notificacao,"resultados":resultados,"semestre":semestre})
@login_required()
def listar(request):
    notificacao = alerta_services.contar(request.user)
    alertas=alerta_services.listar_todos(request.user)
    if request.method == "POST":
        semestre = request.POST['busca']
        resultados = reuniao_service.retornar_por_semestre(semestre)
    return render(request, 'alertas/listagem.html', {"notificacao": notificacao,"alertas":alertas})
