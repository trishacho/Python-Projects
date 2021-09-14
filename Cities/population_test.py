from population import close_pop
import unittest

class CitiesTestCase(unittest.TestCase):
    def test_close_pop(self):
        population = close_pop('Raleigh', 469298)
        self.assertAlmostEqual(population, 460000, delta = 10000)

unittest.main()
