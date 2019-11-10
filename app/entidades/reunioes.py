class Reuniao():
    """docstring for Reuniao"""

    def __init__(self,tipo_reuniao,data, pauta, semestre, local, observacoes, deliberacoes, status):
        self.tipo_reuniao=tipo_reuniao
        self.data=data
        self.pauta = pauta
        self.semestre = semestre
        self.local = local
        self.observacoes = observacoes
        self.deliberacoes = deliberacoes
        self.status = status


class Tipo():
    """docstring for Tipo"""

    def __init__(self, titulo, cor):
        self.titulo = titulo
        self.cor = cor


class Data():
    """docstring for Tipo"""

    def __init__(self, dia, inicio, fim):
        self.dia = dia
        self.inicio = inicio
        self.fim = fim
