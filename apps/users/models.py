# apps/users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        ESTUDIANTE = "EST", "Estudiante"
        EDUCADOR   = "EDU", "Educador"
        ADMIN      = "ADM", "Administrador"

    role = models.CharField(max_length=3, choices=Role.choices)

    def is_estudiante(self): return self.role == self.Role.ESTUDIANTE
    def is_educador(self):   return self.role == self.Role.EDUCADOR
    def is_admin(self):      return self.role == self.Role.ADMIN
