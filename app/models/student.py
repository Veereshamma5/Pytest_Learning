from sqlalchemy import Column, UUID, String, Integer

from app.models.base_model import BaseModel


class Student(BaseModel):
    __tablename__ = 'Student'

    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=True)
    department_id = Column(UUID(as_uuid=True), nullable=True)
    gender = Column(String(255), nullable=True)
    age = Column(Integer, nullable=True)
