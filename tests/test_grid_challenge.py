from coe_6710110212.grid_challenge import gridChallenge
import unittest
class TestGridChallenge(unittest.TestCase):

    def test_sorted_grid(self):
        self.assertEqual(gridChallenge(["art", "cat", "dog"]), "NO")

    def test_unsorted_grid(self):
        self.assertEqual(gridChallenge(["zyx", "bca", "pon"]), "NO")

    def test_single_row(self):
        self.assertEqual(gridChallenge(["uvwxyz"]), "YES")

    def test_single_column(self):
        self.assertEqual(gridChallenge(["h", "g", "f"]), "NO")

    def test_single_element(self):
        self.assertEqual(gridChallenge(["z"]), "YES")

    def test_same_elements(self):
        self.assertEqual(gridChallenge(["bbb", "bbb", "bbb"]), "YES")

    def test_mix_elements(self):
        self.assertEqual(gridChallenge(["acd", "bce", "cfg"]), "YES")

    def test_case_sensitivity(self):
        self.assertEqual(gridChallenge(["aBc", "bCd", "cDe"]), "YES") 
