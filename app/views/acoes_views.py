from django.shortcuts import redirect

def acao_marcar(request):
    if request.method == "POST":
        id = request.POST['id']
        return redirect("marcar_reuniao",id)
    else:
        return redirect("calendario")


def acao_aletrar(request):
    if request.method == "POST":
        id = request.POST['id']
        return redirect("marcar_reuniao",id)
    else:
        return redirect("calendario")


def acao_consolidar(request):
    if request.method == "POST":
        id = request.POST['id']
        return redirect("marcar_reuniao",id)
    else:
        return redirect("calendario")

def acao_cancelar(request):
    if request.method == "POST":
        id = request.POST['id']
        return redirect("marcar_reuniao",id)
    else:
        return redirect("calendario")
