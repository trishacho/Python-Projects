import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    
    def test_first_last_name(self):
        formatted_name = get_formatted_name('mrs', 'kubik')
        self.assertEqual(formatted_name, 'Mrs Kubic')
        #try replacing the 'k' with a 'c'
       
    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfpack Amadeus Mozart')
            

unittest.main()
