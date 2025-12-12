# apps/forums/models.py
from django.conf import settings
from django.db import models
from apps.courses.models import Curso

User = settings.AUTH_USER_MODEL

class ForoDiscusion(models.Model):
    curso = models.OneToOneField(Curso, on_delete=models.CASCADE, related_name="foro")
    titulo = models.CharField(max_length=200, default="Foro del curso")

class Tema(models.Model):
    foro = models.ForeignKey(ForoDiscusion, on_delete=models.CASCADE, related_name="temas")
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    titulo = models.CharField(max_length=200)
    creado_en = models.DateTimeField(auto_now_add=True)

class Mensaje(models.Model):
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE, related_name="mensajes")
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    contenido = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)
