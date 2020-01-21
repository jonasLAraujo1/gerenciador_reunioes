from django.conf.urls import url
from django.urls import path

from django.conf import settings
from django.template.response import TemplateResponse

from .views.acoes_views import *
from .views.reunioes_views import *
from .views.usuario_views import *


if settings.DEBUG:
    urlpatterns = [
    path('agendar/',agendar_reuniao,name="agendar_reuniao"),
    path('tipo/',agendar_tipo,name="agendar_tipo"),
    path('inicio/',calendario,name="calendario"),
    path('excluir/<int:id>', remover, name="remover"),
    path('marcar/<int:id>',marcar_reuniao,name="marcar_reuniao"),
    path('marcar/',acao_marcar,name="acao_marcar"),
    path('gerar/',acao_ata,name="acao_ata"),
    path('excluir/',acao_cancelar,name="acao_cancelar"),
    path('cadastro/', decidir_usuario, name="decidir_usuario"),
    path('cadastro/aluno', cadastarar_aluno, name="cadastarar_aluno"),
    path('cadastro/servidor', cadastarar_servidor, name="cadastarar_servidor"),
    path('login/', logar_usuario, name="logar_usuario"),
    path('logout/', deslogar_usuario, name="deslogar_usuario"),
    path('ata/<int:id>', ata, name="ata"),
    url(r'^', TemplateResponse, {'template': '404.html'}),
    ]

# handler404 = 'app.views.acoes_views.erro_404'
# handler500 = 'app.views.acoes_views.erro_500'
