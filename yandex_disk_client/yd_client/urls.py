from django.urls import path

from yd_client.views import get_files, token_page

urlpatterns = [
    path("get_files/", get_files, name="files"),
    path("get_files/<str:token>/", get_files, name="files_token"),
    path("token/", token_page, name="token"),
]
