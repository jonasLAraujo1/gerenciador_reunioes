from ..models import User,Reuniao, Tipo,Alerta
from .alerta_services import *

def agendar_reuniao(reuniao):
    reuniao_bd=Reuniao.objects.create(tipo_reuniao=reuniao.tipo_reuniao,data_reuniao=reuniao.data,pauta=reuniao.pauta,
                           local=reuniao.local,semestre=reuniao.semestre,observacoes=reuniao.observacoes,deliberacoes=reuniao.deliberacoes,status=reuniao.status)
    reuniao_bd.save()
    titulo="Reunião de "+str(reuniao.tipo_reuniao)
    informacoes = "Uma nova Reunião com a Pauta: " + str(reuniao.pauta) + \
                  " Foi Agendada Para o Dia: " + str(reuniao.data.dia.strftime('%d/%m/%Y'))+\
                  " Com inicio às: "+str(reuniao.data.inicio.strftime('%H:%M'))
    # print(titulo,informacoes)
    for i in reuniao.participantes:
        usuario= User.objects.get(id=i.id)
        Alerta.objects.create(titulo=titulo,informacoes=informacoes,usuario=usuario,status="1")
        reuniao_bd.participantes.add(usuario)


def alterar_reuniao(reuniao_bd,reuniao_nova):
    reuniao_bd.tipo_reuniao=reuniao_nova.tipo_reuniao
    reuniao_bd.data=reuniao_nova.data
    reuniao_bd.pauta=reuniao_nova.pauta
    reuniao_bd.local = reuniao_nova.local
    reuniao_bd.semestre = reuniao_nova.semestre
    reuniao_bd.observacoes = reuniao_nova.observacoes
    reuniao_bd.deliberacoes = reuniao_nova.deliberacoes
    reuniao_bd.cor = reuniao_nova.cor
    reuniao_bd.participantes.set(reuniao_nova.participantes)
    reuniao_bd.status = reuniao_nova.status
    reuniao_bd.save(force_update=True)


def alterar_exceto(reuniao_bd,reuniao_nova):
    reuniao_bd.tipo_reuniao = reuniao_nova.tipo_reuniao
    reuniao_bd.data = reuniao_nova.data
    reuniao_bd.pauta = reuniao_nova.pauta
    reuniao_bd.local = reuniao_nova.local
    reuniao_bd.semestre = reuniao_nova.semestre
    reuniao_bd.observacoes = reuniao_nova.observacoes
    reuniao_bd.deliberacoes = reuniao_nova.deliberacoes
    reuniao_bd.participantes.set(reuniao_nova.participantes)
    reuniao_bd.status = reuniao_nova.status

    reuniao_bd.save(force_update=True)


def cancelar_reuniao(reuniao_bd):
    reuniao_bd.cor = "4"
    reuniao_bd.status = "4"
    reuniao_bd.save(force_update=True)

def apagar_reuniao(reuniao_bd):
    reuniao_bd.delete()



def retornar_por_semestre(semestre):
    resultado = Reuniao.objects.all().filter(semestre=semestre)
    return resultado


def retornar_tudo():
    reunioes = Reuniao.objects.select_related('data_reuniao').all()
    lista_reunioes = []
    for i in reunioes:
        data_i = i.data_reuniao.dia.strftime('%Y-%m-%d')
        hora_i = i.data_reuniao.inicio.strftime('%H:%M:%S')
        hora_f = i.data_reuniao.fim.strftime('%H:%M:%S')
        inicio = data_i + ' ' + hora_i
        fim = data_i + ' ' + hora_f
        lista_reunioes.append({
            'id': i.id,
            'start': inicio,
            'end': fim,
            'title': i.tipo_reuniao.titulo,
            'color': i.get_cor_display,
            'status': i.get_status_display,
        })
    return lista_reunioes


def retornar_status(status):
    reunioes = Reuniao.objects.all().filter(status=status)
    #Reuniao.objects.select_related('data_reuniao').all()
    lista_reunioes = []
    for i in reunioes:
        data_i = i.data_reuniao.dia.strftime('%Y-%m-%d')
        hora_i = i.data_reuniao.inicio.strftime('%H:%M:%S')
        hora_f = i.data_reuniao.fim.strftime('%H:%M:%S')
        inicio = data_i + ' ' + hora_i
        fim = data_i + ' ' + hora_f
        lista_reunioes.append({
            'id': i.id,
            'start': inicio,
            'end': fim,
            'title': i.tipo_reuniao.titulo,
            'color': i.get_cor_display,
            'status': i.get_status_display,
        })
    return lista_reunioes


def  retornar_reuniao_id(id):
    reunioes = Reuniao.objects.get(id=id)
    return reunioes


def usuario_logado(request):
    usuario = request.user
    listName = str(usuario).split()
    usuario = str(listName[0]) + " " + str(listName[1])
    return usuario