from unittest import TestCase
from unittest.mock import patch
from main import filtr_geo_logs, create_list, count_word_requests, unpack_dict, convert_list_to_dicts


class Test(TestCase):
    @patch('main.filtr_geo_logs', return_value=9)
    def test_output_name(self, filtr_geo_logs):
        pass
        self.assertEqual(filtr_geo_logs(), 9)



