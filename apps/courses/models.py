# apps/courses/models.py
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    educador = models.ForeignKey(User, on_delete=models.PROTECT, related_name="cursos_creados")
    administrador = models.ForeignKey(User, on_delete=models.PROTECT, related_name="cursos_gestionados")
    creado_en = models.DateTimeField(auto_now_add=True)

    estudiantes = models.ManyToManyField(
        User, through="Inscripcion", related_name="cursos_inscritos", blank=True
    )

    def __str__(self):
        return self.titulo

class Inscripcion(models.Model):
    estudiante = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    activa = models.BooleanField(default=True)

    class Meta:
        unique_together = ("estudiante", "curso")

class RecursoEducativo(models.Model):
    class Tipo(models.TextChoices):
        VIDEO = "VIDEO", "Video"
        PDF = "PDF", "PDF"
        LINK = "LINK", "Link"
        PRESENTACION = "PPT", "Presentación"

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="recursos")
    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=10, choices=Tipo.choices)
    url = models.URLField(blank=True)              # para link/video
    archivo = models.FileField(upload_to="recursos/", blank=True, null=True)  # PDF/PPT
    creado_en = models.DateTimeField(auto_now_add=True)

class Retroalimentacion(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="retroalimentaciones")
    estudiante = models.ForeignKey(User, on_delete=models.CASCADE, related_name="retroalimentacion_recibida")
    educador = models.ForeignKey(User, on_delete=models.PROTECT, related_name="retroalimentacion_emitida")
    mensaje = models.TextField()
    calificacion = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    creada_en = models.DateTimeField(auto_now_add=True)
