from ..models import Reuniao, Data, Tipo
import simplejson as json
def agendar_reuniao(reuniao):
    Reuniao.objects.create(tipo_reuniao=reuniao.tipo_reuniao,data_reuniao=reuniao.data,pauta=reuniao.pauta,
                           local=reuniao.local,semestre=reuniao.semestre,observacoes=reuniao.observacoes,deliberacoes=reuniao.deliberacoes,status=reuniao.status)

def salvar_data(data):
    data_sv=Data.objects.create(dia=data.dia,inicio=data.inicio,fim=data.fim)
    return data_sv


def salvar_tipo(tipo):
    Tipo.objects.create(titulo=tipo.titulo, cor=tipo.cor)

def listar_reunioes():
	reunioes = Reuniao.objects.select_related('data_reuniao').all()
	return reunioes

def listar_datas():
    datas = Data.objects.all()
    return datas


def  retornar_tudo():
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
        })
    return lista_reunioes


def  retornar_por_id(id):
    reunioes = Reuniao.objects.get(id=id)
    return reunioes