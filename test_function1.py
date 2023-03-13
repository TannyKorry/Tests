import requests
import unittest
# import pytest
from tasks.main_task1 import filtr_geo_logs, create_list, count_word_requests, unpack_dict, convert_list_to_dicts
from tasks.main_task2 import YaUploader


#################  Задание 1 ###################


class Test(unittest.TestCase):
    def test_list_class_geo_logs(self): # Проверка, что получаемый результат является списком
        assert isinstance(filtr_geo_logs(), list)

    def test_list_class_create_list(self): # Проверка, что получаемый результат является списком
        assert isinstance(create_list(), list)

    def test_dict_convert_list_to_dicts(self): # Проверка, что получаемый результат является словарем
        assert isinstance(convert_list_to_dicts(), dict)

    def test_dict_count_word_requests(self): # Проверка, что получаемый результат является словарем
        assert isinstance(count_word_requests(), dict)

    def test_create_list_res(self): # Проверка, что полученный результат равен ожидаемому
        assert sorted(create_list()) == sorted([98, 35, 213, 54, 119, 15])

    def test_unpack_dict_res(self): # Проверка, что полученный результат равен ожидаемому
        assert 'yandex' == unpack_dict()

    def test_values_Regex_geo_logs(self): # Проверка, что значения списка содержат 'Россия'
        res = r'([Р][о][с][с][и][я])'
        for i in filtr_geo_logs():
            for v in i.values():
                self.assertRegex(v[1], res)

    def test_values_In_geo_logs(self): # Проверка, что значения списка содержат 'Россия'
        for i in filtr_geo_logs():
            for v in i.values():
                self.assertIn('Россия', v)

    def test_values_NotIn_geo_logs(self):  # Проверка, что значения списка не содержат 'Индия'
        for i in filtr_geo_logs():
            for v in i.values():
                self.assertNotIn('Индия', v)


if __name__ == '__main__':
    unittest.main()
