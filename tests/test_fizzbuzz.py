import unittest
from coe_6710110212.fizzbuzz import FizzBuzz
class TestFizzBuzz(unittest.TestCase):

    def test_returns_fizz_for_multiples_of_3(self):
        result = FizzBuzz(12)
        self.assertEqual(result[2], "Fizz")
        self.assertEqual(result[8], "Fizz")
    
    def test_returns_buzz_for_multiples_of_5(self):
        result = FizzBuzz(15)
        self.assertEqual(result[4], "Buzz")
        self.assertEqual(result[14], "Buzz")
    
    def test_returns_fizzbuzz_for_multiples_of_3_and_5(self):
        result = FizzBuzz(25)
        self.assertEqual(result[14], "FizzBuzz")
        self.assertEqual(result[24], "Buzz")
    
    def test_returns_number_for_non_multiples_of_3_and_5(self):
        result = FizzBuzz(8)
        self.assertEqual(result[0], "1")
        self.assertEqual(result[1], "2")
        self.assertEqual(result[3], "4")
        self.assertEqual(result[6], "8")
    
    def test_correct_sequence_for_range_1_to_12(self):
        result = FizzBuzz(12)
        expected = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz"]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
