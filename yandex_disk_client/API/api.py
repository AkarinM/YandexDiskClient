import requests

from django.conf import settings



def token(client_id):
    # return 'y0_AgAAAAARA576AAxcnQAAAAEPdQS5AAC3bNa_IaFDcZkq0Jv6TlmEixyQ1A'
    """
    Запрос к API Яндекс.Диск для получения токена
    :param public_key: ссылка для публичного доступа к файлу/папке
    :return:
    """
    response = requests.get(
        'https://oauth.yandex.ru/authorize',
        params={
            'response_type': 'token',
            'client_id': client_id,
        },
    )

    # if response.ok:
    #     return response.json()
    # else:
    #     return {}

def get_files_list(public_key: str, token: str):
    """
    Запрос к API Яндекс.Диск
    :param public_key: ссылка для публичного доступа к файлу/папке
    :return:
    """
    print('tokentoken', token)
    response = requests.get(
        'https://cloud-api.yandex.net/v1/disk/public/resources',
        params={'public_key': public_key},
        # headers={'Authorization': f'OAuth {settings.YAD_APP_TOKEN}'}
        headers={'Authorization': f'OAuth {token}'}
    )

    if response.ok:
        return response.json()
    else:
        return {}