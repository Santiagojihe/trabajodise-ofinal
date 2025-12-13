# apps/courses/urls.py
from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path("", views.curso_list, name="curso_list"),
    #path("", views.CursoListView.as_view(), name="curso_list"),
    path("<int:pk>/", views.CursoDetailView.as_view(), name="curso_detail"),
    path("<int:pk>/inscribir/", views.inscribir_curso, name="curso_inscribir"),
]

