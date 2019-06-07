from django.urls import path

from apps.usuario.views import AgregarUsuario, ConsultarUsuarios, ModificarUsuario, GetUsuariosAjax

urlpatterns = [
    path('agregar/', AgregarUsuario.as_view(), name='agregar_usuario'),
    path('consultar/', ConsultarUsuarios.as_view(), name='consultar_usuario'),
    path('modificar/<id_usuario>/', ModificarUsuario.as_view(), name='modificar_usuario'),
    path('get_usuarios_ajax/', GetUsuariosAjax.as_view(), name='get_usuario_ajax'),
]
