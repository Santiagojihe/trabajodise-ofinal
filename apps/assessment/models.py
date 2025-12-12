# apps/assessments/models.py
from django.conf import settings
from django.db import models
from apps.courses.models import Curso

User = settings.AUTH_USER_MODEL

class Examen(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="examenes")
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    habilitado = models.BooleanField(default=False)
    tiempo_limite_min = models.PositiveIntegerField(default=30)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.curso} - {self.titulo}"

class Pregunta(models.Model):
    class Tipo(models.TextChoices):
        ABIERTA = "AB", "Abierta"
        MULTIPLE = "MC", "Opción múltiple"

    examen = models.ForeignKey(Examen, on_delete=models.CASCADE, related_name="preguntas")
    enunciado = models.TextField()
    tipo = models.CharField(max_length=2, choices=Tipo.choices)
    puntaje = models.PositiveIntegerField(default=1)

class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name="opciones")
    texto = models.CharField(max_length=255)
    es_correcta = models.BooleanField(default=False)

class IntentoExamen(models.Model):
    examen = models.ForeignKey(Examen, on_delete=models.CASCADE, related_name="intentos")
    estudiante = models.ForeignKey(User, on_delete=models.CASCADE, related_name="intentos_examen")
    iniciado_en = models.DateTimeField(auto_now_add=True)
    finalizado_en = models.DateTimeField(null=True, blank=True)
    puntaje_total = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

class Respuesta(models.Model):
    intento = models.ForeignKey(IntentoExamen, on_delete=models.CASCADE, related_name="respuestas")
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto_abierta = models.TextField(blank=True)
    opcion_seleccionada = models.ForeignKey(Opcion, on_delete=models.SET_NULL, null=True, blank=True)
