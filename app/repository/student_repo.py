from app.models import Student
from app.repository.sql_context import SqlContext
from app.schema import StudentResponse


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


def get_student_record(first_name, last_name):
    query = Student.query.filter(
        Student.first_name == first_name,
        Student.last_name == last_name
    )
    # Select * from Student where first_name = " " and last_name=" ";

    return query.scalar() #Return object if found, else None. It won't raise any esception


def get_all_records() -> list[StudentResponse]:
    with SqlContext() as sql_context:
        response = Student.query.all()
        print("response is::::::", response)
    return response
