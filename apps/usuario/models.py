from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):

    CARGOS_USUARIO_CHOICES = (
        ('Secretaria', 'Secretaria'),
        ('Operador', 'Operador'),
        ('Contador', 'Contador'),
        ('Gerente', 'Gerente'),
        ('Auxiliar operacion', 'Auxiliar operacion')
    )
    cargo = models.CharField(max_length=30, choices=CARGOS_USUARIO_CHOICES)
    direccion = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=12, blank=True)
    celular = models.CharField(max_length=12, blank=True)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        empleado = self.username + ' - ' + self.first_name + ' ' + self.last_name
        return empleado

    def get_cargo(self):
        return self.cargo