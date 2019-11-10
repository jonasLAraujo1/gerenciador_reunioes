from django.views.generic import UpdateView
from django.http import HttpResponse
from django.template.loader import render_to_string
from ..models import Tipo
from ..forms import FormTipo

"""
Edit item
"""
class ItemUpdateView(UpdateView):
    model = Tipo
    form_class = FormTipo
    template_name = 'reunioes/criar_tipo.html'

    def form_valid(self, form):
        form.save()
