import os
from datetime import timedelta
from pathlib import Path

from decouple import Csv, config
from dj_database_url import parse as db_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY")

DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

DJANGO_APPS = [
    "unfold",
    "unfold.contrib.filters",
    "unfold.contrib.forms",
    "unfold.contrib.inlines",
    "unfold.contrib.import_export",
    "unfold.contrib.simple_history",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "django_extensions",
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "dj_rest_auth",
]

LOCAL_APPS = [
    "src.base",
    "src.simulador",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "src.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "src.wsgi.application"

DATABASES = {
    "default": db_url("postgresql://desafio:desafio@localhost:5432/desafio"),
}

AUTH_PASSWORD_VALIDATORS = []


LANGUAGE_CODE = config("LANGUAGE_CODE", default="pt-BR")

TIME_ZONE = config("TIME_ZONE", default="America/Cuiaba")

USE_I18N = config("USE_I18N", default="True", cast=bool)

USE_TZ = config("USE_TZ", default="True", cast=bool)

STATIC_PATH = config("STATIC_PATH", default="static")
MEDIA_PATH = config("MEDIA_PATH", default="media")

STATIC_URL = f"/{STATIC_PATH}/"
STATIC_ROOT = os.path.join(BASE_DIR, STATIC_PATH)  # type: ignore

MEDIA_URL = f"/{MEDIA_PATH}/"
MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_PATH)  # type: ignore

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "base.User"

UNFOLD = {
    "SITE_HEADER": "Desafio Scheffer",
    "THEME": "light",
}

REST_FRAMEWORK = {
    "DEFAULT_PARSER_CLASSES": (
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
    ),
    "DEFAULT_PAGINATION_CLASS": "src.base.rest.CustomPagination",
    # "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
        "src.base.rest.CustomSearchFilter",
        "rest_framework.filters.OrderingFilter",
    ),
    "PAGE_SIZE": 20,
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    "COERCE_DECIMAL_TO_STRING": False,
}

REST_AUTH = {
    "USE_JWT": True,
    "JWT_SERIALIZER": "src.base.api.v1.serializers.JWTSerializerV1",
    "USER_DETAILS_SERIALIZER": "src.base.api.v1.serializers.UserSerializerV1",
    "JWT_AUTH_COOKIE": "desafio-cookie",
    "JWT_AUTH_REFRESH_COOKIE": "desafio-refresh-cookie",
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(
        days=config("EXPIRATION_DELTA", default=1, cast=int)
    ),
}

CORS_ALLOW_ALL_ORIGINS = True
