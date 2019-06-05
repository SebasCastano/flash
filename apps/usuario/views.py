from django.shortcuts import render

from apps.usuario.forms import AgregarUsuarioForm
from django.views.generic.edit import CreateView

from apps.usuario.models import Usuario


class AgregarUsuario(CreateView):
    model = Usuario
    form_class = AgregarUsuarioForm
    template_name = 'usuario/agregar_usuario.html'

