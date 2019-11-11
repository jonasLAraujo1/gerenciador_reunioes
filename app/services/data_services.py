from ..models import Data


def salvar_data(data):
    data_sv=Data.objects.create(dia=data.dia,inicio=data.inicio,fim=data.fim)
    return data_sv

def alterar_data(data_bd,data_nova):
    data_bd.dia=data_nova.dia
    data_bd.inicio = data_nova.inicio
    data_bd.fim = data_nova.fim
    data_bd.save(force_update=True)

def retornar_data_id(id):
    data = Data.objects.get(id=id)
    return data
