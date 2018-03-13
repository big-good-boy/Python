import unittest
from city_functions import city_country

class CityFunctionsTest(unittest.TestCase):
  def test_city_coutry(self):
    city_and_country = city_country('santiago', 'chile')
    self.assertEqual(city_and_country, 'Santiago, Chile')
  def test_city_coutry_population(self):
    city_and_country = city_country('santiago', 'chile', 'population=5000000')
    self.assertEqual(city_and_country, 'Santiago, Chile - population=5000000')

unittest.main()