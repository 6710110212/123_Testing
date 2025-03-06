import unittest
from coe_6710110212.alternating_characters import alternating_characters

class TestAlternatingCharacters(unittest.TestCase):
    def test_no_deletions_needed(self):
        s = "ABABABAB"
        result = alternating_characters(s)
        self.assertEqual(result, 0)  

    def test_all_characters_same(self):
        s = "AAAA"
        result = alternating_characters(s)
        self.assertEqual(result, 3)

    def test_mixed_characters(self):
        s = "AABBAABB"
        result = alternating_characters(s)
        self.assertEqual(result, 4)  

    def test_single_character(self):
        s = "A"
        result = alternating_characters(s)
        self.assertEqual(result, 0)  

    def test_alternating_with_some_duplicates(self):
        s = "AABABBAB"
        result = alternating_characters(s)
        self.assertEqual(result, 2) 

    def test_all_b_characters(self):
        s = "BBBBB"
        result = alternating_characters(s)
        self.assertEqual(result, 4) 

