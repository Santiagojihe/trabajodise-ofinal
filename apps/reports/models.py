# apps/reports/models.py
from django.conf import settings
from django.db import models
from apps.courses.models import Curso

User = settings.AUTH_USER_MODEL

class ReporteRendimiento(models.Model):
    estudiante = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reportes")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="reportes")
    promedio = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    total_intentos = models.PositiveIntegerField(default=0)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("estudiante", "curso")