from django.http import Http404, JsonResponse, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.views.generic.list import ListView

from apps.usuario.forms import AgregarUsuarioForm, ModificarUsuarioForm
from django.views.generic.edit import CreateView, UpdateView, FormMixin

from apps.usuario.models import Usuario

class AgregarUsuario(CreateView):
    model = Usuario
    form_class = AgregarUsuarioForm
    success_url = reverse_lazy('consultar_usuario')
    template_name = 'usuario/agregar_usuario.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save();
            return HttpResponse('Usuario guardado con éxito')
        print(form.errors)
        return HttpResponse('Error al guardar el usuario')


class ConsultarUsuarios(ListView):
    model = Usuario
    template_name = 'usuario/consultar_usuario.html'


class ModificarUsuario(UpdateView):
    model = Usuario
    form_class = ModificarUsuarioForm
    success_url = reverse_lazy('consultar_usuario')
    template_name = 'usuario/modificar_usuario.html'
    template_name_suffix = '_update_form'
    id_usuario = None

    def get_context_data(self, **kwargs):
        """ get_context_data let you fill the template context """
        context = super(ModificarUsuario, self).get_context_data(**kwargs)
        # Get Related publishers
        context['id_usuario'] = self.id_usuario
        return context

    def get_object(self, queryset=None):
        self.id_usuario = self.kwargs['id_usuario']
        return Usuario.objects.get(id=self.id_usuario)
