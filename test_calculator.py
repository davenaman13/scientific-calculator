import unittest
import math
import calculator

class TestCalculator(unittest.TestCase):
    def test_square_root(self):
        self.assertAlmostEqual(calculator.square_root(16), 4)
    
    def test_factorial(self):
        self.assertEqual(calculator.factorial(5), 120)
    
    def test_natural_logarithm(self):
        self.assertAlmostEqual(calculator.natural_logarithm(math.e), 1)
    
    def test_power_function(self):
        self.assertAlmostEqual(calculator.power_function(2, 3), 8)

if __name__ == "__main__":
    unittest.main()
