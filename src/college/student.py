class Student:
    def __init__(self, student_id, name,department):
        self.student_id = student_id
        self.name = name
        self.department=department

def get_student_info(student):
    if student is None:
        return "wrong argument"
    
    student_id = getattr(student, 'student_id', None)
    name = getattr(student, 'name', None)
    department = getattr(student, 'department', None)

    if student_id is None or name is None or department is None:
        return "No student information available"
    
    return f"Student ID: {student.student_id}, Name: {student.name}, Department: {student.department}"
