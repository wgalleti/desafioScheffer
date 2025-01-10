from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("base/", include("src.base.urls")),
    path("simulador/", include("src.simulador.urls")),
]
