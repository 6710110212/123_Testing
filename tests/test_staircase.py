import unittest
from coe_6710110212.staircase import staircase

class StaircaseTest(unittest.TestCase):
    def test_default_case(self):
        result = "    @\n   @@\n  @@@\n @@@@\n@@@@@\n"
        self.assertEqual(staircase(5, "@"), result)
    
    def test_with_hash_symbol(self):
        result = "    #\n   ##\n  ###\n ####\n#####\n"
        self.assertEqual(staircase(5), result)
    
    def test_single_step(self):
        self.assertEqual(staircase(1), "#\n")
    
    def test_zero_steps(self):
        self.assertEqual(staircase(0), "")
    
    def test_three_steps(self):
        result = "  $\n $$\n$$$\n"
        self.assertEqual(staircase(3, "$"), result)
