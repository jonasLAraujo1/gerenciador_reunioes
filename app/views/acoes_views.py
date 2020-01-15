from django.contrib.auth.decorators import login_required
from django.core.handlers import exception
from django.shortcuts import redirect,render

@login_required()
def acao_marcar(request):
    if request.method == "POST":
        id = request.POST['id']
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
        return redirect("marcar_reuniao",id)
    else:
        return redirect("calendario")
@login_required()
def acao_cancelar(request):
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
