from datetime import datetime
from uuid import uuid4
import json
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID

DB = SQLAlchemy()
MIGRATE = Migrate()


class BaseModel(DB.Model):
    __abstract__ = True

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    def set_attributes(self, values):
        if not isinstance(values, dict):
            values = json.loads(values.json())
        for key, value in values.items():
            if hasattr(self, key) and (
                    (isinstance(value, str) and value)
                    or (isinstance(value, (bool, int, float, list)))
            ):
                setattr(self, key, value)


class CreateMixin(DB.Model):
    __abstract__ = True

    created_on = Column(DateTime, default=datetime.now)
    created_by = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)


class AuditMixin(DB.Model):
    __abstract__ = True

    created_on = Column(DateTime, default=datetime.now)
    modified_on = Column(DateTime, default=datetime.utcnow, onupdate=datetime.now)


class UpdateMixin(DB.Model):
    __abstract__ = True
    modified_on = Column(DateTime, onupdate=datetime.now, nullable=True)
    modified_by = Column(String(255), nullable=True)


class SubmittedMixin(DB.Model):
    __abstract__ = True
    submitted_on = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    submitted_by = Column(String(255), nullable=False)


class ReviewedMixin(DB.Model):
    __abstract__ = True
    reviewed_on = Column(DateTime)
    reviewed_by = Column(String(255), nullable=False)
