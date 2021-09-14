from one_word_find import one_word
import unittest

class CitiesTestCase(unittest.TestCase):
    def test_one_word(self):
        city_name = one_word("Nevada")
        #Is the city one word? If so, return True. If not, false.
        self.assertTrue(city_name)

unittest.main()
