from app import create_app
from config import DevConfig
from app.api.student import student_bp
# app_config = 'config.DevConfig'

student_app = create_app(DevConfig)
student_app.register_blueprint(student_bp)

if __name__ == '__main__':
    student_app.run()
