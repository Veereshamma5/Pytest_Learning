from flask import Flask
from app.models import DB, MIGRATE
from app.serializers.base_schema import ma as marshmallow_object
import logging
import logging.config
import logging.handlers
import time
from app.logging_config import config as log_config


def create_app(app_config):
    # Intialization for the logging
    logging.config.dictConfig(log_config.LOGGING_CONF)
    logging.Formatter.converter = time.gmtime  #It is important
    student_app = Flask(__name__)
    # config = import_string(app_config)()
    config = app_config()
    student_app.config.from_object(config)

    DB.init_app(student_app)  # Plugin for SQL Alchemy
    MIGRATE.init_app(student_app, DB)  # Plugin for Alembic
    marshmallow_object.init_app(student_app)

    return student_app
