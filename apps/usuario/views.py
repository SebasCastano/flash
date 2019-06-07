from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from apps.usuario.forms import AgregarUsuarioForm, ModificarUsuarioForm
from django.views.generic.edit import CreateView, UpdateView
from apps.usuario.models import Usuario


class AgregarUsuario(CreateView):
    model = Usuario
    form_class = AgregarUsuarioForm
    success_url = reverse_lazy('consultar_usuario')
    template_name = 'usuario/agregar_usuario.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'valid': True, 'mensaje': "Usuario registrado"})
        return JsonResponse({'valid': False, 'mensaje': "Error al registrar el usuario"})


class ConsultarUsuarios(TemplateView):
    template_name = 'usuario/consultar_usuario.html'


class GetUsuariosAjax(ListView):
    model = Usuario

    def get(self, request, *args, **kwargs):
        usuarios = []
        usuarios_qs = self.model.objects.all()
        for usuario in usuarios_qs:
            estado = "Inactivo"
            if (usuario.is_active):
                estado = "Activo"
            temp = {'id': usuario.id, 'identificacion': usuario.username, 'nombre': usuario.first_name,
                    'apellido': usuario.last_name, 'cargo': usuario.cargo, 'email': usuario.email, 'estado': estado}
            usuarios.append(temp)
        return JsonResponse(usuarios, safe=False)


class ModificarUsuario(UpdateView):
    model = Usuario
    form_class = ModificarUsuarioForm
    success_url = reverse_lazy('consultar_usuario')
    template_name = 'usuario/modificar_usuario.html'
    template_name_suffix = '_update_form'
    id_usuario = None

    def get_context_data(self, **kwargs):
        context = super(ModificarUsuario, self).get_context_data(**kwargs)
        context['id_usuario'] = self.id_usuario
        return context

    def get_object(self, queryset=None):
        self.id_usuario = self.kwargs['id_usuario']
        return Usuario.objects.get(id=self.id_usuario)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=Usuario.objects.get(pk=self.kwargs['id_usuario']))
        if form.is_valid():
            form.save()
            return JsonResponse({'valid': True, 'mensaje': "Usuario modificado"})
        print(form.errors)
        return JsonResponse({'valid': False, 'mensaje': "Error al modificar el usuario"})
