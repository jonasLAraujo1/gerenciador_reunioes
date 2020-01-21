from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    nome = models.CharField(max_length=120, null=False, blank=False)
    #registro = models.CharField(max_length=11)
    registro = models.CharField(max_length=11, null=True, blank=True)
    funcao = models.CharField(max_length=35, null=True, blank=True)
    cargo = models.CharField(max_length=50, null=True, blank=True)
    lotacao = models.CharField(max_length=35, null=True, blank=True)

# Create your models here.
from django.utils import timezone


class Tipo(models.Model):

    titulo = models.CharField(max_length=120, null=False, blank=False)

    def __str__(self):
        return self.titulo


class Data(models.Model):
    dia = models.DateField(null=False, blank=False)
    inicio = models.TimeField(null=False, blank=False)
    fim = models.TimeField(null=False, blank=False)


# class Profile(models.Model):
#     user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
#     registro = models.CharField(max_length=11)
#     funcao = models.CharField(max_length=35, null=True, blank=True)
#     cargo = models.CharField(max_length=50, null=True, blank=True)
#     lotacao = models.CharField(max_length=35, null=True, blank=True)


class Reuniao(models.Model):
    COR_CHOICES = (
        ("1", "#5C63DE"),
        ("2", "#CEC02D"),
        ("3", "#81CE2D"),
        ("4", "#2DCEB7"),
    )
    STATUS_CHOICES = (
        ("1", "Agendada"),
        ("2", "Confirmada"),
        ("3", "Consolidada"),
        ("4", "Cancelada"),
    )
    tipo_reuniao = models.ForeignKey('Tipo', on_delete=models.CASCADE)
    data_reuniao = models.ForeignKey('Data', on_delete=models.CASCADE)
    pauta = models.CharField(max_length=120, null=False, blank=False)
    local = models.CharField(max_length=120, null=False, blank=False)
    semestre = models.CharField(max_length=6, null=False, blank=False)
   # participantes = models.TextField(null=False, blank=False)
    observacoes = models.TextField(null=True, blank=True)
    deliberacoes = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="1", null=False, blank=False)
    cor = models.CharField(max_length=1, choices=COR_CHOICES,default="1", null=False, blank=False)

class Alerta(models.Model):
    STATUS_CHOICES = (
        ("1", "Novo"),
        ("2", "Visualizado"),
    )
    titulo = models.CharField(max_length=120, null=False, blank=False)
    observacoes = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="1", null=False, blank=False)
