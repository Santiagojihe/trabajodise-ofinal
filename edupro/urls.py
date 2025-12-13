from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.courses.urls")),
    path("login/", LoginView.as_view(), name="login"),
    #path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    path("", TemplateView.as_view(template_name="index.html"), name="index"),

    #path("cursos/", include("apps.courses.urls")),
    #path("examenes/", include("apps.assessment.urls")),
    #path("foros/", include("apps.forums.urls")),
    #path("reportes/", include("apps.reports.urls")),
]