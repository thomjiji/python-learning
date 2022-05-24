import unittest
from city_function import city_name


class TestCityNameWorksOrNot(unittest.TestCase):
    """Test city_function work or not."""

    def test_city_country(self):
        full_name = city_name('Beijing', 'China')
        self.assertEqual(full_name, 'Beijing, China')

    def test_city_country_population(self):
        full_name_with_population = city_name('Huaihua', 'China', 100000)
        self.assertEqual(full_name_with_population, 'Huaihua, China - population: 100000')


if __name__ == '__main__':
    unittest.main()