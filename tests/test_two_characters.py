from coe_6710110212.two_characters import alternate
import unittest

class TestTwoCharacters(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(alternate("beabeefeab"), 5)  

    def test_no_valid_pair(self):
        self.assertEqual(alternate("abcd"), 2) 

    def test_already_alternating(self):
        self.assertEqual(alternate("abababab"), 8)  

    def test_mixed_characters(self):
        self.assertEqual(alternate("abcabc"), 4)  

    def test_mixed_case(self):
        self.assertEqual(alternate("aAaAaA"), 6)  

    def test_empty_string(self):
        self.assertEqual(alternate(""), 0) 
    
    def test_same_character(self):
        self.assertEqual(alternate("aaaaa"), 0)
    
    def test_special_characters(self):
        self.assertEqual(alternate("a1a1a1"), 6)