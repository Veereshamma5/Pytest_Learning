from flask import Flask
from app.models import DB, MIGRATE
from werkzeug.utils import import_string
from config import DevConfig


def create_app(app_config):
    student_app = Flask(__name__)
    # config = import_string(app_config)()
    config = app_config()
    student_app.config.from_object(config)

    DB.init_app(student_app)
    MIGRATE.init_app(student_app, DB)

    return student_app
