
from django.contrib import admin
from django.urls import path


from .views.acoes_views import *
from .views.reunioes_views import *
urlpatterns = [
    path('sistema/agendar/',agendar_reuniao,name="agendar_reuniao"),
    path('tipo/',agendar_tipo,name="agendar_tipo"),
    path('sistema/inicio/',calendario,name="calendario"),
    path('cad/',cadastarar_usuario,name="cadastarar_usuario"),
    path('sistema/marcar/<int:id>',marcar_reuniao,name="marcar_reuniao"),
    path('marcar/',acao_marcar,name="acao_marcar"),


]
