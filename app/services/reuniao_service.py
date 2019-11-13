from ..models import Reuniao, Tipo
import simplejson as json
def agendar_reuniao(reuniao):
    Reuniao.objects.create(tipo_reuniao=reuniao.tipo_reuniao,data_reuniao=reuniao.data,pauta=reuniao.pauta,
                           local=reuniao.local,semestre=reuniao.semestre,observacoes=reuniao.observacoes,deliberacoes=reuniao.deliberacoes,status=reuniao.status)

def alterar_reuniao(reuniao_db,reuniao_nova):
    reuniao_db.tipo_reuniao=reuniao_nova.tipo_reuniao
    reuniao_db.data=reuniao_nova.data
    reuniao_db.pauta=reuniao_nova.pauta
    reuniao_db.local = reuniao_nova.local
    reuniao_db.semestre = reuniao_nova.semestre
    reuniao_db.observacoes = reuniao_nova.observacoes
    reuniao_db.deliberacoes = reuniao_nova.deliberacoes
    reuniao_db.status = reuniao_nova.status
    reuniao_db.save(force_update=True)

def apagar_reuniao(reuniao_bd):
    reuniao_bd.delete()


def salvar_tipo(tipo):
    Tipo.objects.create(titulo=tipo.titulo, cor=tipo.cor)


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
            'color': i.tipo_reuniao.get_cor_display,
            'status': i.status,
        })
    return lista_reunioes

def  retornar_reuniao_id(id):
    reunioes = Reuniao.objects.get(id=id)
    return reunioes
