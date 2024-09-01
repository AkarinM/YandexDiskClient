from django.shortcuts import render
from django.conf import settings

from django.http import HttpResponse


def index(request):
    context = {
        # 'client_id': settings.YAD_APP_CLIENTID,
        'url_path':f'https://oauth.yandex.ru/authorize?response_type=token&client_id={settings.YAD_APP_CLIENTID}',
        # 'origin_path': 'https://oauth.yandex.ru',
    }


    return render(request, 'yd_client/index.html', context=context)