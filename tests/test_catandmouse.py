import unittest
from coe_6710110212.catandmouse import CatandMouse

class TestCatAndMouse(unittest.TestCase):

    def test_mouse_escapes_when_both_cats_are_equal_distance(self):
        self.assertEqual(CatandMouse(3, 7, 5), "Mouse C")

    def test_cat_a_reaches_mouse_first(self):
        self.assertEqual(CatandMouse(2, 6, 4), "Cat A")

    def test_cat_b_reaches_mouse_first(self):
        self.assertEqual(CatandMouse(4, 8, 6), "Cat B")

    def test_mouse_between_cats_and_escapes(self):
        self.assertEqual(CatandMouse(6, 10, 8), "Mouse C")

    def test_cat_a_wins_when_mouse_near_to_cat_a(self):
        self.assertEqual(CatandMouse(15, 30, 16), "Cat A")

    def test_both_cats_and_mouse_at_same_position(self):
        self.assertEqual(CatandMouse(5, 5, 5), "Mouse C")

    def test_mouse_between_cats(self):
        self.assertEqual(CatandMouse(1, 10, 5), "Mouse C")

    def test_cats_on_opposite_sides_of_mouse(self):
        self.assertEqual(CatandMouse(3, 7, 5), "Mouse C")
    
    def test_negative_positions(self):
        self.assertEqual(CatandMouse(-10, -20, -15), "Mouse C")

    def test_large_numbers(self):
        self.assertEqual(CatandMouse(1000000, 2000000, 1500000), "Mouse C")

