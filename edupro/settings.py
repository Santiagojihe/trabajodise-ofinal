INSTALLED_APPS = [
    # ...
    "apps.users",
    "apps.courses",
    "apps.assessments",
    "apps.forums",
    "apps.reports",
]
ROOT_URLCONF = "edupro.urls"

AUTH_USER_MODEL = "users.User"
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "index"
LOGOUT_REDIRECT_URL = "login"
ROOT_URLCONF = "edupro.urls"
