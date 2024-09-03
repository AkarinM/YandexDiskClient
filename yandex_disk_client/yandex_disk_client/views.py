from django.shortcuts import render
from django.conf import settings


def index(request: 'HttpRequest') -> 'HttpResponse':
    """
    Отображает главную страницу
    :param request:
    :return:
    """
    context: dict = {
        'url_path':f'https://oauth.yandex.ru/authorize?response_type=token&client_id={settings.YAD_APP_CLIENTID}',
    }


    return render(request, 'yd_client/index.html', context=context)