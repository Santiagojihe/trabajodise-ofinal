INSTALLED_APPS = [
        "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "apps.courses",
    "apps.assessment",
    "apps.forums",
    "apps.reports",
    "apps.users",
]
ROOT_URLCONF = "edupro.urls"

AUTH_USER_MODEL = "users.User"
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "index"
LOGOUT_REDIRECT_URL = "login"
ROOT_URLCONF = "edupro.urls"

