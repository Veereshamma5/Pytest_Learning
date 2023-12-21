from pydantic import Field, UUID4


class StudentResponse:
    first_name: str = Field(title="first_name")
    last_name: str = Field(title="Last_name")
    department_id: UUID4 = Field(title='department_id')
    gender: str = Field(title="gender")
    age: int = Field(title="age")
