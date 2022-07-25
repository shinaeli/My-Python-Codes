import unittest

from city_population_function import city_country


class TestCities(unittest.TestCase):
    def test_city_country(self):
        output = city_country('santiago', 'chile', 5000000)
        self.assertEqual(output, 'Santiago, Chile - population 5000000')


if __name__ == '__main__':
    unittest.main()