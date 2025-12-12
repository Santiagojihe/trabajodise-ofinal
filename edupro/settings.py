INSTALLED_APPS = [
    "apps.courses",
    "apps.assessment",
    "apps.forums",
    "apps.reports",
    "apps.users",
]

AUTH_USER_MODEL = "users.User"
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "index"
LOGOUT_REDIRECT_URL = "login"
