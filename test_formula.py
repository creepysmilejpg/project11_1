import unittest
from formula import *


class MyTestCase(unittest.TestCase):

    delta_value = .001

    def test_add(self):
        self.assertEqual(add(-3, -5), -8)
        self.assertEqual(add(-3, 2), -1)
        self.assertEqual(add(1, -6), -5)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(0, 6), 6)
        self.assertEqual(add(8, 0), 8)
        self.assertAlmostEqual(add(1.5, 1.7), 3.2, delta=self.delta_value)
        self.assertAlmostEqual(add(1.5, 3), 4.5, delta=self.delta_value)
        self.assertAlmostEqual(add(3, 4.1), 7.1, delta=self.delta_value)
        self.assertAlmostEqual(add(5, 7), 12, delta=self.delta_value)
        self.assertRaises(ValueError, add, 'x', 'y')
        self.assertRaises(ValueError, add, 'x', 2)
        self.assertRaises(ValueError, add, 5, 'y')

    def test_subtract(self):
        self.assertEqual(subtract(-3, -5), 2)
        self.assertEqual(subtract(-3, 2), -5)
        self.assertEqual(subtract(1, -6), 7)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(0, 6), -6)
        self.assertEqual(subtract(8, 0), 8)
        self.assertAlmostEqual(subtract(1.5, 1.7), -0.2, delta=self.delta_value)
        self.assertAlmostEqual(subtract(1.5, 3), -1.5, delta=self.delta_value)
        self.assertAlmostEqual(subtract(3, 4.1), -1.1, delta=self.delta_value)
        self.assertAlmostEqual(subtract(5, 7), -2, delta=self.delta_value)
        self.assertRaises(ValueError, subtract, 'x', 'y')
        self.assertRaises(ValueError, subtract, 'x', 2)
        self.assertRaises(ValueError, subtract, 5, 'y')

    def test_multiply(self):
        self.assertEqual(multiply(-3, -5), 15)
        self.assertEqual(multiply(-3, 2), -6)
        self.assertEqual(multiply(1, -6), -6)
        self.assertEqual(multiply(0, 0), 0)
        self.assertEqual(multiply(0, 6), 0)
        self.assertEqual(multiply(8, 0), 0)
        self.assertAlmostEqual(multiply(1.5, 1.7), 2.55, delta=self.delta_value)
        self.assertAlmostEqual(multiply(1.5, 3), 4.5, delta=self.delta_value)
        self.assertAlmostEqual(multiply(3, 4.1), 12.3, delta=self.delta_value)
        self.assertAlmostEqual(multiply(5, 7), 35, delta=self.delta_value)
        self.assertRaises(ValueError, multiply, 'x', 'y')
        self.assertRaises(ValueError, multiply, 'x', 2)
        self.assertRaises(ValueError, multiply, 5, 'y')

    def test_divide(self):
        self.assertEqual(divide(-3, -5), .6)
        self.assertEqual(divide(-3, 2), -1.5)
        self.assertEqual(divide(1, -2), -0.5)
        self.assertRaises(ZeroDivisionError, divide, 0, 0)
        self.assertEqual(divide(0, 6), 0)
        self.assertRaises(ZeroDivisionError, divide, 8, 0)
        self.assertAlmostEqual(divide(1.5, 0.5), 3, delta=self.delta_value)
        self.assertAlmostEqual(divide(1.5, 3), .5, delta=self.delta_value)
        self.assertAlmostEqual(divide(3, 1.5), 2, delta=self.delta_value)
        self.assertAlmostEqual(divide(18, 6), 3, delta=self.delta_value)
        self.assertRaises(ValueError, divide, 'x', 'y')
        self.assertRaises(ValueError, divide, 'x', 2)
        self.assertRaises(ValueError, divide, 5, 'y')


if __name__ == '__main__':
    unittest.main()
