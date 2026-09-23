import triangle
import unittest

class TestTriangle(unittest.TestCase):
    def test_area_base(self):
        self.assertEqual(triangle.area(10, 200), 1000)
    def test_area_zero(self):
        self.assertEqual(triangle.area(0, 1), 0)
    def test_area_minus(self):
        with self.assertRaises(ValueError):
            triangle.area(1, -1)

    def test_perimeter_base(self):
        self.assertEqual(triangle.perimeter(10), 30)
    def test_perimeter_zero(self):
        self.assertEqual(triangle.perimeter(0), 0)
    def test_perimeter_minus(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-10)
