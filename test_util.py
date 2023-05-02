import unittest
from util import *

class TestUtil(unittest.TestCase):
    def test_gaussian(self):
        self.assertAlmostEqual(calculate_gaussian_function(0, 0, 1), 0.399, delta=0.001)
        self.assertAlmostEqual(calculate_gaussian_function(1, 0, 1), 0.242, delta=0.001)

        self.assertAlmostEqual(weighted_gaussian(0, 0, 1), 1, delta=0.001)
        self.assertAlmostEqual(weighted_gaussian(1, 0, 1), 0.607, delta=0.001)

    def test_scaler(self):
        self.assertAlmostEqual(get_scaled_value(1, (0, 2), (0, 4)), 2, delta=0.001)
        self.assertAlmostEqual(get_scaled_value(1, (0, 2), (6, 10)), 8, delta=0.001)
        self.assertAlmostEqual(get_scaled_value(10, (0, 100), (-1, 1)), -0.8, delta=0.001)
        self.assertAlmostEqual(get_scaled_value(-1, (-2, 0.5), (0, 500)), 200, delta=0.001)
        self.assertAlmostEqual(get_scaled_value(200, (0, 500), (-2, 0.5)), -1, delta=0.001)

    def test_mandel(self):
        self.assertEqual(mandelbrot_test(-1+0j, 2, 50), -1)
        self.assertEqual(mandelbrot_test(-1 - 0.17142857142857137j, 2, 50), -1)
        self.assertEqual(mandelbrot_test(-0.9920634920634921-0.22619047619047616j, 2, 50), -1)
        self.assertEqual(mandelbrot_test(-0.4523809524-0.09523809524j, 2, 50), -1)
        self.assertEqual(mandelbrot_test(-1-0.20j, 2, 50), -1)
        self.assertEqual(mandelbrot_test(0.339+0.242j, 2, 50), -1)