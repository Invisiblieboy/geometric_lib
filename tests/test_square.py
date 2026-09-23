import square
import unittest

class TestSquare(unittest.TestCase):
    def test_area_base(self):
        self.assertEqual(square.area(10), 100)
    def test_area_zero(self):
        self.assertEqual(square.area(0), 0)
    def test_area_minus(self):
        with self.assertRaises(ValueError):
            square.area(-1)

    def test_perimeter_base(self):
        self.assertEqual(square.perimeter(20), 80)
    def test_perimeter_zero(self):
        self.assertEqual(square.perimeter(0), 0)
    def test_perimeter_minus(self):
        with self.assertRaises(ValueError):
            square.perimeter(-10)
