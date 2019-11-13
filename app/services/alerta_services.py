from ..models import Alerta

def criar_alerta(alerta):
    Alerta.objects.create(titulo=alerta.titulo,observacoes=alerta.observacoes,status=alerta.status)

def listar_todos():
    alertas=Alerta.objects.all()
    return alertas

def atualizar_alerta(alerta_bd,alerta_novo):
   alerta_bd.titulo = alerta_novo.titulo
   alerta_bd.observacoes = alerta_novo.observacoes
   alerta_bd.status = '2'
