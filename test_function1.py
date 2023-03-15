import unittest
import pytest
from tasks.main_task1 import filtr_geo_logs, create_list, count_word_requests, unpack_dict, convert_list_to_dicts


#################  Задание 1 ###################


class Test(unittest.TestCase):
    def setUp(self):
        print("method setUp")

    def tearDown(self):
        print("method tearDown")

    def test_list_class_geo_logs(self): # Проверка, что получаемый результат является списком
        self.assertIsInstance(filtr_geo_logs(), list)

    def test_dict_count_word_requests(self): # Проверка, что получаемый результат не является списком
        self.assertNotIsInstance(count_word_requests(), list)

    def test_unpack_dict_res(self): # Проверка, что полученный результат равен ожидаемому
        self.assertEqual('yandex', unpack_dict())

    def test_values_Regex_geo_logs(self): # Проверка, что значения списка содержат 'Россия'
        res = r'([Р][о][с][с][и][я])'
        for i in filtr_geo_logs():
            for v in i.values():
                self.assertRegex(v[1], res)

    def test_values_In_geo_logs(self): # Проверка, что значения списка содержат 'Россия'
        for i in filtr_geo_logs():
            for v in i.values():
                self.assertIn('Россия', v)

    def test_values_Not_geo_logs(self):  # Проверка, что значения списка не содержат 'Индия'
        for i in filtr_geo_logs():
            for v in i.values():
                self.assertNotIn('Индия', v)


def test_create_list_res(): # Проверка, что полученный результат равен ожидаемому
    assert sorted(create_list()) == sorted([98, 35, 213, 54, 119, 15])


def test_list_class_create_list(): # Проверка, что получаемый результат является списком
    assert isinstance(create_list(), list)


@pytest.mark.parametrize('country', [('Индия'), ('Португалия'), ('Франция')])
def test_values_NotIn_geo_logs(country):  # Проверка, что значения списка не содержат 'Индия', 'Португалия', 'Франция'
    for i in filtr_geo_logs():
        for j in i.values():
            assert country != j[1]


def test_convert_list_to_dicts():
    res = convert_list_to_dicts()
    assert isinstance(res, dict)
    assert 'date' not in res
    assert res['2018-01-01'] == {'yandex': {'cpc': 100}}


if __name__ == '__main__':
    unittest.main()


