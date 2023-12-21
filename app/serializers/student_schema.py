from app.serializers.base_schema import baseMarshmallow


class StudentSchema(baseMarshmallow):
    class Meta:
        # Meta classname is fixed
        fields = (
            'first_name', 'last_name',
            'department_id',
            'gender',
            'age'
        )
