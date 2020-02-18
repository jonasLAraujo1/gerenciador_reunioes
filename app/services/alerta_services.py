from ..models import Alerta

def criar_alerta(alerta):
    Alerta.objects.create(titulo=alerta.titulo,observacoes=alerta.observacoes,usario=alerta.usuario,status=alerta.status)

def contar(usuario):
    alertas=Alerta.objects.filter(usuario=usuario,status="1").all()
    contagem=0
    for i in alertas:
        contagem+=1

    return contagem

def listar_todos(usuario):
    alertas = Alerta.objects.filter(usuario=usuario).all()
    return alertas


def apagar_alerta(id):
    alerta_bd=Alerta.objects.get(id=id)
    alerta_bd.delete()

def atualizar_alerta(alerta_bd,alerta_novo):
   alerta_bd.titulo = alerta_novo.titulo
   alerta_bd.observacoes = alerta_novo.observacoes
   alerta_bd.status = '2'


def visualizar_alerta(id):
    alerta_bd = Alerta.objects.get(id=id)
    alerta_bd.status = '2'
    alerta_bd.save(force_update=True)