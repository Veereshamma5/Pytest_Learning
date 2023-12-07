from flask import Blueprint
from flask import request
from http import HTTPStatus
from app.services import StudentService

# Blueprints are used for grouping the APIs together
student_bp = Blueprint('student_bp', __name__)


@student_bp.route('/student/create', methods=['POST'])
def create_student():
    student_data = request.json

    try:
        student = StudentService.create_student_record(student_data)

    except Exception as ex:
        print("Exception is:::", ex)

    return f"Returned the serialized object", HTTPStatus.CREATED


@student_bp.route('/getall', methods=['GET'])
def get_details():
    return "Welcome"
