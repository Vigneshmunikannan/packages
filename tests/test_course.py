import unittest
from college.course import Course, get_course_info

class TestCourse(unittest.TestCase):
    def test_get_course_info(self):
        course = Course(course_code='CS101', title='Introduction to Computer Science')
        result = get_course_info(course)
        self.assertEqual(result, "Course Code: CS101, Title: Introduction to Computer Science")

    # none as parameter
    def test_student_input(self):
        result = get_course_info(None)
        self.assertEqual(result, "wrong argument")

        # not avilabile student name
    def test_student_name(self):
        result=get_course_info("FST")
        self.assertEqual(result,"No course information available")

if __name__ == '__main__':
    unittest.main()
