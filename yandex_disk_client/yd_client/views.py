from django.conf import settings
from django.shortcuts import render

from django.http import HttpResponse
from urllib3 import request

from API.api import get_files_list, token
from yd_client.forms import KeyInputForm

token_yd = ''

def token_page(request):
    print(request)
    return render(request, 'yd_client/token_page.html')


# def get_token(request):
#     response = token(settings.YAD_APP_CLIENTID)
#     return HttpResponse(request, response)


def get_files(request, token: str):
    """
    Отображает форму для ввода public_key.
    При получен
    :param request:
    :return:
    """
    context: dict = {}

    if request.method == 'POST':
        form = KeyInputForm(request.POST)

        if form.is_valid():
            # res = get_files_list(form.cleaned_data['public_key'])
            res = get_files_list(form.cleaned_data['public_key'], globals().get('token_yd'))

            if res:
                main_items = res['name']

                items = []
                for it in res.get('_embedded', {}).get('items', []):
                    items.append(it['name'])

                # items = res.get('_embedded', {}).get('items', [])

                context = {
                    'main_items': main_items,
                    'items': items,
                }

    else:
        globals()['token_yd'] = token
        form = KeyInputForm()

    context['form'] = form

    return render(request, 'yd_client/list_files.html', context=context)
