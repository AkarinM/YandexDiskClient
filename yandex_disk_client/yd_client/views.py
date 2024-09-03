from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.core.cache import cache

from API.api import get_files_list, download_file_api
from yd_client.forms import KeyInputForm

def token_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'yd_client/token_page.html')


def get_files(request: HttpRequest, token: str) -> HttpResponse:
    """
    Отображает форму для ввода public_key.
    Выводит список файлов
    Скачивание файлов
    :param request:
    :param token: токен Яндес ID
    :return: HttpResponse
    """
    context: dict = {}

    if request.method == 'POST':
        if 'path_f' in request.POST.keys():
            result_d: HttpResponse = download_file_api(request.POST['public_key'], token, request.POST['path_f'])

            response: HttpResponse = HttpResponse(result_d, content_type='application/force-download')
            ex: str = '' if request.POST["type"] == 'file' else '.zip'
            response['Content-Disposition'] = f'attachment; filename="{request.POST["name"]}{ex}"'
            return response


        form: KeyInputForm = KeyInputForm(request.POST)

        if form.is_valid():
            cache_key: str = token
            res: dict | None = cache.get(cache_key)

            if res is None:
                res = get_files_list(form.cleaned_data['public_key'], token)
                cache.set(cache_key, res, 60)

            if res:
                main_items: dict = {
                    'name': res['name'],
                    'type': res['type'],
                    'path': res['path'],
                }

                items: list = []
                for it in res.get('_embedded', {}).get('items', []):
                    items.append(
                        {
                            'name': it['name'],
                            'type': it['type'],
                            'path': it['path'],
                        }
                    )

                context = {
                    'main_items': main_items,
                    'items': items,
                }

    else:
        form: KeyInputForm = KeyInputForm()

    context['form'] = form

    return render(request, 'yd_client/list_files.html', context=context)
