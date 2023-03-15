import requests
import unittest
import configparser
from tasks.main_task2 import YaUploader



#################  Задание 2 ###################


class Test(unittest.TestCase):
    def test_exists_folder(self):
        config = configparser.ConfigParser()
        config.read('settings.ini')
        tokenYa = config['Ya']['token']
        uploader = YaUploader(tokenYa)
        folder_path = uploader.add_folder('ПАПКА')
        headers = uploader._get_headers()
        params = {'path': folder_path}
        response = requests.get(f'{uploader.url}?path={folder_path}', headers=headers, params=params)
        response.raise_for_status()
        self.assertIs(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
