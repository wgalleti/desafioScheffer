from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/auth/", include("dj_rest_auth.urls")),
    path("api/base/", include("src.base.urls")),
    path("api/simulador/", include("src.simulador.urls")),
]
