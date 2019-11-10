
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('sistema/agendar/',agendar_reuniao,name="agendar_reuniao"),
path('tipo/',agendar_tipo,name="agendar_tipo"),
    path('sistema/inicio/',calendario,name="calendario"),
    path('cad/',cadastarar_usuario,name="cadastarar_usuario"),
    path('sistema/agendar2/',agendar_data,name="agendar_data"),


]
