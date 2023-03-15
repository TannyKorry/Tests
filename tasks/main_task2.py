import requests
import configparser

class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources/'

    def _get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def add_folder(self, path):
        headers = self._get_headers()
        params = {'overwrite': 'true'}
        requests.put(f'{self.url}?path={path}', headers=headers, params=params)
        return path


if __name__ == '__main__':

    config = configparser.ConfigParser()
    config.read('settings.ini')
    tokenYa = config['Ya']['token']

    uploader = YaUploader(tokenYa)

    uploader.add_folder('Папка')
