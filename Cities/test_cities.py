import unittest
from city_functions import city_state

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_state(self):
        """Does a simple city and state pair work?"""
        raleigh_nc = city_state('Raleigh', 'Nc')
        self.assertEqual(raleigh_nc, 'Raleigh, Nc')

    def test_city_state_population(self):
        """Can I include a population argument?"""
        raleigh_nc = city_state('Raleigh', 'Nc', population=500000)
        self.assertEqual(raleigh_nc, 'Raleigh, Nc - population 500000')

unittest.main()
