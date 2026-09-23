import circle
import math
import unittest

class TestCircle(unittest.TestCase):
    def test_area_base(self):
        self.assertAlmostEqual(circle.area(10), 10*10*math.pi)
    def test_area_zero(self):
        self.assertEqual(circle.area(0), 0)
    def test_area_minus(self):
        with self.assertRaises(ValueError):
            circle.area(-20)

    def test_perimeter_base(self):
        self.assertAlmostEqual(circle.perimeter(10), 2*10*math.pi)
    def test_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), 0)
    def test_perimeter_minus(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-20)
