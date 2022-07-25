import unittest

from city_function import city_country


class TestCities(unittest.TestCase):
    def test_city_country(self):
        test_result = city_country('santiago', 'chile')
        self.assertEqual(test_result, 'Santiago, Chile')


if __name__ == '__main__':
    unittest.main()

