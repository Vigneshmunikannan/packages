import unittest
from college.student import Student, get_student_info

class TestStudent(unittest.TestCase):
    def test_get_student_info(self):
        student = Student(student_id=1, name='Vignesh', department='CSBS')
        result = get_student_info(student)
        self.assertEqual(result, "Student ID: 1, Name: Vignesh, Department: CSBS")


        # none as parameter
    def test_student_input(self):
        result = get_student_info(None)
        self.assertEqual(result, "wrong argument")


        # not avilabile student name
    def test_student_name(self):
        result=get_student_info("im student")
        self.assertEqual(result,"No student information available")

if __name__ == '__main__':
    unittest.main()
