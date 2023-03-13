import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = 'y0_AgAAAAACJgUTAADLWwAAAADQUu4Ssvs6XLpRRLSvjZbPuH2KGFqk8UA'
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

    uploader = YaUploader()

    uploader.add_folder('Папка')
