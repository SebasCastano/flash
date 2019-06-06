from datetime import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import SelectDateWidget
from django_select2.forms import Select2Widget

from apps.usuario.models import Usuario


class AgregarUsuarioForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(AgregarUsuarioForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = "form-control"
        self.fields['username'].help_text = ""
        self.fields['first_name'].widget.attrs['class'] = "form-control"
        self.fields['last_name'].widget.attrs['class'] = "form-control"
        self.fields['email'].widget.attrs['class'] = "form-control"
        self.fields['telefono'].widget.attrs['class'] = "form-control"
        self.fields['celular'].widget.attrs['class'] = "form-control"
        self.fields['direccion'].widget.attrs['class'] = "form-control"
        self.fields['cargo'].widget.attrs['class'] = "form-control"
        self.fields['fecha_nacimiento'].widget.attrs['class'] = "form-control"
        #self.fields['fecha_nacimiento'].widget.attrs['data-provide'] = "datepicker-inline"
        self.fields['password1'].widget.attrs['class'] = "form-control"
        self.fields['password2'].widget.attrs['class'] = "form-control"

    class Meta:
        model = Usuario
        fields = ('username', 'first_name', 'last_name', 'email', 'telefono', 'celular', 'direccion', 'cargo',
                  'fecha_nacimiento', 'password1', 'password2')

        widgets = {
            "cargo": Select2Widget(),
            "fecha_nacimiento": SelectDateWidget(years=range(1940, datetime.now().year + 1))
        }
        labels = {
            'username': 'Identificacion',
            'first_name': 'Nombre(s)',
            'direccion': 'Dirección',
            'telefono': 'Teléfono',
            'email': 'Correo electrónico',
        }

class ModificarUsuarioForm(forms.ModelForm):
    password1 = forms.CharField(required=False, widget=forms.PasswordInput(), label='Contraseña')
    password2 = forms.CharField(required=False, widget=forms.PasswordInput(), label='Contraseña(confirmación)')

    def __init__(self, *args, **kwargs):
        super(ModificarUsuarioForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = "form-control"
        self.fields['username'].help_text = ""
        self.fields['first_name'].widget.attrs['class'] = "form-control"
        self.fields['last_name'].widget.attrs['class'] = "form-control"
        self.fields['email'].widget.attrs['class'] = "form-control"
        self.fields['telefono'].widget.attrs['class'] = "form-control"
        self.fields['celular'].widget.attrs['class'] = "form-control"
        self.fields['direccion'].widget.attrs['class'] = "form-control"
        self.fields['cargo'].widget.attrs['class'] = "form-control"
        self.fields['fecha_nacimiento'].widget.attrs['class'] = "form-control"
        #self.fields['fecha_nacimiento'].widget.attrs['data-provide'] = "datepicker-inline"
        self.fields['password1'].widget.attrs['class'] = "form-control"
        self.fields['password2'].widget.attrs['class'] = "form-control"

    def clean(self):
        form_data = super().clean()
        pass1 = self.cleaned_data['password1']
        pass2 = self.cleaned_data['password2']

        if pass1 != '' or pass2 != '':
            if pass1 != pass2:
                self.add_error('password2', 'Las contraseñas deben coincidir')
        else:
            pass
        return form_data

    class Meta:
        model = Usuario
        fields = ('username', 'first_name', 'last_name', 'email', 'telefono', 'celular', 'direccion', 'cargo',
                  'fecha_nacimiento', 'is_active')

        widgets = {
            "cargo": Select2Widget(),
            "fecha_nacimiento": SelectDateWidget(years=range(1940, datetime.now().year + 1))
        }
        labels = {
            'username': 'Identificacion',
            'first_name': 'Nombre(s)',
            'direccion': 'Dirección',
            'telefono': 'Teléfono',
            'email': 'Correo electrónico',
        }