from coe_6710110212.caesar_cipher import caesar_cipher
import unittest

class TestCaesarCipher(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(caesar_cipher("sleepy", 2), "unggra")  

    def test_case_2(self):
        self.assertEqual(caesar_cipher("Hi Hello_World!", 4), "Lm Lipps_Asvph!")  

    def test_case_3(self):
        self.assertEqual(caesar_cipher("hello", 1), "ifmmp")  

    def test_case_4(self):
        self.assertEqual(caesar_cipher("Hello! How are you?", 4), "Lipps! Lsa evi csy?")  

    def test_case_5(self):
        self.assertEqual(caesar_cipher("abcdef", 0), "abcdef")  

    def test_case_6(self):
        self.assertEqual(caesar_cipher("y", 1), "z")  
    
    def test_case_7(self):
        self.assertEqual(caesar_cipher("x", 26), "x")
