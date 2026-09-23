import cube
import unittest

class TestCube(unittest.TestCase):
    def test_area_base(self):
        self.assertEqual(cube.area(10), 600)
    def test_area_zero(self):
        self.assertEqual(cube.area(0), 0)
    def test_area_minus(self):
        with self.assertRaises(ValueError):
            cube.area(-1)

    def test_volume_base(self):
        self.assertEqual(cube.volume(20), 8000)
    def test_volume_small(self):
        self.assertEqual(cube.volume(5), 125)
    def test_volume_zero(self):
        self.assertEqual(cube.volume(0), 0)
    def test_volume_minus(self):
        with self.assertRaises(ValueError):
            cube.volume(-10)
