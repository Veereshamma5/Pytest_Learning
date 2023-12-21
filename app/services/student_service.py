from app.lib.custom_exceptions import DuplicateRecordException, CreateRecordFailedException
from app.models import Student
from app.repository import StudentRepo
from app.schema import StudentResponse
from flask import current_app as stdnt_app

# Making it as static so that we can directly call with the classname


def create_student_record(student_data):
    stdnt_app.logger.info('Create student service called.......')
    student = StudentRepo.get_student_record(student_data['first_name'], student_data['last_name'])
    if student:
        raise DuplicateRecordException("Record already exists with the given first_name and last_name")

    try:
        student = StudentRepo.create_student_record(student_data)
    except Exception as ex:
        raise CreateRecordFailedException

    return student


# def get_student_records() -> list[StudentResponse]:
#     student = StudentRepo.get_all_records()
#     print("tupe of student object in the service method is:", type(student))
#     print("student information in the service method", student)
#
#     return student
