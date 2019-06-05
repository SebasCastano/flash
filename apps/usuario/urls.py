from django.urls import path

from apps.usuario.views import AgregarUsuario

urlpatterns = [
    path('agregar/', AgregarUsuario.as_view(), name='agregar_usuario'),
]
