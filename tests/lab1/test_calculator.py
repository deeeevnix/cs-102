import unittest

from src.lab1.calculator import calculate

class CalculatorTestCase(unittest.TestCase):

    def test_basic_operations(self):
        cases = [
            (2, '+', 4, 6),
            (4, '-', 5, -1),
            (5, '*', 5, 25),
            (6, '/', 2, 3),
            (7, '%', 2, 1), 
            (2, '**', 10, 1024),
        ]
        for first, operation, second, expected in cases:
            with self.subTest(operation=operation):
                self.assertAlmostEqual(calculate(first, operation, second), expected)

    def test_float_addition(self):
        self.assertAlmostEqual(calculate(2.5, '+', 4.1), 6.6)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate(5, '/', 0)
        with self.assertRaises(ZeroDivisionError):
            calculate(5, '%', 0)

    def test_unknow_operation(self):
        with self.assertRaises(ValueError):
            calculate(1, '^', 2)

    def test_invalid_power(self):
        with self.assertRaises(ValueError):
            calculate(-8, '**', 0.5)

if __name__ == '__main__':
    unittest.main()
    

