class Course:
    def __init__(self, course_code, title):
        self.course_code = course_code
        self.title = title

def get_course_info(course):
    if course is None:
        return "wrong argument"
    
    course_code = getattr(course, 'course_code', None)
    course_title=getattr(course,'title',None)

    if course_code is None or course_title is None:
        return "No course information available"
    
    return f"Course Code: {course.course_code}, Title: {course.title}"