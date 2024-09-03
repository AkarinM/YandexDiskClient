from django.contrib import admin
from django.urls import path, include

from yandex_disk_client import views

urlpatterns = [
    path("", views.index, name="index"),
    path('admin/', admin.site.urls),
    path("client/", include("yd_client.urls")),
]
