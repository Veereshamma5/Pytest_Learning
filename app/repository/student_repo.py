from http import HTTPStatus
from app.models import Student
from app.repository.sql_context import SqlContext


class StudentRepo:
    @staticmethod
    def create_student_record(student_data):
        student = Student()
        student.first_name = student_data['first_name']
        student.last_name = student_data['last_name']
        student.department_id = student_data['department_id']
        student.gender = student_data['gender']
        student.age = student_data['age']

        with SqlContext() as sql_context:
            sql_context.session.add(student)

        return student
