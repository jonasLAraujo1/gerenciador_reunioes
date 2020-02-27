from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.views.defaults import bad_request
from easy_pdf.rendering import render_to_pdf_response

from ..entidades import reunioes
from ..forms import *
from ..services import reuniao_service, data_services, alerta_services


@login_required()
def agendar_reuniao(request):
    titulo = "Agendar"
    usuario = reuniao_service.usuario_logado(request)
    notificacao = alerta_services.contar(request.user)
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
                participantes = form_reuniao.cleaned_data["participantes"]

                deliberacoes = ""
                observacoes = ""
                status = "1"
                data_bd = data_services.salvar_data(nova_data)
                nova_reuniao = reunioes.Reuniao(tipo_reuniao=tipo, data=data_bd, pauta=pauta, local=local,
                                                semestre=semestre,participantes=participantes, observacoes=observacoes, deliberacoes=deliberacoes,
                                                cor="1",status=status)
                reuniao_service.agendar_reuniao(nova_reuniao)

                return redirect('calendario')
    else:
        form_reuniao = FormAgendaReuniao()
        form_data = FormData()

    return render(request, 'reunioes/form_pre_reuniao.html',
                  {"titulo": titulo, "notificacao": notificacao, "form_reuniao": form_reuniao,
                   "form_data": form_data,"usuario":usuario})


@login_required()
def marcar_reuniao(request, id):
    reuniao_bd = reuniao_service.retornar_reuniao_id(id)
    data_bd = data_services.retornar_data_id(id)

    form_reuniao = FormReuniao(request.POST or None, instance=reuniao_bd)
    form_data = FormData(request.POST or None, instance=data_bd)
    titulo = "Marcar"
    mensagem =""
    notificacao = alerta_services.contar(request.user)

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
            participantes = form_reuniao.cleaned_data["participantes"]
            deliberacoes = form_reuniao.cleaned_data["deliberacoes"]
            observacoes = form_reuniao.cleaned_data["observacoes"]
            status = "2"
            cor = "2"
            data_services.alterar_data(data_bd, nova_data)
            nova_reuniao = reunioes.Reuniao(tipo_reuniao=tipo, data=data_bd, pauta=pauta, local=local,
                                            semestre=semestre,participantes=participantes, observacoes=observacoes, deliberacoes=deliberacoes,
                                            status=status,cor=cor)
            reuniao_service.alterar_reuniao(reuniao_bd, nova_reuniao)
            return redirect('calendario')
        else:
            mensagem = form_reuniao.errors
    else:
        mensagem = form_data.errors
    return render(request, 'reunioes/form_reuniao.html',
                  {"titulo": titulo, "notificacao": notificacao,"mensagem":mensagem ,"form_reuniao": form_reuniao,
                   "form_data": form_data})


@login_required()
def consolidar_reuniao(request, id):

    reuniao_bd = reuniao_service.retornar_reuniao_id(id)
    data_bd = data_services.retornar_data_id(id)
    notificacao = alerta_services.contar(request.user)
    form_reuniao = FormReuniao(request.POST or None, instance=reuniao_bd)
    form_data = FormData(request.POST or None, instance=data_bd)
    titulo = "Consolidar"
    
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
            participantes=form_reuniao.cleaned_data["participantes"]
            deliberacoes = form_reuniao.cleaned_data["deliberacoes"]
            observacoes = form_reuniao.cleaned_data["observacoes"]
            status = "3"
            cor="3"
            data_services.alterar_data(data_bd, nova_data)
            nova_reuniao = reunioes.Reuniao(tipo_reuniao=tipo, data=data_bd, pauta=pauta, local=local,
                                            semestre=semestre,participantes=participantes,
                                            observacoes=observacoes, deliberacoes=deliberacoes,cor=cor,status=status)
            reuniao_service.alterar_reuniao(reuniao_bd, nova_reuniao)
            return redirect('calendario')
    return render(request, 'reunioes/form_reuniao.html',
                  {"titulo": titulo, "notificacao": notificacao, "form_reuniao": form_reuniao,
                   "form_data": form_data})


@login_required()
def alterar_reuniao(request, id):
    usuario = reuniao_service.usuario_logado(request)
    reuniao_bd = reuniao_service.retornar_reuniao_id(id)
    data_bd = data_services.retornar_data_id(id)
    notificacao = alerta_services.contar(request.user)
    form_reuniao = FormReuniao(request.POST or None, instance=reuniao_bd)
    form_data = FormData(request.POST or None, instance=data_bd)
    titulo = "Alterar"

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
            participantes = form_reuniao.cleaned_data["participantes"]
            deliberacoes = form_reuniao.cleaned_data["deliberacoes"]
            observacoes = form_reuniao.cleaned_data["observacoes"]
            status = "3"
            cor = "3"
            data_services.alterar_data(data_bd, nova_data)
            nova_reuniao = reunioes.Reuniao(tipo_reuniao=tipo, data=data_bd, pauta=pauta, local=local,
                                            semestre=semestre, participantes=participantes,
                                            observacoes=observacoes, deliberacoes=deliberacoes, cor=cor, status=status)
            reuniao_service.alterar_exceto(reuniao_bd, nova_reuniao)
            return redirect('calendario')
    return render(request, 'reunioes/form_reuniao.html',
                  {"titulo": titulo, "notificacao": notificacao, "form_reuniao": form_reuniao,
                   "form_data": form_data,"usuario":usuario})


@login_required()
def agendar_tipo(request):
    titulo = "Novo Tipo"
    notificacao = alerta_services.contar(request.user)
    mensagem = ""

    if request.method == "POST":
        form_tipo = FormTipo(request.POST)
        if form_tipo.is_valid():
            titulo = form_tipo.cleaned_data["titulo"]
            novo_tipo = reunioes.Tipo(titulo=titulo)
            reuniao_service.salvar_tipo(novo_tipo)
            return redirect('agendar_reuniao')
        else:
            mensagem = form_tipo.errors


    else:
        form_tipo = FormTipo()
    return render(request, 'reunioes/criar_tipo.html',
                  {"titulo": titulo, "notificacao": notificacao,"mensagem":mensagem, "form_tipo": form_tipo})


@login_required()
def calendario(request):
    usuario=reuniao_service.usuario_logado(request)


    notificacao = alerta_services.contar(request.user)
    reunioes = reuniao_service.retornar_tudo()
    return render(request, 'reunioes/main.html', {"reunioes": reunioes, "notificacao": notificacao, "usuario":usuario})



@login_required()
def resultado_busca(request):
    usuario = reuniao_service.usuario_logado(request)
    notificacao = alerta_services.contar(request.user)
    if request.method == "POST":
        semestre = request.POST['busca']
        resultados = reuniao_service.retornar_por_semestre(semestre)
    return render(request, 'reunioes/info_reuniao.html', { "notificacao": notificacao,"resultados":resultados,
                                                           "semestre":semestre, "usuario":usuario})

@login_required()
def ver_info(request,id):
    usuario = reuniao_service.usuario_logado(request)
    notificacao = alerta_services.contar(request.user)
    reuniao = reuniao_service.retornar_reuniao_id(id)
    return render(request, 'reunioes/info_reuniao.html', { "notificacao": notificacao,"reuniao":reuniao, "usuario":usuario})


@login_required()
def remover(request, id):

    usuario = reuniao_service.usuario_logado(request)
    reuniao_bd = reuniao_service.retornar_reuniao_id(id)
    mensagen_erro = ""
    if reuniao_bd.status == '3':
        mensagen_erro = "Não é Possivel Excluir Reunião Já Consolidada"

    if (request.method == "POST"):
        reuniao_service.apagar_reuniao(reuniao_bd)
        return redirect('calendario')
    acao="Excluir"
    return render(request, 'reunioes/excluir.html', {'reuniao_bd': reuniao_bd,"acao":acao,"mensagen_erro" :mensagen_erro})

def cancelar(request, id):
    usuario = reuniao_service.usuario_logado(request)
    reuniao_bd = reuniao_service.retornar_reuniao_id(id)
    mensagen_erro=""
    if reuniao_bd.status=='3':
        mensagen_erro="Não é Possivel Cancelar Reunião Já Consolidada"

    if (request.method == "POST"):
        reuniao_service.cancelar_reuniao(reuniao_bd)
        return redirect('calendario')
    acao = "Cancelar"
    return render(request, 'reunioes/excluir.html', {'reuniao_bd': reuniao_bd,"acao":acao, "usuario":usuario,"mensagen_erro":mensagen_erro})

@login_required()
def ata(request, id):
    reuniao = reuniao_service.retornar_reuniao_id(id)
    usuario = request.user
    template = 'documentos/modelo_ata.htm'
    participantes=reuniao.participantes.all()

    context = {'reuniao': reuniao,'usuario':usuario,'participantes':participantes}
    return render_to_pdf_response(request,template,context)



