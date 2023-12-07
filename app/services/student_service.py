from app.repository import StudentRepo


class StudentService:
    # Making it as static so that we can directly call with the classname
    @staticmethod
    def create_student_record(student_data):
        student = StudentRepo.create_student_record(student_data)

        return student
