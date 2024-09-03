import requests

def get_files_list(public_key: str, token: str):
    """
    Запрос к API Яндекс.Диск
    :param public_key: ссылка для публичного доступа к файлу/папке
    :param token: яндекс токен
    :return:
    """
    response = requests.get(
        'https://cloud-api.yandex.net/v1/disk/public/resources',
        params={'public_key': public_key},
        headers={'Authorization': f'OAuth {token}'}
    )

    if response.ok:
        return response.json()
    else:
        return {}

def download_file_api(public_key: str, token: str, path_file: str):
    """
    Запрос к API Яндекс.Диск для скачивания файла
    :param public_key: ссылка для публичного доступа к файлу/папке
    :param token: яндекс токен
    :param path_file: путь к файлу в публичной папке
    :return:
    """
    response = requests.get(
        'https://cloud-api.yandex.net/v1/disk/public/resources/download',
        params={
            'public_key': public_key,
            'path': path_file,
        },
        headers={'Authorization': f'OAuth {token}'}
    )

    file_url = response.json().get('href')

    resp = requests.get(file_url)

    return resp