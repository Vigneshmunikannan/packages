import unittest
from src.calculations.add import add_numbers

class TestMathOperations(unittest.TestCase):

    def test_valid_addition(self):
        result = add_numbers(3, 4)
        self.assertEqual(result, 7)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            add_numbers("a", 4)

    def test_missing_input(self):
        with self.assertRaises(ValueError):
            add_numbers(None,2)

    def test_missing_input1(self):
        with self.assertRaises(ValueError):
            add_numbers(None,None)

if __name__ == '__main__':
    unittest.main()
