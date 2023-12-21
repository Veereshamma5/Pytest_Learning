from flask import Blueprint
from flask import request
from flask import jsonify
from http import HTTPStatus

from flask_dantic import serialize
from app.models import Student
from app.services import StudentService
from app.lib.custom_exceptions import DuplicateRecordException, CreateRecordFailedException
from app.serializers.student_schema import StudentSchema
from flask import current_app as stdnt_app


# Blueprints are used for grouping the APIs together
student_bp = Blueprint('student_bp', __name__)


@student_bp.route('/student/create', methods=['POST'])
def create_student():
    stdnt_app.logger.info("Create Student API called...")
    student_data = request.json
    try:
        student = StudentService.create_student_record(student_data)
        schema_obj = StudentSchema()
        serialized_data = schema_obj.dump(student)
    except DuplicateRecordException as ex:
        stdnt_app.logger.error(f'Record already exists | {ex}')
        return str(ex), HTTPStatus.BAD_REQUEST
    except CreateRecordFailedException as ex:
        return str(ex), HTTPStatus.INTERNAL_SERVER_ERROR
    except Exception as ex:
        print("Exception is:::", ex)
        return str(ex), HTTPStatus.INTERNAL_SERVER_ERROR

    return jsonify({'status': 'Success', 'data': serialized_data}), HTTPStatus.CREATED


@student_bp.route('/getall', methods=['GET'])
def get_details():
    try:
        student = StudentService.get_student_records()
        print("student details in the API layer is", student)
        response = list(student)
        print("Response information is::", response)
        student_response = serialize(
            response, Student, json_dump=False, many=True
        )
        return {"status": "success", "data": student_response}

    except Exception as ex:
        print("Exception occured:", ex)

    return f"Fetched student records", HTTPStatus.OK
