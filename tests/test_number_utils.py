from coe_number.number_utils import is_prime_list
import unittest

class PrimeListTest(unittest.TestCase):
    def test_give_1_2_3_is_prime(self):
        prime_list = [1, 2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_2_3_5_7_is_prime(self):
        prime_list = [2, 3, 5, 7]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_11_13_17_is_prime(self):
        prime_list = [2, 3, 5, 7]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_4_6_8_is_not_prime(self):
        prime_list = [4, 6, 8]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)
    
    def test_give_1_is_not_prime(self):
        prime_list = [1]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_96_98_99_is_not_prime(self):
        prime_list = [96, 98, 99]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_empty_list_is_prime(self):
        prime_list = []
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
    
