from django import forms
from django.contrib.auth.forms import UserCreationForm
from django_select2.forms import Select2Widget

from apps.usuario.models import Usuario


class AgregarUsuarioForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(AgregarUsuarioForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = "form-control col-md-6"
        self.fields['first_name'].widget.attrs['class'] = "form-control col-md-6"
        self.fields['last_name'].widget.attrs['class'] = "form-control col-md-6"
        self.fields['email'].widget.attrs['class'] = "form-control col-md-6"
        self.fields['telefono'].widget.attrs['class'] = "form-control col-md-6"
        self.fields['celular'].widget.attrs['class'] = "form-control col-md-6"
        self.fields['direccion'].widget.attrs['class'] = "form-control col-md-6"
        self.fields['cargo'].widget.attrs['class'] = "form-control col-md-6"
        self.fields['fecha_nacimiento'].widget.attrs['class'] = "form-control col-md-6"
        self.fields['password1'].widget.attrs['class'] = "form-control col-md-6"
        self.fields['password2'].widget.attrs['class'] = "form-control col-md-6"

    class Meta:
        model = Usuario
        fields = ('username', 'first_name', 'last_name', 'email', 'telefono', 'celular', 'direccion', 'cargo',
                  'fecha_nacimiento', 'password1', 'password2')

        widgets = {
            "cargo": Select2Widget(),
        }
        labels = {
            'first_name': 'Nombre(s)',
            'direccion': 'Dirección',
            'telefono': 'Teléfono',
            'email': 'Correo electrónico',
        }
