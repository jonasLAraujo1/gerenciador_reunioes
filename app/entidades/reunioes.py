from datetime import date
class Reuniao():
    """docstring for Reuniao"""

    def __init__(self,tipo_reuniao,data, pauta, semestre, local,participantes, observacoes, deliberacoes, cor, status):
        self.tipo_reuniao=tipo_reuniao
        self.data=data
        self.pauta = pauta
        self.semestre = semestre
        self.local = local
        self.participantes = participantes
        self.observacoes = observacoes
        self.deliberacoes = deliberacoes
        self.cor = cor
        self.status = status


class Tipo():
    """docstring for Tipo"""

    def __init__(self, titulo):
        self.titulo = titulo


class Data():
    """docstring for Tipo"""
    def __init__(self, dia, inicio, fim):
        self.dia = dia
        self.inicio = inicio
        self.fim = fim

