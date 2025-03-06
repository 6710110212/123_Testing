import unittest
from coe_6710110212 import funny_string

class TestFunnyString(unittest.TestCase):
    
    def test_string_acxz(self):
        s = "acxz"
        result = funny_string(s)
        self.assertEqual(result, "Funny")

    def test_string_bcxz(self):
        s = "bcxz"
        result = funny_string(s)
        self.assertEqual(result, "Not Funny")

    def test_single_character(self):
        s = "a"
        result = funny_string(s)
        self.assertEqual(result, "Funny") 

    def test_string_madam(self):
        s = "madam"
        result = funny_string(s)
        self.assertEqual(result, "Funny")

    def test_string_carbonara(self):
        s = "carbonara"
        result = funny_string(s)
        self.assertEqual(result, "Funny")  

    def test_string_with_numbers(self):
        s = "m4a1"
        result = funny_string(s)
        self.assertEqual(result, "Not Funny")




