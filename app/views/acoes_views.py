from django.contrib.auth.decorators import login_required
from django.core.handlers import exception
from django.shortcuts import redirect,render

@login_required()
def acao_marcar(request):
    if request.method == "POST":
        id = request.POST['id']
        print(id)
        #
        return redirect("marcar_reuniao",id)
    else:
        return redirect("calendario")


@login_required()
def acao_aletrar(request):
    if request.method == "POST":
        id = request.POST['id']
        return redirect("marcar_reuniao",id)
    else:
        return redirect("calendario")

@login_required()
def acao_consolidar(request):
    if request.method == "POST":
        id = request.POST['id']
        return redirect("consolidar_reuniao",id)
    else:
        return redirect("calendario")
@login_required()
def acao_cancelar(request):
    if request.method == "POST":
        id = request.POST['id']
        return redirect("cancelar",id)
    else:
        return redirect("calendario")
@login_required()
def acao_remover(request):
    if request.method == "POST":
        id = request.POST['id']
        return redirect("remover",id)
    else:
        return redirect("calendario")
@login_required()
def acao_ata(request):
    if request.method == "POST":
        id = request.POST['id']
        return redirect("ata",id)
    else:
        return redirect("calendario")

@login_required()
def acao_busca(request):
    if request.method == "POST":
        semestre = request.POST['busca']
        return redirect("resultado_busca",semestre)
    else:
        return redirect("calendario")


@login_required()
def acao_info(request):
    if request.method == "POST":
        id = request.POST['id']
        return redirect("ver_info", id)
    else:
        return redirect("listar")
