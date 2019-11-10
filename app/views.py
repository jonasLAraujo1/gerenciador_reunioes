from django.middleware import http
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.defaults import bad_request
import simplejson as json
from .forms import *
from .entidades import reunioes
from .services import reuniao_service


# Create your views here.


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
                tipo=form_reuniao.cleaned_data["tipo_reuniao"]
                pauta = form_reuniao.cleaned_data["pauta"]
                local = form_reuniao.cleaned_data["local"]
                semestre = form_reuniao.cleaned_data["semestre"]
                deliberacoes = ""
                observacoes = ""
                status = "1"
                data_bd=reuniao_service.salvar_data(nova_data)
                nova_reuniao = reunioes.Reuniao(tipo_reuniao=tipo,data=data_bd,pauta=pauta,local=local,
                                                semestre=semestre, observacoes=observacoes,deliberacoes=deliberacoes, status=status)
                reuniao_service.agendar_reuniao(nova_reuniao)
                return redirect('calendario')
    else:
        form_reuniao = FormAgendaReuniao()
        form_data = FormData()
    
    return render(request, 'reunioes/form_pre_reuniao.html',
                  {"titulo": titulo, "notificacao": notificacao, "form_reuniao": form_reuniao,
                   "form_data": form_data})


def marcar_reuniao(request,id):
    titulo = "Marcar"
    notificacao = 0
    reuniao_bd = reuniao_service.listar_por_id(id)
    form_reuniao =  FormReuniao(request.POST or None, instance=reuniao_bd)
    form_data = FormData(request.POST or None, instance=reuniao_bd)

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
            status = "1"
            data_bd = reuniao_service.salvar_data(nova_data)
            nova_reuniao = reunioes.Reuniao(tipo_reuniao=tipo, data=data_bd, pauta=pauta, local=local,
                                            semestre=semestre, observacoes=observacoes, deliberacoes=deliberacoes,
                                            status=status)
            reuniao_service.agendar_reuniao(nova_reuniao)
            return redirect('calendario')

    return render(request, 'reunioes/form_reuniao.html',
                  {"titulo": titulo, "notificacao": notificacao, "form_reuniao": form_reuniao,
                   "form_data": form_data})


def agendar_data(request):
    titulo = "Data"
    notificacao = 0
    if request.method == "POST":
            return redirect('calendario')
    else:

        form_data = FormData()

    return render(request, 'reunioes/form_data_reuniao.html',
                  {"titulo": titulo, "notificacao": notificacao, "form_data": form_data})


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
        form_tipo = FormTipo(request.POST)
    return render(request, 'reunioes/criar_tipo.html',
                  {"titulo": titulo, "notificacao": notificacao, "form_tipo": form_tipo})




def calendario(request):
    notificacao =""
    reunioes = reuniao_service.retornar_tudo()
    #print(reunioes)
    return render(request, 'reunioes/main.html', {"reunioes": reunioes, "notificacao": notificacao})


def eventos_lista():
    reunioes = reuniao_service.listar_reunioes()
    event_list = []
    for i in reunioes:
        data_i = i.data_reuniao.dia.strftime('%d-%m- %Y')
        hora_i = i.data_reuniao.inicio.strftime('%H:%M:%S')
        hora_f = i.data_reuniao.inicio.strftime('%H:%M:%S')
        inicio=data_i+' '+hora_i
        fim = data_i + ' ' + hora_f
        event_list.append({
            'id': i.id,
            'start': inicio,
            'end': fim,
            'title': i.tipo_reuniao.titulo,
        })
    return json.dumps(event_list)


def confirmar_reuniao(request):
    form_reuniao = FormAgendaReuniao()
    return render(request, 'reunioes/form_pre_reuniao.html')


def cancelar_reuniao(request):
    form_reuniao = FormAgendaReuniao()
    return render(request, 'reunioes/form_pre_reuniao.html')


def consolidar_reuniao(request):
    form_reuniao = FormAgendaReuniao()
    return render(request, 'reunioes/form_pre_reuniao.html')


def cadastarar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        form_perfil = FormProfile(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('calendario')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'reunioes/form_cadastro_usuario.html',
                  {"form_usuario": form_usuario, "form_perfil": form_perfil})

def novo_tipo(request):
    form = FormTipo(request.POST)
    if form.is_valid():
        form.save(commit=True)
        return redirect('#')
    else:
        return bad_request(request, None, 'ops_400.html')

# 	all_events = Events.objects.all() 
# 	get_event_types = Events.objects.only('tipo_reuniao') 
# 	# if filters applied then get parameter and filter based on condition else return object 
# 	if request.GET: event_arr = [] 
# 	if request.GET.get('event_type') == "all": 
# 		all_events = Events.objects.all() 
# 	else: 
# 		all_events = Events.objects.filter(event_type__icontains=request.GET.get('event_type')) 
# 		for i in all_events: 
# 			event_sub_arr = {} event_sub_arr['title'] = i.event_name 
# 			start_date = datetime.datetime.strptime(str(i.start_date.date()), "%Y-%m-%d").strftime("%Y-%m-%d") 
# 			end_date = datetime.datetime.strptime(str(i.end_date.date()), "%Y-%m-%d").strftime("%Y-%m-%d") 
# 			event_sub_arr['start'] = start_date 
# 			event_sub_arr['end'] = end_date 
# 			event_arr.append(event_sub_arr) 
# 			return HttpResponse(json.dumps(event_arr)) 
# 			context = { "events":all_events, "get_event_types":get_event_types, } 
# 			return render(request,'admin/poll/event_management.html',context)
