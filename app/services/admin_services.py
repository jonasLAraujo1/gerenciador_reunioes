from ..models import Tipo


def salvar_tipo(tipo):
    Tipo.objects.create(titulo=tipo.titulo)
