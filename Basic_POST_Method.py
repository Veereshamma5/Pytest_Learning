from flask import Blueprint
from flask import request
from http import HTTPStatus
from app.repository.sql_context import SqlContext
from app.models import Student

# Blueprints are used for grouping the APIs together
student_bp = Blueprint('student_bp', __name__)


@student_bp.route('/student/create', methods=['POST'])
def create_student():
    student_data = request.json
    student = Student()
    student.first_name = student_data['first_name']
    student.last_name = student_data['last_name']
    student.department_id = student_data['department_id']
    student.gender = student_data['gender']
    student.age = student_data['age']

    with SqlContext() as sql_context:
        sql_context.session.add(student)

    return 'Student record created successfully', HTTPStatus.CREATED