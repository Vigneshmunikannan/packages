import unittest
from college.grade import calculate_grade

class TestGrade(unittest.TestCase):
    def test_calculate_grade(self):
        self.assertEqual(calculate_grade(95), 'A')
        self.assertEqual(calculate_grade(85), 'B')
        self.assertEqual(calculate_grade(75), 'C')
        self.assertEqual(calculate_grade(65), 'D')
        self.assertEqual(calculate_grade(55), 'F')
    
    # none as input 
    def test_none_input(self):
        result=calculate_grade(None)
        self.assertEqual(result,"Score must not be None")
    
    # string input
    def test_string_input(self):
        with self.assertRaises(TypeError):
            calculate_grade("Hello")
    
    # input below 0
    def test_below_zero_input(self):
        with self.assertRaises(ValueError):
            calculate_grade(-100)


if __name__ == '__main__':
    unittest.main()
