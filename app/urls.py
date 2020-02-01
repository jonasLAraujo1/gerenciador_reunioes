from django.conf.urls import url
from django.urls import path

from django.conf import settings
from django.template.response import TemplateResponse

from .views.acoes_views import *
from .views.reunioes_views import *
from .views.usuario_views import *


if settings.DEBUG:
    urls_reuniao = [
        path('agendar/', agendar_reuniao, name="agendar_reuniao"),
        path('tipo/', agendar_tipo, name="agendar_tipo"),
        path('inicio/', calendario, name="calendario"),
        path('cancelar/<int:id>', cancelar, name="cancelar"),
        path('excluir/<int:id>', remover, name="remover"),
        path('marcar/<int:id>', marcar_reuniao, name="marcar_reuniao"),
        path('consolidar/<int:id>', consolidar_reuniao, name="consolidar_reuniao"),
        path('marcar/', acao_marcar, name="acao_marcar"),
        path('consolidar/', acao_consolidar, name="acao_consolidar"),
        #path('busca/', acao_busca, name="acao_busca"),
        path('busca/', resultado_busca, name="resultado_busca"),
        path('gerar/', acao_ata, name="acao_ata"),
        path('excluir/', acao_remover, name="acao_remover"),
        path('cancelar/', acao_cancelar, name="acao_cancelar"),
        path('ata/<int:id>', ata, name="ata"),
    ]
    urls_usuario = [
        path('cadastro/', decidir_usuario, name="decidir_usuario"),
        path('cadastro/aluno', cadastarar_aluno, name="cadastarar_aluno"),
        path('cadastro/servidor', cadastarar_servidor, name="cadastarar_servidor"),
        path('login/', logar_usuario, name="logar_usuario"),
        path('logout/', deslogar_usuario, name="deslogar_usuario"),
        url(r'^', TemplateResponse, {'template': '404.html'}),
    ]
    urlpatterns = urls_reuniao+urls_usuario

