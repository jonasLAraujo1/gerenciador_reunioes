from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.defaults import bad_request

from ..entidades import reunioes, alertas
from ..forms import *
from ..services import reuniao_service, data_services, alerta_services


@login_required()
def agendar_reuniao(request):
    titulo = "Agendar"
    notificacao = 0
    if request.method == "POST":
        form_data = FormData(request.POST)
        form_reuniao = FormAgendaReuniao(request.POST)

        if form_data.is_valid():
            dia = form_data.cleaned_data["dia"]
            inicio = form_data.cleaned_data["inicio"]
            fim = form_data.cleaned_data["fim"]
            nova_data = reunioes.Data(dia=dia, inicio=inicio, fim=fim)

            if form_reuniao.is_valid():
                tipo = form_reuniao.cleaned_data["tipo_reuniao"]
                pauta = form_reuniao.cleaned_data["pauta"]
                local = form_reuniao.cleaned_data["local"]
                semestre = form_reuniao.cleaned_data["semestre"]
                deliberacoes = ""
                observacoes = ""
                status = "1"
                data_bd = data_services.salvar_data(nova_data)
                nova_reuniao = reunioes.Reuniao(tipo_reuniao=tipo, data=data_bd, pauta=pauta, local=local,
                                                semestre=semestre, observacoes=observacoes, deliberacoes=deliberacoes,
                                                status=status)
                reuniao_service.agendar_reuniao(nova_reuniao)
                observacoes = "Uma nova Reunião com a Pauta: " + str(pauta) + \
                              " Foi Agendada Para o Dia: " + str(dia) + " com  previsão de Inicioa as " + str(inicio)
                alerta_novo = alertas.Alerta(titulo="Reunião Agendada", observacoes=observacoes, status="1")
                alerta_services.criar_alerta(alerta_novo)

                return redirect('calendario')
    else:
        form_reuniao = FormAgendaReuniao()
        form_data = FormData()

    return render(request, 'reunioes/form_pre_reuniao.html',
                  {"titulo": titulo, "notificacao": notificacao, "form_reuniao": form_reuniao,
                   "form_data": form_data})


@login_required()
def marcar_reuniao(request, id):
    reuniao_bd = reuniao_service.retornar_reuniao_id(id)
    data_bd = data_services.retornar_data_id(id)

    form_reuniao = FormReuniao(request.POST or None, instance=reuniao_bd)
    form_data = FormData(request.POST or None, instance=data_bd)
    titulo = "Marcar"
    notificacao = 0
    if form_data.is_valid():
        dia = form_data.cleaned_data["dia"]
        inicio = form_data.cleaned_data["inicio"]
        fim = form_data.cleaned_data["fim"]
        nova_data = reunioes.Data(dia=dia, inicio=inicio, fim=fim)
        if form_reuniao.is_valid():
            tipo = form_reuniao.cleaned_data["tipo_reuniao"]
            pauta = form_reuniao.cleaned_data["pauta"]
            local = form_reuniao.cleaned_data["local"]
            semestre = form_reuniao.cleaned_data["semestre"]
            deliberacoes = form_reuniao.cleaned_data["deliberacoes"]
            observacoes = form_reuniao.cleaned_data["observacoes"]
            status = "2"
            data_services.alterar_data(data_bd, nova_data)
            nova_reuniao = reunioes.Reuniao(tipo_reuniao=tipo, data=data_bd, pauta=pauta, local=local,
                                            semestre=semestre, observacoes=observacoes, deliberacoes=deliberacoes,
                                            status=status)
            reuniao_service.alterar_reuniao(reuniao_bd, nova_reuniao)
            return redirect('calendario')
    return render(request, 'reunioes/form_reuniao.html',
                  {"titulo": titulo, "notificacao": notificacao, "form_reuniao": form_reuniao,
                   "form_data": form_data})


@login_required()
def consolidar_reuniao(request, id):
    reuniao_bd = reuniao_service.retornar_reuniao_id(id)
    data_bd = data_services.retornar_data_id(id)

    form_reuniao = FormReuniao(request.POST or None, instance=reuniao_bd)
    form_data = FormData(request.POST or None, instance=data_bd)
    titulo = "Consolidar"
    notificacao = 0
    if form_data.is_valid():
        dia = form_data.cleaned_data["dia"]
        inicio = form_data.cleaned_data["inicio"]
        fim = form_data.cleaned_data["fim"]
        nova_data = reunioes.Data(dia=dia, inicio=inicio, fim=fim)
        if form_reuniao.is_valid():
            tipo = form_reuniao.cleaned_data["tipo_reuniao"]
            pauta = form_reuniao.cleaned_data["pauta"]
            local = form_reuniao.cleaned_data["local"]
            semestre = form_reuniao.cleaned_data["semestre"]
            deliberacoes = form_reuniao.cleaned_data["deliberacoes"]
            observacoes = form_reuniao.cleaned_data["observacoes"]
            status = "3"
            data_services.alterar_data(data_bd, nova_data)
            nova_reuniao = reunioes.Reuniao(tipo_reuniao=tipo, data=data_bd, pauta=pauta, local=local,
                                            semestre=semestre, observacoes=observacoes, deliberacoes=deliberacoes,
                                            status=status)
            reuniao_service.alterar_reuniao(reuniao_bd, nova_reuniao)
            return redirect('calendario')
    return render(request, 'reunioes/form_reuniao.html',
                  {"titulo": titulo, "notificacao": notificacao, "form_reuniao": form_reuniao,
                   "form_data": form_data})


@login_required()
def agendar_tipo(request):
    titulo = "Novo Tipo"
    notificacao = 0
    if request.method == "POST":
        form_tipo = FormTipo(request.POST)
        if form_tipo.is_valid():
            titulo = form_tipo.cleaned_data["titulo"]
            cor = form_tipo.cleaned_data["cor"]
            novo_tipo = reunioes.Tipo(titulo=titulo, cor=cor)
            reuniao_service.salvar_tipo(novo_tipo)
            return redirect('agendar_reuniao')
    else:
        form_tipo = FormTipo()
    return render(request, 'reunioes/criar_tipo.html',
                  {"titulo": titulo, "notificacao": notificacao, "form_tipo": form_tipo})


@login_required()
def calendario(request):
    notificacao = ""
    reunioes = reuniao_service.retornar_tudo()
    # print(reunioes)
    return render(request, 'reunioes/main.html', {"reunioes": reunioes, "notificacao": notificacao})


def novo_tipo(request):
    form = FormTipo(request.POST)
    if form.is_valid():
        form.save(commit=True)
        return redirect('#')
    else:
        return bad_request(request, None, 'ops_400.html')


@login_required()
def remover(request, id):
    reuniao_bd = reuniao_service.retornar_reuniao_id(id)
    if (request.method == "POST"):
        reuniao_service.apagar_reuniao(reuniao_bd)
        return redirect('calendario')
    return render(request, 'reunioes/excluir.html', {'reuniao_bd': reuniao_bd})